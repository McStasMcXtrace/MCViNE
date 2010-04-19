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

class App(Script):

    class Inventory(Script.Inventory):

        import pyre.inventory

        supplier = pyre.inventory.str('supplier')
        supplier.meta['tip'] = 'supplier of mcvine component. eg. mcstas2'
        
        category = pyre.inventory.str('category')
        category.meta['tip'] = 'category of mcvine component. eg. sources'

        type = pyre.inventory.str('type')
        type.meta['tip'] = 'type of mcvine component. eg. Source_simple'

    
    def main(self, *args, **kwds):
        supplier = self.supplier
        category = self.category
        type = self.type
        
        import mcvine
        print mcvine.componentinfo(category=category, type=type, supplier=supplier)
        return


    def __init__(self, name='mcvine-component-info'):
        super(App, self).__init__(name)
        return


    def _configure(self):
        super(App, self)._configure()
        self.supplier = self.inventory.supplier
        self.category = self.inventory.category
        self.type = self.inventory.type
        return


def main():
    app = App()
    app.run()
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
