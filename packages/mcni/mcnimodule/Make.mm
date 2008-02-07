# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = mcni
PACKAGE = mcnimodule
MODULE = mcni

include std-pythonmodule.def
include local.def

PROJ_CXX_SRCLIB = -lmcni -lbpext

PROJ_SRCS = \
	bindings.cc \
	exceptions.cc \
	misc.cc \
	register_bp_voidptr_converters.cc \


# version
# $Id$

# End of file
