#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import units
meV = units.energy.meV
angstrom = units.length.angstrom


def coherentinelastic_polyxtal_kernel(
    dispersion,
    Ei = 70*meV, max_omega = 55 *meV, max_Q = 12 / angstrom,
    nMCsteps_to_calc_RARV = 10000):
    from CoherentInelastic_PolyXtal_Kernel import CoherentInelastic_PolyXtal_Kernel as f
    return f( dispersion, Ei, max_omega, max_Q, nMCsteps_to_calc_RARV )


def linearlyinterpolateddispersion(
    nAtoms, dimension,
    Qaxes, eps_npyarr, E_npyarr,
    **kwds
    ):
    from LinearlyInterpolatedDispersionOnGrid \
         import LinearlyInterpolatedDispersionOnGrid
    return LinearlyInterpolatedDispersionOnGrid(
        nAtoms, dimension,
        Qaxes, eps_npyarr, E_npyarr,
        **kwds)


def periodicdispersion( dispersion, reciprocalcell ):
    from PeriodicDispersion import PeriodicDispersion
    return PeriodicDispersion( dispersion, reciprocalcell )


def dispersion_fromidf( datapath ):
    from mccomponents.sample.idf import readDispersion
    nAtoms, dimension, Qaxes, polarizations, energies, dos = readDispersion( datapath )
        
    dispersion = linearlyinterpolateddispersion(
        nAtoms, dimension,
        Qaxes, polarizations, energies, dos = dos )

    return dispersion


def periodicdispersion_fromidf( datapath ):
    dispersion = dispersion_fromidf( datapath )
    
    from mccomponents.sample.idf import readDispersion
    nAtoms, dimension, Qaxes, polarizations, energies, dos = readDispersion( datapath )
    reciprocalcell = [ bi for bi,n in Qaxes ]
    
    return periodicdispersion(dispersion, reciprocalcell)
    

import ComputationEngineRendererExtension

#make bindings available
def _import_bindings():
    import bindings
    return

_import_bindings()



# version
__id__ = "$Id$"

# End of file 