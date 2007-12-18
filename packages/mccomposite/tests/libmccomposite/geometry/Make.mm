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

PROJECT = mccomposite
PACKAGE = tests

PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_PYTESTS =  alltests.py
PROJ_CPPTESTS = testPrinter testArrowIntersector testDilation testLocator
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -ljournal -lmccomposite -lmcni -lmcstas_compact


#--------------------------------------------------------------------------
#

all: $(PROJ_TESTS)

test:
	for test in $(PROJ_TESTS) ; do $${test}; done

release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#

testDilation: testDilation.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testDilation.cc $(PROJ_LIBRARIES)

testPrinter: testPrinter.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testPrinter.cc $(PROJ_LIBRARIES)

testLocator: testLocator.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testLocator.cc $(PROJ_LIBRARIES)

testArrowIntersector: testArrowIntersector.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testArrowIntersector.cc $(PROJ_LIBRARIES)


# version
# $Id: Make.mm 620 2007-07-11 23:24:50Z linjiao $

# End of file
