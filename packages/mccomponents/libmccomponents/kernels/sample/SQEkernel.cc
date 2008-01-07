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


#include <cmath>
#include "mccomponents/kernels/sample/SQEkernel.h"
#include "mccomponents/kernels/sample/AbstractSQE.h"
#include "mccomponents/exception.h"
#include "mccomponents/math/random.h"
#include "mccomponents/physics/constants.h"


struct mccomponents::kernels::SQEkernel::Details {
  random::Generator random_number_generator;
};


mccomponents::kernels::SQEkernel::SQEkernel
( double absorption_cross_section,
  double scattering_cross_section,
  const sample::AbstractSQE & sqe, 
  double Qmin, double Qmax,
  double Emin, double Emax) 
  : m_absorption_cross_section( absorption_cross_section ),
    m_scattering_cross_section( scattering_cross_section ),
    m_epsilon(1.e-10),
    m_Qmin(Qmin), m_Qmax(Qmax), m_DQ(Qmax-Qmin),
    m_Emin(Emin), m_Emax(Emax), m_DE(Emax-Emin),
    m_sqe(sqe),
    m_details( new Details )
{}


double
mccomponents::kernels::SQEkernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  // !!!!!!!!!!!!!!!!
  // we need better implementation here
  return m_absorption_cross_section;
}


double
mccomponents::kernels::SQEkernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  // !!!!!!!!!!!!!!!!
  // we need better implementation here
  return m_scattering_cross_section;
}


void
mccomponents::kernels::SQEkernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::SQEkernel::scatter
( mcni::Neutron::Event & ev )
{
  typedef mcni::Neutron::State::position_t position_t;
  typedef mcni::Neutron::State::velocity_t velocity_t;
  typedef mcni::Vector3<double> V3d;

  namespace conversion = mcni::neutron_units_conversion;

  // input neutron state
  mcni::Neutron::State & state = ev.state;
  // incident neutron velocity, energy
  double vi = state.velocity.length();
  double Ei = conversion::v2E( vi ), ki = conversion::v2k * vi;

  // randomly pick energy transfer
  double E;
  if (m_Emin > Ei) return; // if Ei is too small, won't scatter. nothing happen
  E = m_details->random_number_generator.generate( m_Emin, std::min(Ei, m_Emax) );

  // final energy, wave vector
  double Ef = Ei - E;
  double kf = conversion::E2k(Ef);

  // randomly pick momentum transfer
  // Q must satisfy abs(ki-kf)<Q<ki+kf and Qmin<Q<Qmax
  double Qmin = std::max(m_Qmin, std::abs(ki-kf)),
    Qmax = std::min(m_Qmax, ki+kf);
  if (Qmax<Qmin) return; // no scatter
  double Q = m_details->random_number_generator.generate(Qmin, Qmax);

  // adjust probability of neutron event
  // !!!!!!!!!
  // need normalization factor here
  ev.probability *= m_sqe(Q,E);

  // figure out the direction of the out-going neutron
  double cost = (kf*kf + ki*ki - Q*Q)/2/kf/ki;

  double sint = sqrt(1-cost*cost);

  double phi = m_details->random_number_generator.generate(0, 2 * physics::pi);

  double cosp = cos(phi), sinp = sin(phi);

  V3d e1 = ev.state.velocity; e1.normalize();

  // if e1 is not in z-direction
  // we set e2 to be the cross product of e1 and (0,0,1)
  // if e1 is right on the z-direction, that means e1 = (0,0,1)
  // and we set e2 = (1,0,0) or whatever
  V3d e2;
  if (abs(e1.x)>m_epsilon || abs(e1.y)>m_epsilon) { 
    e2 = V3d(0,0,1) * e1; e2.normalize();
  } else {
    e2 = V3d(1,0,0);
  }

  V3d e3 = e1 * e2;

  V3d ekf = e1*cost + e2*sint*cosp + e3 *sint*sinp;
  
  ev.state.velocity = ekf * (kf*conversion::k2v);
}



// version
// $Id$

// End of file 