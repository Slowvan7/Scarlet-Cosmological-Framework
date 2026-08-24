### Appendix AI: Effective Field Theory Formulation of Space Fabric Dynamics

#### AI.9 Action, Scales, and Mass Dimensions
We work in natural units ($\hbar = c = k_B = 1$) under the mostly-plus metric signature $(-,+,+,+)$. The macroscopic spacetime manifold is governed by an Effective Field Theory (EFT) coupling metric-affine geometry to a dimensionless scalar order parameter $\zeta$ representing the internal state of the spatial fabric.

The total action for the system is:
$$S = \int d^4x \sqrt{-g} \left[ \frac{1}{2\kappa} F(\zeta) R + \mathcal{L}_{\text{kin}}(\zeta) - V(\zeta) + \frac{\alpha_T \ell_*^2}{2\kappa} I_T \right] + S_{\text{matter}}[g_{\mu\nu}, \psi]$$

where $\kappa \equiv 8\pi G = M_{\text{Pl}}^{-2}$ is Einstein's gravitational constant ($[\kappa] = E^{-2}$), and $R$ is the Ricci scalar constructed from the Levi-Civita connection ($[R] = E^2$).

##### Parameter Definitions & Power Counting
* **Microscopic Length and Time Scales:** The fundamental UV lattice parameters are $\ell_*$ ($[\ell_*] = E^{-1}$) and $t_*$ ($[t_*] = E^{-1}$). The ratio $c_{\text{eff}} \equiv \ell_*/t_*$ defines the microscopic torsional relaxation velocity.
* **Effective Hierarchy Parameter:** The dimensionless power-counting parameter is defined as $\beta \equiv \ell_*/L$, where $L$ is the characteristic macro-coarse-graining scale ($L \gg \ell_*$). In the infrared limit $L \to \infty$, $\beta \to 0$.
* **Torsion Tensor & Invariants:** Torsion scales as $T^\lambda_{\phantom{\lambda}\mu\nu} \sim \beta / L = \ell_*/L^2$, giving $[T] = E^2$. The quadratic torsion invariant $I_T \equiv T_{\alpha\beta\gamma} T^{\alpha\beta\gamma}$ carries mass dimension $[I_T] = E^4$ and scales as $I_T \sim \ell_*^2 / L^4$. The dimensionless factor $\alpha_T$ regulates the higher-derivative torsional corrections.
* **Order Parameter Scale:** The order parameter $\zeta$ is dimensionless ($[\zeta] = 1$). Consequently, $M_\zeta$ ($[M_\zeta] = E^1$) represents the characteristic energy/relaxation scale (symmetry-breaking parameter) of the space fabric substrate, maintaining the correct overall Lagrangian density dimension $[\mathcal{L}] = E^4$.

---

#### AI.9.2 Kinetic, Potential, and Coupling Definitions
The coupling function $F(\zeta)$ introduces a non-minimal coupling between the order parameter and curvature:
$$F(\zeta) = 1 + \xi_{\text{SF}} \zeta^2$$
where $\xi_{\text{SF}}$ is a dimensionless non-minimal coupling parameter. Within this effective action, $\xi_{\text{SF}} \approx 2/11$ is adopted as a phenomenological ansatz chosen to match the $d_s: 2 \to 4$ spectral dimension transition of the underlying substrate flow, pending an explicit Functional Renormalization Group (FRG) fixed-point derivation.

The kinetic Lagrangian density for the order parameter is:
$$\mathcal{L}_{\text{kin}}(\zeta) = -\frac{1}{2} M_\zeta^2 g^{\mu\nu} \nabla_\mu \zeta \nabla_\nu \zeta$$

The background potential $V(\zeta)$ ($[V] = E^4$) satisfies the physical vacuum ground-state conditions:
$$V(0) = 0, \quad \left.\frac{\partial V}{\partial \zeta}\right|_{\zeta=0} = 0, \quad \left.\frac{\partial^2 V}{\partial \zeta^2}\right|_{\zeta=0} > 0$$
ensuring that $\zeta_0 = 0$ corresponds to a stable dynamical infrared minimum.

---

#### AI.9.3 Scalar Order Parameter Field Equation
Varying the total action with respect to the dimensionless scalar field $\zeta$ via $\frac{\delta S}{\delta \zeta} = 0$ yields:
$$M_\zeta^2 \Box \zeta - V_{,\zeta} + \frac{1}{2\kappa} \left(\frac{\partial F}{\partial \zeta}\right) R = 0$$

Substituting $F_{,\zeta} = 2\xi_{\text{SF}}\zeta$, the scalar field equation takes the explicit form:
$$M_\zeta^2 \Box \zeta - V_{,\zeta} + \frac{\xi_{\text{SF}} \zeta}{\kappa} R = 0$$

##### Cosmological Reduction in FLRW Geometry
In a flat FLRW background with metric signature $(-,+,+,+)$, the d'Alembertian operator acting on a homogeneous field $\zeta(t)$ is:
$$\Box \zeta \equiv g^{\mu\nu} \nabla_\mu \nabla_\nu \zeta = -\ddot{\zeta} - 3H\dot{\zeta}$$

Substituting this operator identity directly into the field equation yields:
$$-M_\zeta^2 \left(\ddot{\zeta} + 3H\dot{\zeta}\right) - V_{,\zeta} + \frac{\xi_{\text{SF}} \zeta}{\kappa} R = 0$$

Multiplying by $-1$ gives the final cosmological evolution equation for the order parameter:
$$M_\zeta^2 \left(\ddot{\zeta} + 3H\dot{\zeta}\right) + V_{,\zeta} - \frac{\xi_{\text{SF}} \zeta}{\kappa} R = 0$$

---

#### AI.10 Metric Field Equations & Tetrad Variation
Varying the action with respect to the metric tensor $g^{\mu\nu}$ yields the modified gravitational field equations:
$$F(\zeta) G_{\mu\nu} + \left( g_{\mu\nu} \Box - \nabla_\mu \nabla_\nu \right) F(\zeta) + \alpha_T \ell_*^2 \Theta_{\mu\nu}^{(T)} = \kappa \left[ T_{\mu\nu}^{(\zeta)} + T_{\mu\nu}^{(\text{matter})} \right]$$

where $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R$ is the standard Einstein tensor of the Levi-Civita connection, and $\Theta_{\mu\nu}^{(T)}$ is the metric stress-energy response of the quadratic torsion term:
$$\Theta_{\mu\nu}^{(T)} \equiv -\frac{2}{\sqrt{-g}} \frac{\delta \left( \frac{1}{2} \sqrt{-g} I_T \right)}{\delta g^{\mu\nu}}$$

---

#### AI.11 Stress-Energy Tensor of the Order Parameter
The canonical stress-energy tensor $T_{\mu\nu}^{(\zeta)} \equiv -\frac{2}{\sqrt{-g}} \frac{\delta (\sqrt{-g} \mathcal{L}_\zeta)}{\delta g^{\mu\nu}}$ derived from the scalar Lagrangian density $\mathcal{L}_\zeta = \mathcal{L}_{\text{kin}} - V$ is given by:
$$T_{\mu\nu}^{(\zeta)} = M_\zeta^2 \nabla_\mu \zeta \nabla_\nu \zeta - g_{\mu\nu} \left[ \frac{1}{2} M_\zeta^2 g^{\alpha\beta} \nabla_\alpha \zeta \nabla_\beta \zeta + V(\zeta) \right]$$

For a homogeneous spatial background field $\zeta(t)$, $g^{\alpha\beta} \nabla_\alpha \zeta \nabla_\beta \zeta = g^{00} (\dot{\zeta})^2 = -(\dot{\zeta})^2$. The component energy density $\rho_\zeta \equiv T_{00}^{(\zeta)}$ and isotropic pressure $p_\zeta \equiv T_{ii}^{(\zeta)} / a^2$ resolve to:
$$\rho_\zeta = \frac{1}{2} M_\zeta^2 \dot{\zeta}^2 + V(\zeta)$$
$$p_\zeta = \frac{1}{2} M_\zeta^2 \dot{\zeta}^2 - V(\zeta)$$

---

#### AI.12 Infrared General Relativity Limit ($\beta \to 0$)
In the macroscopic infrared limit ($L \gg \ell_* \implies \beta \to 0$):
1. The quadratic torsion terms decay as $\alpha_T \ell_*^2 \Theta_{\mu\nu}^{(T)} \sim \mathcal{O}(\beta^2) \to 0$.
2. The order parameter relaxes to its stable potential minimum $\zeta \to 0$.
3. The non-minimal coupling function reduces to $F(0) = 1$.
4. The scalar stress-energy tensor vanishes $T_{\mu\nu}^{(\zeta)} \to 0$.

Under these conditions, the modified field equation reduces identically to standard General Relativity:
$$G_{\mu\nu} = \kappa T_{\mu\nu}^{(\text{matter})}$$
recovering standard Einsteinian gravity as an exact infrared fixed point.

---

#### AI.13 Structural Limitations and Open Physical Specifications
While the field equations, power-counting scheme, and infrared GR limit of this scalar-torsion EFT are mathematically self-consistent, Appendix AI represents a minimal kinematic scaffold rather than a fully specified physical theory. Closing the framework requires three distinct next steps:

1. **Explicit Specification of the Potential $V(\zeta)$:**
  While the vacuum conditions $V(0) = V'(0) = 0$ and $V''(0) > 0$ are fixed to enforce the IR ground state, the full non-linear structure of $V(\zeta)$ (e.g., polynomial quartic vs. non-perturbative exponential/axionic forms) remains open. The explicit functional form dictates early-universe inflationary dynamics, order parameter phase transitions, and late-time dark energy behavior.

2. **Dynamical Constraint on the Torsional Coupling $\alpha_T$:**
  The dimensionless coefficient $\alpha_T$ regulates higher-derivative quadratic torsion terms ($\Theta_{\mu\nu}^{(T)}$). Currently treated as an $\mathcal{O}(1)$ EFT coupling, its precise numerical bounds must be constrained either through microscopic lattice matching or phenomenological bounds from precision solar-system tests and frame-dragging measurements.

3. **Extraction of Observational and Testable Predictions:**
  To elevate the scaffold to a testable physical theory, the field equations yield clear targets for experimental falsification, prioritized by immediate availability of existing data:
  * **Sub-Millimeter Fifth-Force Bounds (Primary Immediate Constraint):** Expanding $V(\zeta)$ around $\zeta = 0$ yields an effective scalar mass $m_\zeta^2 = V''(0)/M_\zeta^2$. Precision Eöt-Wash torsion-balance experiments bound residual Yukawa forces at short ranges ($\lambda \lesssim 50\ \mu\text{m}$), establishing an immediate experimental ceiling on $M_\zeta$ and $V''(0)$ prior to full FLRW cosmological modeling.
  * **B-Mode Polarization & Torsional Waves:** Propagation signatures and dispersion relations for microscopic contortion modes in primordial gravitational wave backgrounds via higher-derivative $\alpha_T \Theta_{\mu\nu}^{(T)}$ terms.
  * **Cosmological Perturbations:** Scale-dependent modification of the scalar/tensor power spectrum during spectral dimension flow ($d_s: 2 \to 4$).
