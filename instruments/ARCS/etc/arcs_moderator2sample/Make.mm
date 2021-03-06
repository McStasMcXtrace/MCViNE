# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = arcs_moderator2sample
PACKAGE = 

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
# export

EXPORT_ETC = \
	arcs_moderator2sample.pml \
	fermichopper-100-1.5-SMI.odb \
	fermichopper-100-1.5-SMI.pml \
	fermichopper-700-1.5-SMI.odb \
	fermichopper-700-1.5-SMI.pml \
	fermichopper-700-0.5-AST.odb \
	fermichopper-700-0.5-AST.pml \
	guide511.pml.example \


export:: export-etc

# version
# $Id$

# End of file
