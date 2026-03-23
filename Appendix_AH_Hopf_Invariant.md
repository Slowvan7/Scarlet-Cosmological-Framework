
Appendix AH — Topological Structure of Torsional Fields via the Hopf Invariant










AH.1 Overview





This appendix defines a topological invariant associated with smooth field configurations on spatial slices of physical space \mathbb{R}^3, compactified via:



\mathbb{R}^3 \cup \{\infty\} \cong S^3 \tag{AH.1}



The construction classifies maps:



S^3 \to S^2 \tag{AH.2}



through the Hopf invariant Q_{\text{top}}, an integer-valued quantity that characterizes the global linking structure of the field configuration.



All fields are assumed:



Smooth (C^\infty)
Globally defined
Approaching a constant at spatial infinity









AH.2 Fundamental Field and Gauge Structure





We introduce a complex two-component field:



\psi(x) \in \mathbb{C}^2



subject to the normalization:



\psi^\dagger(x)\psi(x) = 1 \tag{AH.3}



Thus:



\psi(x) \in S^3 \tag{AH.4}



The field admits a local U(1) gauge redundancy:



\psi(x) \sim e^{i\chi(x)} \psi(x) \tag{AH.5}



Physical configurations correspond to the quotient:



S^3 / U(1) \cong S^2 \tag{AH.6}








AH.3 Induced Map to S^2





Define the unit vector field:



\tilde{n}^a(x) = \psi^\dagger(x)\,\sigma^a\,\psi(x), \quad a=1,2,3 \tag{AH.7}



The Pauli matrices satisfy:



[\sigma^a, \sigma^b] = 2i\,\epsilon^{abc}\sigma^c \tag{AH.8}



This ensures:



|\tilde{n}(x)| = 1, \quad \tilde{n}(x) \in S^2 \tag{AH.9}



Thus defining the mapping:



\tilde{n} : S^3 \to S^2 \tag{AH.10}








AH.4 U(1) Connection and Curvature





Define the connection:



A = -i\,\psi^\dagger d\psi \tag{AH.11}



Under a gauge transformation:



\psi \to e^{i\chi(x)}\psi



we have:



A \to A + d\chi \tag{AH.12}



The curvature 2-form is:



F = dA \tag{AH.13}



or in components:



F_{ij} = \partial_i A_j - \partial_j A_i \tag{AH.14}



The curvature is proportional to the pullback of the area 2-form on S^2. Explicitly:



F = \frac{1}{2} \epsilon^{abc} \tilde{n}^a\, d\tilde{n}^b \wedge d\tilde{n}^c \tag{AH.15}








AH.5 Hopf Invariant and Integral Representation





The Hopf invariant is defined as:



Q_{\text{top}} = \frac{1}{4\pi^2} \int_{S^3} A \wedge dA \tag{AH.16}



Using the identity:



A \wedge dA = \frac{1}{2} \epsilon^{ijk} A_i F_{jk} \, d^3x



this can be written over \mathbb{R}^3 as:



Q_{\text{top}} = \frac{1}{8\pi^2} \int_{\mathbb{R}^3} d^3x \, \epsilon^{ijk} A_i F_{jk} \tag{AH.17}



For smooth configurations satisfying the boundary conditions (AH.23–AH.24), which compactify \mathbb{R}^3 to S^3, this normalization ensures:



Q_{\text{top}} \in \mathbb{Z}, \quad Q_{\text{top}} = 1 \text{ for the standard Hopf map} \tag{AH.18}








AH.6 Gauge Invariance





Under a gauge transformation:



A \to A + d\chi



we obtain:



(A + d\chi)\wedge d(A + d\chi) = A \wedge dA + d\chi \wedge dA



Using:



d\chi \wedge dA = d(\chi\, dA)



we find:



A \wedge dA \to A \wedge dA + d(\chi\, dA) \tag{AH.19}



Since S^3 has no boundary:



\int_{S^3} d(\chi\, dA) = 0 \tag{AH.20}



Thus:



Q_{\text{top}} \text{ is gauge invariant} \tag{AH.21}








AH.7 Topological Interpretation





The invariant satisfies:



Q_{\text{top}} \in \mathbb{Z}



and classifies homotopy classes of maps:



S^3 \to S^2 \tag{AH.22}



For a regular value of \tilde{n}, the preimage consists of closed loops in S^3. The Hopf invariant equals the linking number of these loops.








AH.8 Boundary Conditions





Require:



\psi(x) \to \psi_0 \quad \text{as } |x| \to \infty \tag{AH.23}



equivalently:



\tilde{n}(x) \to \tilde{n}_0 \in S^2 \tag{AH.24}



ensuring:



Compactification to S^3
Well-defined topological charge
Vanishing boundary contributions









AH.9 Hopf Fibration Structure





This construction realizes the Hopf fibration:



S^1 \hookrightarrow S^3 \to S^2 \tag{AH.25}



where:



\psi defines the total space
The U(1) phase defines the fiber
\tilde{n} defines the base space




The connection A encodes the bundle twisting.








AH.10 Relation to Torsional Structure





Two distinct notions are identified:








(A) Local twist density of the field





\nabla \times \tilde{n}



This describes the local twisting of the field configuration and is coordinate-dependent.








(B) Geometric torsion





T^a = de^a + \omega^a_{\ b} \wedge e^b \tag{AH.26}



This is an intrinsic property of spacetime geometry.



\boxed{ \text{These two notions are conceptually distinct and should not be identified.} }








AH.11 Summary





We have defined:



Field normalization: (AH.3)
Mapping: (AH.10)
Connection: (AH.11)
Curvature: (AH.13)
Topological invariant:




\boxed{ Q_{\text{top}} = \frac{1}{4\pi^2} \int_{S^3} A \wedge dA = \frac{1}{8\pi^2} \int_{\mathbb{R}^3} d^3x \, \epsilon^{ijk} A_i F_{jk} \in \mathbb{Z} } \tag{AH.27}



This provides a complete, gauge-invariant classification of field configurations into discrete topological sectors based on global linking structure.

