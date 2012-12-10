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



import mccomposite.bindings
mccomposite.bindings.get('BoostPython')
import mccomponents.mccomponentsbp as binding


from AbstractBinding import AbstractBinding as Interface
from mccomposite.bindings.BoostPythonBinding import BoostPythonBinding as base


class BoostPythonBinding(base, Interface):

    '''factory class of boost python computing engine of scatterers
    '''

    def srandom(self, seed):
        return binding.srandom( seed )
    

    def compositekernel(self, kernels, average):
        return binding.CompositeScatteringKernel( kernels, average )


    def kernelcontainer(self, size = 0):
        return binding.pointer_vector_Kernel( size )


    def homogeneousscatterer(self, shape, kernel, weights):
        cweights = binding.MCWeights_AbsorptionScatteringTransmission( *weights )
        return binding.HomogeneousNeutronScatterer(shape, kernel, cweights )


    pass # end of BoostPythonBinding


def register( methodname, method, override = False ):
    '''register a new handling method'''
    if hasattr(BoostPythonBinding, methodname):
        if not override:
            raise ValueError , "Cannot register handler %s. "\
                  "It was already registered." % (
                methodname )
        pass
    
    setattr( BoostPythonBinding, methodname, method )

    return


def extend( klass ):
    "extend binding class with the new class"
    global BoostPythonBinding
    old = BoostPythonBinding
    class _( klass, old ): pass
    BoostPythonBinding = _
    return


# version
__id__ = "$Id$"

# End of file 
