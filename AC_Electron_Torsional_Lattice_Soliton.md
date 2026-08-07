Appendix AC — Topological Defect Relaxation and the Emergent Electron
A Metric-Affine Derivation of Mass, Spin, Charge, and Electromagnetic Coupling
Framework: Scarlet–VanAcker Cosmological Framework (SCARLET 2.0)
AC.1 — Physical Motivation and Scope
The electron is characterized experimentally by a remarkably small set of precisely determined observables:
m_e,  e,  s = 1/2,  α,  μ_e
which conventional quantum field theory ordinarily introduces through measured parameters and subsequently uses to construct the particle sector.
SCARLET instead investigates whether these quantities can arise as macroscopic observables of a localized excitation of a more fundamental metric-affine torsional substrate.
The Central Hypothesis:
The electron is a stable topological torsional defect whose observable properties emerge from geometry, dimensional projection, and relaxation.
The electron is therefore not regarded as a static remnant of primordial energy. Rather, it is identified with the lowest-energy stable configuration within a non-trivial topological sector after the primordial torsional substrate has undergone cosmic relaxation.
The general mass relation is:
E_e(t_0) = E_* · R(t_0) · K_{11→4}
where E_* is the primordial defect scale, R(t_0) is the accumulated relaxation factor, and K_{11→4} describes the surviving four-dimensional projection of the higher-dimensional excitation.
The objective of this appendix is consequently to replace a phenomenological particle-property assignment with a sequence of mathematically testable mappings:
Metric-affine substrate → torsional defect → topological stabilization → cosmic relaxation → dimensional projection → (m_e, e, s, α, μ_e)
AC.2 — Metric-Affine Substrate
SCARLET employs a metric-affine connection:
Γ^λ_{μν} = {^λ_{μν}} + K^λ_{μν}
where {^λ_{μν}} is the Levi-Civita connection and K^λ_{μν} is the contortion.
The associated torsion tensor is:
T^λ_{μν} = Γ^λ_{μν} - Γ^λ_{νμ}
Its axial component is represented by:
S_μ = (1/6) · ε_{μνρσ} T^{νρσ}
and the SCARLET vacuum is taken to possess an ordered torsional background:
S_μ^{(0)} ≠ 0
The primordial substrate is characterized by the Bedrock scales:
ℓ_* = 10^-35 m
t_* = 10^-41 s
Σ_f = 10^35 Pa
These quantities establish the microscopic spatial scale, temporal update scale, and effective torsional response of the underlying lattice.
AC.3 — Formation of the Localized Defect
A particle excitation is introduced as a perturbation of the ordered torsional background:
K^λ_{μν} = K^{(0)λ}{μν} + δK^λ{μν}
The corresponding Bedrock frequency is:
ω_* = 1 / t_*
so that the initial excitation scale is:
E_* = ħ · ω_* = ħ / t_*
For t_* = 10^-41 s:
E_* = (1.05457 × 10^-34) / 10^-41 ≈ 1.05 × 10^7 J
Thus:
E_* ≈ 1.05 × 10^7 J
This is not identified with the present electron rest energy. It represents the characteristic microscopic energy associated with the primordial defect before cosmological relaxation.
A stable present-day particle therefore requires a dynamical mechanism capable of reducing this initial excitation by many orders of magnitude while preserving its non-trivial topology.
AC.4 — Topological Stabilization
Dissipation by itself would return a localized excitation to the trivial vacuum. SCARLET therefore requires a conserved defect current:
∇_μ J_T^μ = 0
The associated charge is:
Q_T = ∫_Σ J_T^μ dΣ_μ
The physical defect belongs to a fixed non-trivial topological sector:
Q_T ≠ 0
The electron is then defined as the minimum-energy configuration within that sector:
δF_{eff} = 0   (subject to Q_T = constant ≠ 0)
Consequently, the electron mass is not interpreted as residual primordial strain. It is the energy of the stable ground-state configuration remaining after relaxation while the topological invariant prevents complete decay.
AC.5 — Variational Defect Dynamics
The effective four-dimensional particle action is written:
S_{AC} = ∫ d^4x √(-g) ( L_{MA} + L_S + L_Ψ + L_{int} )
The metric-affine sector is:
L_{MA} = (1 / 2κ) · ( R + T_scalar )
where T_scalar denotes the relevant torsional scalar.
The propagating axial-torsion sector is:
L_S = - (1/4) H_{μν} H^{μν} - V_S(S_μ S^μ)
with
H_{μν} = ∇_μ S_ν - ∇_ν S_μ
The normalized defect field is represented schematically by:
Ψ = [ m/E_,  ℓ_ e^a_μ S^μ,  Θ ]^T
where m/E_* is the dimensionless energy amplitude, the second component describes the local axial-torsion configuration, and Θ denotes the torsional backreaction state.
Its covariant kinetic sector is:
L_Ψ = (1/2) (D_μ Ψ)† (D^μ Ψ) - U(Ψ)
while the localized torsional current couples through:
L_{int} = g_T J_T^μ S_μ
Variation with respect to Ψ† gives:
D_μ D^μ Ψ + ∂U / ∂Ψ† = 0
Variation with respect to S_ν produces:
∇_μ H^{μν} + ∂V_S / ∂S_ν = g_T J_T^ν
The localized excitation is therefore sourced within the same metric-affine system rather than being imposed independently on a pre-existing background.
AC.6 — Spinorial Coupling to Torsion
For spinorial degrees of freedom the covariant derivative contains the contortion contribution:
D_μ = ∂_μ + Γ_μ^{(T)} + i q A_μ
where
Γ_μ^{(T)} = (1/4) K_{μab} γ^{ab}
The corresponding Dirac operator may be written:
D_T = i γ^μ ∇_μ + (3i/4) γ^μ γ^5 S_μ
This provides the microscopic connection between the torsional geometry and spinorial matter.
The torsional background is decomposed as:
S_μ = S_μ^{(0)} + δS_μ
with S_μ^{(0)} describing the ordered vacuum and δS_μ the localized excitation.
AC.7 — Cosmic Relaxation
The defect does not remain at the Bedrock energy scale. Its effective order parameter evolves according to an infrared relaxation equation:
D_t Ψ = - Γ_{rel}(t) (δF_{eff} / δΨ†) + η(t) Θ Ψ
This equation is not intended to replace the fundamental action. It represents the coarse-grained regime obtained after microscopic lattice modes have been integrated out.
The overdamped approximation applies when:
|D_t^2 Ψ| << Γ_{rel} |D_t Ψ|
The accumulated energy reduction is represented by:
R(t_0) = exp[ - ∫{t*}^{t_0} (γ_R(t') / t') dt' ]
The present-day defect energy is therefore:
E_e(t_0) = E_* · R(t_0) · K_{11→4}
AC.7.1 Epoch-Dependent Relaxation
The dimensionless relaxation rate is modeled as:
γ_R(t) = γ_{intrinsic}(t) · Ξ(t)
where
γ_{intrinsic}(t) = γ_{late} + (γ_{early} - γ_{late}) / [ 1 + (t/τ_r)^p ]
and
Ξ(t) = 1 / [ 1 + (t/τ_f)^n ]
During the primordial high-strain regime:
γ_R → γ_{early} ≈ 0.38
At late times the intrinsic relaxation coefficient approaches:
γ_{late} = (η · sin β_0) / ξ_{11}
with
η = 0.083
β_0 = 0.21°
ξ_{11} = π^5 / 10395 ≈ 0.0294
Since sin(0.21°) ≈ 3.665 × 10^-3, one obtains:
γ_{late} ≈ 1.03 × 10^-2
The freeze-out function subsequently suppresses the effective late-time rate.
AC.8 — Electron Mass Closure
The SCARLET cosmic age is taken to be:
t_0 = 14.6 Gyr = 4.61 × 10^17 s
The logarithmic temporal interval is:
ln(t_0 / t_*) = ln(4.61 × 10^58) ≈ 135.08
For the specified relaxation trajectory:
I_R = ∫{t*}^{t_0} (γ_R(t') / t') dt' ≈ 46.31
Consequently:
R(t_0) = e^-46.31 ≈ 7.76 × 10^-21
The projected defect energy becomes:
E_e = (1.0546 × 10^7) · (7.76 × 10^-21) · K_{11→4}
The mass closure target requires:
K_{11→4} ≈ 1
Under this closure:
E_e ≈ 8.18 × 10^-14 J
m_e = E_e / c^2 ≈ 9.11 × 10^-31 kg
m_e c^2 ≈ 0.511 MeV
The interpretation is that the observed electron mass corresponds to the lowest-energy surviving defect state after relaxation and dimensional projection.
AC.9 — Present-Day Mass Stability
The fractional mass evolution follows from the relaxation law:
m_e_dot / m_e = - γ_R(t) / t
At the present epoch the freeze-out factor is assumed to have strongly suppressed the relaxation rate:
Ξ(t_0) → 0
with the model requiring:
γ_R(t_0) < 10^-8
Using the present cosmic age gives:
|(m_e_dot / m_e)| < 10^-8 / (1.46 × 10^10 yr) ≈ 10^-18 yr^-1
This is a direct falsifiability condition. A statistically established secular variation above the model's predicted bound would rule out the proposed frozen-relaxation mechanism.
AC.10 — Dimensional Reduction and the 11D-to-4D Projection
The primordial substrate is taken to possess eleven-dimensional geometric degrees of freedom, M^11, with the observed sector represented by M^4 ⊂ M^11.
The dimensional projection is represented by:
P_{11→4} : K^(11) → K^(4)
The survival fraction is defined by:
K_{11→4} = [ ∫{M^4} |δK^(4)|^2 dV_4 ] / [ ∫{M^11} |δK^(11)|^2 dV_11 ]
The electron mass therefore follows the chain:
(ℓ_, t_, Σ_f, β_0, η) → P_{11→4} → E_e → m_e
The condition K_{11→4} → 1 is consequently a mathematical target that must emerge from the compactification geometry rather than being treated as an adjustable empirical coefficient.
AC.11 — Spin as a Topological Quantum Property
The defect's rotational configuration is required to possess a non-trivial double-cover structure.
A 2π rotation gives:
Φ(θ + 2π) = -Φ(θ)
whereas a 4π rotation restores the state:
Φ(θ + 4π) = Φ(θ)
This corresponds to the double cover SU(2) → SO(3).
In the Finkelstein–Rubinstein construction, the rotational configuration space contains:
π_1( C_{defect}^{rot} ) ≅ π_1(SO(3)) = Z_2
Quantization of the corresponding collective coordinate permits half-integer angular momentum:
s = 1/2, 3/2, 5/2, ...
with the electron identified with the lowest spinorial sector:
s = 1/2
The half-integer character is therefore associated with the topology of configuration space rather than classical rotation of a finite-size object.
AC.12 — Torsional Charge and Charge Conjugation
The axial torsion field provides the geometric quantity from which the defect flux is constructed:
S_μ = (1/6) · ε_{μνρσ} T^{νρσ}
A conserved torsional flux is defined by:
Q_T = ∮_Γ S_μ dx^μ
The electromagnetic charge is then related through a normalization factor:
e = g_Q · Q_T
Charge conjugation is represented geometrically by:
C_T : S_μ → -S_μ
which induces Q_T → -Q_T and e → -e.
Thus the electron and positron correspond to opposite orientations of the same underlying topological defect family:
e^- ⟷ e^+
The corresponding current obeys:
∇_μ J_Q^μ = 0
AC.13 — Fine-Structure Constant
SCARLET identifies the electromagnetic coupling with a geometric projection of the torsional substrate.
The proposed relation is:
α = f_{geom} · (1 - η) · sin(β_0) · Φ_{11}
The geometric packing factor is:
f_{geom} = π / (3 √2) ≈ 0.74048
while β_0 = 0.21° and η = 0.083.
The internal projection normalization is required to satisfy:
Φ_{11} ≈ 2.932
Substitution gives:
α = (0.74048) · (0.917) · (3.665 × 10^-3) · (2.932) ≈ 7.297 × 10^-3
or
α^-1 ≈ 137.036
The critical requirement is that Φ_{11} be calculated from the compact geometry rather than selected to reproduce the measured coupling.
AC.14 — Compact Geometry and Closure Invariants
The compact sector is represented by a seven-dimensional manifold K^7 with G_2 structure.
For the associative three-form Φ_3:
Φ_3 ∧ *Φ_3 = |Φ_3|^2 · vol_7
With canonical normalization |Φ_3|^2 = 7, therefore:
vol_7 = (1/7) · Φ_3 ∧ *Φ_3
The decisive closure quantities are: K_{11→4}, Φ_{11}, and g_Q.
The dimensional survival factor must satisfy K_{11→4} → 1.
The electromagnetic projection invariant is targetted at:
Φ_{11} ≈ 2.932
These are closure targets, not additional phenomenological inputs.
AC.15 — Warped Dimensional Reduction
A warped eleven-dimensional geometry may be represented by:
ds_{11}^2 = e^(2A(y)) g_{μν_bar}(x) dx^μ dx^ν + g_{ab}^(7)(y) dy^a dy^b
Different four-dimensional operators acquire different warp-weighted integrals:
K_{11→4}^(X) = [ ∫{K^7} e^(p_X A(y)) √(g_7) d^7y ] / [ ∫{K^7} √(g_7) d^7y ]
Representative values in the proposed reduction are:
p_{grav} = 2,  p_{scalar} = 4,  p_{gauge} = 0
This formulation allows the projection of the torsional defect to be computed from a specified compact geometry and warp factor rather than assuming a universal numerical suppression factor.
AC.16 — Topological Couplings
AC.16.1 Torsional Charge Coupling
The effective charge normalization is represented by a period integral of the normalized G_2 form Φ_3_hat = ℓ_P^-3 Φ_3. For a non-trivial three-cycle C_3 ⊂ K^7:
g_Q = N_Q · (1 / 2π) ∫_{C_3} Φ_3_hat
AC.16.2 Chern–Simons Projection
The eleven-dimensional topological contribution is represented through:
Φ_{11} = ∫{M^11} Ω{CS}(ω) ∧ Ψ_4
where dΩ_{CS} = Tr(R^4) and Ψ_4 = *{K^7} Φ_3 is the co-associative four-form. The required closure is Φ{11} ≈ 2.932.
AC.17 — Nonlinear Defect Lagrangian and Localization
For numerical soliton construction, the effective static torsional Lagrangian is augmented by a higher-order field-strength term:
L_T = - (1/2) g^(ij) (D_i Ψ)† (D_j Ψ) - U(Ψ) - (1/4) H_{μν} H^{μν} - (κ_T / 4) (H_{μν} H^{μν})^2 - V_S(S_μ S^μ) - g_T S_μ J_T^μ
The stabilization coefficient is required to satisfy κ_T > 0.
The total defect energy is:
E = ∫_{R^3} d^3x H_T
Finite-energy configurations must obey:
lim_{r→∞} Ψ = Ψ_{vac}  and  lim_{r→∞} S_μ = S_μ^{(0)}
AC.18 — Derrick Scaling Condition
For a three-dimensional localized configuration, decompose the static energy into gradient, higher-order, and potential pieces:
E = E_2 + E_4 + E_0
Under scaling x → λx:
E(λ) = λ E_2 + λ^-1 E_4 + λ^3 E_0
Stationarity at λ = 1 requires:
dE/dλ |_{λ=1} = E_2 - E_4 + 3 E_0 = 0
hence:
E_4 = E_2 + 3 E_0
A numerical defect solution therefore cannot be accepted as a stable SCARLET electron unless it satisfies this virial/Derrick balance to numerical accuracy.
AC.19 — Radial Boundary-Value Problem
For an initial axisymmetric numerical search, use the physical azimuthal ansatz S_vec(r) = S_φ(r) φ_hat.
The resulting radial system is:
φ'' + (2/r) φ' - ∂U/∂φ = 0
S_φ'' + (2/r) S_φ' - (2 S_φ / r^2) - 2 V_S'(S_φ^2) S_φ - g_T j_T(r) = 0
Θ'' + (2/r) Θ' - ∂U/∂Θ = 0
Regularity at origin: φ(0) = 0, S_φ(r) = s_1 r + O(r^3), Θ'(0) = 0
Asymptotic vacuum: lim_{r→∞} φ(r) = v, lim_{r→∞} S_φ(r) = 0, lim_{r→∞} Θ(r) = 0
A converged solution has rest energy:
M_e c^2 = 4π ∫_0^∞ r^2 H_T(r) dr
AC.20 — Stability Operator
The second variation of the energy defines the coupled stability operator H_T_hat.
Stability requires all physical eigenvalues to be non-negative:
λ_i(H_T_hat) ≥ 0
The linearized spectrum satisfies:
H_T_hat ψ_k = ω_k^2 ψ_k
These fluctuation frequencies describe internal excitations of the defect and must not be confused with the classical rest mass itself.
AC.21 — Fermionic Quantization
The rotational sector possesses π_1(C_{defect}^{rot}) = Z_2, allowing a Finkelstein–Rubinstein quantization where:
Ψ(2π) = -Ψ  and  Ψ(4π) = Ψ
This supplies the required spin-1/2 sector.
The torsion-coupled Dirac operator is:
D_T = i γ^μ ∇_μ + (3i/4) γ^μ γ^5 S_μ
A candidate closure condition is Index(D_T) = 1.
AC.22 — Fermion Mass Spectrum
Let (Ψ_n, S_n) denote a sequence of nonlinear stationary solutions with masses:
M_n c^2 = E[Ψ_n, S_n] = ∫_{R^3} d^3x T^00[Ψ_n, S_n]
The electron is the lowest stable member. Higher lepton states must satisfy m_e < m_μ < m_τ without inserting observed ratios as inputs.
AC.23 — Magnetic Moment
At the classical level the target is the tree-level Dirac value g_e^{tree} = 2, with magnetic moment:
μ_e^{tree} = - (e ħ) / (2 m_e)
Experimental target:
|μ_e| ≈ 9.284764 × 10^-24 J/T
AC.24 — Geometry-to-Observable Mapping
The complete proposed mapping is:
K^7 ⟶ (K_{11→4}, Φ_{11}, g_Q) ⟶ (Ψ_e, S_e) ⟶ (m_e, e, s, α, μ_e)
Sectors:
 Topological sector: Q_T → e,  π_1(C_{defect}) → s
 Geometric sector: K^7 → Φ_{11} → α
 Dynamical sector: (Ψ_e, S_e) → E_e → m_e
 Collective sector: rotational zero modes → s, μ_e
AC.25 — Numerical Closure Pipeline
1. Step 1 — Specify compact geometry: Choose explicit K^7 with required G_2 structure, metric, cycles, warp factor.
2. Step 2 — Calculate geometric invariants: Evaluate K_{11→4}, Φ_{11}, g_Q.
3. Step 3 — Construct effective 4D action.
4. Step 4 — Solve nonlinear defect equations: δS_{eff}/δΨ_e = 0, δS_{eff}/δS_e = 0.
5. Step 5 — Verify localization: Check 0 < E_{defect} < ∞ and Derrick balance E_4 = E_2 + 3 E_0.
6. Step 6 — Test dynamical stability: Calculate spectrum of H_T_hat.
7. Step 7 — Quantize collective modes: Determine s = 1/2 and tree-level magnetic moment.
8. Step 8 — Compare observables against targets.
AC.26 — Observable Closure Conditions
The final electron solution must satisfy:
 Rest mass: 4π ∫_0^∞ r^2 H_T(r) dr = m_e c^2 ≈ 0.511 MeV
 Electric charge: Q_{EM} = ∫ J_{EM}^0 d^3x = -e
 Spin: |J| = ħ / 2
 Magnetic moment: μ_e ≈ -9.284764 × 10^-24 J/T
 Fine-structure constant: α^-1 ≈ 137.036
AC.27 — Falsification Criteria
1. Mass-drift test: If |m_e_dot / m_e| ≳ 10^-18 yr^-1, freeze-out is falsified.
2. Soliton existence: If no finite-energy solution exists, construction fails.
3. Derrick balance: Violation of E_4 = E_2 + 3 E_0 rules out static localized defect.
4. Stability: Negative eigenvalue in H_T_hat indicates instability.
5. Topological quantization: Failure to yield Z_2 structure invalidates spin-1/2 state.
6. Simultaneous closure: K^7 ⟶ (K_{11→4}, Φ_{11}, g_Q) ⟶ (m_e, e, s, α, μ_e) with zero post-hoc tuning.
AC.28 — Final Closure Map
(ℓ_, t_, Σ_f, β_0, η, t_0)
↓
11D metric-affine torsional substrate
↓
K^7 compact geometry
↓
(K_{11→4}, Φ_{11}, g_Q)
↓
localized nonlinear torsional defect
↓
cosmic relaxation and freeze-out
↓
(m_e, e, s, α, μ_e)
Principal Targets:
 K_{11→4} → 1
 Φ_{11} ≈ 2.932
 Index(D_T) = 1
 m_e c^2 ≈ 0.511 MeV
 s = 1/2
 Q_{EM} = -e
 α^-1 ≈ 137.036
 μ_e ≈ -9.284764 × 10^-24 J/T
Final Question:
Can a specified K^7 independently generate the required projection invariants and a stable electron defect?
Summary, Predictions, and Open Tests
 Closing Perspective: Electron is an emergent topological remnant of a bedrock torsional defect that relaxed over cosmic time.
 Consistency: Unifies cosmological torsional expansion with particle-scale localized structures.
 Primary Predictions:
1. Fractional mass drift |m_e_dot / m_e| < 10^-18 yr^-1.
2. Residual spin-dependent torsional coupling in high-precision atomic tests.
3. Geometric orientation duality corresponding to matter-antimatter symmetry.
 Final Statement: Appendix AC presents the electron as a surviving topological defect whose observed properties reflect the cosmic history of the underlying space fabric.
