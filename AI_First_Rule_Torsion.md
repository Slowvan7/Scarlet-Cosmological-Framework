# Appendix AI: Substrate Kinematics, Biharmonic Buckling, Metric-Affine Field Theory Formulation, and Microscopic Boundaries

### AI.1 Substrate Topology and Domain Boundary Conditions
To analyze the pre-geometric mechanics of space fabric collapse without boundary energy dissipation, we model the primary 2D substrate on an orientable 2-torus fundamental domain:

$$\Omega = [0, L_x] \times [0, L_y] \quad \text{with no boundary } (\partial T^2 = \emptyset)$$

The substrate displacement field $\mathbf{u}(x, y) = (u_x, u_y)$ satisfies periodic boundary conditions along both spatial directions:

$$\mathbf{u}(0, y) = \mathbf{u}(L_x, y), \quad \mathbf{u}(x, 0) = \mathbf{u}(x, L_y)$$

Because the 2-torus is a compact manifold with no boundary ($\partial T^2 = \emptyset$), the domain provides total spatial energy containment during localized compression events, preventing boundary edge dissipation.

---

### AI.2 Mechanical Torque and Hydrodynamic Circulation
Centripetal collapse within the space fabric substrate is driven by non-central localized collisions. Let two distinct space fabric density perturbations interact with relative translational momentum $\mathbf{p}_{\text{rel}}$ and a non-zero mechanical impact vector $\mathbf{b} \neq \mathbf{0}$.

The initial orbital angular momentum density injected into the 2D fluid domain is given by:

$$\mathbf{L}_{\text{collision}} = \mathbf{b} \times \mathbf{p}_{\text{rel}}$$

Adopting the 2D Levi-Civita orientation $\epsilon^{12} = +1$ with in-plane vorticity defined as $\omega_z \equiv \epsilon^{ij} \partial_i u_j = \partial_x u_y - \partial_y u_x$, the total circulation $\Gamma$ around the central interaction core evaluates to:

$$\Gamma = \oint_{\partial \text{core}} \mathbf{u} \cdot d\mathbf{x} = \iint_{\text{core}} \omega_z \, dA \neq 0$$

The sign of the circulation $\text{sgn}(\Gamma)$ is strictly fixed by the kinetic collision geometry: $\text{sgn}(\Gamma) = \text{sgn}(\mathbf{b} \times \mathbf{p}_{\text{rel}})$.

**Field Mass Dimension Specification:** In the pre-geometric space fabric substrate, the field $\mathbf{u}$ represents a linear momentum density field rather than a spatial displacement distance. Thus, its mass dimension is explicitly set to $[\mathbf{u}] = M^1$ ($L^{-1}$). Consequently, spatial derivatives ($\partial_i \sim M^1$) yield a vorticity dimension of $[\omega_z] = M^2$, preserving exact dimensional closure across all field couplings.

---

### AI.3 Biharmonic Buckling into 3D Space
When localized compression stress accumulated within the 2D planar core exceeds the critical lattice threshold, the substrate undergoes an out-of-plane buckling transition into 3D space, described by a spatial height displacement field $h(x, y)$ ($[h] = M^{-1}$).

Coupling the in-plane flow to out-of-plane deformation via a Dzyaloshinskii–Moriya (DM) type chiral interaction term in the surface action yields the non-homogeneous biharmonic plate-bending equation:

$$\kappa_{\text{flex}} \nabla^4 h = \gamma \epsilon^{ij} \partial_i u_j = \gamma \omega_z$$

where $\kappa_{\text{flex}}$ is the flexural rigidity ($[\kappa_{\text{flex}}] = M^1$) and $\gamma$ is the chiral coupling constant ($[\gamma] = M^2$). The orientation convention $\epsilon^{ij}\partial_i u_j \equiv +\omega_z$ ensures that positive kinetic vorticity $\omega_z > 0$ acts as a positive source for out-of-plane displacement. The resulting continuous 3D helical vortex channel generates a structural spatial helicity current density vector:

$$\mathbf{J}^{\text{helicity}} \equiv \omega_z \, \nabla h = (\epsilon^{ij} \partial_i u_j) \nabla h \quad ([\mathbf{J}^{\text{helicity}}] = M^2)$$

---

### AI.4 Field-Theoretic Decomposition of Quadratic Torsion and Contortion Mapping
In metric-affine geometry under signature $(-,+,+,+)$, the torsion tensor $T^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\mu\nu} - \Gamma^\lambda{}_{\nu\mu}$ and its quadratic invariant $I_T \equiv T_{\alpha\beta\gamma} T^{\alpha\beta\gamma}$ decompose under $SO(1,3)$ into three orthogonal irreducible representations:

$$T_{\alpha\beta\gamma} = \frac{1}{3} \left( v_\beta g_{\alpha\gamma} - v_\gamma g_{\alpha\beta} \right) + \epsilon_{\alpha\beta\gamma\delta} S^\delta + q_{\alpha\beta\gamma}$$

where:
* **Vector Torsion ($v_\mu$):** $v_\mu \equiv T^\alpha{}_{\mu\alpha} = -T^\alpha{}_{\alpha\mu}$
* **Axial Contortion Vector ($S_\mu$):** $S_\mu \equiv \frac{1}{6} \epsilon_{\mu\alpha\beta\gamma} T^{\alpha\beta\gamma}$ (with $\epsilon_{0123} = +1$)
* **Pure Tensor Torsion ($q_{\alpha\beta\gamma}$):** Trace-free and non-pseudovector part ($q^\alpha{}_{\mu\alpha} = 0$, $\epsilon^{\mu\alpha\beta\gamma} q_{\alpha\beta\gamma} = 0$).

Contracting this irreducible decomposition yields the exact Lorentzian identity:

$$I_T \equiv T_{\alpha\beta\gamma} T^{\alpha\beta\gamma} = +\frac{2}{3} v_\mu v^\mu - 6 S_\mu S^\mu + q_{\alpha\beta\gamma} q^{\alpha\beta\gamma}$$

**Mass Dimension Note:** Since $S_\mu$ is constructed linearly from the raw torsion tensor $T^{\alpha\beta\gamma}$, it inherits the same mass dimension as $T$ itself. Requiring $I_T$ to carry overall dimension $M^4$ (so that $S_{\text{torsion}}$ below is a properly dimensionless action) fixes $[S_\mu] = M^2$, matching $[v_\mu] = [q_{\alpha\beta\gamma}] = M^2$.

Inserting this expansion into the quadratic torsion action $S_{\text{torsion}} = \frac{\alpha_T \ell_*^2}{2\kappa} \int d^4x \sqrt{-g} \, I_T$ isolates the explicit quadratic action for the axial contortion field $S_\mu$:

$$\mathcal{L}_{\text{axial}} = -3 \alpha_T \ell_*^2 M_{\text{Pl}}^2 \, S_\mu S^\mu \equiv -\xi_{\text{ax}} S_\mu S^\mu$$

where $\xi_{\text{ax}} \equiv 3 \alpha_T \ell_*^2 M_{\text{Pl}}^2$ is the dimensionless contortion stiffness parameter ($[\xi_{\text{ax}}] = M^0$). With $[S_\mu] = M^2$, this term now carries the correct Lagrangian-density dimension $M^4$ directly, with no additional compensating factor required.

Coupling $S_\mu$ to the 4-current density vector $\mathcal{J}_\mu^{\text{helicity}} = (0, \mathbf{J}^{\text{helicity}})$ via effective action:

$$\mathcal{S}_{\text{eff}} = \int d^4x \sqrt{-g} \left[ -\xi_{\text{ax}} S^\mu S_\mu + \alpha_c S^\mu \mathcal{J}_\mu^{\text{helicity}} \right]$$

Dimensional matching of the source term ($[\alpha_c] + [S_\mu] + [\mathcal{J}^{\text{helicity}}] = 0 + 2 + 2 = 4$) requires $[\alpha_c] = M^0$ (dimensionless).

Variation $\frac{\delta \mathcal{S}_{\text{eff}}}{\delta S^\mu} = 0$ locks the contortion expectation value to the substrate buckling source:

$$\langle S_0 \rangle = 0, \quad \langle \mathbf{S} \rangle = \frac{\alpha_c}{2 \xi_{\text{ax}}} \mathbf{J}^{\text{helicity}} = \frac{\alpha_c}{6 \alpha_T \ell_*^2 M_{\text{Pl}}^2} \, \omega_z \nabla h \quad ([\langle \mathbf{S} \rangle] = M^2)$$

---

### AI.5 Downstream Coupling and Anisotropic Cosmic Birefringence
The contortion vector expectation value $\langle \mathbf{S} \rangle$ couples to electromagnetic fields in the effective action via the axial Chern-Simons term:

$$\mathcal{L}_{\text{CS}} = -\frac{1}{4} g_{\text{A}S} S_\mu A_\nu \tilde{F}^{\mu\nu}$$

With $[S_\mu] = M^2$, $[A_\nu] = M^1$, and $[\tilde F^{\mu\nu}] = M^2$, requiring $\mathcal{L}_{\text{CS}}$ to carry dimension $M^4$ fixes $[g_{\text{A}S}] = M^{-1}$ — matching the standard convention for axion-like Chern-Simons couplings in the particle-physics literature (e.g. $g_{a\gamma\gamma}$, conventionally quoted in $\text{GeV}^{-1}$).

We write $g_{\text{A}S} = \tilde{g}_{\text{A}S} / M_{\text{Pl}}$, with $\tilde{g}_{\text{A}S} \sim \mathcal{O}(1)$ dimensionless.

Integrating $\mathcal{L}_{\text{CS}}$ along a photon worldline over a cosmological propagation distance $L_{\text{H}} \sim H_0^{-1}$ yields the anisotropic cosmic polarization rotation angle $\beta$:

$$\beta(\hat{\mathbf{k}}) = \frac{1}{2} g_{\text{A}S} \int \langle \mathbf{S} \rangle \cdot \hat{\mathbf{k}} \, dr = \frac{\tilde{g}_{\text{A}S}}{2 M_{\text{Pl}}} \, |\langle \mathbf{S} \rangle| \, L_{\text{H}}$$

#### AI.5.1 Natural-Scale Calibration of the Helicity Transfer Efficiency

**Microscopic input.** At the fundamental UV lattice scale, the substrate fields have no available scale other than $\ell_*$ and $M_{\text{Pl}}$ themselves ($\ell_* \sim 1/M_{\text{Pl}}$). Taking the natural saturation estimates $\mathbf{u} \sim M_{\text{Pl}}$ and $h \sim \ell_*$ at the lattice cutoff gives:

$$\omega_z \sim \frac{u}{\ell_*} \sim M_{\text{Pl}}^2, \qquad \nabla h \sim \frac{h}{\ell_*} \sim \mathcal{O}(1) \implies \mathbf{J}^{\text{helicity}} = \omega_z \nabla h \sim M_{\text{Pl}}^2$$

**Resulting closed-form relation.** Writing $\alpha_c \equiv \eta_{\text{cut}}^2$ (dimensionless), and using $6\,\alpha_T \ell_*^2 M_{\text{Pl}}^2 \approx 6$ for $\alpha_T \sim \mathcal{O}(1)$:

$$|\langle \mathbf{S} \rangle| \approx \frac{\eta_{\text{cut}}^2}{6} \, M_{\text{Pl}}^2$$

**Calibration against observation.** Using $\beta_{\text{slip}} = 0.21^\circ \approx 3.665\times10^{-3}\,\text{rad}$, $L_{\text{H}} = 1/H_0 \approx 6.7\times10^{41}\,\text{GeV}^{-1}$ (for $H_0 \approx 67$–$73\ \text{km/s/Mpc}$), and $\tilde{g}_{\text{A}S} \sim 1$:

$$|\langle \mathbf{S} \rangle|_{\text{required}} = \frac{2\beta_{\text{slip}} M_{\text{Pl}}}{\tilde{g}_{\text{A}S} L_{\text{H}}} \approx 1.3\times10^{-25}\ \text{GeV}^2$$

Solving for the suppression parameter:

$$\eta_{\text{cut}} = \sqrt{\frac{6\,|\langle \mathbf{S} \rangle|_{\text{required}}}{M_{\text{Pl}}^2}} \approx 7.3\times10^{-32}$$

**Methodological Note on Parameter Calibration and Remaining Gap:** $\eta_{\text{cut}} \approx 7.3\times10^{-32}$ is obtained by calibrating against the observed birefringence angle $\beta \approx 0.21^\circ$ (ACT DR6), combined with an explicit, checkable assumption — Planck-scale saturation of the substrate fields at the UV cutoff — rather than being silently absorbed into an unconstrained coupling. This is a genuine improvement over treating $\eta_{\text{cut}}$ as a free fit to an unspecified microscopic input: the saturation assumption is itself falsifiable and could be revised.

Compared against the candidate natural scale $\sqrt{H_0/M_{\text{Pl}}} \approx 3.5\times10^{-31}$, the calibrated value differs by a factor of $\sim 4.8$ — smaller than an earlier draft's $\sim7$ estimate (which used an $L_{\text{H}}$ value approximately $2\times$ too large; corrected here to $L_{\text{H}}=1/H_0$ directly) and substantially smaller than the two-order-of-magnitude discrepancy found under the original dimensionally inconsistent treatment. Closing this residual factor of $\sim 4.8$ remains the concrete open target for full predictive closure of this sector.

---

### AI.6 Macro-EFT Action, Mass Dimensions, and Parameter Hierarchy
We work in natural units ($\hbar = c = k_B = 1$) under signature $(-,+,+,+)$. The macroscopic spacetime manifold is governed by an EFT coupling metric-affine geometry to a dimensionless scalar order parameter $\zeta$:

$$S = \int d^4x \sqrt{-g} \left[ \frac{1}{2\kappa} F(\zeta) R + \mathcal{L}_{\text{kin}}(\zeta) - V(\zeta) + \frac{\alpha_T \ell_*^2}{2\kappa} I_T \right] + S_{\text{matter}}[g_{\mu\nu}, \psi]$$

where $\kappa \equiv 8\pi G = M_{\text{Pl}}^{-2}$ is Einstein's gravitational constant ($[\kappa] = M^{-2}$), and $R$ is the Ricci scalar ($[R] = M^2$).

#### AI.6.1 Master Mass Dimensions Table
All physical quantities across the microscopic substrate and macroscopic EFT satisfy exact mass dimension closure $[X] = M^d$:

| Quantity | Symbol | Mass Dimension $[X]$ | Definition / Physical Scaling |
| :--- | :--- | :--- | :--- |
| **Lattice Cutoff** | $\ell_*$ | $M^{-1}$ | Fundamental UV cutoff length scale |
| **Micro Relaxation Time** | $t_*$ | $M^{-1}$ | Internal substrate clock scale ($c_{\text{eff}} = \ell_*/t_*$) |
| **Planck Mass** | $M_{\text{Pl}}$ | $M^1$ | $M_{\text{Pl}} = 1/\sqrt{\kappa}$ |
| **Substrate Field** | $\mathbf{u}$ | $M^1$ | Pre-geometric momentum density vector field |
| **Height Displacement** | $h$ | $M^{-1}$ | Spatial out-of-plane coordinate |
| **Vorticity** | $\omega_z$ | $M^2$ | $\omega_z = \epsilon^{ij} \partial_i u_j$ |
| **Flexural Rigidity** | $\kappa_{\text{flex}}$ | $M^1$ | Substrate plate bending stiffness |
| **Chiral Source Coupling** | $\gamma$ | $M^2$ | DM-type out-of-plane coupling |
| **Helicity Density Current**| $\mathbf{J}^{\text{helicity}}$ | $M^2$ | $\mathbf{J}^{\text{helicity}} = \omega_z \nabla h$ |
| **Helicity Coupling Scale** | $\alpha_c$ | $M^0$ (Dimensionless) | $\alpha_c = \eta_{\text{cut}}^2$, substrate-to-torsion coupling |
| **Axial Contortion Vector** | $S_\mu$ | $M^2$ | $S_\mu = \frac{1}{6} \epsilon_{\mu\alpha\beta\gamma} T^{\alpha\beta\gamma}$ |
| **Chern-Simons Coupling** | $g_{\text{A}S}$ | $M^{-1}$ | $g_{\text{A}S} = \tilde g_{\text{A}S}/M_{\text{Pl}}$; axion-like normalization |
| **Axial Stiffness Parameter**| $\xi_{\text{ax}}$ | $M^0$ (Dimensionless) | $\xi_{\text{ax}} = 3 \alpha_T \ell_*^2 M_{\text{Pl}}^2$ |
| **Order Parameter** | $\zeta$ | $M^0$ (Dimensionless) | Internal state of the space fabric |
| **Symmetry Energy Scale** | $M_\zeta$ | $M^1$ | Mass scale of order-parameter field |
| **Order Potential** | $V(\zeta)$ | $M^4$ | Vacuum potential density |

---

### AI.7 Kinetic, Potential, and Coupling Definitions
The coupling function $F(\zeta)$ introduces a non-minimal coupling between the order parameter and curvature:

$$F(\zeta) = 1 + \xi_{\text{SF}} \zeta^2$$

where $\xi_{\text{SF}} \approx 2/11$ is a dimensionless non-minimal ansatz matching the $d_s: 2 \to 4$ spectral dimension transition. The kinetic Lagrangian density for the order parameter is:

$$\mathcal{L}_{\text{kin}}(\zeta) = -\frac{1}{2} M_\zeta^2 g^{\mu\nu} \nabla_\mu \zeta \nabla_\nu \zeta$$

The background potential $V(\zeta)$ ($[V] = M^4$) satisfies the physical vacuum ground-state conditions: $V(0) = 0$, $V'(0) = 0$, and $V''(0) > 0$.

---

### AI.8 Scalar Order Parameter Field Equation
Varying the total action with respect to $\zeta$ via $\frac{\delta S}{\delta \zeta} = 0$ yields:

$$M_\zeta^2 \Box \zeta - V_{,\zeta} + \frac{\xi_{\text{SF}} \zeta}{\kappa} R = 0$$

In a flat FLRW background with metric signature $(-,+,+,+)$, the evolution equation for a homogeneous field $\zeta(t)$ reduces to:

$$M_\zeta^2 \left(\ddot{\zeta} + 3H\dot{\zeta}\right) + V_{,\zeta} - \frac{\xi_{\text{SF}} \zeta}{\kappa} R = 0$$

---

### AI.9 Metric Field Equations & Stress-Energy Tensor

#### AI.9.1 Modified Einstein Equations
Varying the action with respect to $g^{\mu\nu}$ yields:

$$F(\zeta) G_{\mu\nu} + \left( g_{\mu\nu} \Box - \nabla_\mu \nabla_\nu \right) F(\zeta) + \alpha_T \ell_*^2 \Theta_{\mu\nu}^{(T)} = \kappa \left[ T_{\mu\nu}^{(\zeta)} + T_{\mu\nu}^{(\text{matter})} \right]$$

#### AI.9.2 Stress-Energy Tensor of the Order Parameter
The canonical stress-energy tensor $T_{\mu\nu}^{(\zeta)}$ is:

$$T_{\mu\nu}^{(\zeta)} = M_\zeta^2 \nabla_\mu \zeta \nabla_\nu \zeta - g_{\mu\nu} \left[ \frac{1}{2} M_\zeta^2 g^{\alpha\beta} \nabla_\alpha \zeta \nabla_\beta \zeta + V(\zeta) \right]$$

#### AI.9.3 Infrared General Relativity Limit ($\beta \to 0$)
In the macroscopic infrared limit ($L \gg \ell_* \implies \beta \equiv \ell_*/L \to 0$):
1. Quadratic torsion terms decay as $\alpha_T \ell_*^2 \Theta_{\mu\nu}^{(T)} \sim \mathcal{O}(\beta^2) \to 0$.
2. The order parameter relaxes to its stable potential minimum $\zeta \to 0$.
3. $F(0) = 1$ and $T_{\mu\nu}^{(\zeta)} \to 0$.

The field equations reduce identically to standard General Relativity ($G_{\mu\nu} = \kappa T_{\mu\nu}^{(\text{matter})}$) as an exact infrared fixed point.

#### AI.9.4 Scope Clarification: Not a Dark-Sector Replacement

This appendix models the pre-geometric-to-4D transition and the resulting torsional contribution to cosmic birefringence. It does **not** constitute a dark matter or dark energy replacement mechanism. As shown above, both $T_{\mu\nu}^{(\zeta)}$ and the torsion backreaction $\Theta_{\mu\nu}^{(T)}$ vanish identically in the macroscopic IR limit, and the calibrated axial contortion $\langle \mathbf{S} \rangle \sim 10^{-25}\ \text{GeV}^2$ (AI.5.1) is many orders of magnitude too small to source galactic-scale or cosmological-scale curvature. The frozen background contortion of AI.10.3 sources the Chern-Simons photon coupling of AI.5 — a small, cumulative, non-gravitational effect — not the metric directly.

Explaining flat galaxy rotation curves, cluster virial dynamics, CMB acoustic peak structure, and late-time cosmic acceleration remains outside the scope of this appendix. Any account of these phenomena within the broader SCARLET framework requires either a standard $\Lambda$CDM-type dark sector or a separate, independently-derived mechanism — not an extension of the torsion sector modeled here.

---

### AI.10 Resolution of Microscopic Substrate Kinematics and Boundaries

#### AI.10.1 Kinematic Lapse Function Parametrization
The time parameter $t$ in the biharmonic buckling equation is an internal phase parameter of the 2D substrate, governed by $t_* \sim 10^{-41}\text{ s}$ via $c_{\text{eff}} = \ell_*/t_*$. Macroscopic cosmic proper time $\tau$ emerges post-buckling ($h \neq 0$) via the order-parameter lapse function $N(\zeta)$:

$$d\tau = N(\zeta) \, dt$$

We model the clock freezing mechanism via the even-parity, positive-definite functional form (derived in AI.12.1, replacing an earlier power-law ansatz):

$$N(\zeta) = N_0 \left(1 - e^{-(\zeta/\zeta_0)^2}\right)$$

In the unbuckled symmetric vacuum ($\zeta = 0, h = 0$), $N(0) = 0$, freezing cosmic proper time ($d\tau = 0$) while internal phase ordering proceeds along $t$. As buckling drives field condensation ($|\zeta| \gtrsim \zeta_0$), $N(\zeta) \to N_0$, establishing smooth 4D Lorentzian clock pacing. Because $N(\zeta)$ depends only on $\zeta^2$, it remains well-behaved even if $\zeta$ oscillates through zero during reheating (AI.10.4).

#### AI.10.2 UV Domain Scale Setting ($L_x, L_y$)
The spatial dimensions of the fundamental 2-torus domain $\Omega = [0, L_x] \times [0, L_y]$ are fixed at the UV lattice scale $L_x \sim L_y \sim \ell_* \approx \ell_{\text{Pl}} \sim 10^{-35}\text{ m}$. Macroscopic volume grows via the topological expansion of the height field $h(x,y,t)$.

#### AI.10.3 Phase-Locked Master Buckling Event
Periodic in-plane collision waves circulate around $T^2$, generating deterministic vorticity cycles $\omega_z(t)$. Once accumulated stress exceeds flexural rigidity $\kappa_{\text{flex}}$, the system undergoes an irreversible topological phase transition ($d_s: 2 \to 4$). This converts in-plane kinetic energy into a single non-linear expansion event along $h$, leaving microscopic contortion expectation values $\langle \mathbf{S} \rangle$ frozen into the background.

#### AI.10.4 Entropy Production via Order Parameter Reheating
Post-buckling, coherent displacement of $\zeta(t)$ drives damped oscillations around the stable IR minimum $\zeta_0 = 0$:

$$M_\zeta^2 \left(\ddot{\zeta} + 3H\dot{\zeta}\right) + V_{,\zeta} = -\Gamma_\zeta M_\zeta^2 \dot{\zeta}$$

(The friction term includes an explicit $M_\zeta^2$ factor, absent in an earlier draft, which was dimensionally short by $M^2$: with $[\Gamma_\zeta]=M^1$ and $[\dot\zeta]=M^1$, $\Gamma_\zeta\dot\zeta$ alone carries dimension $M^2$, not the $M^4$ required to match every other term in this equation. The corrected form follows directly from substituting the canonically normalized field $\phi\equiv M_\zeta\zeta$ into the standard Klein-Gordon-with-friction equation $\ddot\phi+3H\dot\phi+V'(\phi)=-\Gamma_\zeta\dot\phi$, which is self-consistent at dimension $M^3$, and dividing through by $M_\zeta$.)

The perturbative decay rate $\Gamma_\zeta$ governs energy transfer into standard matter fields $\psi$ within $S_{\text{matter}}[g_{\mu\nu}, \psi]$, thermalizing the substrate and producing the hot Big Bang entropy density $S_{\text{CMB}}$.

Note that $\Gamma_\zeta$ is specified explicitly in AI.12.2 (decay channel, coupling value, and resulting reheat temperature). This equation is a damped-oscillator equation; the generic solution for $\zeta$ settling toward $\zeta_0 = 0$ from a displaced initial value involves oscillation through zero rather than monotonic approach, which the even-parity lapse function of AI.10.1/AI.12.1 is constructed to handle correctly.

#### AI.10.5 Quantum Lattice Regularization and Non-Singular Bounce Dynamics
At short distances ($r < \ell_*$), spatial gradients are regularized by the discrete lattice dispersion relation:

$$\nabla^4 \longrightarrow \frac{16}{\ell_*^4} \left[ \sin^2\left(\frac{k_x \ell_*}{2}\right) + \sin^2\left(\frac{k_y \ell_*}{2}\right) \right]^2$$

(Prefactor corrected from an earlier draft's $4/\ell_*^4$: Taylor-expanding $\sin^2(k\ell_*/2)\approx(k\ell_*/2)^2$ for $k\ell_*\ll1$ requires $16/\ell_*^4$, not $4/\ell_*^4$, to correctly recover the continuum limit $\nabla^4 \to k^4$.)

Integrating the 2D surface bending energy density ($E/A \sim M^3$) across the effective transverse substrate layer thickness $d_\perp \sim \ell_*$ yields the exact 4D energy density scale:

$$\rho_{\text{max}} \sim \frac{\kappa_{\text{flex}}}{\ell_*^3} \quad ([\rho_{\text{max}}] = M^4)$$

In the high-density regime ($\rho \to \rho_{\text{max}}$), non-linear lattice acoustic modes contribute a negative high-density pressure term $P_{\text{eff}} = w\rho - \chi \left(\frac{\rho^2}{\rho_{\text{max}}}\right)$. The modified Raychaudhuri equation becomes:

$$\dot{H} = -\frac{\kappa}{2} (\rho + P_{\text{eff}}) = -\frac{\kappa}{2} \left[ (1+w)\rho - \chi \frac{\rho^2}{\rho_{\text{max}}} \right]$$

Evaluating at critical density $\rho = \rho_{\text{max}}$ with non-linear lattice stiffness parameter $\chi > 1 + w$ gives $\dot{H} = +\frac{\kappa}{2} (\chi - 1 - w) \rho_{\text{max}} > 0$. This guarantees accelerating expansion away from the minimum scale factor ($H = 0, \dot{H} > 0$), resolving spatial collapse via a non-singular quantum torsional bounce.

---

### AI.11 Open Parameters and Empirical Constraints

1. **Explicit Specification of the Potential $V(\zeta)$:**
 The non-linear form of $V(\zeta)$ remains an open functional pending full numerical bounce integration. It regulates early-universe inflationary dynamics and the smooth exit into slow-roll spatial expansion.

2. **Dynamical Constraint on Torsional Coupling $\alpha_T$:**
 The coefficient $\alpha_T$ is locked to contortion stiffness via $\xi_{\text{ax}} = 3 \alpha_T \ell_*^2 M_{\text{Pl}}^2$. Its magnitude is directly bounded by precision solar-system tests and cosmic birefringence limits.

3. **FRG Derivation of $\xi_{\text{SF}}$:**
 The non-minimal coupling constant $\xi_{\text{SF}} \approx 2/11$ is introduced as a structural ansatz matching spectral dimension flow ($d_s: 2 \to 4$), pending rigorous Functional Renormalization Group (FRG) flow derivation.

4. **Variational Derivation of $N(\zeta)$:**
  The even-parity form $N(\zeta) = N_0(1-e^{-(\zeta/\zeta_0)^2})$ (AI.10.1, AI.12.1) serves as a non-singular kinematic clock-freezing parametrization ($N(0)=0$, well-defined for all real $\zeta$). Deriving this form explicitly from first principles requires evaluating the ADM Hamiltonian constraint $\mathcal{H}=0$ under scalar-tensor variation.

5. **Sub-Millimeter Fifth-Force Bounds:**
 Expanding $V(\zeta)$ around $\zeta = 0$ yields an effective scalar mass $m_{\text{eff}}^2 \simeq V_{, \zeta\zeta} - (\xi_{\text{SF}}/\kappa)R$. State-of-the-art Eöt-Wash short-range gravity experiments establish that any gravitational-strength Yukawa interaction $V(r) = -\alpha G M r^{-1} e^{-r/\lambda}$ must satisfy:

$$\lambda < 38.6\ \mu\text{m} \quad (95\%\text{ CL}) \implies m_{\text{eff}} \gtrsim 5.1\ \text{meV}$$

 This places an immediate experimental floor on the scalar mass scale $m_{\text{eff}}$, tightly constraining $M_\zeta$ and $V_{,\zeta\zeta}(0)$ within the macroscopic effective action.

6. **Residual Factor in Natural-Scale Calibration:**
  The corrected calibration of $\eta_{\text{cut}}$ (AI.5.1, using $L_{\text{H}}=1/H_0$ directly) against the candidate natural scale $\sqrt{H_0/M_{\text{Pl}}}$ leaves an unexplained factor of $\sim 4.8$. Closing this gap requires an explicit $\mathcal{O}(1)$ prefactor from a proper loop-level or normal-mode calculation of the substrate-to-torsion transfer efficiency, rather than a new hierarchy of scales.

7. **Reheat Temperature and BBN Consistency:**
 As resolved in AI.12.2, modeling energy transfer via $\mathcal{L}_{\text{int}} = -g(M_\zeta\zeta)\bar\psi\psi$ through the electron pair-production channel, using the correct decay rate $\Gamma_\zeta = g^2m_{\text{eff}}\beta^3/(8\pi)$ (note the $\beta^3$ phase-space dependence, not $\beta^1$), and requiring $T_{\text{reheat}} \ge 1\ \text{MeV}$ at an illustrative benchmark $m_{\text{eff}}=10\ \text{MeV}$ fixes $g \approx 4.8\times10^{-11}$ — a natural, non-fine-tuned coupling, not highly sensitive to the specific benchmark chosen. Because item 5 establishes $m_{\text{eff}}$ only as a lower bound, a specific value above the $2m_e$ threshold must be chosen explicitly rather than assumed.

8. **Lapse Function Behavior During Reheating Oscillation:**
 Resolved in AI.10.1/AI.12.1: the even-parity form $N(\zeta) = N_0(1-e^{-(\zeta/\zeta_0)^2})$ replaces the earlier power-law ansatz and remains non-negative and well-defined for all real $\zeta$, correctly handling oscillation through zero during reheating.

9. **Solar System Constraints on $\xi_{\text{SF}}$:**
 The non-minimal coupling $\xi_{\text{SF}} \approx 2/11$ (AI.7) is distinct from, and in addition to, the short-range scalar mass bound of item 5. Non-minimal scalar-tensor couplings of this size are independently constrained by Solar System post-Newtonian tests — the Cassini bound on the PPN parameter $\gamma$ and Nordtvedt-effect tests of the equivalence principle. AI.12.3 shows that the direct scalar-exchange fifth-force is negligible at AU scales given $m_{\text{eff}} \ge 5.1\ \text{meV}$; however, whether the non-minimal coupling's modification of the effective gravitational constant (via $F(\zeta)$ in the metric field equations) is separately screened — via a chameleon- or symmetron-type density-dependent mechanism — remains unresolved and is required for full Cassini/Nordtvedt compliance.

10. **Explicit Form of the Torsion Stress-Energy Response $\Theta_{\mu\nu}^{(T)}$:**
 $\Theta_{\mu\nu}^{(T)}$ (AI.9.1) is defined formally as $-\frac{2}{\sqrt{-g}}\frac{\delta(\frac{1}{2}\sqrt{-g}I_T)}{\delta g^{\mu\nu}}$ but is never computed explicitly in terms of the torsion decomposition of AI.4. Its claimed $\mathcal{O}(\beta^2)$ decay in the IR limit (AI.9.3) follows from the general power-counting $I_T\sim\beta^2$, but an explicit component-level derivation of $\Theta_{\mu\nu}^{(T)}$ has not been carried out and remains an open task.

---

### AI.12 Resolution of Open Targets: ADM Lapse, Reheating, and PPN Screening

#### AI.12.1 Positive-Definite Lapse Function

To prevent zero-crossing anomalies during reheating oscillations ($\zeta \to 0$), the clock-freezing lapse function is updated to the even-parity form:

$$N(\zeta) = N_0 \left(1 - e^{-(\zeta/\zeta_0)^2}\right) \ge 0, \quad \forall \zeta \in \mathbb{R}$$

This function is manifestly even in $\zeta$ ($N(-\zeta) = N(\zeta)$), smooth, and satisfies $N(0) = 0$ and $N(\zeta) \to N_0$ as $|\zeta| \to \infty$. Because $N(\zeta)$ depends only on $\zeta^2$, it remains well-defined and non-negative regardless of the sign of $\zeta$, resolving the oscillation-through-zero problem identified in item 8 above without restricting the reheating dynamics of AI.10.4. This replaces the power-law ansatz of AI.10.1.

#### AI.12.2 Explicit BBN Reheating Thermalization

Coupling $\zeta$ to matter requires a properly dimensioned interaction. Using the canonically normalized field $\phi \equiv M_\zeta \zeta$ ($[\phi] = M^1$, consistent with the kinetic term of AI.7), the Yukawa-type interaction

$$\mathcal{L}_{\text{int}} = -g \, (M_\zeta \zeta) \, \bar\psi \psi \quad ([g] = M^0)$$

carries the correct Lagrangian-density dimension $M^4$ directly, with no additional UV scale required. For Yukawa coupling to fermions of mass $m_\psi$, the standard tree-level decay rate (derived from the spin-summed matrix element $\sum|M|^2 = 2g^2 m_{\text{eff}}^2 \beta^2$ combined with two-body phase space $\beta/8\pi$) is:

$$\Gamma_\zeta = \frac{g^2 \, m_{\text{eff}}}{8\pi}\left(1-\frac{4m_\psi^2}{m_{\text{eff}}^2}\right)^{3/2} = \frac{g^2 m_{\text{eff}} \beta^3}{8\pi}$$

where $m_{\text{eff}}$ is the same physical scalar mass already defined in item 5 ($m_{\text{eff}}^2 = V_{,\zeta\zeta}(0)/M_\zeta^2$), so no new mass scale is introduced. Note that $\beta \to 0$ exactly at threshold ($m_{\text{eff}} \to 2m_\psi$), so $m_{\text{eff}}$ must be taken meaningfully above the electron pair-production threshold ($m_{\text{eff}} \ge 2m_e \approx 1.022\ \text{MeV}$) for the channel to be open at all; item 5 establishes only a lower bound on $m_{\text{eff}}$ (5.1 meV), not a fixed value, so a specific benchmark above threshold must be chosen explicitly.

Using the standard reheating relation $T_{\text{reheat}} \approx 0.55\,g_*^{-1/4}\sqrt{\Gamma_\zeta M_{\text{Pl}}}$ with $g_* = 10.75$, requiring $T_{\text{reheat}} \gtrsim 1\ \text{MeV}$ (the BBN floor) at the illustrative benchmark $m_{\text{eff}} = 10\ \text{MeV}$ ($\beta_e \approx 0.995$) fixes:

$$g \approx 4.8 \times 10^{-11}$$

This is a natural, non-fine-tuned dimensionless coupling; the result is not highly sensitive to the specific benchmark chosen, ranging from $g\approx1.9\times10^{-10}$ near threshold ($m_{\text{eff}}=1.5\ \text{MeV}$) to $g\approx1.5\times10^{-11}$ at $m_{\text{eff}}=100\ \text{MeV}$. No further reheating channel is required to satisfy the BBN floor.

#### AI.12.3 Yukawa Screening of Direct Scalar-Exchange Forces

Enforcing the short-range bound $m_{\text{eff}} \ge 5.1\ \text{meV}$ ($\lambda \le 38.6\ \mu\text{m}$, item 5) gives a Compton wavelength $\lambda \approx 38.7\ \mu\text{m}$, versus $1\ \text{AU} \approx 1.5\times10^{11}\ \text{m}$ — a ratio of $\sim 4\times10^{15}$. The direct scalar-exchange fifth-force is therefore exponentially suppressed to complete irrelevance at Solar System distances:

$$e^{-r/\lambda}\Big|_{r=\text{AU}} \sim e^{-4\times10^{15}} \approx 0$$

**Scope of this result:** this addresses only the direct-exchange channel of the fifth-force constraint. It does **not** by itself establish full consistency with Cassini or Nordtvedt bounds, because the non-minimal coupling $\xi_{\text{SF}}$ in $F(\zeta) = 1+\xi_{\text{SF}}\zeta^2$ modifies the effective gravitational coupling through the metric field equations (AI.9.1) independently of the scalar's propagating mass. In real chameleon- and symmetron-type scalar-tensor theories, this requires a separate, explicit density-dependent screening mechanism (the scalar's effective mass growing near a dense source such as the Sun) — not merely a large vacuum mass. Demonstrating that $\xi_{\text{SF}} \approx 2/11$ is compatible with Cassini/Nordtvedt bounds via such a mechanism remains open (item 9, above).
