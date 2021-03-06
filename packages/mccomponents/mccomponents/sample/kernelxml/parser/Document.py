#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C) 2005-2013  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mccomponents.homogeneous_scatterer.hsxml.parser.Document import Document as base


class Document(base):
    
    
    tags = [
        'HomogeneousScatterer',
        'KernelContainer',
        
        'SQEkernel',
        'GridSQE',
        'SQE_fromexpression',
        'ConstantEnergyTransferKernel',
        'ConstantQEKernel', 'ConstantvQEKernel',
        'E_Q_Kernel',
        'Broadened_E_Q_Kernel', 
        'E_vQ_Kernel',
        
        'IsotropicKernel',
        ]
    
    
    pass # end of Document

# version
__id__ = "$Id$"

# End of file 
