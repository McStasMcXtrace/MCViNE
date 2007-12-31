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

#include <iostream>
#include <cassert>
#include "mccomposite/mccomposite.h"
#include "mccomponents/CompositeScatteringKernel.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


class Kernel1: public mccomponents::AbstractScatteringKernel {
public:
  Kernel1( double mu, double sigma ) 
    : absorbed(0),
      scattered(0),
      m_mu(mu), 
      m_sigma(sigma)
  {}
  virtual double absorption_coefficient( const mcni::Neutron::Event & ev )
  {
    return m_mu;
  }
  virtual double scattering_coefficient( const mcni::Neutron::Event & ev )
  {
    return m_sigma;
  }
  virtual void scatter( mcni::Neutron::Event & ev ) 
  {
    scattered += ev.probability;
    return;
  }
  virtual void absorb( mcni::Neutron::Event & ev ) 
  {
    absorbed += ev.probability;
  }
  double absorbed, scattered, m_mu, m_sigma;
};



void test1()
{
  using namespace mccomponents;

  Kernel1 kernel1(1,1), kernel2(2,2);
  CompositeScatteringKernel::kernels_t kernels;
  kernels.push_back( &kernel1 );
  kernels.push_back( &kernel2 );
  CompositeScatteringKernel csk( kernels );
  
  mcni::Neutron::Event event, save;
  save.state.position = mccomposite::geometry::Position( 0,0, -5 );
  save.state.velocity = mccomposite::geometry::Direction( 0,0, 1 );
  
  event = save;
  
  assert (csk.absorption_coefficient( event ) == 3);
  assert (csk.scattering_coefficient( event ) == 3);

  size_t N = 10000;
  for (size_t i=0; i<N; i++) {
    event = save;
    csk.scatter( event );
  }
  
  assert( std::abs(kernel1.scattered-N/3.) < std::sqrt(N) * 2 );
  assert( std::abs(kernel2.scattered-N*2/3.) < std::sqrt(N) * 2 );

  for (size_t i=0; i<N; i++) {
    event = save;
    csk.absorb( event );
  }
  
  assert( std::abs(kernel1.absorbed-N/3.) < std::sqrt(N) * 2 );
  assert( std::abs(kernel2.absorbed-N*2/3.) < std::sqrt(N) * 2 );

}


int main()
{
#ifdef DEBUG
  //journal::debug_t("HomogeneousNeutronScatterer").activate();
  // journal::debug_t("CompositeNeutronScatterer_Impl").activate();
#endif
  test1();
  return 0;
}

// version
// $Id$

// End of file 
