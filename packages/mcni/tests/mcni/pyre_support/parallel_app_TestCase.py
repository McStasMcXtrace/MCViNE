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


import sys
sys.argv.append('--mpirun.nodes=2')


import unittestX as unittest
import journal

debug = journal.debug( "mcni.pyre_support.test" )
warning = journal.warning( "mcni.pyre_support.test" )


class TestCase(unittest.TestCase):


    def test(self):
        'mcni.pyre_support: a simple pyre simulation app'
        app = App('test-parallel-app')
        app.testFacility = self
        app.run()
        return
    
        
    pass  # end of TestCase



from mcni.pyre_support.MpiApplication import Application as base
class App(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        pass # end of Inventory


    def main(self):
        super(App, self).main()
        from mcni.utils.mpi import rank
        print "in app.main(): mode=%s, rank=%s" % (
            self.inventory.mode, rank)
        return

    
    def _defaults(self):
        super(App, self)._defaults()
        return



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    import journal
    journal.info('mpirun').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
