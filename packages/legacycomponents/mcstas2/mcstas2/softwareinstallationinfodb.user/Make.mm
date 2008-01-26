# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = softwareinstallationinfodb
PACKAGE = softwareinstallationinfodb


RECURSE_DIRS = \

#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
    Info.py \
    __init__.py \
    boostpython.py \
    caltech_config.py \
    mcni.py \
    mcstas2.py \
    mcvine.py \
    mcvine_deps.py \
    pythia.py \

EXPORT_BINS = \

export:: export-python-modules export-binaries

# version
# $Id: Make.mm 470 2006-06-17 09:37:10Z linjiao $