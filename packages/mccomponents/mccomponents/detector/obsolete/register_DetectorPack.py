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


# the interface
from register_CompositeDetector import CompositeDetector as base
class DetectorPack(base):
    def identify(self, visitor): return visitor.onDetectorPack(self)
    pass


# 2. the handler to construct c++ engine
def onDetectorPack(self, detectorPack):
    return self.onCompositeDetector( detectorPack )


# 4. register the new class and handlers
import mccomponents.homogeneous_scatterer as mh
mh.register_engine_renderer_handler (DetectorPack, onDetectorPack )




def onDetectorPackCopy(self, copy):
    pack = copy.reference()
    return self.onDetectorPack(pack)

class DetectorPackCopy: pass
mh.register_engine_renderer_handler( DetectorPackCopy, onDetectorPackCopy )



# version
__id__ = "$Id$"

# End of file 
