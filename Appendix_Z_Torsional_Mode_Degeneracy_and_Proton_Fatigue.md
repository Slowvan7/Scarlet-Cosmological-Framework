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
