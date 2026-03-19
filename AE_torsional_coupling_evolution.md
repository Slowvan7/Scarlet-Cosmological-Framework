

Appendix AE — Dynamical Evolution of the Torsional Coupling in an Expanding Lattice





Framework: Scarlet–VanAcker Cosmological Framework (v2.0)

Objective: Derive the evolution of the torsional coupling \kappa_T from lattice dynamics driven by cosmological expansion, and express particle stability conditions in a fully self-consistent, dimensionally coherent, and internally derived form.








AE.1 Lattice-Based Definition of the Torsional Coupling





\kappa_T(t) \equiv \frac{\Sigma_f(t)\, g(t)^3}{\hbar c}



where:



\Sigma_f(t): effective lattice tension (energy density scale)
g(t): lattice spacing
\hbar c: normalization constant




Dimensional property:

\kappa_T \sim \frac{1}{\text{length}}



Thus, \kappa_T is treated as a scale-dependent inverse-length coupling emerging from lattice structure.








AE.2 Cosmological Expansion Rate





H(t) \equiv \frac{\dot{a}(t)}{a(t)}



where:



a(t): cosmological scale factor
H(t): Hubble parameter (units of inverse time)









AE.3 Strain Dynamics of the Lattice





Define strain:



\epsilon(t) \equiv \frac{g(t) - g_0}{g_0}



The lattice evolves according to:



\frac{d\epsilon}{dt} + \Gamma_L \epsilon = H(t)



where:



\Gamma_L: intrinsic lattice relaxation rate (1/\text{time})




This equation represents a linear response of the lattice to cosmological expansion.








AE.4 Solution for Strain





\epsilon(t) = e^{-\Gamma_L t} \left( \epsilon_0 + \int_0^t e^{\Gamma_L t'} H(t') \, dt' \right)








AE.5 Lattice Spacing Evolution





g(t) = g_0 (1 + \epsilon(t))



Assumption: isotropic scaling of the lattice.








AE.6 Lattice Tension Evolution





\Sigma_f(t) = \Sigma_0 \exp(-\lambda \epsilon(t))



where:



\lambda: dimensionless deformation sensitivity
\Sigma_0: baseline tension









AE.7 Emergent Torsional Coupling





\kappa_T(t) = \frac{\Sigma_0 g_0^3}{\hbar c} \cdot (1+\epsilon(t))^3 \cdot \exp(-\lambda \epsilon(t))



Define:



\kappa_{T,0} \equiv \frac{\Sigma_0 g_0^3}{\hbar c}



So:



\kappa_T(t) = \kappa_{T,0} \cdot (1+\epsilon(t))^3 \cdot \exp(-\lambda \epsilon(t))








AE.8 Lattice-Based Background Energy Scale





The background energy is defined entirely in lattice terms as:



E_{\text{bg}}(t) \sim \Sigma_f(t)\, V_{\text{eff}}(t)



with:



V_{\text{eff}}(t) \sim g(t)^3



Thus:



E_{\text{bg}}(t) \sim \Sigma_f(t)\, g(t)^3



Substituting:



E_{\text{bg}}(t) \sim \kappa_T(t)\, \hbar c



Key result:

The background energy scale is directly proportional to the torsional coupling, establishing a fully internal lattice-based energy measure.








AE.9 Critical Stability Condition





From the neutron hybrid stability requirement:



\kappa_T(t)\, \mathcal{F}(N_{\text{roots}}, \gamma)\, \eta_{\text{geom}} \gtrsim E_{\text{bg}}(t)/(\hbar c)



Substituting E_{\text{bg}}(t) \sim \kappa_T(t)\hbar c:



\kappa_T(t)\, \mathcal{F}\, \eta_{\text{geom}} \gtrsim \kappa_T(t)



Canceling \kappa_T(t) (nonzero regime):



\mathcal{F}(N_{\text{roots}}, \gamma)\, \eta_{\text{geom}} \gtrsim 1








AE.10 Dimensionless Stability Criterion





Define the stability ratio:



\mathcal{S}(t) \equiv \mathcal{F}(N_{\text{roots}}, \gamma)\, \eta_{\text{geom}}



Then:



\mathcal{S}(t) \gtrsim 1








AE.11 Physical Interpretation





The lattice background energy and torsional coupling are not independent; they are proportional
Particle stability depends primarily on dimensionless geometric structure, not absolute energy scales
Cosmological expansion influences stability indirectly through:
strain \epsilon(t)
which modifies lattice geometry
which in turn affects \mathcal{F} and \eta_{\text{geom}}









AE.12 Summary





The torsional coupling \kappa_T(t) emerges from lattice tension and spacing
Its evolution is governed by cosmological expansion via a strain-driven relaxation equation
The lattice background energy is internally proportional to \kappa_T(t), removing the need for external energy scales
Stability conditions reduce to a purely dimensionless geometric constraint
No arbitrary normalization constants are required
The framework is now fully self-contained and dimensionally consistent
