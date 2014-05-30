# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2008-2014  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


__doc__ = """
convert scattereed neutrons to events (pixelID, tofChannelNo, prob)
intercepted by a detector system.
"""

__implementation__ = """
This script runs a mcvine instrument simulation script consisting
of two components, a neutron player and a detector system.

The neutron player replay the neutrons stored in a neutron
storage. Those neutrons were scattered off of a sample
in a neutron beam.

The detector system is specified by a xml file.
"""


cmd_help = __doc__


# application 
from pyre.applications.Script import Script as AppBase
class App(AppBase):
    
    class Inventory(AppBase.Inventory):
        
        import pyre.inventory
        neutrons = pyre.inventory.str('neutrons', default='neutrons.dat')
        workdir = pyre.inventory.str('workdir', default='work-neutrons2events')
        nodes = pyre.inventory.int('nodes', default=0)
        
        tofbinsize = pyre.inventory.float('tofbinsize', default=0.1) # microsecond
        tofmax = pyre.inventory.float('tofmax', default=0.2) # second
        
        # instrument name. if given, assume instrument xml (danse) is 
        # at $MCVINE_DIR/share/mcvine/instruments/<instrument>/<instrument>.xml.fornxs
        instrument = pyre.inventory.str('instrument') 
        
        # path instrument.xml.fornxs (danse). this overrides the instrument option
        detsys = pyre.inventory.str('detsys') # detector system xml path
        z_rotation = pyre.inventory.float('z_rotation') # rotation around z (vertical) applied to detector system
        
    def main(self):
        neutrons = self.inventory.neutrons; neutrons = os.path.abspath(neutrons)
        workdir = self.inventory.workdir; workdir = os.path.abspath(workdir)
        if os.path.exists(workdir):
            raise IOError("%s already exists" % workdir)
        os.makedirs(workdir)
        
        nodes = self.inventory.nodes
        tofbinsize = self.inventory.tofbinsize
        tofmax = self.inventory.tofmax
        detsys = self.inventory.detsys
        if not detsys:
            instrument = self.inventory.instrument
            if not instrument:
                raise RuntimeError("Please specify instrument name or path to <instrument>.xml.fornxs")
            detsys = os.path.join(
                mcvinedir, 'share', 'mcvine', 'instruments', 
                instrument.upper(), '%s.xml.fornxs' % instrument)
        run(neutrons, workdir, 
            nodes=nodes, tofbinsize=tofbinsize, tofmax=tofmax, 
            detsys=detsys, z_rotation=z_rotation)
        return


    def help(self):
        print cmd_help
    

# main methods
def run(neutrons, workdir, **kwds):
    eventdat = sendneutronstodetsys(neutronfile=neutrons, workdir=workdir, **kwds)
    return


def sendneutronstodetsys(
    neutronfile=None, scattering_rundir=None, nodes=None, ncount=None,
    workdir = None, tofbinsize = None, tofmax=None, detsys = None,
    z_rotation = None,
    ):
    """
    run a simulation to send neutrons to det system
    
    workdir: directory where the simulation is run
    tofmax: unit: second
    tofbinsize: unit: microsecond
    
    z_rotation: angle of rotation applied to the detector system around z axis (vertical). unit: degree
    """
    # create workdir if it does not exist
    if not os.path.exists(workdir):
        os.makedirs(workdir)
        
    # number of neutrons scattered
    if not neutronfile:
        neutronfile = os.path.join(scattering_rundir, 'out', 'scattered-neutrons')
    if not ncount:
        from mcni.neutron_storage.idf_usenumpy import count
        ncount = count(neutronfile)
        
    # create simulation command
    cmd_name = 'sd'
    sim_cmd = os.path.join(workdir, cmd_name)
    open(sim_cmd, 'wt').write(sd_txt)
    
    
    # build command
    cmd = ['python '+cmd_name]
    args = {
        'source': 'NeutronFromStorage',
        'detsys': 'DetectorSystemFromXml',
        'output-dir': 'out',
        'detsys.tofparams': '0,%s,%s' % (tofmax, 1e-6*tofbinsize,), 
        'detsys.instrumentxml': detsys,
        'detsys.eventsdat': 'events.dat',
        'geometer.detsys': '(0,0,0), (0, %s, 0)' % z_rotation or 0,
        'ncount': ncount,
        'source.path': neutronfile,
        }
    if nodes:
        args['mpirun.nodes'] = nodes
    cmd += ['--%s=%s' % (k,v) for k,v in args.iteritems()]
    cmd = ' '.join(cmd)
    run_sh = os.path.join(workdir, 'run.sh')
    open(run_sh, 'w').write(cmd+'\n')
    execute(cmd, workdir)
    
    # events.dat
    outfile = os.path.join(workdir, 'out', 'events.dat')
    return outfile

sd_txt = """
import mcvine
from mcvine.applications.InstrumentBuilder import build
components = ['source', 'detsys']
App = build(components)
app = App('sd')
app.run()
"""


# utils
import os, subprocess as sp, shlex
def execute(cmd, workdir):
    print '* executing %s... ' % cmd
    args = shlex.split(cmd)
    p = sp.Popen(args, cwd=workdir)
    p.communicate()
    if p.wait():
        raise RuntimeError, "%r failed" % cmd
    return


import numpy as np
from mcvine.deployment_info import mcvinedir
import os, subprocess as sp

#
# version
__id__ = "$Id$"

# End of file 


