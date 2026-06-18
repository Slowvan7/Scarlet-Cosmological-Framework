Appendix Z — Numerical Closure & Implementation

Z.1 Phase-Space Normalization & Cutoff
The phase-space measure in D dimensions is defined as:
\(\Omega _{D}\equiv \int \frac{d^{D}x\cdot d^{D}k}{(2\pi \hbar )^{D}}\)
Torsional excitations follow the dispersion relation:
\(\omega ^{2}=|\mathbf{k}|{}^{2}+m_{\text{eff}}^{2}\)
An isotropic ultraviolet cutoff is imposed:
\(\omega \le \omega _{\max },\quad \omega _{\max }\equiv \frac{1}{t_{V}}\)
⸻
 Z.2 Torsional Multiplicity
The total torsional degeneracy is:
\(N_{\text{torsion}}\equiv F=349\)
with decomposition:
\(N_{\text{torsion}}=240+109\)
and active projection:
\(N_{\text{active}}=332\)
⸻

 Z.3 Stress–Energy Conservation and Transfer
Global conservation is enforced across all fields:
\(\nabla _{\mu }T_{\text{total}}^{\mu \nu }=0\)
with inter-sector energy transfer defined by:
\(Q^{\nu }=-\left[n_{b}\left(\frac{dm_{p,\text{eff}}}{d\tau }\right)\right]u^{\nu }\)
⸻

 Z.4 Redshift Evolution & Numerical Jacobian
Mass evolution in proper time is related to redshift via:
\(\frac{dm_{p,\text{eff}}}{d\tau }=\frac{dm_{p,\text{eff}}}{dz}\cdot \left[-(1+z)\cdot H_{\text{eff}}(z)\right]\)
The effective Hubble parameter is:
\(H_{\text{eff}}(z)=H_{\Lambda \text{CDM}}(z)\cdot (1-\delta _{t})\)
⸻

 Z.5 Coupling Normalization
The baryon number density is given by:
\(n_{b}=\mathcal{C}\cdot \eta _{\text{geom}}\cdot \Lambda _{0}^{3}\)
with the geometric correction factor scaling as:
\(\eta _{\text{geom}}=1-\left(\frac{\varepsilon _{c}}{\varepsilon _{\text{init}}}\right)^{3}\)
and scaling:
\(\mathcal{C}\sim \frac{1}{N_{\text{roots}}},\quad N_{\text{roots}}=240\)
⸻

 Z.6 Observational Quantities
The baryon-to-photon ratio tracks as:
\(\eta _{\text{obs}}=\frac{n_{b}}{n_{\gamma }}\)
The baryonic energy density evolves over space-time as:
\(\rho _{b}(z)=n_{b}\cdot m_{p,\text{eff}}(z)\cdot (1+z)^{3}\)
⸻
Z.7 Closure Conditions
The framework is fully specified by the following core boundary criteria:
UV Cutoff: \(\omega_{\max} = \frac{1}{t_V}\)
Finite Torsional Spectrum: Finite dimensional boundary limited by \(N_{\text{torsion}}\).
Energy Conservation: Globally maintained via the identity \(\nabla_\mu T^{\mu\nu}_{\text{total}} = 0\).
Redshift Mapping: Established via the direct Jacobian relation between proper time (τ) and redshift (z).
Geometric Baryon Generation: Governed by the cosmic asymmetry parameter \(\eta _{\text{geom}}\) and its associated normalization scalar \(\mathcal{C}\).
These relations collectively define a closed numerical system connecting the microscopic, geometric phase-space structure directly to macroscopic cosmological observables.
⸻


Z.8 Telemetry Inversion and Spectral Closure via Appendix AO
To map geometric phase-space parameters to observable data streams, the framework must account for real-time environmental interactions and noise. The deterministic evolution calculated across redshift (z) and proper time (τ) experiences phase-decoherence when interacting with an open cosmic environment. This shifts the spacing profile of the system's states away from its pure, uncorrupted layout toward a chaotic continuum. This open-system degradation is closed by introducing an adaptive linear operator matrix, derived directly from the thermalization trajectory established in Appendix AO.

Z.8.1 The Decoherence Mapping
The interaction between the active torsional multiplicity (\(N_{\text{active}} = 332\)) and the surrounding environment is modeled as a continuous thermalization function parameterized by an effective temperature \(T_{\text{env}}(z)\). This temperature parameter is dynamically coupled to the global redshift evolution scale:
\(T_{\text{env}}(z)=\alpha \cdot \left[\frac{H_{\text{eff}}(z)}{H_{\Lambda \text{CDM}}(0)}\right]\)
This temperature acts as a localized phase-de-locking variable. It deforms the baseline spacing distribution of the crystalline lattice (\(P_{\text{twin}}\) at T=0) into a mixed state (\(P(s, T_{\text{env}})\)):
\(P(s,T_{\text{env}})=\frac{1}{Z(T_{\text{env}})}\cdot s^{(1-0.5T_{\text{env}})}\cdot \exp \left(-\left[1-\left(1-\frac{4}{\pi }\right)T_{\text{env}}\right]s^{1.5}\right)\)
Where \(Z(T_{\text{env}})\) serves as a local partition function, ensuring strict stress-energy probability conservation (\(\int P(s)ds = 1\) matching the closure conditions in Section Z.3).

Z.8.2 The Critical Phase Boundary
The system maintains structural stability against environmental noise as long as the effective operating temperature stays below the critical phase boundary (\(T_{\text{env}} < T_c\)). This boundary represents the maximum velocity of information dissipation, where the specific heat capacity (\(C_v(T)\)) of the phase-space measure spikes:
\(C_{v}(T)=T\cdot \frac{dH}{dT}\implies T_{c}\approx 0.4464\)
In the Coherent Regime (\(T_{\text{env}} < T_c\)): The underlying crystalline lattice remains structurally stable. The mapping between the microscopic torsional multiplicity (\(N_{\text{torsion}} = 349\)) and macroscopic observables is mathematically reversible.
In the Chaotic Regime (\(T_{\text{env}} \ge T_c\)): The system undergoes a complete phase collapse into the universal Gaussian Unitary Ensemble (GUE) continuum, permanently erasing the unique geometric signatures of the operator.

Z.8.3 Real-Time Linear Matrix Inversion
To recover the uncorrupted geometric lattice parameters from a noisy streaming telemetry vector (\(\vec{P}_{\text{corrupted}}\)), the pipeline implements a discrete matrix transformation filter. This filter collapses the complex integro-differential equations of decoherence into an instantaneous linear execution step with a complexity of \(\mathcal{O}(N)\):
\(\vec{P}_{\text{recovered}}=\mathbf{M}_{\text{filter}}\cdot \vec{P}_{\text{corrupted}}\)
The transformation matrix \((\mathbf{M}_{\text{filter}})\) is compiled as a static diagonal operator. It is stabilized using a Tikhonov regularization factor (ε = 0.01) to shield the system from zero-boundary measurement errors at the origin (s → 0):
\(\mathbf{M}_{\text{filter},ii}=\left(s_{i}+\varepsilon \right)^{0.5T_{\text{env}}}\cdot \exp \left(\left[1-\frac{4}{\pi }\right]T_{\text{env}}\cdot s_{i}^{1.5}\right)\)

Z.8.4 Complete System Integration
By introducing this streaming filter, the numerical loop is fully closed. The complete SCARLET pipeline can now process incoming data, strip away environmental noise, and map the underlying structural parameters back to the core geometric roots (\(N_{\text{roots}} = 240\)) and active torsional multiplicities defined in Appendix Z.
