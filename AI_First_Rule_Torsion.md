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

AI.13.1 Overview

The First Rule introduced in Appendix AI is formulated as a microscopic alignment principle:

\boxed{
\text{Microscopic degrees of freedom evolve toward alignment with a common center}
}

governed by the Bedrock Horizon Scale

t_* = 10^{-41}\,\mathrm{s},
\qquad
\ell_* = 10^{-35}\,\mathrm{m}.

These scales define the minimum physically meaningful temporal and spatial resolution of the spacetime fabric. Below this scale, spacetime is not treated as a continuous manifold, but as a pre-dynamic geometric phase in which ordinary metric descriptions no longer apply.

In the effective field theory developed in Appendix AI, this alignment principle is encoded through the tetrad field, torsion tensor, and the resulting Riemann–Cartan geometry. However, the formal structure does not require specification of the deeper microscopic origin of these alignment dynamics.

This section provides that constitutive interpretation and explains how the same framework preserves precision local tests of General Relativity through density screening.

The First Rule is understood as arising from the interaction of two constitutive alignment sectors of the vacuum manifold: the Warp sector and the Weft sector. Their coherence generates the emergent tetrad structure, while imperfect local closure produces torsion and higher-order geometric corrections.

This is not introduced as an additional dynamical theory, but as the physical origin of the effective theory already defined in Appendix AI.


AI.13.2 Pre-Geometric Warp–Weft Structure

We postulate the existence of two fundamental pre-geometric alignment sectors:

\mathcal{W}
\qquad
\text{(Warp Sector)}

and

\mathcal{F}
\qquad
\text{(Weft Sector)}

which belong to a pre-metric configuration space

\mathcal{P}.

These sectors are not embedded spacetime hypersurfaces and do not initially possess metric structure in the General Relativistic sense. They are constitutive alignment sectors whose interaction defines the microscopic origin of geometry.

The Warp sector provides persistent longitudinal geometric anchoring, while the Weft sector provides transverse closure and local alignment recovery.

Spacetime geometry emerges from the coherence of these two sectors rather than from a pre-existing metric background.

Their mutual compatibility is described by the constitutive coherence functional

\boxed{
\mathcal{C} :
\mathcal{P}\times\mathcal{P}
\rightarrow
\mathbb{R}
}

with

\mathcal{C}(\mathcal{W},\mathcal{F})

measuring the degree of local geometric coherence between the two sectors.

Perfect coherence corresponds to uniform alignment, while incomplete coherence generates residual geometric strain within the structured torsion-capable vacuum manifold.

We define the emergent relation

\boxed{
e^a_{\ \mu}(x)
\sim
\mathcal{C}(\mathcal{W},\mathcal{F})
}

so that the tetrad field represents the coarse-grained macroscopic response of local alignment deviation.

Thus, the tetrad is not assumed to be fundamental, but emerges as the geometric response of warp–weft coherence.


AI.13.3 Emergence of Torsion

Local failure of perfect warp–weft coherence produces gradients in the emergent tetrad field:

\partial_\nu e^a_{\ \mu},

which generate the Weitzenböck connection

\Gamma^{(W)\lambda}_{\ \ \mu\nu}
=
e^\lambda_a
\partial_\nu e^a_{\ \mu}.

The antisymmetric part defines the torsion tensor:

\boxed{
T^\lambda_{\ \mu\nu}
=
\Gamma^{(W)\lambda}_{\ \ \mu\nu}
-
\Gamma^{(W)\lambda}_{\ \ \nu\mu}
}

Torsion therefore represents the residual geometric memory of incomplete local alignment.

In this interpretation:

uniform warp–weft coherence without local gradients corresponds to vanishing torsion,
finite torsion corresponds to persistent alignment gradients,
metric curvature governs leading-order gravitational dynamics,
torsion corrections appear as higher-order effective contributions.
Thus torsion is not introduced as an auxiliary correction, but as the geometric imprint of incomplete constitutive closure itself.

It is the constitutive record of how the spacetime fabric locally resists perfect geometric alignment.


AI.13.4 Bedrock Horizon Scale and Torsional Stiffness

The Bedrock Horizon Scale

t_* = 10^{-41}\,\mathrm{s},
\qquad
\ell_* = 10^{-35}\,\mathrm{m}

defines the intrinsic resolution limits of the alignment process.

These scales represent the smallest physically meaningful temporal and spatial excitations of the fabric and establish the lower bound below which classical geometry is no longer valid.

The effective alignment propagation scale is defined by

\boxed{
c_{\mathrm{eff}}
=
\frac{\ell_*}{t_*}
}

which characterizes the maximum rate at which alignment information can propagate through the emergent manifold.

This quantity may coincide with the observed speed of light or represent a deeper geometric alignment scale from which relativistic propagation emerges.

In material terms, this propagation is governed by the Torsional Stiffness of the vacuum manifold:

c^2
=
\frac{K_t}{\rho_t}

where

K_t is the Torsional Stiffness,
\rho_t is the Torsional Inertia Density.
Together these define how rapidly the spacetime fabric restores equilibrium after local torsional displacement.

Photon propagation couples to transverse torsional transport modes of the vacuum manifold, while standard electromagnetic gauge structure remains unchanged.

This preserves Maxwell theory and the observed U(1) gauge symmetry while providing a constitutive interpretation of propagation through the structured vacuum.


AI.13.5 Emergent Lorentz Symmetry

The pre-geometric Warp and Weft sectors are not required to obey Lorentz symmetry at the microscopic level.

Lorentz invariance is instead interpreted as an emergent infrared symmetry of the effective manifold after coarse-graining across many alignment cells of size \ell_*.

Thus,

\text{Pre-geometric alignment sectors}
\neq
\text{Lorentz-invariant spacetime}

while

\text{Macroscopic vacuum manifold}
\rightarrow
\text{Lorentz-invariant effective dynamics}.

This prevents interpretation of the framework as a classical ether theory.

The pre-geometric sector does not define an observable kinematic ether frame because Lorentz symmetry emerges in the effective metric sector.

There is therefore no experimentally accessible preferred rest frame, even though deeper constitutive structure exists at the Bedrock Horizon Scale.

The First Rule does not describe matter moving through a pre-existing medium; it describes the constitutive process by which spacetime itself emerges.

Observable relativity is preserved because Lorentz symmetry is a large-scale statistical property of the aligned manifold.


AI.13.6 Not Teleparallel Gravity

Although the framework uses tetrads, torsion, and the Weitzenböck connection, Scarlet is not a formulation of pure Teleparallel Equivalent General Relativity (TEGR).

In TEGR, one typically imposes

R(\Gamma^{(W)}) = 0

and rewrites gravity entirely in terms of torsion.

Scarlet instead remains a Riemann–Cartan effective field theory in which both curvature and torsion are physically present:

\boxed{
R(\nabla) \neq 0,
\qquad
T^\lambda_{\ \mu\nu} \neq 0
}

where:

R(\nabla) is the Ricci scalar of the Levi-Civita connection governing leading-order gravitational dynamics,
torsion provides suppressed higher-order corrections within the effective action.
Thus:

curvature is the dominant gravitational response,
torsion is the constitutive correction arising from imperfect warp–weft coherence.
Scarlet therefore preserves the Einsteinian limit while extending General Relativity through controlled torsional corrections rather than replacing curvature entirely.


AI.13.7 Density Screening and Local GR Recovery

A central requirement of any torsion-inclusive gravitational framework is consistency with precision local tests of General Relativity.

Observations within the Solar System strongly constrain deviations from Einstein gravity through:

post-Newtonian orbital tests,
light deflection,
gravitational redshift,
binary pulsar timing,
gravitational wave propagation.
Since Scarlet treats spacetime as a structured torsion-capable vacuum manifold with effective dissipation and geometric drag, the framework must explain why these effects do not produce observable violations of local General Relativistic behavior.

The resolution is density screening.

Torsional dissipation and late-time geometric drag are not universal local corrections of fixed magnitude. They are effective large-scale responses of the vacuum manifold that self-suppress in sufficiently high-density regions.

Thus:

\boxed{
\eta_{\mathrm{eff}}(\rho)
\rightarrow
0
\qquad
\text{for}
\qquad
\rho \gg \rho_c
}

where \rho_c is the critical screening density.

This ensures local recovery of standard General Relativity while preserving cosmological torsional corrections at low-density large scales.


AI.13.8 Effective Density-Dependent Screening

We define the effective torsional viscosity as

\boxed{
\eta_{\mathrm{eff}}(\rho)
=
\eta_0
\exp\left(
-\frac{\rho}{\rho_c}
\right)
}

where:

\eta_0 is the unscreened cosmological torsional viscosity,
\rho is the local matter density,
\rho_c is the critical density scale for screening.
This form is phenomenological and chosen as the minimal monotonic constitutive model; alternative screening profiles preserve the same effective field theory structure.

It captures the constitutive behavior of the spacetime fabric:

low-density regions retain full torsional response,
high-density regions suppress non-Einsteinian corrections.
Thus:

\rho \ll \rho_c
\quad\Rightarrow\quad
\eta_{\mathrm{eff}} \approx \eta_0

for cosmological scales, while

\rho \gg \rho_c
\quad\Rightarrow\quad
\eta_{\mathrm{eff}} \approx 0

for stellar and planetary environments.

The fabric becomes locally rigid under high-density anchoring.


AI.13.9 Screening Radius

For a localized gravitating source of mass M, we define the screening radius r_s by

\boxed{
\rho(r_s)
\sim
\rho_c
}

such that:

r < r_s
\quad\Rightarrow\quad
\text{local GR recovery}

and

r > r_s
\quad\Rightarrow\quad
\text{torsional corrections become effective}.

For viable parameter choices, r_s is expected to exceed Solar System precision-test scales, ensuring agreement with post-Newtonian constraints and local gravitational observations.

Local gravity remains effectively Einsteinian because the manifold is locally locked.


AI.13.10 Why Gravitational Waves Do Not Exhibit Lattice Drag

A common objection to any structured-medium interpretation of spacetime is:

If spacetime possesses material properties such as stiffness and viscosity, why do gravitational waves not behave like sound waves moving through matter?

The resolution is that gravitational waves are not external objects moving through a medium.

They are coherent geometric excitations of the manifold itself.

They propagate along the effective metric structure rather than through an independent background substance.

At leading order:

\boxed{
\text{GW propagation is metric-governed and effectively non-dispersive}
}

with only higher-order torsional corrections entering through

\Delta_{\mathrm{GW}}
\sim
\mathcal{O}(\beta^2).

Since

\beta
=
\frac{\ell_*}{L}
\ll 1,

these corrections are strongly suppressed for astrophysical wavelengths.

Thus:

no ordinary lattice drag appears,
no large dispersive violation is expected,
only small cumulative ringdown corrections survive.
This is the origin of the predicted \sim 5\% damping modification in the dominant Kerr quasinormal mode, as derived in Appendix X and the associated ringdown technical memorandum.


AI.13.11 Interpretation

The First Rule may therefore be summarized as:

\boxed{
\text{Warp–Weft Coherence}
\rightarrow
\text{Emergent Tetrad}
\rightarrow
\text{Torsion}
\rightarrow
\text{Curvature}
\rightarrow
\text{Macroscopic Gravity}
}

Spacetime is not treated as an abstract empty background, but as a structured torsion-capable vacuum manifold with finite stiffness, fatigue thresholds, recovery dynamics, and discrete anchoring scales.

Gravity emerges as the leading-order curvature response of this medium.

Torsion is the residual geometric memory of incomplete alignment.

The Bedrock Horizon Scale provides the lower bound of valid geometry, while the effective manifold preserves Lorentz symmetry and the equivalence principle at observable scales.

The purpose is precision, not rebranding.

If a quantity behaves as stiffness, it is named stiffness.
If a quantity behaves as fatigue, it is named fatigue.
If a structure functions as a geometric anchor, it is named accordingly.

The First Rule is therefore not a statement about matter moving through space, but about the physical mechanism by which spacetime itself becomes possible.



