// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <iostream>
#include "mccomponents/kernels/sample/phonon/LinearlyInterpolatedDOS.h"


namespace test{

  using namespace DANSE::phonon;

  struct LinearlyInterpolatedDOS_Example {
    
    typedef std::vector<double> array_t;
    typedef LinearlyInterpolatedDOS<double, array_t> w_t;
    
    LinearlyInterpolatedDOS_Example ()
      : emin(0), emax(50)
    {
      array_t Z(50);
      for (size_t i=0; i<50; i++) {
	Z[i] = i*i;
      }
      
      dos = new w_t(0, 1., 50, Z);
    }
    
    ~LinearlyInterpolatedDOS_Example() {
      delete dos;
    }
    
    w_t *dos;
    double emin, emax;
  };

}

// version
// $Id$

// End of file
