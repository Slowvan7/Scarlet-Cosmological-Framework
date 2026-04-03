Appendix AI — First-Rule Torsion Framework (Final Consistent Formulation)







AI.1 Fundamental Postulate (First Rule)





We postulate a microscopic alignment principle:



\boxed{ \text{Microscopic degrees of freedom evolve toward alignment with a common center governed by fundamental scales } t_* \text{ and } \ell_* }



with:



t_* = 10^{-41}\,\mathrm{s}, \quad \ell_* = 10^{-35}\,\mathrm{m}



These define the fundamental temporal and spatial scales of the theory. To ensure macroscopic consistency, we define an emergent propagation speed:



\boxed{ c_{\text{eff}} = \frac{\ell_*}{t_*} }



This sets the characteristic propagation speed of alignment dynamics, which may coincide with the physical speed of light or represent a distinct fundamental scale.








AI.2 Expansion Parameter





Define a small dimensionless parameter:



\boxed{ \beta \equiv \frac{\ell_*}{L}, \quad \beta \ll 1 }



where L is a macroscopic length scale. All fields are expanded perturbatively in powers of \beta.








AI.3 Tetrad Field (Fundamental Variable)





The geometric degrees of freedom are encoded in the tetrad:



\boxed{ e^a_{\ \mu}(x) = \delta^a_{\ \mu} + \beta\,\omega^a_{\ \mu}(x) }



where \omega^a_{\ \mu}(x) is dimensionless and |\beta\,\omega^a_{\ \mu}| \ll 1 to ensure perturbative control. The tetrad is invertible:



\det(e^a_{\ \mu}) \neq 0








AI.4 Metric Construction





The spacetime metric is constructed as:



\boxed{ g_{\mu\nu} = \eta_{ab} e^a_{\ \mu} e^b_{\ \nu} }



Expanding to first order in \beta:



g_{\mu\nu} = \eta_{\mu\nu} + \beta \left( \omega_{\mu\nu} + \omega_{\nu\mu} \right) + \mathcal{O}(\beta^2)








AI.5 Connections





AI.5.1 Levi-Civita Connection



\boxed{ \nabla_\lambda g_{\mu\nu} = 0 }



Produces curvature via second derivatives of the metric: G_{\mu\nu} \sim \partial^2 g.



AI.5.2 Weitzenböck Connection



\boxed{ \Gamma^{(W)\lambda}{}_{\mu\nu} = e^\lambda_a \, \partial_\nu e^a_{\ \mu} }



Properties:



\boxed{ \nabla^{(W)}_\lambda g_{\mu\nu} = 0 }, \quad \boxed{ R^\rho_{\ \sigma\mu\nu}(\Gamma^{(W)}) \equiv 0 }








AI.6 Torsion Tensor





\boxed{ T^\lambda_{\ \mu\nu} = \Gamma^{(W)\lambda}{}_{\mu\nu} - \Gamma^{(W)\lambda}{}_{\nu\mu} }



Scaling:



\boxed{ T^\lambda_{\ \mu\nu} \sim \frac{\beta}{L} = \frac{\ell_*}{L^2} }, \quad [T] = L^{-1}








AI.7 Scaling Hierarchy





Curvature (Einstein tensor scale):
\boxed{ G_{\mu\nu} \sim \frac{\beta}{L^2} = \frac{\ell_*}{L^3} }
Torsion invariant:
\boxed{ \mathcal{I}_T \sim T^2 \sim \frac{\beta^2}{L^2} = \frac{\ell_*^2}{L^4} }
Hierarchy:
\boxed{ \mathcal{I}_T \ll G_{\mu\nu} \quad \text{for } \beta \ll 1 }









AI.8 Effective Action





\boxed{ S = \int d^4x \, \sqrt{-g} \left[ \frac{1}{2\kappa} R(\nabla) + \frac{\alpha}{\ell_*^2} \mathcal{I}_T \right] }



where:



R(\nabla) is the Ricci scalar of the Levi-Civita connection.
\mathcal{I}_T is the quadratic torsion invariant.
\kappa \sim \ell_*^2, \alpha is dimensionless.









AI.9 Torsion Invariant





\boxed{ \mathcal{I}_T = a_1 T^\rho{}_{\mu\nu} T_\rho{}^{\mu\nu} + a_2 T^\rho{}_{\mu\nu} T^{\nu\mu}{}_\rho + a_3 T^\rho{}_{\mu\rho} T^\sigma{}_{\nu\sigma} }



with constants a_i.








AI.10 Field Equations





Variation of the action yields:



\boxed{ G_{\mu\nu} + \frac{\alpha}{\ell_*^2} \kappa \, \Theta_{\mu\nu} = \kappa T_{\mu\nu} }



where:



T_{\mu\nu} is the matter stress-energy tensor.
\Theta_{\mu\nu} is the effective contribution from torsion invariants.









AI.11 Limiting Behavior





GR Limit: \ell_* \to 0 \Rightarrow \beta \to 0
\boxed{ G_{\mu\nu} = \kappa T_{\mu\nu} }
Effective Field Theory Regime: \beta \ll 1
\boxed{ \text{Torsion effects appear as suppressed corrections of order } \beta^2 }









AI.12 Interpretation of the First Rule





The first rule establishes the following structural correspondence:

Microscopic

Macroscopic / Geometric

Alignment of degrees of freedom

Emergent geometric structure

Tetrad

Deviation from perfect alignment

Torsion

Gradients of alignment deviation

Curvature

Leading-order gravitational interaction

Torsion corrections

Higher-order EFT corrections

The expansion parameter:



\boxed{ \beta = \frac{\ell_*}{L} }



controls deviations from classical General Relativity.

