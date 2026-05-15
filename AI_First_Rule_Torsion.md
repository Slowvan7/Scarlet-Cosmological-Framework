
Appendix AI — First-Rule Framework (EFT-Consistent Formulation)


AI.1 Fundamental Postulate (First Rule)

The microscopic structure of spacetime is governed by ultraviolet cutoff scales:

t_{*}=10^{-41}\,\mathrm{s}, \qquad \ell_{*}=10^{-35}\,\mathrm{m}

These define the fundamental UV resolution of torsional and tetrad degrees of freedom.

A derived microscopic scale is defined:

c_{\mathrm{eff}}=\frac{\ell_*}{t_*}

which represents the characteristic relaxation scale of microscopic torsional alignment dynamics, and not the propagation speed of light or any macroscopic causal signal.

The observed invariant speed c is not imposed at the UV level. Instead, it emerges in the infrared as the causal structure of the coarse-grained effective metric after renormalization of torsional degrees of freedom.

The “mutual center” of the First Rule is defined as a dynamical attractor in configuration space, not a spacetime point, and therefore does not introduce a preferred inertial frame.

Natural units are used in the infrared:

c=\hbar=1


AI.2 EFT Expansion Parameter

\beta=\frac{\ell_*}{L}\ll 1

where L is a macroscopic curvature scale. All fields admit a perturbative expansion in \beta.


AI.3 Fundamental Field: Tetrad

e^{a}{}_{\mu }=\delta ^{a}{}_{\mu }+\beta \,\omega ^{a}{}_{\mu }

with:

|\beta \omega^{a}{}_{\mu}|\ll 1, \qquad \det(e^{a}{}_{\mu})\neq 0

The metric is:

g_{\mu \nu }=\eta _{ab}e^{a}{}_{\mu }e^{b}{}_{\nu }


AI.4 Metric Expansion

g_{\mu \nu }=\eta _{\mu \nu }+\beta (\omega _{\mu \nu }+\omega _{\nu \mu })+\mathcal{O}(\beta ^2)


AI.5 Geometric Structure

AI.5.1 Levi–Civita Sector

\nabla_\lambda g_{\mu\nu}=0, \qquad R_{\mu\nu}\sim \mathcal{O}(1/L^2)


AI.5.2 Weitzenböck Sector

\Gamma^{(W)\lambda}{}_{\mu\nu}=e^\lambda{}_a\,\partial_\nu e^a{}_\mu

R(\Gamma^{(W)})=0


AI.5.3 Riemann–Cartan Decomposition

\Gamma^\lambda{}_{\mu\nu}=\left\{{}^{\lambda}_{\mu\nu}\right\}+K^\lambda{}_{\mu\nu}

Torsion:

T^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\mu\nu}-\Gamma^\lambda{}_{\nu\mu}

Contortion:

K^\lambda{}_{\mu\nu}=\frac{1}{2}\left(T^\lambda{}_{\mu\nu}-T_\mu{}^\lambda{}_\nu-T_\nu{}^\lambda{}_\mu\right)


AI.6 Torsion Scaling

T^\lambda{}_{\mu\nu}\sim \frac{\beta}{L}


AI.7 Quadratic Torsion Invariant

\mathcal{I}_T=
a_1 T^\rho{}_{\mu\nu}T_\rho{}^{\mu\nu}
+a_2 T^\rho{}_{\mu\nu}T^{\mu\nu}{}_{\rho}
+a_3 T_\mu T^\mu

T_\mu = T^\lambda{}_{\mu\lambda}

\mathcal{I}_T \sim \frac{\beta^2}{L^2}


AI.8 Curvature–Torsion Hierarchy

R \sim \frac{1}{L^2}, \qquad \mathcal{I}_T \sim \beta^2 R

Thus torsion enters as a controlled second-order EFT correction.


AI.9 Effective Action

S=\int d^4x\sqrt{-g}\left[\frac{1}{2\kappa}R+\frac{\alpha}{\ell_*^2}\mathcal{I}_T\right]

\kappa \sim \ell_*^2


AI.10 Field Equations

G_{\mu\nu}+\frac{\alpha}{\ell_*^2}\Theta_{\mu\nu}=\kappa T_{\mu\nu}

\Theta_{\mu\nu}=\sum_{i=1}^3 a_i \Theta^{(i)}_{\mu\nu}


AI.10.1 Tensor Basis

(1) Direct sector

\Theta_{\mu\nu}^{(1)}
=
-2T_{\mu\rho\sigma}T_\nu{}^{\rho\sigma}
+4T^{\rho\sigma}{}_{\mu}T_{\rho\sigma\nu}
-\frac{1}{2}g_{\mu\nu}T_{\alpha\rho\sigma}T^{\alpha\rho\sigma}


(2) Exchange sector

\Theta_{\mu\nu}^{(2)}
=
-4T_{\mu\rho\sigma}T^{\rho\sigma}{}_{\nu}
-\frac{1}{2}g_{\mu\nu}T_{\alpha\rho\sigma}T^{\rho\sigma\alpha}


(3) Trace sector

\Theta_{\mu\nu}^{(3)}
=
2T_\mu T_\nu
-\frac{1}{2}g_{\mu\nu}T_\alpha T^\alpha


AI.11 Stress–Energy Tensors

T_{\mu\nu}^{(i)}=
-\frac{2}{\sqrt{-g}}
\frac{\delta(\sqrt{-g}\mathcal{L}_i)}{\delta g^{\mu\nu}}

Scalar sector:

T_{\mu\nu}^{(\zeta)}=
\nabla_\mu \zeta \nabla_\nu \zeta
-g_{\mu\nu}\left[\frac{1}{2}(\nabla \zeta)^2+V(\zeta)\right]

Torsion sector:

\mathcal{L}_{\mathrm{torsion}}=\alpha \mathcal{I}_T


AI.12 Conservation Laws

\nabla_\mu^{(\Gamma)}T^{\mu\nu}_{\mathrm{total}}=0

\nabla_\mu^{(LC)}T^{\mu\nu}_{\mathrm{total}}=\mathcal{O}(\beta^2)


AI.13 Infrared Limit

\beta \to 0 \quad \Rightarrow \quad G_{\mu\nu}=\kappa T_{\mu\nu}

General Relativity emerges as the infrared fixed point.


AI.14 Physical Structure (Aligned Formulation)

The First Rule defines a relaxation hierarchy:

microscopic tetrad fluctuations
torsional degrees of freedom
curvature emergence
macroscopic spacetime geometry
The “mutual center” refers to a configuration-space attractor governing the relaxation of torsion and tetrad fields, and does not correspond to a spacetime point or preferred inertial frame.

