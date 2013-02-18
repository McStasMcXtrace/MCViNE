#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from mccomponents.homogeneous_scatterer.hsxml.parser.HomogeneousScatterer import HomogeneousScatterer as base

class HomogeneousScatterer( base ):

    onConstantQEKernel = onConstantEnergyTransferKernel = base.onKernel
    onBroadened_E_Q_Kernel = onE_Q_Kernel = onE_vQ_Kernel = base.onKernel
    onSQEkernel = base.onKernel
    onIsotropicKernel = base.onKernel


# version
__id__ = "$Id$"

# End of file 
