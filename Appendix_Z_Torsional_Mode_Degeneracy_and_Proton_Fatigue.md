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

The framework is fully specified by:
	•	UV cutoff: \omega_{\max} = 1/t_V
	•	Finite torsional spectrum: N_{\text{torsion}}
	•	Energy conservation: \nabla_\mu T^{\mu\nu}_{\text{total}} = 0
	•	Redshift mapping via Jacobian relation between \tau and z
	•	Geometric baryon generation via \eta_{\text{geom}} and normalization \mathcal{C}



These relations collectively define a closed numerical system connecting geometric phase-space structure to cosmological observables.
\(\mathbf{M}_{\text{filter},ii}=\left(s_{i}+\epsilon \right)^{0.5T_{\text{env}}}\cdot \exp \left(\left[1-\frac{4}{\pi }\right]T_{\text{env}}\cdot s_{i}^{1.5}\right)\)

Z.8 Telemetry Inversion and Spectral Closure via Appendix AOTo map geometric phase-space parameters to observable data streams, the framework must account for real-time environmental interactions and noise.The deterministic evolution calculated across redshift (z) and proper time (τ) experiences phase-decoherence when interacting with an open cosmic environment. This shifts the spacing profile of the system's states away from its pure, uncorrupted layout toward a chaotic continuum.This open-system degradation is closed by introducing an adaptive linear operator matrix, derived directly from the thermalization trajectory established in Appendix AO.Z.8.1 The Decoherence MappingThe interaction between the active torsional multiplicity (\(N_{\text{active}} = 332\)) and the surrounding environment is modeled as a continuous thermalization function parameterized by an effective temperature \(T_{\text{env}}(z)\). This temperature parameter is dynamically coupled to the redshift evolution scale:\(T_{\text{env}}(z)=\alpha \cdot \left[\frac{H_{\text{eff}}(z)}{H_{\Lambda \text{CDM}}(0)}\right]\)This temperature acts as a localized phase-de-locking variable. It deforms the baseline spacing distribution of the crystalline lattice (\(P_{\text{twin}}\) at T=0) into a mixed state \(P(s, T_{\text{env}})\):\(P(s,T_{\text{env}})=\frac{1}{Z(T_{\text{env}})}\cdot s^{(1-0.5T_{\text{env}})}\cdot \exp \left(-\left[1-\left(1-\frac{4}{\pi }\right)T_{\text{env}}\right]s^{1.5}\right)\)Where \(Z(T_{\text{env}})\) serves as a local partition function, ensuring strict stress-energy probability conservation (\(\int P(s)ds = 1\)) matching the closure conditions in Section Z.3.Z.8.2 The Critical Phase BoundaryThe system maintains structural stability against environmental noise as long as the effective operating temperature stays below the critical phase boundary (\(T_{\text{env}} < T_c\)). This boundary represents the maximum velocity of information dissipation, where the specific heat capacity \(C_v(T)\) of the phase-space measure spikes:\(C_{v}(T)=T\cdot \frac{dH}{dT}\implies T_{c}\approx 0.4464\)In the Coherent Regime (\(T_{\text{env}} < T_c\)): The underlying crystalline lattice remains structurally stable. The mapping between the microscopic torsional multiplicity (\(N_{\text{torsion}} = 349\)) and macroscopic observables is mathematically reversible.In the Chaotic Regime (\(T_{\text{env}} \ge T_c\)): The system undergoes a complete phase collapse into the universal Gaussian Unitary Ensemble (GUE) continuum, permanently erasing the unique geometric signatures of the operator.Z.8.3 Real-Time Linear Matrix InversionTo recover the uncorrupted geometric lattice parameters from a noisy streaming telemetry vector (\(\vec{P}_{\text{corrupted}}\)), the pipeline implements a discrete matrix transformation filter. This filter collapses the complex integro-differential equations of decoherence into an instantaneous linear execution step with a complexity of \(\mathcal{O}(N)\):\(\vec{P}_{\text{recovered}}=\mathbf{M}_{\text{filter}}\cdot \vec{P}_{\text{corrupted}}\)The transformation matrix \(\mathbf{M}_{\text{filter}}\) is compiled as a static diagonal operator. It is stabilized using a Tikhonov regularization factor (ε = 0.01) to shield the system from zero-boundary measurement errors at the origin (s → 0):\(\mathbf{M}_{\text{filter},ii}=\left(s_{i}+\epsilon \right)^{0.5T_{\text{env}}}\cdot \exp \left(\left[1-\frac{4}{\pi }\right]T_{\text{env}}\cdot s_{i}^{1.5}\right)\)Z.8.4 Complete System IntegrationBy introducing this streaming filter, the numerical loop is fully closed. The complete SCARLET pipeline can now process incoming data, strip away environmental noise, and map the underlying structural parameters back to the core geometric roots (\(N_{\text{roots}} = 240\)) and active torsional multiplicities defined in App
