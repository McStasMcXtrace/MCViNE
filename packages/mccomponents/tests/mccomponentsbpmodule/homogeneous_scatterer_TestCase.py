#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import unittestX as unittest
import journal

debug = journal.debug( "homogeneous_scatterer_TestCase" )
warning = journal.warning( "homogeneous_scatterer_TestCase" )


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class homogeneous_scatterer_TestCase(unittest.TestCase):

    def testHomogeneousNeutronScatterer(self):
        'HomogeneousNeutronScatterer'
        shape = mccompositebp.Block(1,1,1)

        from neutron_printer3 import cKernel as Printer
        printer = Printer( )

        mcweights = mccomponentsbp.MCWeights_AbsorptionScatteringTransmission()
        scatterer = mccomponentsbp.HomogeneousNeutronScatterer(
            shape, printer, mcweights )

        for i in range(10):
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )
            scatterer.scatter(ev)
            continue
        return

    def testCompositeScatteringKernel(self):
        'CompositeScatteringKernel'
        shape = mccompositebp.Block(1,1,1)

        from neutron_printer3 import cKernel as Printer
        printer = Printer( )

        kernels = mccomponentsbp.pointer_vector_Kernel(0)
        kernels.append( printer )

        kernelcomposite = mccomponentsbp.CompositeScatteringKernel( kernels )

        mcweights = mccomponentsbp.MCWeights_AbsorptionScatteringTransmission()
        scatterer = mccomponentsbp.HomogeneousNeutronScatterer(
            shape, kernelcomposite, mcweights )

        for i in range(10):
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )
            scatterer.scatter(ev)
            continue
        return


    def testRandom(self):
        'random, srandom'
        binding = mccomponentsbp
        
        binding.srandom( 1 )
        r11 = binding.random( 0, 1 )
        r12 = binding.random( 0, 1 )
        self.assert_( r11 != r12 )
        self.assert_( r11 >=0 and r11 <=1 )
        self.assert_( r12 >=0 and r12 <=1 )

        binding.srandom( 2 )
        r21 = binding.random( 0, 1 )
        r22 = binding.random( 0, 1 )
        self.assert_( r21 != r22 )
        self.assert_( r21 >=0 and r21 <=1 )
        self.assert_( r22 >=0 and r22 <=1 )
        self.assert_( r21 != r11 )
        self.assert_( r22 != r12 )
        
        binding.srandom( 1 )
        r31 = binding.random( 0, 1 )
        r32 = binding.random( 0, 1 )
        self.assert_( r31 != r32 )
        self.assert_( r31 >=0 and r31 <=1 )
        self.assert_( r32 >=0 and r32 <=1 )
        self.assert_( r31 == r11 )
        self.assert_( r32 == r12 )
        return

    pass  # end of homogeneous_scatterer_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(homogeneous_scatterer_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
