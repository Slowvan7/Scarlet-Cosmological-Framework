

Appendix AI — First-Rule Torsion Framework (Final Consistent Formulation)










AI.1 Fundamental Postulate (First Rule)





We postulate a microscopic alignment principle:



\boxed{ \text{Microscopic degrees of freedom evolve toward alignment with a common center governed by fundamental scales } t_* \text{ and } \ell_*. }



with:



t_* = 10^{-41}\,\text{s}, \quad \ell_* = 10^{-35}\,\text{m}



These define the fundamental temporal and spatial scales of the theory.



To ensure macroscopic consistency, we define an emergent propagation speed:



\boxed{ c_{\text{eff}} = \frac{\ell_*}{t_*} }



This quantity sets the characteristic propagation speed of alignment dynamics. Depending on interpretation, it may coincide with the physical speed of light or represent a distinct fundamental propagation scale.








AI.2 Expansion Parameter





We define a small dimensionless parameter:



\boxed{ \beta \equiv \frac{\ell_*}{L}, \quad \beta \ll 1 }



where L is a macroscopic length scale.



All fields are treated perturbatively in powers of \beta.








AI.3 Tetrad Field (Fundamental Variable)





The geometric degrees of freedom are encoded in the tetrad:



\boxed{ e^a_{\ \mu}(x) = \delta^a_{\ \mu} + \beta\, \omega^a_{\ \mu}(x) }



where:



\omega^a_{\ \mu}(x) is dimensionless
|\beta \, \omega^a_{\ \mu}| \ll 1 ensures perturbative control
The tetrad is invertible: \det(e^a_{\ \mu}) \neq 0









AI.4 Metric Construction





The spacetime metric is defined by:



\boxed{ g_{\mu\nu} = \eta_{ab}\, e^a_{\ \mu} e^b_{\ \nu} }



Expanding to first order in \beta:



g_{\mu\nu} = \eta_{\mu\nu} + \beta\left(\omega_{\mu\nu} + \omega_{\nu\mu}\right) + \mathcal{O}(\beta^2)








AI.5 Connections







AI.5.1 Levi-Civita Connection





Defined by metric compatibility:



\boxed{ \nabla_\lambda g_{\mu\nu} = 0 }



It produces curvature via second derivatives of the metric:



G_{\mu\nu} \sim \partial^2 g








AI.5.2 Weitzenböck Connection





\boxed{ \Gamma^{(W)\lambda}_{\ \ \mu\nu} = e^\lambda_a \, \partial_\nu e^a_{\ \mu} }



Properties:



\boxed{ \nabla^{(W)}_\lambda g_{\mu\nu} = 0 }



\boxed{ R^\rho_{\ \sigma\mu\nu}\big(\Gamma^{(W)}\big) \equiv 0 }








AI.6 Torsion Tensor





\boxed{ T^\lambda_{\ \mu\nu} = \Gamma^{(W)\lambda}_{\ \ \mu\nu} - \Gamma^{(W)\lambda}_{\ \ \nu\mu} }



Scaling:



\boxed{ T^\lambda_{\ \mu\nu} \sim \frac{\beta}{L} = \frac{\ell_*}{L^2} }



Dimensional consistency:



[T] = L^{-1}








AI.7 Scaling Hierarchy





Curvature (Einstein tensor scale):



\boxed{ G_{\mu\nu} \sim \frac{\beta}{L^2} = \frac{\ell_*}{L^3} }



Torsion invariant:



\boxed{ \mathcal{I}_T \sim T^2 \sim \frac{\beta^2}{L^2} = \frac{\ell_*^2}{L^4} }



Hierarchy:



\boxed{ \mathcal{I}_T \ll G_{\mu\nu} \quad \text{for } \beta \ll 1 }








AI.8 Effective Action (Dimensionally Consistent)





\boxed{ S = \int d^4x \, \sqrt{-g} \left[ \frac{1}{2\kappa} R(\nabla) + \frac{\alpha}{\ell_*^2}\,\mathcal{I}_T \right] }



where:



R(\nabla): Ricci scalar of the Levi-Civita connection
\mathcal{I}_T: quadratic torsion invariant
\kappa \sim \ell_*^2
\alpha is dimensionless
The factor 1/\ell_*^2 ensures dimensional consistency









AI.9 Torsion Invariant





\boxed{ \mathcal{I}_T = a_1 T^\rho_{\ \mu\nu} T_\rho^{\ \mu\nu} + a_2 T^\rho_{\ \mu\nu} T^{\nu\mu}_{\ \ \rho} + a_3 T^\rho_{\ \mu\rho} T^\sigma_{\ \ \nu\sigma} }



with constants a_i.








AI.10 Field Equations (Effective Form)





Variation of the action yields:



\boxed{ G_{\mu\nu} + \frac{\alpha}{\ell_*^2}\kappa \,\Theta_{\mu\nu} = \kappa T_{\mu\nu} }



where:



T_{\mu\nu}: matter stress-energy tensor
\Theta_{\mu\nu}: effective contribution from torsion invariants









AI.11 Limiting Behavior







GR Limit





\ell_* \to 0 \quad \Rightarrow \quad \beta \to 0



\boxed{ G_{\mu\nu} = \kappa T_{\mu\nu} }








Effective Field Theory Regime





\beta \ll 1



\boxed{ \text{Torsion effects appear as suppressed corrections of order } \beta^2 }








AI.12 Interpretation of the First Rule





The first rule establishes the following structural correspondence:



Microscopic alignment → geometric structure
Tetrad → deviation from perfect alignment
Torsion → gradients of alignment deviation
Curvature → leading-order gravitational interaction
Torsion → higher-order corrections within an EFT hierarchy




The expansion parameter:



\boxed{ \beta = \frac{\ell_*}{L} }



controls deviations from classical General Relativity.

