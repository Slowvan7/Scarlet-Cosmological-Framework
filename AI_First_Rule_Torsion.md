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

Appendix AI.14 — Observation–Reality Separation Principle


AI.14.1 Fundamental Postulate

Standard cosmology does not assume naïve direct access to physical reality; rather, observables are reconstructed from measurements after applying known geometric, radiative, and instrumental corrections.

SCARLET extends this framework by introducing an additional physical modulation arising from spacetime coherence dynamics.

The foundational statement is:

\boxed{
\mathcal{O}
=
\mathcal{P}
\left[
\mathcal{R}, \zeta
\right]
}

\mathcal{O}=\mathcal{P}[\mathcal{R},\zeta]

where:

\mathcal{O} is the observed quantity
\mathcal{R} is the underlying bedrock physical state
\zeta(x^\mu) is the spacetime coherence relaxation field
\mathcal{P} is the projection operator induced by propagation through a torsion-bearing medium
Observation is therefore not a direct measurement of reality, but a transformation of reality through signal propagation across a structured spacetime background.


AI.14.2 Path-Dependent Projection Operator

In full generality, the projection is defined along the propagation path:

\[
\boxed{
\mathcal{B}[\gamma]
=
\exp
\left[
-
\int_{\gamma}
\zeta(x^\mu)\, d\\lambda
\right]
}
\]

\mathcal{B}[\gamma]=\exp\left[-\int_{\gamma}\zeta(x^\mu),d\lambda\right]

where:

\gamma is the null or timelike signal trajectory
\lambda is an affine (or proper-time) parameter chosen such that \zeta\,d\lambda is dimensionless
\zeta(x^\mu) encodes the local rate of coherence relaxation
This emphasizes that observation depends on propagation history, not merely local pointwise evaluation.


AI.14.3 Homogeneous Cosmological Limit

In a spatially homogeneous FRW background, the path-dependent projection reduces to a time-dependent form:

\boxed{
\mathcal{B}(t)
=
\exp
\left[
-
\int
\zeta(t)\,dt
\right]
}

\mathcal{B}(t)=\exp\left[-\int\zeta(t)dt\right]

where:

\zeta(t) is the spatially averaged coherence relaxation rate
\mathcal{B}(t) is the cumulative observational attenuation over cosmic time
For a fatigued cosmological medium:

0 < \mathcal{B}(t) < 1

so observed quantities may differ systematically from their underlying physical values.


AI.14.4 Leading-Order Approximation

For weak coherence relaxation and approximately homogeneous propagation conditions, the full projection operator reduces to the leading-order approximation:

\boxed{
\mathcal{O}
\approx
\mathcal{R}
\cdot
\mathcal{B}(t)
}

\mathcal{O}\approx\mathcal{R}\cdot\mathcal{B}(t)

This approximation is valid only when:

coherence gradients are small
backreaction on geometry is subleading
propagation remains close to homogeneous
It is not assumed to hold universally.


AI.14.5 Physical Interpretation

The universe is not directly observed.

Instead:

physical sources generate signals
signals propagate through a torsion-bearing spacetime medium
coherence relaxation modifies effective amplitudes and inferred parameters
phase corrections may arise depending on the propagation channel
observers reconstruct physical quantities from filtered signals
Thus measured quantities are not identical to underlying physical states, but are projections through a dynamically evolving medium.


AI.14.6 Observable Relations

Luminosity Distance

Let d_L^{\mathrm{true}} denote the metric luminosity distance determined by the underlying spacetime geometry.

Coherence attenuation modifies the inferred flux relation, producing:

\boxed{
d_L^{\mathrm{obs}}
=
\frac{
d_L^{\mathrm{true}}
}{
\mathcal{B}(t)
}
}

d_L^{\mathrm{obs}}=\frac{d_L^{\mathrm{true}}}{\mathcal{B}(t)}

Thus attenuation causes distant sources to appear dimmer and therefore farther away than the purely geometric metric distance would imply.


Neutrino Sector (consistent with Appendix AK)

\boxed{
m_{\nu,\mathrm{eff}}
=
m_\nu
-
g_\nu\,\zeta
}

m_{\nu,\mathrm{eff}}=m_\nu-g_\nu\zeta

where:

m_\nu is the bare neutrino mass from particle physics
g_\nu is the neutrino coherence coupling constant
This relation represents mass screening through direct coupling to the coherence field and is not a propagation attenuation effect.

It allows the gravitationally inferred effective mass to be smaller than the bare particle-physics mass.


Redshift Relation (First-Order Torsional Correction)

\boxed{
1 + z_{\mathrm{obs}}
=
(1 + z_{\mathrm{metric}})
\,
(1 + \delta z_{\mathrm{torsion}})
}

1+z_{\mathrm{obs}}=(1+z_{\mathrm{metric}})(1+\delta z_{\mathrm{torsion}})

valid to first order in torsional corrections.

This preserves the correct multiplicative composition of frequency shifts.


AI.14.7 Relation to Appendix AK

Appendix AK provides one explicit dynamical realization of this projection principle:

Hopf sector structure generates discrete vacuum contributions
sector dynamics source coherence relaxation \zeta
coherence relaxation couples into the neutrino sector
cosmological backreaction modifies inferred observables
Thus:

AI.14 defines the general observational structure
AK provides one explicit dynamical realization of that structure
The appendices are complementary: AI.14 establishes the principle, while AK provides a concrete physical mechanism.


AI.14.8 Operational Testability

The framework is empirically testable because different observational channels probe different effective propagation histories.

Compare:

electromagnetic redshift
gravitational-wave propagation
relic neutrino background
CMB transfer functions
birefringence constraints
Prediction:

If \zeta \neq 0, different channels will reconstruct slightly different effective cosmological parameters from the same underlying cosmological background.

If all channels agree exactly:

\zeta \rightarrow 0
\quad\Rightarrow\quad
\mathcal{B}(t)\rightarrow 1

and SCARLET reduces continuously to standard cosmology.


Final Statement

\boxed{
\mathcal{O}
=
\mathcal{P}
\left[
\mathcal{R}, \zeta
\right]
}

\mathcal{O}=\mathcal{P}[\mathcal{R},\zeta]

General Relativity describes how geometry governs propagation.

SCARLET extends this by including coherence relaxation as a physical modulation of signal transmission through spacetime:

\boxed{
\text{geometry}
+
\text{torsional coherence}
+
\text{observational projection}
}

This is the Observation–Reality Separation Principle:

reality exists first as a physical state, while observation is its dynamically filtered projection through spacetime structure



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

