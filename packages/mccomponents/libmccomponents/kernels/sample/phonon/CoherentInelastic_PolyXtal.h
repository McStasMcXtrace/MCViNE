// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2005 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef PHONON_COHERENTINELASTIC_POLYXTAL_H
#define PHONON_COHERENTINELASTIC_POLYXTAL_H

#include <memory>
#include "KernelBase.h"
#include "AtomicScatterer.h"
#include "vector3.h"

//forward declaration
namespace DANSE{
  namespace phonon{
    class AbstractDispersion_3D;
    template <typename Float> 
    class AbstractDebyeWallerFactorCalculator;
  }
}

namespace mccomponents{
  
  namespace kernels{

    namespace phonon{

      //! coherent inelastic phonon scattering. polycrystalline sample.
      class CoherentInelastic_PolyXtal : public KernelBase {
      public:
	// typedefs
	typedef double float_t;
	typedef mcni::Vector3<float_t> R_t;
	typedef mcni::Vector3<float_t> K_t;
	typedef mcni::Vector3<float_t> V_t;
	typedef DANSE::phonon::AbstractDispersion_3D dispersion_t;
	typedef std::complex<float_t> complex_t;
	typedef mcni::Vector3< complex_t > epsilon_t;
	typedef AtomicScatterer atom_t;
	typedef std::vector< atom_t >  atoms_t;
	typedef DANSE::phonon::AbstractDebyeWallerFactorCalculator<float_t> dwcalculator_t;
	typedef mcni::Neutron::Event neutron_t;
	
	//! ctor
	/*!
	  parameters
	   max_omega   maximum phonon energy
	   a,b,c       lattice vectors
	   dw_calctor  debye waller factor calculator
	   temperature temperature. unit: K
	   epsilon     small number to avoid divide by 0 error
	*/
	CoherentInelastic_PolyXtal
	( const dispersion_t &disp,
	  const atoms_t &atoms,
	  const R_t &a, const R_t &b, const R_t &c,
	  dwcalculator_t & dw_calctor,
	  float_t temperature,
	  float_t max_omega,
	  float_t min_omega = 0.01,
	  float_t epsilon = 1.e-10 ) ;
	
	virtual float_t absorption_coefficient( const neutron_t & ev );
	virtual float_t scattering_coefficient( const neutron_t & ev );
	virtual void S( neutron_t & ev );
	virtual void absorb( neutron_t & ev );

      private:
	
	// data
	const dispersion_t & m_disp;
	atoms_t m_atoms;
	R_t m_a, m_b, m_c;
	dwcalculator_t *m_DW_calc;
	float_t m_Temperature;
	float_t m_uc_vol;
	
	float_t m_max_omega, m_min_omega;
	
	float_t m_total_scattering_xs;
	float_t m_total_absorption_xs;
	
	float_t m_epsilon;
	
	// implementation details
	struct Details;
	std::auto_ptr<Details> m_details;
      };

    } // phonon::
  } // kernels::
} // mccomponents::

#endif//  PHONON_COHERENTINELASTIC_POLYXTAL_H



// version
// $Id$

// End of file 
