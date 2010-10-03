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

import journal
debug = journal.debug("homogeneous_scatterer.xmlparser")


from pyre.xml.Node import Node
import urllib



class XMLFormatError(Exception): pass


class AbstractNode(Node):

    def content(self, content):
        debug.log( "content=%s" % content )
        content = content.strip()
        if len(content)==0: return
        #...
        self.locator = self.document.locator
        return


    def _parse(self, expr):
        return self._parser.parse(expr)

    from pyre.units import parser
    _parser = parser()
    pass




# version
__id__ = "$Id$"

# End of file 
