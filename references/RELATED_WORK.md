# Related work and scope

The result developed in this repository concerns the optimal transfer of a **noise eigenstate** under fixed Markovian dephasing and bounded coherent control. Its mathematical ingredients connect established two-level control bounds, the geometry of dephasing generators, and purity production. The specific contribution is an exact reduction of the leading transfer error to a shortest-path distance, with a saturating construction and a converse that remains valid at finite noise and arbitrary duration.

Bibliographic keys below match [references.bib](references.bib). Publication status and source coverage were checked on 24 October 2026.

## The statement being compared

The [model](../science/model.md) uses mutually commuting Hermitian jumps,

```math
\dot\rho_\epsilon=-i[H(t),\rho_\epsilon]
+\epsilon\sum_a\gamma_a\mathcal D[L_a](\rho_\epsilon),
\qquad
\mathcal D[L](\rho)=L\rho L-\tfrac12\{L^2,\rho\},
```

with common eigenvalues $`\lambda_{ai}`$ and a global Hamiltonian spectral halfwidth at most $`\Omega`$. Set

```math
Q_{ij}=\sum_a\gamma_a(\lambda_{ai}-\lambda_{aj})^2,
\qquad
d_Q(s,t)=\min_{s=i_0,\ldots,i_m=t}\sum_{k=1}^m Q_{i_{k-1}i_k}.
```

The physical coherence-decay rate without control is $`\epsilon Q_{ij}/2`$. For basis-state transfer, with every outcome outside the target counted as failure, the results are

```math
q_\epsilon(H,T)\ge
\frac{\pi\epsilon d_Q(s,t)}
{16\Omega+8\pi\epsilon d_Q(s,t)}
```

for every admissible finite-duration protocol, and

```math
\inf_{H,T}q_\epsilon(H,T)
=\frac{\pi d_Q(s,t)}{16\Omega}\epsilon+O(\epsilon^2)
```

when selective pair rotations on a minimizing path are available. The finite-noise expression is a lower bound, not a claimed exact finite-noise optimum. The lower bound is uniform over protocols whose duration or controls depend on the noise strength.

The graph is built from **noise signatures**, rather than physical adjacency or allowed hopping terms. The optimization still allows arbitrary many-level superpositions and interference. The [proof](../science/geometry.md) establishes that a sequence of pair rotations attains the global leading optimum; it does not assume such a sequence at the outset.

## Established ingredients and the present extension

| Ingredient | Primary antecedent | Role here |
|---|---|---|
| Sharp amplitude-constrained two-level dephasing sensitivity | [Lu2013](https://doi.org/10.1103/PhysRevA.88.033406) | Supplies the scalar crossing kernel. |
| Dephasing rates as squared differences of noise eigenvalue vectors | [Fagnola2019](https://doi.org/10.1088/1751-8121/ab38ec) | Supplies the geometry whose metric closure is optimized. |
| Purity-loss rates, variances, and control-speed estimates | [Kallush2014](https://doi.org/10.1088/1367-2630/16/1/015008) | Precedent for the lower-bound method. |
| Noise-aware paths can outperform the fastest implementation | [SchulteHerbrueggen2011](https://doi.org/10.1088/0953-4075/44/15/154013) | Established design principle; the contribution here is an exact certificate in a restricted model. |
| Topology-dependent transfer through lossy intermediate states | [Yuan2012](https://doi.org/10.1103/PhysRevA.85.033417) | Analytic control precedent with a different dissipation model. |
| Repetition encoding can reshape or filter gate noise | [Ma2025](https://doi.org/10.1103/16gx-m7kg), [Benito2026](https://arxiv.org/abs/2606.17709) | Explains why disposable syndrome registers change the operational question. |

### Two-level optimality: Lu et al.

Xiao-Jing Lu and collaborators derive the integrated dephasing sensitivity for a driven two-level system and show that a flat $`\pi`$ pulse minimizes it under a maximum Rabi-frequency constraint. Section IV, Eqs. (22)–(26), of their [primary manuscript](https://arxiv.org/pdf/1305.6127) contains the relevant result. With their Rabi frequency equal to $`2\Omega`$ in the present convention, the scalar variance integral is $`\pi/(4\Omega)`$.

This two-level optimum and its saturating pulse are prior results. The extension here is the reduction of every admissible multilevel path to weighted binary crossings, yielding the metric closure of the full noise-distance matrix. The finite-noise converse additionally controls optimization over arbitrarily long, noise-dependent protocols. Merely applying the known scalar formula to a chosen chain would establish an upper bound, not the all-control optimum.

### Noise geometry: Fagnola et al. and Schirmer–Solomon

Franco Fagnola, John E. Gough, Hendra I. Nurdin and Lorenza Viola explicitly represent dephasing by vectors of diagonal jump eigenvalues. In their [accepted manuscript](https://arxiv.org/pdf/1811.11784), Lemma 14, Eq. (20), gives the coherence generator; Section 3.2.1, Eq. (27) and its following discussion, interprets damping through squared lengths of differences between the vectors. The published article is *Journal of Physics A: Mathematical and Theoretical* **52**, 385301 (2019).

Thus the Euclidean representation of the noise is established. The shortest-path closure of those squared distances, and its exact operational meaning for bounded coherent transfer, are the additional statements here. To fix normalization, this repository uses its explicit dissipator and the directly derived coherence rate $`Q_{ij}/2`$.

Earlier work by S. G. Schirmer and A. I. Solomon derives complete-positivity constraints on relaxation and dephasing rates in multilevel systems ([SchirmerSolomon2004](https://arxiv.org/pdf/quant-ph/0312231)). It is relevant to which rate matrices are physically admissible. That structural problem does not optimize coherent transfer. The current model specifies Hermitian commuting jumps from the start, so complete positivity is automatic.

### Purity production: Kallush, Khasin and Kosloff

In [Kallush2014](https://arxiv.org/pdf/1308.6128), Sections 2.1–2.2 combine purity-loss rates, state variances, and transformation-time estimates. Their setting emphasizes noise in control fields and scaling with the dimension of a representation of the control algebra. The estimates explicitly invoke weak noise or small purity loss.

The present [finite-noise proof](../science/finite_noise.md) also uses purity production and a speed bound. Its additional step is an endpoint-controlled lower bound on coherence across every cut, applied to the actual mixed trajectory. This gives a duration-uniform converse and consequently justifies optimization before taking the weak-noise limit. Purity loss as a control limitation is not itself a new observation.

## Multilevel optimal control and global bounds

### Jirari–Pötz: dissipative state steering

H. Jirari and W. Pötz formulate Markovian coherent control using Pontryagin's principle and a Lindblad equation in [Jirari2005](https://doi.org/10.1103/PhysRevA.72.013409), *Physical Review A* **72**, 013409 (2005). The publisher abstract describes numerical state steering in two-, three-, and four-level systems using conjugate-gradient optimization, with field-independent population and polarization decay.

This is directly relevant antecedent work on noise-aware multilevel transfer. The abstract does not state a shortest-path formula, a saturating all-control bound, or a duration-uniform endpoint inequality. **The full paper was not accessible in this review**, and no accessible author manuscript was located. Consequently, this comparison identifies the documented model and method but does not exclude overlap with particular results inside the paper.

### Liu–Yang–Li: perturbative objectives for Markovian noise

Ran Liu, Xiaodong Yang and Jun Li develop a robust-control method that optimizes noise-induced perturbation terms order by order ([Liu2024](https://doi.org/10.1103/PhysRevA.110.012402), *Physical Review A* **110**, 012402 (2024)). Their publisher abstract lists state-transfer examples in two-level and three-level $`\Lambda`$ systems, and gate examples in two-level and three-level ladder systems. It reports substantial improvement for state transfer and more limited improvement for gate fidelity.

The present theorem gives an analytic global optimum for a specific fixed-dephasing, eigenstate-transfer problem. That distinction should be tested against their detailed objectives and control constraints before using their numerical examples as direct benchmarks. **Only the publisher abstract and author-institution publication records were accessible.** Those sources do not provide enough information for a complete theorem-level exclusion of overlap.

### Lutz–Privat: existence and general time/error estimates

Killian Lutz and Yannick Privat's [LutzPrivat2025](https://hal.science/hal-05176524), *Time Optimal Synthesis of Gates for Markovian Open Qudits*, is listed by both [Lutz](https://killianlutz.github.io/research) and [Privat](https://yannick-privat.perso.math.cnrs.fr/publi.html) as forthcoming in *Journal de Mathématiques Pures et Appliquées*.

The authors' institution describes the results in the [2025 SPHINX activity report](https://radar.inria.fr/rapportsactivite/RA2025/sphinx/SPHINX-RA-2025.pdf), Section 7.3, printed p. 15: existence of a time-minimal error-minimizing gate protocol, and general upper/lower estimates for time and mean-square gate error under constrained multichromatic controls. The report explicitly describes these estimates as nonsharp and dependent on dimension, control constraints and decoherence parameters.

This documented scope differs from the exact leading eigenstate-transfer cost considered here. However, **the HAL manuscript was inaccessible**, so the comparison rests on the authors' publication records and institutional result summary. The detailed hypotheses and possible special-case coincidences remain unverified.

### Global certificates and relaxation-aware numerical controls

[Zhang2021](https://arxiv.org/html/2105.06054v2), by Hanwen Zhang, Zeyu Kuang, Shruti Puri and Owen D. Miller, develops global control bounds through conservation laws, quadratically constrained optimization and semidefinite relaxations. Its applications include three-level driving, decoherence suppression and gate implementation; Supplement VI explains a Lindblad extension. This is a general framework for certifying optimality. The present restricted model instead admits an explicit graph-distance certificate and analytic saturating protocol.

[SchulteHerbrueggen2011](https://arxiv.org/pdf/quant-ph/0609037), by T. Schulte-Herbrüggen, A. Spörl, N. Khaneja and S. J. Glaser, develops openGRAPE and demonstrates the benefit of remaining in weakly relaxing subspaces, even when this differs from time-optimal control. Its numerical optimization is not claimed to guarantee the global optimum. The broad idea of taking a slower path to reduce loss is therefore prior. The graph theorem specifies exactly when a detour helps under fixed diagonal dephasing and certifies its best possible leading cost.

## Adiabatic passage and protected endpoint sectors

[Yuan2012](https://arxiv.org/pdf/1004.4050), by Haidong Yuan, Christiane P. Koch, Peter Salamon and David J. Tannor, gives analytic optimal-control results for transfer through decaying intermediate states. It recovers STIRAP as a global infinite-time optimum for one lossy intermediate and establishes an obstruction for paths containing two consecutive lossy intermediates at finite power. This is an important topology-dependent transfer theorem. Its amplitude-loss model and constraints differ from the unital dephasing generator and squared-noise-distance cost here.

In [Huang2022](https://doi.org/10.1140/epjqt/s40507-022-00152-z), Wei Huang, Wentao Zhang, Xinwei Du and Chu Guo study transfer through a locally dephased intermediate spin. Their three-state jump has labels $`(-1,+1,-1)`$: the endpoints have identical noise signatures. In the present graph they therefore have distance zero. Suppression of loss by longer adiabatic passage is consistent with the theorem. The comparison also illustrates a control distinction: an unrestricted direct rotation within the protected endpoint sector need not be available in a particular chain Hamiltonian.

The earlier study [Ivanov2004](https://doi.org/10.1103/PhysRevA.70.063409), by P. A. Ivanov, N. V. Vitanov and K. Bergmann, analyzes dephasing effects on STIRAP. Its publisher abstract was inspected; the full text was not available here. It is cited as a primary antecedent for adiabatic dephasing sensitivity, without attributing an unrestricted-control theorem to it.

## Bias preservation, encoding and reusable workspace

### Continuous implementations and ideal endpoint gates

Appendix A of [GuillaudMirrahimi2019](https://arxiv.org/pdf/1904.09474) establishes an exact obstruction to continuously implementing a bias-preserving CNOT with strictly two-level qubits. The present finite-error bounds quantify required population-error production under a specified noise model and control resource. They do not replace the earlier qualitative obstruction.

[EtxezarretaMartinez2026](https://doi.org/10.1103/q7w6-nljp) studies residual CNOT noise bias and bias-preserving controlled-phase gates at circuit level. Section II.1 and Appendix B of the [primary preprint](https://arxiv.org/html/2505.17718v1) analyze a specified CNOT Hamiltonian and phase-noise model. This supplies a relevant concrete comparison; it is not an optimization over every bounded Hamiltonian trajectory.

[Roy2025](https://arxiv.org/abs/2510.07532), by Debadrito Roy, Aryaman Manish Kolhe, V. Lalitha and Navin Kashyap, characterizes ideal bias-preserving gates and their synthesis. Whether an endpoint unitary preserves an error algebra is distinct from whether noise occurring throughout a finite-time implementation remains in that algebra. A circuit-level endpoint characterization alone cannot settle the latter question.

Stabilized cat-qubit gates in [Puri2020](https://doi.org/10.1126/sciadv.aay5901) provide an established physical way to preserve a strong noise bias using oscillator encoding and stabilization. The theorem here assumes fixed finite-dimensional commuting Hermitian jumps and a charged Hamiltonian resource. It should not be extrapolated to a changing encoded manifold or to stabilizing dissipation without checking those hypotheses.

### Repetition filtering and syndrome storage

[Ma2025](https://doi.org/10.1103/16gx-m7kg) analytically and numerically studies repetition-code circuits that reshape native trapped-ion entangling-gate noise, including a hardware demonstration. [Benito2026](https://arxiv.org/html/2606.17709v1), Section IV and Fig. 5, introduces a repetition-encoded CNOT bias filter using measurement and feedforward. The repetition encode–transversal gate–decode–majority mechanism is credited to that prior work; making its correction coherent does not make the coding principle new.

The [workspace analysis](../science/workspace.md) concerns the complete retained system. Auxiliary states that only repeat existing noise signatures cannot shorten the graph distance, but a protocol can improve the data's marginal accuracy by leaving a syndrome in the workspace. The resulting bound is a tradeoff between data error and pure-work return. It is not a data-only lower bound when syndrome entropy may be discarded.

[CzartowskiBinder2026](https://arxiv.org/html/2609.03825v2), Sections III–IV and Appendix A, relates syndrome entropy to the work needed to maintain a reusable error-correction memory. That establishes the thermodynamic accounting for a supplied code and noise model. The additional control question here is how much joint error or residual workspace impurity is forced by a required noise-signature change under a bounded Hamiltonian. No universal erasure-work formula follows from the transfer theorem without specifying the memory and thermodynamic protocol.

## Fixed versus control-dependent noise

Lixiang Ding, Jingtao Fan and Xingze Qiu derive robust controls that explicitly account for drive-induced changes of system–environment coupling ([Ding2026](https://doi.org/10.1038/s41534-025-01166-y); [primary manuscript](https://arxiv.org/pdf/2508.07379)). Such a model can change the effective jump operators and rates as the control is changed.

The graph theorem holds the physical jumps and rates fixed. Noise-dependent control amplitudes are allowed within the budget; control-dependent changes of the noise generator are a different physical assumption. Successful noise suppression in that broader setting does not contradict a bound for the fixed generator.

## Source coverage and limits of the comparison

The detailed mathematical comparisons use inspected primary text from Lu et al. (Section IV), Fagnola et al. (Lemma 14 and Sections 3–4), Kallush et al. (Sections 2.1–2.2), Zhang et al. (main applications and Lindblad supplement), Schulte-Herbrüggen et al. (control formulation and numerical setting), Yuan et al. (model and analytic scope), Huang et al. (model and transfer analysis), Guillaud–Mirrahimi (Appendix A), Etxezarreta Martinez et al. (CNOT model and Appendix B), Benito et al. (Section IV), and Czartowski–Binder (syndrome accounting).

The following distinctions remain explicit:

| Work | Material available for this comparison | Limitation |
|---|---|---|
| Jirari–Pötz 2005 | Publisher abstract and bibliographic record | Full-text theorem comparison incomplete. |
| Liu–Yang–Li 2024 | Publisher abstract and author-institution records | Detailed objectives, controls and special cases not verified. |
| Lutz–Privat 2025 | Author publication pages and institutional research reports | Manuscript hypotheses and individual bounds not inspected. |
| Ivanov–Vitanov–Bergmann 2004 | Publisher abstract | Cited for documented STIRAP scope only. |
| Ma et al. 2025 | Publisher abstract and bibliographic record | No detailed comparison of its circuit error formulas is asserted. |

This account supports a narrowly stated contribution: the exact metric-closure law for eigenstate transfer, its saturating path, and its duration-uniform finite-noise and retained-workspace consequences. It is not an exhaustive priority determination. In particular, the scalar optimum, squared-distance representation, relaxation-aware routing principle, and repetition-code filtering mechanism are explicitly treated as established results.
