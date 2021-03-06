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


from AbstractVisitor import AbstractVisitor

class KernelComputationEngineRenderer( AbstractVisitor ):


    def __init__(self, factory):
        self.factory = factory
        return


    def render(self, target):
        return target.identify(self)
    

    def onCompositeKernel(self, composite):
        factory = self.factory
        
        elements = composite.elements()
        
        ckernels = factory.kernelcontainer()
        cweights = factory.binding.vector_double(len(elements))
        for index, element in enumerate(elements):
            ckernel = element.identify(self) 
            ckernels.append( ckernel )
            w = getattr(element, 'weight', None)
            if w is None:
                import warnings
                scatterer = getattr(element, 'scatterer_origin', None)
                if scatterer:
                    scatterer = str(scatterer).split(':')[0]
                    warnings.warn(
                        'kernel %s of %s does not define its weight' % (
                            element.__class__.__name__, scatterer,
                            )
                    )
            cweights[index] = w or 1.
            print "weight: ", cweights[index]
            continue

        return factory.compositekernel( ckernels, cweights, composite.average )

    
    def onHomogeneousScatterer(self, scatterer):
        factory = self.factory

        ckernel = scatterer.kernel().identify(self)

        cshape = scatterer.shape().identify(self)

        mcweights = scatterer.mcweights

        max_multiplescattering_loops = scatterer.max_multiplescattering_loops
        min_neutron_probability = scatterer.min_neutron_probability
        packing_factor = scatterer.packing_factor
        
        return factory.homogeneousscatterer( 
            cshape, ckernel, mcweights, 
            max_multiplescattering_loops, min_neutron_probability, 
            packing_factor)
    

    pass # end of KernelComputationEngineRenderer


def register( kernel_type, renderer_handler_method, override = False ):
    '''register computing engine constructor method for a new kernel type'''
    
    global _registry

    name = kernel_type.__name__
    methodname = 'on%s' % name
    if hasattr(KernelComputationEngineRenderer, methodname):
        if not override:
            raise ValueError , "Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                kernel_type, methodname, _registry[name] )
        pass
    
    setattr( KernelComputationEngineRenderer, methodname, renderer_handler_method )

    _registry[ name ] = kernel_type
    return


_registry = {}
def _init_registry():
    from CompositeKernel import CompositeKernel
    _registry['CompositeKernel'] = CompositeKernel
    from HomogeneousScatterer import HomogeneousScatterer
    _registry['HomogeneousScatterer'] = HomogeneousScatterer
    return


_init_registry()



def extend( klass ):
    "extend renderer class with the new class"
    global KernelComputationEngineRenderer
    old = KernelComputationEngineRenderer
    class _( klass, old ): pass
    KernelComputationEngineRenderer = _
    return


# version
__id__ = "$Id$"

# End of file 
