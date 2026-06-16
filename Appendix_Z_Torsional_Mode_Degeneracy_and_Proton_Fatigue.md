Appendix Z — Numerical Closure & Implementation

Z.1 Phase-Space Normalization & Cutoff

The phase-space measure in D dimensions is defined as:
\Omega_D \equiv \int \frac{d^D x \, d^D k}{(2\pi \hbar)^D}

Torsional excitations follow the dispersion relation:
\omega^2 = |\mathbf{k}|^2 + m_{\text{eff}}^2

An isotropic ultraviolet cutoff is imposed:
\omega \le \omega_{\max}, \quad \omega_{\max} \equiv \frac{1}{t_V}

⸻

Z.2 Torsional Multiplicity

The total torsional degeneracy is:
N_{\text{torsion}} \equiv F = 349

with decomposition:
N_{\text{torsion}} = 240 + 109

and active projection:
N_{\text{active}} = 332

⸻

Z.3 Stress–Energy Conservation and Transfer

Global conservation is enforced:
\nabla_\mu T^{\mu\nu}_{\text{total}} = 0

with inter-sector energy transfer defined by:
Q^\nu = - \left[ n_b \left(\frac{d m_{p,\text{eff}}}{d\tau}\right) \right] u^\nu

⸻

Z.4 Redshift Evolution & Numerical Jacobian

Mass evolution in proper time is related to redshift via:
\frac{d m_{p,\text{eff}}}{d\tau}
=
\frac{d m_{p,\text{eff}}}{dz} \cdot \left[-(1+z)\,H_{\text{eff}}(z)\right]

The effective Hubble parameter is:
H_{\text{eff}}(z) = H_{\Lambda\text{CDM}}(z)\,(1 - \delta_t)

⸻

Z.5 Coupling Normalization

The baryon number density is given by:
n_b = \mathcal{C} \cdot \eta_{\text{geom}} \cdot \Lambda_0^3

with:
\eta_{\text{geom}} = 1 - \left(\frac{\varepsilon_c}{\varepsilon_{\text{init}}}\right)^3

and scaling:
\mathcal{C} \sim \frac{1}{N_{\text{roots}}}, \quad N_{\text{roots}} = 240

⸻

Z.6 Observational Quantities

The baryon-to-photon ratio is:
\eta_{\text{obs}} = \frac{n_b}{n_\gamma}

The baryonic energy density evolves as:
\rho_b(z) = n_b \, m_{p,\text{eff}}(z) \, (1+z)^3

⸻
Z.7 Closure Conditions
The framework is fully specified by the following core boundary criteria:
 UV Cutoff: \omega_{\max} = \frac{1}{t_V}
 Finite Torsional Spectrum: N_{\text{torsion}}
 Energy Conservation: \nabla_\mu T^{\mu\nu}_{\text{total}} = 0
 Redshift Mapping: Established via the direct Jacobian relation between proper time (\tau) and redshift (z).
 Geometric Baryon Generation: Governed by the cosmic asymmetry parameter \eta_{\text{geom}} and its associated normalization scalar \mathcal{C}.
These relations collectively define a closed numerical system connecting the microscopic, geometric phase-space structure directly to macroscopic cosmological observables.

Z.8 Telemetry Inversion and Spectral Closure via Appendix AO
To map geometric phase-space parameters to observable data streams, the framework must account for real-time environmental interactions and noise. The deterministic evolution calculated across redshift (z) and proper time (\tau) experiences phase-decoherence when interacting with an open cosmic environment. This shifts the spacing profile of the system's states away from its pure, uncorrupted layout toward a chaotic continuum.
This open-system degradation is closed by introducing an adaptive linear operator matrix, derived directly from the thermalization trajectory established in Appendix AO.

Z.8.1 The Decoherence Mapping
The interaction between the active torsional multiplicity (N_{\text{active}} = 332) and the surrounding environment is modeled as a continuous thermalization function parameterized by an effective temperature T_{\text{env}}(z). This temperature parameter is dynamically coupled to the global redshift evolution scale:
