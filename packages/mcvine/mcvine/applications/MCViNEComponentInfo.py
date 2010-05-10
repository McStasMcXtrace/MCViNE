#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from pyre.applications.Script import Script

class Application(Script):

    class Inventory(Script.Inventory):

        import pyre.inventory

        supplier = pyre.inventory.str('supplier')
        supplier.meta['tip'] = 'supplier of mcvine component. eg. mcstas2'
        
        category = pyre.inventory.str('category')
        category.meta['tip'] = 'category of mcvine component. eg. sources'

        type = pyre.inventory.str('type')
        type.meta['tip'] = 'type of mcvine component. eg. Source_simple'


    def help(self):
        print
        print 'Display information about a mcvine component type'
        print
        print ' mcvine-component-info --supplier=<supplier> --category=<category> --type=<type>'
        print 
        print 'Examples:'
        print 
        print ' mcvine-component-info --supplier=mcstas2 --category=sources --type=Source_simple'
        print
        print 'See also:'
        print
        print ' mcvine-list-components'
        return

    
    def main(self, *args, **kwds):
        supplier = self.supplier
        category = self.category
        type = self.type
        
        if not supplier or not category or not type:
            self.help()
            return
        
        import mcvine
        print mcvine.componentinfo(category=category, type=type, supplier=supplier)
        return


    def _configure(self):
        super(Application, self)._configure()
        self.supplier = self.inventory.supplier
        self.category = self.inventory.category
        self.type = self.inventory.type
        return


# version
__id__ = "$Id$"

# End of file 