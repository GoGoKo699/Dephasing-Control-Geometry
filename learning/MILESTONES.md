# Thirty milestones for dephasing control geometry

This map connects the physical objects, proof mechanisms, constructions, and limits of the project. The [learning introduction](README.md) gives a concrete entry through a three-level example; the [scientific model](../science/model.md) is the authoritative statement of assumptions and results.

## Allocation and selected anchor

The map has **14 milestones in background/preliminaries** and **16 in narrative/innovation**. The first phase is substantial because the argument joins several kinds of reasoning: density matrices and reduced states, Markovian dephasing, bounded coherent motion, purity production, weak-noise expansions, quantum trajectories, graph distances, and channel error metrics. These ingredients must be connected before an optimization over arbitrary controls has a precise meaning. The second phase follows the cut certificate into the sharp control law, then develops the logical-gate, spectral, and workspace consequences. Its final milestones combine those consequences with physical resources and the evidence supporting them.

Within each phase the order is local to global. Background/preliminaries starts with individual states and measured probabilities and ends with the complete optimization problem. Narrative/innovation starts with a local comparison of noise costs, builds the all-control theorem, and ends with an integrated design principle and its domain. The map covers the contribution's conceptual structure; the linked science pages retain the full derivations and technical details.

The single educational anchor is **Heinz-Peter Breuer and Francesco Petruccione, *The Theory of Open Quantum Systems*, Oxford University Press, 2007 paperback, ISBN 9780199213900**. The [official Oxford listing and contents](https://academic.oup.com/book/27757) verify the edition and the chapter pointers used here:

| Pointer | Verified chapter title |
|---|---|
| BP2 | Chapter 2, Quantum Probability |
| BP3 | Chapter 3, Quantum Master Equations |
| BP4 | Chapter 4, Decoherence |
| BP6 | Chapter 6, Stochastic Dynamics in Hilbert Space |
| BP7 | Chapter 7, The Stochastic Simulation Method |

Every anchor pointer below links to the corresponding official chapter page, with its chapter identity checked against that contents listing. The [Breuer–Petruccione bridge](BREUER_PETRUCCIONE_BRIDGE.md) translates the source's framework into the project's notation and assumptions. Chapter pointers identify prerequisite context, rather than asserting that the book contains the metric-closure theorem, its control constraints, or every channel and coding calculation used here. Those steps are supplied in the canonical project sources. Primary research citations remain in [Related work](../references/RELATED_WORK.md).

## Route through the map

| Phase and milestones | Connection established |
|---|---|
| [Background/preliminaries: M01–M06](#m01-states-populations-and-coherence) | States, the measured task, open dynamics and physical noise signatures |
| [Background/preliminaries: M07–M13](#m07-the-control-budget-is-a-physical-assumption) | Control resources, variance, purity, trajectories, distances and channel quality |
| [Background/preliminaries: M14](#m14-the-complete-optimization-problem-and-its-quantifiers) | The complete problem and its optimization quantifiers |
| [Narrative/innovation: M15–M20](#m15-a-distance-potential-separates-the-endpoints) | The cut certificate, attainable coefficient and duration-uniform theorem |
| [Narrative/innovation: M21–M25](#m21-exact-path-probabilities-and-coherent-logical-gates) | Gates, spectral refinement, coherent error and implementation resources |
| [Narrative/innovation: M26–M28](#m26-pure-workspace-return-is-a-separate-operational-requirement) | Pure-work return, coherent correction and retained entropy |
| [Narrative/innovation: M29–M30](#m29-what-establishes-each-part-of-the-scientific-account) | Evidence, attribution and the complete design principle |

## Phase 1: background/preliminaries

### M01: States, populations, and coherence

- **Phase:** background/preliminaries.
- **Central question:** What information about a quantum state is contained in its populations and its coherences?
- **Understanding target:** Interpret a density matrix in a specified basis, distinguish a pure superposition from a probabilistic mixture, and connect its diagonal entries to measurement probabilities. Explain why a basis choice matters when identifying which parts of a state the environment changes.
- **Dependencies and story role:** Entry point. Establishes the state description used by every later dynamical and operational statement.
- **Conceptual connection:** The common noise eigenbasis makes the distinction between stationary populations and decaying coherences physically meaningful.
- **Project sources:** [Dynamics and conventions](../science/model.md#dynamics-and-conventions); [physical interpretation](../science/interpretation.md).
- **Anchor pointer:** [BP2 — Quantum Probability](https://academic.oup.com/book/27757/chapter/197977987).

### M02: The event that counts as a transfer failure

- **Phase:** background/preliminaries.
- **Central question:** What does the population-transfer error measure, and which failures does it include?
- **Understanding target:** Read $q=1-\langle t|\rho(T)|t\rangle$ as the probability of any outcome other than the desired basis state. Distinguish an incorrect logical bit, leakage to a helper level, and loss of coherence that a single basis-population measurement cannot detect.
- **Dependencies and story role:** Uses M01. Gives the optimization a measurable objective before introducing control or noise.
- **Conceptual connection:** Counting leakage prevents a successful-looking logical subspace projection from replacing the unconditional transfer task.
- **Project sources:** [Transfer task](../science/model.md#dynamics-and-conventions); [logical channel and leakage weights](../science/constructions.md#6-logical-phase-transverse-and-leakage-weights).
- **Anchor pointer:** [BP2 — Quantum Probability](https://academic.oup.com/book/27757/chapter/197977987).

### M03: A subsystem can look correct while the whole system changes

- **Phase:** background/preliminaries.
- **Central question:** How can data remain reliable while an auxiliary register becomes mixed?
- **Understanding target:** Explain a tensor-product register, reduced density matrix, and partial trace. Distinguish purity of the full retained state from purity of either subsystem, and recognize correlations and entropy in workspace as properties that data measurements alone do not determine.
- **Dependencies and story role:** Uses M01–M02. Establishes the system boundary needed to interpret later workspace results.
- **Conceptual connection:** A theorem about returning a complete pure state and a theorem about data after tracing out work address different physical tasks.
- **Project sources:** [Retained and disposable workspace](../science/model.md#retained-and-disposable-workspace); [workspace model](../science/workspace.md#1-model-with-local-mixing-budgets).
- **Anchor pointer:** [BP2 — Quantum Probability](https://academic.oup.com/book/27757/chapter/197977987).

### M04: Coherent control inside a Markovian master equation

- **Phase:** background/preliminaries.
- **Central question:** Which parts of the evolution describe deliberate motion and which describe environmental noise?
- **Understanding target:** Identify the Hamiltonian commutator and Lindblad dissipator in the master equation, and explain why trace preservation and complete positivity matter for physical state evolution. State what is held fixed when a laboratory-frame noise model is combined with a time-dependent control.
- **Dependencies and story role:** Uses M01 and M03. Turns the state description into a controlled open-system model.
- **Conceptual connection:** The optimization changes H and the duration; it does not silently change the specified jump operators, noise rates, or retained system.
- **Project sources:** [Dynamics and conventions](../science/model.md#dynamics-and-conventions); [finite-noise setup](../science/finite_noise.md#1-model-and-theorem).
- **Anchor pointer:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616).

### M05: Dephasing can spare a state but harm its motion

- **Phase:** background/preliminaries.
- **Central question:** Why does diagonal dephasing leave a basis state unchanged yet create population error during a gate?
- **Understanding target:** Explain the decay of an off-diagonal matrix element under commuting Hermitian jumps and the invariance of populations under noise alone. Track the convention that $\kappa\mathcal D[Z]$ gives coherence decay rate $2\kappa$, and relate transient superposition to exposure during transfer.
- **Dependencies and story role:** Uses M04. Identifies the physical mechanism whose minimum cost the project studies.
- **Conceptual connection:** Stationary initial and final states do not imply a noise-free connecting control path.
- **Project sources:** [Dephasing graph and rate convention](../science/model.md#the-dephasing-graph); [physical mechanism](../science/interpretation.md).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190).

### M06: Noise signatures and observable pair costs

- **Phase:** background/preliminaries.
- **Central question:** What physical information is encoded by the eigenvalues of the noise operators?
- **Understanding target:** Associate each common eigenstate with its weighted noise signature and explain $Q_{ij}=\sum_a\gamma_a(\lambda_{ai}-\lambda_{aj})^2$ as twice a reference coherence-decay rate. Recognize when two states share a noise signature and why real scalar shifts and orthogonal mixing of the weighted Hermitian jumps do not change Q.
- **Dependencies and story role:** Uses M05. Converts the microscopic noise model into a finite set of physically interpretable pair costs.
- **Conceptual connection:** The graph used later is built from environmental distinguishability, rather than from spatial adjacency or available hopping terms.
- **Project sources:** [The dephasing graph](../science/model.md#the-dephasing-graph); [inference from measured rates](../science/interpretation.md#what-can-be-inferred-from-measured-dephasing-rates).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190).

### M07: The control budget is a physical assumption

- **Phase:** background/preliminaries.
- **Central question:** What does a bound on Hamiltonian spectral half-width constrain?
- **Understanding target:** Distinguish spectral half-width from the displayed operator norm, a laboratory power limit, and separate bounds on terms in a sum. Explain why a scalar energy shift is irrelevant and why a global half-width bound limits the matrix blocks that mix two subspaces.
- **Dependencies and story role:** Uses M01 and M04. Supplies the resource convention against which protocols can be compared fairly.
- **Conceptual connection:** A small noise error obtained by increasing the aggregate mixing strength is a change of resources, not a violation of a fixed-budget converse.
- **Project sources:** [Control budget](../science/control_resources.md#1-what-is-bounded); [mixed-state block estimates](../science/finite_noise.md#3-two-block-estimates-for-a-mixed-state).
- **Anchor pointer:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616), with the norm and mixing-block analysis supplied in the project.

### M08: A selective two-level rotation as an elementary operation

- **Phase:** background/preliminaries.
- **Central question:** How does a bounded pulse move population between two specified levels?
- **Understanding target:** Connect the sinusoidal populations of a two-level rotation to its mixing strength and duration. Distinguish a population swap with known phases from an exact phase-free transposition, and identify the selective pair shift needed by the phase-free implementation.
- **Dependencies and story role:** Uses M05 and M07. Establishes the elementary operation later assembled into multilevel transfers and logical gates.
- **Conceptual connection:** The simplest allowed trajectory makes the relation among coherence exposure, control speed, and gate phase explicit.
- **Project sources:** [Elementary transposition](../science/constructions.md#1-a-phase-free-elementary-transposition); [pulse conventions](../science/control_resources.md#pulse-conventions).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190).

### M09: Purity production as a record of irreversible mixing

- **Phase:** background/preliminaries.
- **Central question:** Why can global purity constrain a noisy control path?
- **Understanding target:** Interpret $\operatorname{Tr}\rho^2$, explain why Hamiltonian evolution preserves it, and understand its monotonic decrease under the specified unital noise. Connect the commutator $[L_a,\rho]$ to the exact purity-loss rate and explain why high final purity constrains every earlier state.
- **Dependencies and story role:** Uses M03–M05. Introduces the noisy-state quantity that makes a duration-uniform proof possible.
- **Conceptual connection:** The finite-noise argument measures irreversible mixing directly instead of assuming the noisy state stays close to its ideal trajectory.
- **Project sources:** [Coherence and joint purity](../science/finite_noise.md#32-coherence-forced-by-high-joint-purity); [permitted additional noise](../science/finite_noise.md#7-weaker-sufficient-control-assumptions-and-additional-noise).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190).

### M10: Weak-noise error along one fixed protocol

- **Phase:** background/preliminaries.
- **Central question:** Why is the first-order error of an exact noiseless transfer an integrated noise variance?
- **Understanding target:** Explain the interaction picture as a way to remove the intended unitary motion, and connect the first-order target-overlap loss to $\int\sum_a\gamma_a\operatorname{Var}(L_a)\,dt$. Identify the fixed finite protocol and duration assumptions behind the perturbation remainder.
- **Dependencies and story role:** Uses M08–M09. Supplies the sensitivity functional that the geometric argument minimizes.
- **Conceptual connection:** A state-dependent noise exposure becomes a scalar action along a controlled path, while the scope of the expansion remains explicit.
- **Project sources:** [Fixed-protocol sensitivity](../science/geometry.md#1-first-order-error-of-a-fixed-exact-transfer); [weak-noise claim](../science/model.md#sharp-weak-noise-optimum).
- **Anchor pointer:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616).

### M11: Quantum jumps describe an unconditional channel

- **Phase:** background/preliminaries.
- **Central question:** What can a jump representation establish without measuring the environment?
- **Understanding target:** Distinguish the unconditional master equation from a mathematical ensemble of no-jump and jump trajectories. Explain why unitary Z jumps have a state-independent intensity, how their count becomes Poisson, and why correcting all one-jump branches can yield a bound from the probability of two or more jumps.
- **Dependencies and story role:** Uses M04–M05. Provides the probabilistic tool needed for the coherent-workspace boundary construction.
- **Conceptual connection:** Trajectory bookkeeping can prove a channel-level error statement without adding a measurement or feedback resource to the physical protocol.
- **Project sources:** [Exact jump-count bound](../science/workspace.md#46-exact-bound-from-two-or-more-jumps); [workspace verification](../verification/README.md#4-continuous-one-jump-correction-with-retained-workspace).
- **Anchor pointers:** [BP6 — Stochastic Dynamics in Hilbert Space](https://academic.oup.com/book/27757/chapter/197981235); [BP7 — The Stochastic Simulation Method](https://academic.oup.com/book/27757/chapter/197981984).

### M12: From pair costs to a shortest-path distance

- **Phase:** background/preliminaries.
- **Central question:** Why can two smaller noise steps cost less than one direct step?
- **Understanding target:** Distinguish an edge weight from the minimum sum of weights over paths. Explain why squared distances can violate the triangle inequality, how metric closure repairs that property, and how zero-cost duplicate signatures can be identified without changing distances between distinct signatures.
- **Dependencies and story role:** Uses M06. Introduces the graph language needed by the control certificate without yet assuming that a quantum trajectory follows graph edges.
- **Conceptual connection:** The three-level direct-versus-middle comparison suggests a candidate control invariant, but its all-control meaning still requires a proof.
- **Project sources:** [Graph definition](../science/model.md#the-dephasing-graph); [multilevel example](../science/interpretation.md#a-small-multilevel-example); [learning introduction](README.md).
- **Anchor pointer:** [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190) for the physical context; the shortest-path definitions are supplied in the project.

### M13: Population reliability and coherent channel quality

- **Phase:** background/preliminaries.
- **Central question:** Why does a low truth-table error not establish a high-fidelity quantum gate?
- **Understanding target:** Distinguish population error, phase error, leakage, and a full-channel distance. Explain the role of an ideal-corrected projected logical map, its unconditioned Choi weights, and why normalizing after successful projection would change the task.
- **Dependencies and story role:** Uses M02–M04. Completes the operational vocabulary needed to assess a construction beyond basis inputs.
- **Conceptual connection:** Bias shaping can reduce one error component while worsening another; channel bookkeeping keeps that tradeoff visible.
- **Project sources:** [Logical error components](../science/constructions.md#6-logical-phase-transverse-and-leakage-weights); [full-channel budget](../science/constructions.md#7-a-rigorous-fixed-total-channel-error-budget).
- **Anchor pointers:** [BP2 — Quantum Probability](https://academic.oup.com/book/27757/chapter/197977987); [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616). The particular Choi and norm conventions are defined in the project.

### M14: The complete optimization problem and its quantifiers

- **Phase:** background/preliminaries.
- **Central question:** What is allowed to vary when the project asks for the smallest transfer error?
- **Understanding target:** Assemble the specified noise, retained state, target event, and control budget into one optimization. Distinguish a fixed-protocol expansion from an infimum over controls and durations that can depend on noise strength, and distinguish a fixed finite model from a changing-dimension family.
- **Dependencies and story role:** Integrates M01–M13. Ends the background phase with a precise statement of the problem and of the stronger inferences that require additional arguments.
- **Conceptual connection:** A sharp derivative for one schedule becomes a global optimum only after the lower bound covers the entire admissible family.
- **Project sources:** [Exact claims and domains](../science/model.md#exact-claims-and-their-domains); [optimization at nonzero noise](../science/geometry.md#5-optimization-at-nonzero-noise); [resource scope](../science/control_resources.md#7-scope-of-the-claim).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190), connected to the optimization through the project derivations.

## Phase 2: narrative/innovation

### M15: A distance potential separates the endpoints

- **Phase:** narrative/innovation.
- **Central question:** How can a shortest-path distance supply a certificate that constrains every coherent trajectory?
- **Understanding target:** Explain the truncated distance coordinate $u_i=\min\{d_Q(s,i),d_Q(s,t)\}$ and the inequality $|u_i-u_j|\leq Q_{ij}$. Understand how thresholds of that coordinate define binary observables that all separate the initial state from the target.
- **Dependencies and story role:** Uses M06, M12, and M14. Begins the proof with a local pairwise inequality and a finite family of necessary crossings.
- **Conceptual connection:** The graph contributes a family of observables, rather than an assumption that physical motion follows a classical path.
- **Project sources:** [Distance certificate](../science/geometry.md#2-a-certificate-from-graph-distances); [cut construction](../science/finite_noise.md#2-a-family-of-cuts-certified-by-the-noise-distance).
- **Anchor pointers:** [BP2 — Quantum Probability](https://academic.oup.com/book/27757/chapter/197977987); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190), with the distance certificate supplied locally.

### M16: Comparing the real noise with weighted binary cuts

- **Phase:** narrative/innovation.
- **Central question:** Why does every state pay at least the weighted exposure of the separating cuts?
- **Understanding target:** Connect the decomposition of $|u_i-u_j|$ into threshold separations to the variance inequality for pure states and the commutator-norm inequality for mixed states. Distinguish this entrywise Dirichlet-form comparison from a claim that one Lindblad generator is another plus a completely positive remainder.
- **Dependencies and story role:** Uses M09–M10 and M15. Converts the local certificate into an inequality that applies along any allowed control path.
- **Conceptual connection:** The same comparison links perturbative noise action to the exact purity-loss argument used later.
- **Project sources:** [Pure and mixed cut comparison](../science/geometry.md#2-a-certificate-from-graph-distances); [finite-noise Dirichlet comparison](../science/finite_noise.md#2-a-family-of-cuts-certified-by-the-noise-distance).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190).

### M17: The unavoidable cost of one binary crossing

- **Phase:** narrative/innovation.
- **Central question:** Why must a bounded coherent change of a binary label accumulate a definite variance?
- **Understanding target:** Connect the mixing-block speed bound to the integrated crossing cost $\pi/(4\Omega)$. Explain why nonmonotone motion and backtracking cannot lower it and why a maximal-strength two-level rotation attains it. Recognize the scalar result as an inherited ingredient with a specified normalization.
- **Dependencies and story role:** Uses M07–M08, M10, and M15. Supplies the local dynamical cost that every certificate cut must pay.
- **Conceptual connection:** A speed restriction becomes a noise-exposure restriction because a changing label must pass through states with nonzero variance.
- **Project sources:** [Binary crossing proof](../science/geometry.md#3-the-binary-crossing-cost); [Lu et al. attribution](../references/RELATED_WORK.md#two-level-optimality-lu-et-al).
- **Anchor pointer:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616), with the scalar optimal-control ingredient and attribution in the linked sources.

### M18: The sharp first-order distance law

- **Phase:** narrative/innovation.
- **Central question:** Why does the sum of cut costs equal an attainable shortest-path cost?
- **Understanding target:** Combine M16 and M17 into the lower coefficient $\pi d_Q(s,t)/(16\Omega)$. Explain how successive maximal-strength pair rotations on a minimizing path attain the same coefficient, despite the converse allowing arbitrary many-level superpositions and interference.
- **Dependencies and story role:** Uses M10 and M15–M17. Integrates the local certificate and scalar crossing into the first global optimality statement.
- **Conceptual connection:** A classical distance characterizes a quantum control optimum without restricting all optimal protocols to classical sequences.
- **Project sources:** [Crossing sum](../science/geometry.md#3-the-binary-crossing-cost); [attaining path](../science/geometry.md#4-a-path-that-attains-the-lower-bound); [explicit transfer](../science/constructions.md#2-transfer-along-a-shortest-path).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190), extended by the project's distance theorem.

### M19: A finite-noise converse from the actual mixed state

- **Phase:** narrative/innovation.
- **Central question:** What prevents a very long noisy protocol from evading the perturbative crossing argument?
- **Understanding target:** Explain how high target success bounds final purity from below, how unitality transfers that constraint to earlier times, and how block coherence must then accompany each cut crossing. Understand the self-consistent error inequality and its extension to the complete domain $q\in[0,1]$.
- **Dependencies and story role:** Uses M09, M14, and M16–M18. Replaces ideal-trajectory reasoning with a lower bound valid at arbitrary noise strength and duration.
- **Conceptual connection:** The target's accuracy constrains the entire noisy history, giving a converse even for controls that are not exact when noise is switched off.
- **Project sources:** [Mixed-state estimates](../science/finite_noise.md#3-two-block-estimates-for-a-mixed-state); [scalar integral](../science/finite_noise.md#4-the-scalar-crossing-integral); [assembled bound](../science/finite_noise.md#5-assemble-the-finite-noise-bound).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190).

### M20: Optimizing controls that depend on the noise

- **Phase:** narrative/innovation.
- **Central question:** How does a finite-noise bound justify the exact weak-noise optimum over all controls?
- **Understanding target:** Explain the sandwich between the uniform converse and one fixed constructive upper bound. Identify why no minimizer, uniform duration bound, or interchange of optimization and differentiation is needed, and why the resulting remainder is stated for a fixed finite noise model.
- **Dependencies and story role:** Uses M14 and M18–M19. Completes the central theorem with its strongest quantifiers.
- **Conceptual connection:** Uniform control of a family of noisy experiments turns a perturbative coefficient into an optimization theorem.
- **Project sources:** [Uniform noisy optimization](../science/finite_noise.md#6-uniformity-over-noisy-optimization); [optimized asymptotic argument](../science/geometry.md#5-optimization-at-nonzero-noise); [canonical claim](../science/model.md#sharp-weak-noise-optimum).
- **Anchor pointer:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616), with the optimization argument supplied by the project.

### M21: Exact path probabilities and coherent logical gates

- **Phase:** narrative/innovation.
- **Central question:** How can an optimal transfer route act correctly on both logical basis inputs and their superpositions?
- **Understanding target:** Explain why the active two-level block gives an exact product success probability for a simple path. Connect the forward/back sequence to an ideal endpoint swap with restored interior levels, and identify the phase-free conditional controls required for an exact ideal controlled logical X. Keep ideal coherent action separate from noisy phase fidelity.
- **Dependencies and story role:** Uses M08, M13, M18, and M20. Extends the state-transfer result to a computational primitive and supplies exact probabilities for later scaling limits.
- **Conceptual connection:** Pulse phases, both input columns, and leakage accounting must agree before a transfer construction becomes a gate construction.
- **Project sources:** [Exact finite-noise success](../science/constructions.md#3-exact-success-probability-at-finite-noise); [endpoint logical gate](../science/constructions.md#4-a-coherent-logical-x-with-internal-helper-levels); [controlled extension](../science/constructions.md#controlled-extension).
- **Anchor pointers:** [BP2 — Quantum Probability](https://academic.oup.com/book/27757/chapter/197977987); [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616).

### M22: Which additional states actually shorten the noise distance?

- **Phase:** narrative/innovation.
- **Central question:** Why do intermediate noise values help while repeated or binary signatures can fail to help?
- **Understanding target:** Contrast a scalar spectrum's sum of squared adjacent gaps with the weighted Hamming metric generated by binary labels. Explain the zero-distance protected case and why extra degeneracy does not create new spectral resolution between distinguishable endpoints.
- **Dependencies and story role:** Uses M06, M12, and M18–M20. Turns the general theorem into a classification of useful auxiliary physical levels.
- **Conceptual connection:** Hilbert-space dimension becomes a resource only through the noise signatures and controls that its added states supply.
- **Project sources:** [Two useful geometries](../science/geometry.md#6-two-useful-geometries); [binary dephasing interpretation](../science/interpretation.md#why-binary-dephasing-behaves-differently); [protected zero-distance case](../science/geometry.md#5-optimization-at-nonzero-noise).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190).

### M23: Spectral refinement and a controlled growing-dimension limit

- **Phase:** narrative/innovation.
- **Central question:** What is held fixed when refining a spectrum reduces population error as $1/m$?
- **Understanding target:** Relate a fixed endpoint span split into m equal gaps to distance $\gamma\Delta^2/m$, helper count, and duration. Distinguish the fixed-m weak-noise expansion from the fixed-noise large-m limit justified by exact probabilities, and contrast both with a physical ladder whose noise span grows with m.
- **Dependencies and story role:** Uses M14, M21, and M22. Converts the geometry classification into an asymptotic mechanism with explicit resource accounting.
- **Conceptual connection:** Smaller noise differences on individual steps can outweigh a longer path for populations, but this comparison changes if the noise normalization changes.
- **Project sources:** [Uniform refinement](../science/constructions.md#5-a-uniformly-refined-noise-spectrum); [fixed span versus physical ladder](../science/interpretation.md#fixed-span-and-a-fixed-physical-ladder); [normalized finite-spin example](../science/control_resources.md#5-a-finite-spin-model-with-its-normalization-explicit).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190).

### M24: The phase, leakage, and time budget of bias shaping

- **Phase:** narrative/innovation.
- **Central question:** What is the cost of reducing population errors through a longer refined-spectrum gate?
- **Understanding target:** Explain why the leading phase-error coefficient grows with m while truth error decreases, with leakage included in the latter. Distinguish that fixed-m expansion from the separate fixed-noise coherence-loss estimate. Relate the unconditioned channel components to the full-channel bound, and understand how an explicit total-error budget can support reduced truth error without substituting a growing m into an uncontrolled perturbation remainder.
- **Dependencies and story role:** Uses M13 and M21–M23. Evaluates the gate as a quantum operation rather than only as a population-transfer experiment.
- **Conceptual connection:** The construction reshapes error bias; dimension and time buy a particular redistribution of errors, not unlimited improvement in every fidelity measure.
- **Project sources:** [Logical error weights](../science/constructions.md#6-logical-phase-transverse-and-leakage-weights); [coherence at fixed noise](../science/constructions.md#coherence-at-fixed-noise-as-the-ladder-grows); [fixed total-channel-error budget](../science/constructions.md#7-a-rigorous-fixed-total-channel-error-budget); [resource table](../science/control_resources.md#4-what-spectral-refinement-pays-for).
- **Anchor pointers:** [BP2 — Quantum Probability](https://academic.oup.com/book/27757/chapter/197977987); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190).

### M25: When the mathematical optimum is physically attainable

- **Phase:** narrative/innovation.
- **Central question:** Which device constraints preserve the lower bound but obstruct its saturating construction?
- **Understanding target:** Separate known noise signatures from selective access to their optimal path. Account for pair shifts, conditional interactions, aggregate mixing strength, and additional noise; explain why a restricted hardware graph supplies a constructive upper bound without automatically defining the exact restricted optimum.
- **Dependencies and story role:** Uses M07, M20–M24. Combines the control law and gate mechanism with their implementation assumptions.
- **Conceptual connection:** A noise graph and a control-access graph answer different questions, and a diagonal interaction-frame change preserves cut norms without automatically preserving a global spectral-width budget.
- **Project sources:** [Control accounting](../science/control_resources.md#1-what-is-bounded); [required access](../science/control_resources.md#2-access-required-for-achievability); [restricted hardware graphs](../science/control_resources.md#3-restricted-hardware-graphs); [extra noise](../science/control_resources.md#6-additional-noise-changes-the-graph).
- **Anchor pointer:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616), with the control-access and resource analysis in the project.

### M26: Pure workspace return is a separate operational requirement

- **Phase:** narrative/innovation.
- **Central question:** What remains unavoidable when arbitrary coherent workspace is included in the target state?
- **Understanding target:** Explain the local mixing-budget parameter $R=\sum_a\kappa_a/h_a$ and the bound on joint pure-state return. Relate joint failure to data error plus work-return error, and identify the pure initialization, retained-work, and label-preserving unital-noise assumptions needed by the proof.
- **Dependencies and story role:** Uses M03, M09, M19, and M25. Extends the converse to coherent controllers while keeping the measured output and resource boundary explicit.
- **Conceptual connection:** Protecting data by moving uncertainty into a helper does not preserve the same complete pure target.
- **Project sources:** [Local workspace model](../science/workspace.md#1-model-with-local-mixing-budgets); [full return theorem](../science/workspace.md#2-full-pure-state-return); [data and workspace errors](../science/workspace.md#separate-data-and-workspace-errors).
- **Anchor pointers:** [BP2 — Quantum Probability](https://academic.oup.com/book/27757/chapter/197977987); [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616).

### M27: Coherent correction defeats a data-only linear floor

- **Phase:** narrative/innovation.
- **Central question:** How can finite noisy pulses suppress first-order data bit errors while respecting the workspace bound?
- **Understanding target:** Follow temporary repetition encoding, transversal CNOT, decoding, and compiled coherent majority correction. Explain why every zero- or one-jump data Kraus operator is diagonal after removing the ideal gate, why the remaining error is bounded by the two-or-more-jump probability, and where the syndrome is retained.
- **Dependencies and story role:** Uses M11, M13, and M26. Supplies a concrete boundary example that prevents an overly broad interpretation of the converse.
- **Conceptual connection:** Error correction redistributes information; phase noise and work contamination remain compatible with quadratic suppression of data population error. The repetition mechanism is explicitly attributed to prior work.
- **Project sources:** [Full coherent circuit proof](../science/workspace.md#4-an-explicit-coherent-escape-from-a-data-only-linear-floor); [consistency with the bound](../science/workspace.md#5-consistency-with-the-return-and-entropy-bounds); [repetition filtering attribution](../references/RELATED_WORK.md#repetition-filtering-and-syndrome-storage).
- **Anchor pointers:** [BP6 — Stochastic Dynamics in Hilbert Space](https://academic.oup.com/book/27757/chapter/197981235); [BP7 — The Stochastic Simulation Method](https://academic.oup.com/book/27757/chapter/197981984).

### M28: The entropy retained when data error is suppressed

- **Phase:** narrative/innovation.
- **Central question:** What quantitative uncertainty must remain in work when data population error is smaller than first order?
- **Understanding target:** Connect the finite joint-purity loss, near-correct data output, and the work-marginal purity bound. Explain how majorization produces a dimension-independent entropy bound and why $e=o(R)$ forces at least a contribution proportional to $R\ln(1/R)$. Recognize the correction circuit's matching order and the limits on additive or thermodynamic interpretations.
- **Dependencies and story role:** Uses M03, M09, and M26–M27. Quantifies the resource used by the data-only escape without imposing pure work return.
- **Conceptual connection:** The same irreversible mixing that obstructs joint return becomes a lower bound on retained syndrome uncertainty when the data is protected.
- **Project sources:** [Finite work-entropy bound](../science/workspace.md#3-work-entropy-without-a-clean-return-requirement); [matching scaling example](../science/workspace.md#5-consistency-with-the-return-and-entropy-bounds); [correction and interpretation](../science/interpretation.md#how-correction-changes-the-conclusion).
- **Anchor pointers:** [BP2 — Quantum Probability](https://academic.oup.com/book/27757/chapter/197977987); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190).

### M29: What establishes each part of the scientific account

- **Phase:** narrative/innovation.
- **Central question:** Which conclusions follow from proof, explicit construction, finite verification, and earlier literature?
- **Understanding target:** Distinguish the universal cut converse from the finite channel calculations that check pulse phases, constants, leakage, and one-jump mechanisms. Identify the inherited scalar inequality, dephasing geometry, and repetition correction, and explain why neither numerical agreement nor an educational source certifies a new all-control theorem or hardware implementation.
- **Dependencies and story role:** Uses M20–M28. Connects the complete result to its analytical, computational, and bibliographic support.
- **Conceptual connection:** Reproducibility and attribution strengthen a result by specifying what each kind of evidence does and does not establish.
- **Project sources:** [Verification scope](../verification/README.md); [established ingredients and extension](../references/RELATED_WORK.md#established-ingredients-and-the-present-extension); [source coverage](../references/RELATED_WORK.md#source-coverage-and-limits-of-the-comparison).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP7 — The Stochastic Simulation Method](https://academic.oup.com/book/27757/chapter/197981984). The project's finite checks use deterministic channel calculations rather than a Monte Carlo estimate of the converse.

### M30: The complete design principle and its boundaries

- **Phase:** narrative/innovation.
- **Central question:** What does the combined theory imply for designing a dephasing-exposed quantum operation?
- **Understanding target:** Connect measured coherence-decay rates to the noise distance, available controls to attainability, and the chosen output task to its error accounting. Explain the distinct effects of faster mixing, intermediate physical noise signatures, and retained syndrome work, while keeping phase costs, normalization, reset assumptions, and excluded noise models explicit.
- **Dependencies and story role:** Integrates M15–M29 with the framework assembled in M14. Completes the progression from individual noise-sensitive crossings to the project's global scientific meaning.
- **Conceptual connection:** Reliable control depends jointly on the environment's distinguishability geometry, the actual coherent-control resource, and where the protocol is allowed to leave uncertainty.
- **Project sources:** [Physical interpretation](../science/interpretation.md); [canonical result domains](../science/model.md#exact-claims-and-their-domains); [resource scope](../science/control_resources.md#7-scope-of-the-claim); [workspace consequences](../science/workspace.md).
- **Anchor pointers:** [BP3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616); [BP4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190), connected to the complete account through the [selected-source bridge](BREUER_PETRUCCIONE_BRIDGE.md).
