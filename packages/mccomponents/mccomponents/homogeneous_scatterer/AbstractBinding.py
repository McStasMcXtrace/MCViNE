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


class AbstractBinding:


    def srandom(self, seed):
        raise NotImplementedError


    def homogeneousscatterer(self, shape, kernel, weights):
        raise NotImplementedError
    
        
    def compositekernel(self, kernels):
        raise NotImplementedError


    def kernelcontainer(self):
        raise NotImplementedError


    pass # end of AbstractBinding


# version
__id__ = "$Id$"

# End of file 
