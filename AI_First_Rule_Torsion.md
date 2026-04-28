Appendix AI — First-Rule Framework


AI.1 Fundamental Postulate (First Rule)

We postulate that microscopic degrees of freedom obey an alignment principle toward a common dynamical center defined by fundamental scales:

t_* = 10^{-41}\,\text{s}, \qquad \ell_* = 10^{-35}\,\text{m}

These define the ultraviolet cutoff of the theory.

The associated emergent causal scale is:

c_{\text{eff}} = \frac{\ell_*}{t_*}

which sets the propagation speed of alignment dynamics and may coincide with the observed invariant speed c.


AI.2 Expansion Parameter

We define the EFT expansion parameter:

\beta \equiv \frac{\ell_*}{L} \ll 1

where L is a macroscopic curvature scale.

All fields admit a perturbative expansion in powers of \beta.


AI.3 Fundamental Field: Tetrad

The fundamental variable is the tetrad field:

e^a{}_{\mu} = \delta^a{}_{\mu} + \beta\,\omega^a{}_{\mu}

with |\beta \omega^a{}_{\mu}| \ll 1.

Invertibility is assumed:

\det(e^a{}_{\mu}) \neq 0


AI.4 Metric Construction

The spacetime metric is constructed as:

g_{\mu\nu} = \eta_{ab} e^a{}_{\mu} e^b{}_{\nu}

Expanding to leading order:

g_{\mu\nu}
=
\eta_{\mu\nu}
+
\beta(\omega_{\mu\nu} + \omega_{\nu\mu})
+
\mathcal{O}(\beta^2)


AI.5 Connections and Geometry

AI.5.1 Levi–Civita Connection

\nabla_\lambda g_{\mu\nu} = 0

This defines the curvature sector:

R_{\mu\nu} \sim \partial^2 g_{\mu\nu}

with scaling:

|R_{\mu\nu}| \sim \mathcal{O}\!\left(\frac{1}{L^2}\right)


AI.5.2 Weitzenböck Connection

\Gamma^{(W)\lambda}{}_{\mu\nu}
=
e^\lambda{}_a \partial_\nu e^a{}_{\mu}

Properties:

R(\Gamma^{(W)}) = 0,
\qquad
\nabla^{(W)}_\lambda g_{\mu\nu} = 0


AI.5.3 Full Connection Decomposition

The affine connection is decomposed as:

\Gamma^\lambda{}_{\mu\nu}
=
\{^{\,\lambda}_{\mu\nu}\}
+
K^\lambda{}_{\mu\nu}

where:

\{^{\,\lambda}_{\mu\nu}\} is the Levi–Civita connection
K^\lambda{}_{\mu\nu} is the contortion tensor
K^\lambda{}_{\mu\nu} is algebraically determined by torsion

AI.6 Torsion Tensor

T^\lambda{}_{\mu\nu}
=
\Gamma^{(W)\lambda}{}_{\mu\nu}
-
\Gamma^{(W)\lambda}{}_{\nu\mu}

Scaling:

T^\lambda{}_{\mu\nu} \sim \frac{\beta}{L} = \frac{\ell_*}{L^2}


AI.7 Torsion Invariant and Hierarchy

Define the quadratic torsion invariant:

\mathcal{I}_T = T^\rho{}_{\mu\nu} T_\rho{}^{\mu\nu}

Scaling:

\mathcal{I}_T \sim \frac{\beta^2}{L^2}

Curvature scale:

|R_{\mu\nu}| \sim \frac{1}{L^2}

Hierarchy:

\mathcal{I}_T \sim \beta^2 R

Thus torsion effects enter at second order in the EFT expansion.


AI.8 Effective Action

S = \int d^4x \sqrt{-g}
\left[
\frac{1}{2\kappa} R(\nabla)
+
\frac{\alpha}{\ell_*^2} \mathcal{I}_T
\right]

with:

\kappa \sim \ell_*^2


AI.9 Field Equations

Variation yields:

G_{\mu\nu}
+
\frac{\alpha}{\ell_*^2}\Theta_{\mu\nu}
=
\kappa T_{\mu\nu}

where \Theta_{\mu\nu} encodes torsional backreaction.


AI.10 Stress–Energy Tensors

All matter and field sectors are defined via:

T_{\mu\nu}^{(i)}
=
-\frac{2}{\sqrt{-g}}
\frac{\delta(\sqrt{-g}\mathcal{L}_i)}{\delta g^{\mu\nu}}
\quad (\text{torsion held fixed})


Scalar coherence field:

T^{(\zeta)}_{\mu\nu}
=
\nabla_\mu \zeta \nabla_\nu \zeta
-
g_{\mu\nu}
\left[
\frac{1}{2}(\nabla \zeta)^2 + V(\zeta)
\right]


Torsion sector:

T^{(T)}_{\mu\nu}
=
-\frac{2}{\sqrt{-g}}
\frac{\delta(\sqrt{-g}\mathcal{L}_{\text{torsion}})}{\delta g^{\mu\nu}}

with:

\mathcal{L}_{\text{torsion}} = \alpha \mathcal{I}_T


AI.11 Conservation Laws

Full Riemann–Cartan conservation:

\nabla^{(\Gamma)}_\mu T^{\mu\nu}_{\text{total}} = 0

EFT Levi–Civita projection:

\nabla^{(LC)}_\mu T^{\mu\nu}_{\text{total}} = \mathcal{O}(\beta^2)


AI.12 Limiting Behavior

GR limit:

\beta \to 0
\quad \Rightarrow \quad
G_{\mu\nu} = \kappa T_{\mu\nu}

EFT regime:

\beta \ll 1
\quad \Rightarrow \quad
\text{torsion appears as suppressed corrections}


AI.13 Physical Interpretation

The theory defines a geometric emergence hierarchy:

microscopic alignment → tetrad field
tetrad fluctuations → torsion
torsion gradients → curvature
curvature → macroscopic gravity
General Relativity appears as the infrared fixed point of the torsion-based EFT.


