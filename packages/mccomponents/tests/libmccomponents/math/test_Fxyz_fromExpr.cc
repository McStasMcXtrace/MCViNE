// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2010  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include <iostream>
#include <cassert>
#include <string>
#include <cmath>
#include "mcni/test/assert.h"
#include "mccomponents/math/Fxyz_fromExpr.h"


using mcni::assertAlmostEqual;


int test1()
{
  std::string function = "sin(x+y+z)";
  std::cout << "* Testing " << function << std::endl;

  double pi = 3.1415926535897932;

  mccomponents::math::Fxyz_fromExpr f(function);
  
  assertAlmostEqual( f(0,0,0), 0 );
  assertAlmostEqual( f(pi,0,0), 0);
  assertAlmostEqual( f(0,pi,0), 0);
  assertAlmostEqual( f(0,0,pi), 0);
  assertAlmostEqual( f(pi/2,0,0), 1);
  assertAlmostEqual( f(0,pi/2,0), 1);
  assertAlmostEqual( f(0,0,pi/2), 1);
  
  return 0;
}


int main()
{
  std::cout << "== Fxyz_fromExpr tests ==" << std::endl;
  if (test1()) return 1;
  std::cout << "* All tests passed" << std::endl;
  return 0;
}

// version
// $Id: test_fparser.cc 854 2011-02-09 12:51:28Z linjiao $

// End of file 
