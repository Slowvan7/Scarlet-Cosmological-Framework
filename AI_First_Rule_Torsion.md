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

Appendix AI.13 — Density Screening, Local GR Recovery, and the Warp–Weft Origin of the First Rule


Appendix AI.13 — Density Screening, Local GR Recovery, and Warp–Weft Origin of the First Rule

(Rewritten in formal EFT / Riemann–Cartan framework form)


AI.13.1 Fundamental Alignment Postulate

We postulate a microscopic alignment principle governing pre-geometric degrees of freedom at the Bedrock Horizon Scale:

\ell_* = 10^{-35}\,\mathrm{m}, \qquad
t_* = \frac{\ell_*}{c}

such that:

\boxed{\ell_* = c t_*}

This identifies the causal propagation speed of alignment dynamics with the observed invariant speed c:

c_{\mathrm{eff}} = c

Below this scale, spacetime is not described by a differentiable Lorentzian manifold but by a pre-geometric alignment phase with no metric structure.


AI.13.2 Expansion Parameter and EFT Regime

We define the dimensionless expansion parameter:

\boxed{\beta \equiv \frac{\ell_*}{L} \ll 1}

where L is a macroscopic curvature scale.

All observables admit a systematic expansion in powers of \beta, defining a controlled effective field theory.


AI.13.3 Warp–Weft Constitutive Structure

Spacetime geometry emerges from two pre-geometric alignment sectors:

\mathcal{W} \quad (\text{Warp sector}), \qquad
\mathcal{F} \quad (\text{Weft sector})

defined on a non-metric configuration space \mathcal{P}.

The tetrad field is defined as a coarse-grained constitutive functional:

\boxed{
e^a_{\ \mu}(x;\ell_*) =
\mathcal{E}^a_{\ \mu}[\mathcal{W},\mathcal{F};x,\ell_*]
}

with perturbative expansion:

e^a_{\ \mu} = \delta^a_{\ \mu} + \beta\,\omega^a_{\ \mu} + \mathcal{O}(\beta^2)

The map \mathcal{E} encodes coarse-graining over pre-geometric alignment cells of size \ell_*.


AI.13.4 Metric Structure

The emergent metric is constructed from the tetrad:

\boxed{
g_{\mu\nu} = \eta_{ab}\, e^a_{\ \mu} e^b_{\ \nu}
}

with expansion:

g_{\mu\nu} =
\eta_{\mu\nu}
+
\beta(\omega_{\mu\nu}+\omega_{\nu\mu})
+
\mathcal{O}(\beta^2)


AI.13.5 Connections and Torsion

Levi–Civita Connection

\nabla_\lambda g_{\mu\nu} = 0

defines the standard curvature sector:

R(\nabla) \sim \partial^2 g


Weitzenböck Connection

\boxed{
\Gamma^{(W)\lambda}_{\ \ \mu\nu}
=
e^\lambda_a \partial_\nu e^a_{\ \mu}
}

satisfies:

\nabla^{(W)}_\lambda g_{\mu\nu} = 0,
\qquad
R(\Gamma^{(W)}) \equiv 0


Torsion Tensor

\boxed{
T^\lambda_{\ \mu\nu}
=
\Gamma^{(W)\lambda}_{\ \ \mu\nu}
-
\Gamma^{(W)\lambda}_{\ \ \nu\mu}
}

Scaling:

\boxed{
T^\lambda_{\ \mu\nu}
\sim
\frac{\beta}{L}
=
\frac{\ell_*}{L^2}
}


AI.13.6 Torsion Invariant and Scaling Hierarchy

Define:

\boxed{
\mathcal{I}_T
=
T^\lambda_{\ \mu\nu} T_\lambda^{\ \mu\nu}
}

Scaling:

\mathcal{I}_T \sim \frac{\beta^2}{L^2}

Einstein curvature scale:

G_{\mu\nu} \sim \frac{1}{L^2}

Hence:

\boxed{
\mathcal{I}_T \sim \beta^2 G_{\mu\nu}
}

establishing torsion as a second-order EFT correction.


AI.13.7 Effective Action

The low-energy effective action is:

\boxed{
S = \int d^4x\,\sqrt{-g}
\left[
\frac{1}{2\kappa} R(\nabla)
+
\frac{\alpha}{\ell_*^2}\,\mathcal{I}_T
\right]
}

with:

\kappa \sim \ell_*^2

The torsion sector is thus UV-sensitive but IR-suppressed by \beta^2.


AI.13.8 Emergent Lorentz Symmetry

Lorentz invariance arises as an infrared fixed-point symmetry after coarse-graining:

\text{microscopic sector} \neq \text{Lorentz invariant}

\text{effective manifold} \rightarrow \text{Lorentz invariant EFT}

No preferred observable frame exists despite underlying pre-geometric structure.


AI.13.9 Density Screening Mechanism

Torsional dissipation is environment-dependent and suppressed in high-density regimes.

We define an effective viscosity:

\boxed{
\eta_{\mathrm{eff}}(\rho)
=
\eta_0 \exp\!\left(-\frac{\rho}{\rho_c}\right)
}

with:

\rho_c: critical screening density
\rho: local matter density
Limits:

\rho \gg \rho_c \Rightarrow \eta_{\mathrm{eff}} \to 0
\qquad
\rho \ll \rho_c \Rightarrow \eta_{\mathrm{eff}} \to \eta_0

This ensures restoration of General Relativity in high-density environments.


AI.13.10 Screening Radius

Defined implicitly by:

\boxed{
\rho(r_s) = \rho_c
}

Regimes:

r < r_s: GR-dominated regime
r > r_s: torsion-active regime
This guarantees consistency with Solar System constraints.


AI.13.11 Gravitational Waves

Gravitational waves correspond to metric perturbations of the emergent manifold:

\boxed{
\text{GW propagation is metric-governed and non-dispersive at leading order}
}

Torsional corrections enter only at:

\mathcal{O}(\beta^2)

Thus:

no lattice drag
no leading dispersion
only suppressed cumulative phase/ringdown corrections
Any nonlinear enhancement (e.g., “Snap regime” effects) is interpreted as a higher-order strong-field amplification beyond the perturbative EFT regime.


AI.13.12 Interpretation of the First Rule

The emergent structure is:

\boxed{
\text{Warp–Weft coherence}
\;\rightarrow\;
\text{tetrad field}
\;\rightarrow\;
\text{torsion}
\;\rightarrow\;
\text{curvature}
\;\rightarrow\;
\text{macroscopic gravity}
}

Spacetime is therefore a structured Riemann–Cartan medium characterized by:

stiffness (elastic response)
torsional inertia
density-dependent screening
UV cutoff at \ell_*
General Relativity is recovered as the leading-order IR limit:

\boxed{
\beta \to 0 \;\Rightarrow\; R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \kappa T_{\mu\nu}
}


Final Statement

The First Rule is not a dynamical law of matter in spacetime, but a constitutive principle of spacetime emergence from pre-geometric alignment sectors. It defines General Relativity as the infrared fixed point of a torsion-suppressed Riemann–Cartan effective field theory.

