// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>
#include "mccomposite/mccomposite.h"


namespace wrap_mccomposite {

  typedef mccomposite::geometry::Vector Vector;
  inline double V3_getitem( const Vector & v3, size_t i)
  {
    return v3[i];
  }
  
  inline size_t V3_size( const Vector & v3)
  {
    return Vector::size();
  }
  
  void wrap_basics()
  {
    using namespace boost::python;
    class_<Vector>
      ("Vector",
       init<double, double, double>()
       )
      .def(init<> () )
      .def("__len__", &V3_size )
      .def("__getitem__", &V3_getitem)
      .def("__iter__", iterator<Vector>() )
      ;

    class_<mccomposite::geometry::RotationMatrix>
      ("RotationMatrix",
       init<double, double, double, double, double, double, double, double, double>()
       )
      .def(init<> () )
      ;
  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
