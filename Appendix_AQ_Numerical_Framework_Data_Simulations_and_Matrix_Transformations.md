# Appendix AQ: Numerical Framework, Data Simulations, and Matrix Transformations 

### Purpose
This appendix presents the numerical formulations, simulation procedures, statistical validation methods, and matrix transformation operators used to analyze the thermal evolution of the Twin Prime Operator. Its purpose is to define a reproducible computational framework linking arithmetic spacing statistics, information-theoretic measures, and streaming matrix transformations.

All results reported in this appendix are empirical numerical observations derived from finite computational samples and should not be interpreted as formal mathematical proofs.

---

## AQ.1 Fundamental Probability Densities

The framework evaluates four probability distributions over the unfolded spacing coordinate:

$$s \in [0,3]$$

For consistency, all densities are normalized on the finite interval $[0,3]$. If $f(s)$ denotes an unnormalized profile, the corresponding normalized density is:

$$P(s)=\frac{f(s)}{\int_0^3 f(u)\,du}$$

### Poisson Limit
Using the exponential profile $f_{\rm poisson}(s)=e^{-s}$, the normalized density is:

$$P_{\rm poisson}(s)= \frac{e^{-s}}{1-e^{-3}}, \qquad 0\le s\le 3$$

This distribution serves as the reference model for uncorrelated spacing statistics.

### GUE Reference Distribution
Using the standard Wigner–surmise form:

$$f_{\rm gue}(s)= \frac{32}{\pi^2} s^2 \exp\left( -\frac{4}{\pi}s^2 \right)$$

The normalized finite-interval density is:

$$P_{\rm gue}(s)= \frac{f_{\rm gue}(s)}{\int_0^3 f_{\rm gue}(u)\,du}$$

This distribution serves as a benchmark associated with strong level repulsion.

### Random Control Distribution
The control profile is defined as:

$$f_{\rm random}(s)= 2.2 e^{-2.2s}$$

The rate parameter $2.2$ is an empirically selected calibration constant chosen to produce a rapidly decaying reference curve distinct from both the Poisson and Twin Prime baselines over the interval $[0,3]$. The normalized density is:

$$P_{\rm random}(s)= \frac{2.2 e^{-2.2s}}{1-e^{-6.6}}$$

### Twin Prime Operator Baseline
Using the empirical profile:

$$f_{\rm twin}(s)= \frac{8}{\pi} s e^{-s^2}$$

The normalized baseline density is:

$$P_{\rm twin}(s)= \frac{f_{\rm twin}(s)}{\int_0^3 f_{\rm twin}(u)\,du}$$

This distribution exhibits linear level repulsion in the numerical model:

$$P_{\rm twin}(s)\propto s, \qquad s\rightarrow0$$

which is weaker than the quadratic repulsion of the GUE reference profile.

---

## AQ.2 Brody Parameterization and Information Metrics

To quantify numerical similarity between the Twin Prime Operator and standard random-matrix ensembles, the Brody family is employed:

$$P_{\rm Brody}(s)= \frac{ b(\beta+1)s^\beta \exp(-bs^{\beta+1}) }{\int_0^3 b(\beta+1)u^\beta \exp(-bu^{\beta+1})\,du}$$

where:

$$b= \left[ \Gamma \left( \frac{\beta+2}{\beta+1} \right) \right]^{\beta+1}$$

The parameter $b$ retains its conventional Brody definition, while finite-interval normalization is enforced separately through the denominator integral. This finite-interval normalization ensures absolute consistency with the distributions defined in **AQ.1**.

A numerical optimization procedure minimizes the mean-squared error between $P_{\rm Brody}$ and $P_{\rm twin}$. The resulting effective Brody parameter converges in simulation to:

$$\beta \approx 0.92$$

This value is an empirical characterization of the model profile rather than a universal constant. The informational separation from the GUE reference distribution is quantified using the Kullback–Leibler divergence:

$$D_{\rm KL} = \int_0^3 P_{\rm twin}(s) \ln \left( \frac{P_{\rm twin}(s)}{P_{\rm gue}(s)} \right) ds$$

---

## AQ.3 Thermal Decoherence Continuum

To model the progressive degradation of structural order, a one-parameter thermal family is introduced:

$$P(s,T) = \frac{1}{Z(T)} s^{(1-0.5T)} \exp\left[ -\left( 1- \left( 1-\frac{4}{\pi} \right) T \right) s^{1.5} \right]$$

The normalization factor is defined on the common support:

$$Z(T)= \int_0^3 u^{(1-0.5T)} \exp\left[ -\left( 1- \left( 1-\frac{4}{\pi} \right) T \right) u^{1.5} \right] du$$

The parameter $0 \le T \le 1$ acts as an effective decoherence coordinate within the numerical framework.

* **$(T=0)$:** Minimum-decoherence state of the thermal family.
* **$(T=1)$:** Maximally thermalized state within the model family.

The thermal family is a phenomenological deformation inspired by the Twin Prime Operator baseline but does not exactly reproduce $P_{\rm twin}(s)$ at $T=0$. The parameter $T$ is a numerical control variable and should not be interpreted as a physical thermodynamic temperature without an underlying microscopic derivation.

---

## AQ.4 Entropy Evolution and Critical Response Boundary

The Shannon entropy associated with the thermalized distribution is:

$$H(T) = -\int_0^3 P(s,T)\ln P(s,T)\,ds$$

Numerical simulations performed over the sampled interval indicate monotonic entropy growth across $0\le T\le 1$. The entropy-response function is defined by:

$$C_v(T) = T \frac{dH}{dT}$$

The maximum of this response curve defines an effective critical operating boundary:

$$T_c = \operatorname*{arg\,max} \left[ C_v(T) \right]$$

For the numerical implementation used in SCARLET 2.0, simulations yield:

$$T_c \approx 0.446$$

This value identifies the point of maximum entropy-growth sensitivity within the model and does not constitute evidence of a thermodynamic phase transition.

---

## AQ.5 Streaming Matrix Transformation

To stabilize real-time processing near $s\rightarrow0$, the transformation operator incorporates Tikhonov regularization:

$$\varepsilon=0.01$$

The diagonal filter matrix elements are calculated via:

$$M_{ii} = (s_i+\varepsilon)^{0.5T_{\rm env}} \exp\left[ \left( 1-\frac{4}{\pi} \right) T_{\rm env} s_i^{1.5} \right]$$

The filter is designed as an approximate inverse thermal-decoherence operator. Consequently, the exponential weighting appears with the opposite sign relative to the forward thermal deformation defined in **AQ.3**. This allows partial recovery of low-entropy structure from corrupted telemetry streams.

Recovered telemetry is obtained through:

$$\vec P_{\rm recovered} = \mathbf M_{\rm filter} \vec P_{\rm corrupted}$$

Because the operator is diagonal, computational complexity scales linearly:

$$\mathcal O(N)$$

---

## AQ.6 Arithmetic Validation Through Twin Prime Unfolding

To connect the continuous model distribution with arithmetic data, spacing statistics are extracted from consecutive twin-prime coordinates. We define:

$$G_i = p_{i+1}-p_i$$

where $p_i$ denotes the lower member of each twin-prime pair. Because prime densities vary logarithmically with scale, the raw spacings are unfolded using local normalization:

$$s_i = \frac{G_i}{\langle G\rangle_{\rm local}}$$

The Hardy–Littlewood twin-prime constant $C_2 \approx 0.66016$ provides theoretical context for twin-prime density but is not required by the unfolding algorithm implemented in the present code.

The resulting unfolded spacing histogram is compared with:

$$P_{\rm twin}(s) = \frac{f_{\rm twin}(s)}{\int_0^3 f_{\rm twin}(u)\,du}$$

Agreement is quantified using mean-squared error metrics, Kullback–Leibler divergence, and Brody-parameter estimation.

The numerical experiments exhibit agreement with the proposed baseline model over the tested computational range. These findings provide empirical support for the model but do not constitute a formal asymptotic proof.

Accordingly, all convergence statements in this appendix should be interpreted as numerical validation rather than theorem-level derivation.

---

## AQ.7 Summary

The framework establishes:
1. A normalized **Twin Prime Operator baseline distribution** on $s\in[0,3]$.
2. An empirical **Brody-parameter characterization** ($\beta \approx 0.92$), where $b$ retains its standard form while finite normalization is managed via the denominator integral.
3. A **thermal decoherence continuum** exhibiting monotonic entropy growth in numerical simulations.
4. An empirically identified **entropy-response boundary** near $T_c \approx 0.446$.
5. A stable $\mathcal O(N)$ **streaming filter implementation** operating as an inverse deformation kernel.
6. A reproducible **arithmetic validation pipeline** based on localized twin-prime spacing data.

This appendix therefore provides a computationally testable statistical framework linking arithmetic spacing structures, information theory, and streaming telemetry analysis. All conclusions are derived from numerical experiments and empirical comparisons and are independent of any claim of formal theorem status.
