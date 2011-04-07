#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



class ComputationEngineRendererExtension:

    
    def onGridSQE(self, gridsqe):
        sqehist = gridsqe.sqehist
        
        qbb = sqehist.axisFromName('Q').binBoundaries().asNumarray()
        qbegin, qend, qstep = qbb[0], qbb[-1], qbb[1]-qbb[0]
        
        try:
            ebb = sqehist.axisFromName('E').binBoundaries().asNumarray()
        except KeyError:
            ebb = sqehist.axisFromName('energy').binBoundaries().asNumarray()
            
        ebegin, eend, estep = ebb[0], ebb[-1], ebb[1]-ebb[0]
        
        s = sqehist.data().storage().asNumarray()
        
        return self.factory.gridsqe(
            qbegin, qend, qstep,
            ebegin, eend, estep,
            s )


    def onSQE_fromexpression(self, sqe_fromexpression):
        expr = sqe_fromexpression.expression
        return self.factory.sqeFromExpression(expr)


    def onSQEkernel(self, sqekernel):
        
        t = sqekernel
        
        Erange = t.Erange
        Erange = self._unitsRemover.remove_unit( Erange, units.energy.meV )
        
        Qrange = t.Qrange
        Qrange = self._unitsRemover.remove_unit( Qrange, 1./units.length.angstrom )
        
        csqe = t.SQE.identify(self)
        
        abs = t.absorption_cross_section
        sctt = t.scattering_cross_section
        if abs is None or sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections( origin, include_density=False)
            sctt = inc + coh
            pass

        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), units.length.meter**2)
        
        unitcell_vol = t.unitcell_vol
        if unitcell_vol is None:
            origin = t.scatterer_origin
            structure = origin.phase.unitcell
            unitcell_vol = structure.lattice.getVolume()
            # convert to meter^3
            unitcell_vol *= 1.e-30
        
        return self.factory.sqekernel(
            abs, sctt, unitcell_vol,
            csqe, Qrange, Erange )


    def onIsotropicKernel(self, kernel):
        t = kernel

        abs = t.absorption_cross_section
        sctt = t.scattering_cross_section

        if abs is None or sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections( origin )
            sctt = inc + coh
            pass
        
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )
        
        return self.factory.isotropickernel(abs, sctt)


    def onConstantEnergyTransferKernel(self, kernel):
        t = kernel

        abs = t.absorption_cross_section
        sctt = t.scattering_cross_section

        if abs is None or sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections( origin )
            sctt = inc + coh
            pass
        
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )
        E = self._unitsRemover.remove_unit(kernel.E, units.energy.meV)
        return self.factory.constantEnergyTransferKernel(E, abs, sctt)


    def onConstantQEKernel(self, kernel):
        t = kernel

        abs = t.absorption_cross_section
        sctt = t.scattering_cross_section

        if abs is None or sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections( origin )
            sctt = inc + coh
            pass
        
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )
        Q = self._unitsRemover.remove_unit(kernel.Q, 1./units.length.angstrom)
        E = self._unitsRemover.remove_unit(kernel.E, units.energy.meV)
        return self.factory.constantQEKernel(Q, E, abs, sctt)


    def onE_Q_Kernel(self, kernel):
        t = kernel

        # cross section related
        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient

        if abs is None or sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections(origin, include_density=True)
            sctt = inc + coh
            pass
        
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )

        # functors
        E_Q = kernel.E_Q
        S_Q = kernel.S_Q

        # Q range
        Qmin = self._unitsRemover.remove_unit(
            kernel.Qmin, 1./units.length.angstrom)
        Qmax = self._unitsRemover.remove_unit(
            kernel.Qmax, 1./units.length.angstrom)
        
        return self.factory.E_Q_Kernel(E_Q, S_Q, Qmin, Qmax, abs, sctt)


    def onKernelContainer(self, kernelcontainer):
        #each kernel needs to know its scatterer origin.
        for kernel in kernelcontainer.elements():
            kernel.scatterer_origin = kernel
            continue
        return self.onCompositeKernel( kernelcontainer )
    
    
    pass # end of ComputationEngineRendererExtension



def register( type, renderer_handler_method, override = False ):
    '''register computing engine constructor method for a new type'''

    Renderer = ComputationEngineRendererExtension
    global _registry

    name = type.__name__
    methodname = 'on%s' % name
    if hasattr(Renderer, methodname):
        if not override:
            raise ValueError , "Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                type, methodname, _registry[name] )
        pass
    
    setattr( Renderer, methodname, renderer_handler_method )

    _registry[ name ] = type
    return
_registry = {}



from mccomponents.homogeneous_scatterer import registerRendererExtension
registerRendererExtension( ComputationEngineRendererExtension )


import units


# version
__id__ = "$Id$"

# End of file 
