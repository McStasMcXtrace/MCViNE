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


class Binding:

    """data structure to hold information about a python-c binding project"""

    def __init__(self, python_package, binding_module,
                 c_headers, c_sources, python_sources,
                 c_libs = [], c_includes = []):
        self.python_package = python_package
        self.binding_module = binding_module
        self.c_headers = c_headers
        self.c_sources = c_sources
        self.python_sources = python_sources
        self.c_libs = c_libs
        self.c_includes = c_includes
        return


    pass # end of Binding    
                 


# version
__id__ = "$Id$"

# End of file 
