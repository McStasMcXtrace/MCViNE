// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#ifndef MCCOMPOSITE_GEOMETRY_OPERATIONS_DIFFERENCE_H
#define MCCOMPOSITE_GEOMETRY_OPERATIONS_DIFFERENCE_H


#include "Composition.h"


namespace mccomposite {
  
  namespace geometry {
    
    struct Difference: public Composition {
      
      //meta methods
      Difference( const AbstractShape & body1, const AbstractShape & body2)
	: Composition( body1, body2 )
      {}
      virtual ~Difference( ) {};
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const 
      {
	visitor.visit( this );
      }
    };
    
  }
  
}


#endif

// version
// $Id$

// End of file 
