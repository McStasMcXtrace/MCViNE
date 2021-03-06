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


# autotest will skip this one
skip = True



import unittestX as unittest
import journal


class build_TestCase(unittest.TestCase):

    def test(self):
        "binding builder using mm"
        from mcstas2.wrappers.binding_builder.mm import build
        from mcstas2.wrappers.binding_builder.Binding import Binding
        binding = Binding(
            python_package = 'projectname', binding_module = 'projectname',
            c_headers = [
            'src/bindings.h',
            'src/exceptions.h',
            'src/misc.h',
            ],
            c_sources = [
            'src/bindings.cc',
            'src/exceptions.cc',
            'src/misc.cc',
            'src/projectnamemodule.cc',
            ],
            python_sources = [
            'src/__init__.py',
            ],
            c_libs = [
            ],
            c_includes = [
            ],
            )
        build(binding)

        import projectname.projectname as p
        self.assertEqual( p.hello(), 'hello' )
        return

    pass  # end of build_TestCase



def pysuite():
    suite1 = unittest.makeSuite(build_TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
