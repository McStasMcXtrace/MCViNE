#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2009 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
fcc Ni scatterer constructed from an xml file
'''


import unittestX as unittest
import journal



class TestCase(unittest.TestCase):

    interactive = False

    def test(self):
        "fcc Ni scatterer constructed from an xml file"
        
        from mcstas2 import componentfactory
        category = 'monitors'
        componentname = 'IQE_monitor'
        factory = componentfactory( category, componentname )

        Qmin=0; Qmax=13.; nQ=130
        Emin=-50; Emax=50.; nE=100
        
        component = factory(
            'component',
            Ei=Ei,
            Qmin=Qmin, Qmax=Qmax, nQ=nQ,
            Emin=Emin, Emax=Emax, nE=nE,
            max_angle_out_of_plane=30, min_angle_out_of_plane=-30,
            max_angle_in_plane=120, min_angle_in_plane=-30,
            )

        scatterer = makeScatterer()
        
        import mcni
        N = 10000
        neutrons = mcni.neutron_buffer( N )
        for i in range(N):
            neutron = mcni.neutron(r=(0,0,0), v=(0,0,vi), time=0, prob=1)
            scatterer.scatter(neutron)
            neutrons[i] = neutron
            #print neutrons[i]
            continue
        
        component.process( neutrons )
        
        hist = get_histogram(component)
        import os
        f = os.path.basename(__file__)
        filename = 'IQE-%s.h5' % f
        if os.path.exists(filename): os.remove(filename)
        import histogram.hdf as hh
        hh.dump(hist, filename, '/', 'c')
        
        if self.interactive:
            from histogram.plotter import defaultPlotter
            defaultPlotter.plot(hist)
        return

    pass  # end of TestCase



mass = 50
temperature = 300
Ei = 70
from mcni.utils import conversion as C
vi = C.e2v(Ei)



def makeScatterer():
    import mccomponents.sample.phonon.xml
    from mccomponents.sample.kernelxml import parse_file
    scatterer = parse_file('fccNi-plate-scatterer-cubic-reciprocal-unitcell.xml')
    kernel = scatterer.kernel()

    from sampleassembly.predefined import shapes
    plate = shapes.plate(width=0.04, height=0.10, thickness=0.003)
    scatterer._shape = plate

    from sampleassembly import elements
    sample = elements.powdersample('fccNi', shape=plate)

    crystal = elements.crystal(unitcell=makeUnitcell())
    sample.phase = crystal

    kernel.scatterer_origin = sample
    
    from mccomponents.homogeneous_scatterer import scattererEngine
    return scattererEngine(scatterer)


def makeUnitcell():
    from matter import Atom, Structure, Lattice
    atoms = [Atom('Ni')]
    # positions = [(0,0,0)]
    cellvectors = [ (3.57,0,0), (0,3.57,0), (0,0,3.57) ]
    lattice = Lattice(base=cellvectors)
    return Structure(lattice=lattice, atoms=atoms)



from mcstas2.pyre_support._component_interfaces.monitors.IQE_monitor import get_histogram
import numpy as N


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    TestCase.interactive = True
    #debug.activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    #journal.debug('phonon_coherent_inelastic_polyxtal_kernel').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
