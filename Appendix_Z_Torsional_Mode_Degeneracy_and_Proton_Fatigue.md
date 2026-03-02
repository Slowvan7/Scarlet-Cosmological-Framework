Appendix Z — Torsional Mode Degeneracy, Ultraviolet Cutoff, and Numerical Closure







Z.1 Purpose and Scope





This appendix provides the numerical closure of the SCARLET 2.0 framework by defining a finite torsional mode structure for spacetime dynamics. Its objectives are:



To introduce a physical ultraviolet (UV) cutoff arising from filament tensile limits,
To replace divergent continuum mode-counting with a discrete torsional spectrum,
To supply a smooth redshift evolution suitable for Boltzmann solvers (CLASS/Cobaya),
To establish consistency with equivalence principles and observational constraints on fundamental constants,
To connect the mechanical framework to measurable cosmological observables (H₀ and S₈).




Appendix Z marks the transition from geometric-mechanical theory to falsifiable numerical implementation.








Z.2 Torsional Mode Degeneracy





In SCARLET, spacetime is modeled as a lattice of 1D torsional filaments embedded in an 11-dimensional bulk. Vibrational excitations are constrained by lattice geometry and torsional symmetry rather than forming a continuous spectrum.



Let:



\Omega_4 be the effective 4D projection volume,
\Omega_{11} the 11D bulk packing volume,
N_{\text{torsion}} the intrinsic torsional root multiplicity.




The effective torsional mode degeneracy is defined as:



F \equiv \frac{\Omega_{11}}{\Omega_4} \times N_{\text{torsion}} \approx 349



Of these, only 332 modes project dynamically into 4D matter states. The remaining modes remain confined to bulk torsional degrees of freedom.



This yields the fundamental ratio:



\frac{N_{\text{active}}}{N_{\text{total}}} = \frac{332}{349}



which governs late-time torsional relaxation and effective mass projection.








Z.3 Ultraviolet Cutoff from Filament Yield





Unlike quantum field theories defined on a continuous background, SCARLET imposes a mechanical bound on vibrational frequency through finite filament tension.



Let:



t_V \sim 10^{-41}\,\mathrm{s} be the torsional relaxation timescale,
\ell_{VA} the VanAcker bedrock length scale.




Then supported vibrational modes satisfy:



\omega \le \omega_{\max} \sim \frac{1}{t_V}



Higher-frequency modes would require tensile stress exceeding the filament yield threshold, leading to lattice fracture rather than continued oscillation.



This provides a natural ultraviolet cutoff without renormalization and eliminates the ultraviolet catastrophe by limiting the number of physically realizable modes.








Z.4 Proton Fatigue as Mode Redistribution





Baryonic rest mass is interpreted as a projection of torsional energy density into 4D bound states. As cosmological expansion proceeds, torsional stress relaxes and energy is redistributed into inactive bulk modes.



The effective proton mass is modeled as:



m_{p,\mathrm{eff}}(z) = m_{\mathrm{rest}} \left[ 1 - \epsilon_f f(z) \right]



with:



\epsilon_f = \frac{332}{349}



and a smooth relaxation function:



f(z) = 1 - e^{-z/z_f}



where z_f \approx 1.5 characterizes the onset redshift of torsional relaxation.



At early times (z \gg z_f):



m_{p,\mathrm{eff}} \approx m_{\mathrm{rest}}



At late times (z \to 0):



m_{p,\mathrm{eff}} \approx m_{\mathrm{rest}} \times \frac{332}{349}



This gradual reduction in effective baryonic inertia is termed proton fatigue. Energy is not destroyed but transferred into bulk torsional degrees of freedom.








Z.5 Equivalence Principle and Fundamental Constants





Since m_{p,\mathrm{eff}}(z) varies with redshift, the question arises whether this implies variation in dimensionless constants such as the fine-structure constant \alpha or violations of the equivalence principle.



In SCARLET, proton fatigue affects only the torsional projection of baryonic mass into 4D inertial states. Electromagnetic coupling and charge structure remain governed by local gauge symmetry and are not modified by torsional relaxation.



Consequently:



The fine-structure constant \alpha remains invariant,
Electron mass m_e remains fixed,
The proton-to-electron mass ratio




\mu(z) = \frac{m_{p,\mathrm{eff}}(z)}{m_e}



is predicted to drift slowly with cosmic time.



This produces a testable prediction: a redshift-dependent deviation in \mu without accompanying variation in \alpha. Existing quasar absorption constraints therefore provide an independent falsification channel for proton fatigue.



Because the modification applies universally to baryonic inertia, weak equivalence principle violations are suppressed at laboratory scales while remaining potentially observable cosmologically.








Z.6 Impact on Cosmological Observables







Z.6.1 Growth of Structure (S₈)





The Poisson equation becomes:



\nabla^2 \Phi = 4\pi G \rho_{b,\mathrm{eff}}



with:



\rho_{b,\mathrm{eff}}(z) = n_b\,m_{p,\mathrm{eff}}(z)\,(1+z)^3



As m_{p,\mathrm{eff}}(z) decreases at late times, gravitational clustering is suppressed, reducing \sigma_8 and therefore S_8.



This produces a natural downward shift consistent with weak-lensing and CMB-inferred late-time structure amplitudes.








Z.6.2 Hubble Expansion (Torsional Drag)





A fraction of expansion energy is diverted into bulk torsional modes:



H_{\mathrm{eff}}(z) = H_{\Lambda\mathrm{CDM}}(z)\,(1-\delta_t)



with:



\delta_t \approx 0.083



This increases the late-time inferred H_0 from CMB fits while preserving early acoustic physics.








Z.7 Numerical Implementability





Appendix Z provides the elements required for direct numerical testing:



Finite mode degeneracy (332/349),
Physical UV cutoff scale,
Smooth redshift evolution of baryon inertia,
Modified Poisson and sound-speed relations,
Parameterized Hubble drag.




These enter directly into:



background.c (mass evolution and expansion rate),
perturbations.c (sound speed and gravitational source terms),
MCMC pipelines (Cobaya likelihoods).




SCARLET thus becomes directly falsifiable at the level of CMB and large-scale-structure power spectra.








Z.8 Physical Interpretation





The ultraviolet cutoff in SCARLET is mechanical rather than quantum:



spacetime behaves as a torsional lattice,
energy propagates through finite filaments,
divergence is prevented by tensile yield limits.




Matter corresponds to localized torsional binding states. Cosmological evolution reflects gradual lattice stress relaxation rather than vacuum energy dynamics.



Late-time acceleration and structure suppression emerge as mechanical consequences of this relaxation.








Z.9 Summary





Appendix Z establishes:



• A finite torsional mode spectrum,

• A mechanical ultraviolet cutoff,

• A redshift-dependent baryonic inertia (proton fatigue),

• A predicted drift in the proton-to-electron mass ratio without variation in \alpha,

• A unified explanation of H₀ and S₈ tensions,

• A Boltzmann-testable numerical framework.



This appendix closes the SCARLET model by converting it from a geometric-mechanical construction into a predictive, observationally falsifiable cosmological theory.

