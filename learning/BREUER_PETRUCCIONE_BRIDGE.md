# From Breuer–Petruccione to dephasing control geometry

This bridge connects the open-system framework in **Heinz-Peter Breuer and Francesco Petruccione, *The Theory of Open Quantum Systems*** to the specific control problem in this repository. The book supplies the foundation for density matrices, master equations, decoherence and trajectory descriptions. The graph certificate, sharp control optimization and workspace bounds are developed in the project's scientific pages.

Begin with the [complete three-level example](README.md#2-a-complete-three-level-example) for the physical mechanism. Use the [30-milestone map](MILESTONES.md) for the common conceptual route. The chapter pointers below are selective references; reading the whole book is not a prerequisite for using the explanations here.

## 1. Selected source and reliable pointers

**Selected edition:** Oxford University Press, 2007 paperback, print ISBN **9780199213900**. The [official Oxford record](https://academic.oup.com/book/27757) gives a publication date of 25 January 2007, online ISBN 9780191706349, and [book DOI](https://doi.org/10.1093/acprof:oso/9780199213900.001.0001).

| Verified chapter | Foundation to consult | Project connection |
|---|---|---|
| [2 — Quantum Probability](https://academic.oup.com/book/27757/chapter/197977987) | States, composite systems, reduced states, entropy and operations | Population error, joint purity and retained workspace |
| [3 — Quantum Master Equations](https://academic.oup.com/book/27757/chapter/197978616) | Master-equation description of open dynamics | The fixed Lindblad generator and its assumptions |
| [4 — Decoherence](https://academic.oup.com/book/27757/chapter-abstract/197980190) | Environmental suppression of coherence | Why noise eigenvalue differences matter during control |
| [6 — Stochastic Dynamics In Hilbert Space](https://academic.oup.com/book/27757/chapter/197981235) | Conditional trajectories and master-equation unraveling | Jump bookkeeping for the coherent correction example |
| [7 — The Stochastic Simulation Method](https://academic.oup.com/book/27757/chapter/197981984) | Stochastic representations used computationally | Interpreting simulation evidence and its limits |

These identities and chapter-level pointers were checked against Oxford's table of contents and chapter records. Full chapter text was not available through the public records used here, so no unverified subsection numbers or book-equation numbers are supplied.

The formulas below use **project notation** and are derived or explained locally. They are not transcriptions of particular textbook equations.

## 2. The convention bridge

The retained finite system has density matrix $`\rho`$, a positive matrix of trace one. A diagonal entry $`\rho_{ii}`$ is the probability of basis outcome $`i`$. The Hamiltonian $`H(t)`$ generates coherent motion; throughout this project $`\hbar=1`$.

The canonical equation is

```math
\dot\rho_\epsilon
=-i[H(t),\rho_\epsilon]
+\epsilon\sum_a\gamma_a\mathcal D[L_a](\rho_\epsilon),
\qquad
\mathcal D[L](\rho)
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

Here $`\{A,B\}=AB+BA`$. The project restricts $`L_a`$ to fixed, mutually commuting Hermitian operators, so $`L_a^\dagger=L_a`$ and a common eigenbasis exists.

| Quantity or convention | Translation used here |
|---|---|
| A jump operator with its rate absorbed | Write $`C_a=\sqrt{\epsilon\gamma_a}L_a`$, so $`\mathcal D[C_a]=\epsilon\gamma_a\mathcal D[L_a]`$. |
| Reference rate and noise strength | $`\gamma_a`$ is fixed while $`\epsilon`$ scales the noise. An actual rate is $`\kappa_a=\epsilon\gamma_a`$. |
| Common noise eigenbasis | $`L_a\lvert i\rangle=\lambda_{ai}\lvert i\rangle`$. The weighted signature is $`(\sqrt{\gamma_a}\lambda_{ai})_a`$. |
| Reference graph cost | $`Q_{ij}=\sum_a\gamma_a(\lambda_{ai}-\lambda_{aj})^2`$. |
| Physical coherence-decay rate | $`\Gamma_{ij}=\epsilon Q_{ij}/2`$ when the coherent drive is off. |
| Pure-state variance | $`\mathrm{Var}_{\psi}(L)=\langle L^2\rangle_\psi-\langle L\rangle_\psi^2`$. |
| Purity | $`P=\mathrm{Tr}\rho^2`$; $`P=1`$ for a pure state. |
| Control resource | $`h(H)=\min_{c\in\mathbb R}\lVert H-cI\rVert_\infty\leq\Omega`$, where the norm is the operator norm. |
| Population-transfer failure | $`q=1-\langle t\lvert\rho(T)\rvert t\rangle`$, including every outcome outside the target. |
| Workspace-page rates | The $`\kappa_a`$ in [workspace.md](../science/workspace.md) are actual rates, already including any weak-noise scaling. |

Comparing two noise formulas requires comparing their complete generators. A coefficient named “dephasing rate” may be the coefficient of a dissipator or the decay rate of an off-diagonal matrix element; those differ by a factor of two for the Pauli convention below.

### A compact qubit normalization check

Let $`Z=\mathrm{diag}(1,-1)`$ and turn off $`H`$. Then

```math
\kappa\mathcal D[Z](\rho)
=\kappa(Z\rho Z-\rho)
=-\frac{\kappa}{2}[Z,[Z,\rho]],
\qquad
\dot\rho_{01}=-2\kappa\rho_{01}.
```

Starting from $`\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2`$ gives

```math
\rho(t)=\frac12
\begin{pmatrix}
1&e^{-2\kappa t}\\
e^{-2\kappa t}&1
\end{pmatrix},
\qquad
P(t)=\frac{1+e^{-4\kappa t}}2.
```

The populations stay at one half while coherence and purity decrease. Thus a measured coherence-decay rate $`\Gamma_\phi`$ corresponds to $`\kappa=\Gamma_\phi/2`$ in this convention. This check fixes the normalization; the transfer theorem itself starts in a noise eigenstate.

## 3. Assumptions added to the textbook framework

A general open-system description covers more processes than the theorem here. The specialization is essential.

| Assumption in this project | Why it matters |
|---|---|
| Fixed commuting Hermitian jumps | Provides common noise signatures and preserves their basis populations when $`H=0`$. |
| Fixed laboratory-frame noise during a protocol | The same cost matrix applies along the entire controlled trajectory. |
| Unital retained dynamics | Purity cannot increase; final high purity constrains the preceding trajectory. Hermitian dephasing has this property. General relaxation need not. |
| A bound on total coherent mixing | Limits how quickly a trajectory can cross each partition used in the converse. |
| All controlled workspace retained during the interval | Prevents entropy disposal from being silently identified with pure joint return. |
| No feedback conditioned on an observed noise record | The control problem concerns the unconditional master-equation state. |
| Fixed finite model when $`\epsilon\to0`$ | Gives the stated weak-noise expansion. The growing-ladder limit is treated separately through exact probabilities. |

The lower bound allows arbitrary admissible control shapes and finite durations, including choices that depend on $`\epsilon`$. Attaining it additionally requires selective pair rotations on a shortest path. Hardware selection rules, pulse bandwidth and conditional interactions must therefore be distinguished from the Lindblad description itself. The [model](../science/model.md) and [control-resource account](../science/control_resources.md) specify these domains.

### Norm and phase conventions

The spectral halfwidth is unchanged by a scalar energy shift. For Hermitian $`H`$,

```math
h(H)=\frac{\lambda_{\max}(H)-\lambda_{\min}(H)}2.
```

For a pair of levels, let $`X_{ij}=\lvert i\rangle\langle j\rvert+\lvert j\rangle\langle i\rvert`$ and $`P_{ij}=\lvert i\rangle\langle i\rvert+\lvert j\rangle\langle j\rvert`$. A pulse $`\Omega X_{ij}`$ has halfwidth $`\Omega`$ and produces $`-iX`$ on the pair after $`\tau=\pi/(2\Omega)`$. The phase-free pulse $`\Omega(X_{ij}-P_{ij})`$ produces $`X`$ in the same time. Its displayed operator norm is $`2\Omega`$, but its halfwidth is still $`\Omega`$.

The selective pair energy shift is part of the second control. A phase that is common within a logical subspace can become a relative phase when the operation is conditioned on another register. The [construction](../science/constructions.md#1-a-phase-free-elementary-transposition) accounts for this explicitly.

## 4. Locally supplied steps from a master equation to the theorem

The book's framework makes the objects meaningful. The following steps connect them to this project's result. Each has an authoritative derivation under science/.

### Step A: Extract the physical noise geometry

In the common eigenbasis,

```math
\bigl(\mathcal D[L_a](\rho)\bigr)_{ij}
=\left(\lambda_{ai}\lambda_{aj}
-\frac{\lambda_{ai}^2+\lambda_{aj}^2}{2}\right)\rho_{ij}
=-\frac{(\lambda_{ai}-\lambda_{aj})^2}{2}\rho_{ij}.
```

Summing gives $`\Gamma_{ij}=\epsilon Q_{ij}/2`$. Equal weighted signatures mean that every active jump acts identically on the two states; their common eigenspace is protected against this dissipator. Zero-rate jumps have no physical effect.

The squared-distance description has established research antecedents, credited to Fagnola and collaborators in [Related work](../references/RELATED_WORK.md). The control theorem uses its shortest-path closure, which can be smaller than a direct squared distance.

### Step B: Convert a fixed ideal trajectory into leading error

Suppose one fixed finite control transfers $`\lvert s\rangle`$ exactly to $`\lvert t\rangle`$ when $`\epsilon=0`$, with ideal trajectory $`\lvert\psi(u)\rangle`$. The interaction-picture expansion gives

```math
q_\epsilon
=\epsilon\int_0^T
\sum_a\gamma_a\mathrm{Var}_{\psi(u)}(L_a)\,du
+O(\epsilon^2).
```

The local identity behind the sign is

```math
\langle\psi\lvert
\mathcal D[L](\lvert\psi\rangle\langle\psi\rvert)
\rvert\psi\rangle
=-\mathrm{Var}_{\psi}(L).
```

This explains why exposure during a coherent motion matters even though its endpoint eigenstates do not dephase. It also fixes a second factor of two: instantaneous purity loss of a pure state is twice this fidelity-loss rate. The [interaction-picture derivation](../science/geometry.md#1-first-order-error-of-a-fixed-exact-transfer) states the precise fixed-protocol expansion.

### Step C: Prove a bound for every coherent path

Let $`d=d_Q(s,t)`$ be the shortest-path distance of $`Q`$, and define a potential $`u_i=\min\{d_Q(s,i),d\}`$. It satisfies $`|u_i-u_j|\leq Q_{ij}`$. Thresholding the potential produces binary observables $`D_k`$ that separate the endpoints, with positive increments $`\delta_k`$ summing to $`d`$.

The comparison is

```math
\sum_a\gamma_a\mathrm{Var}_{\psi}(L_a)
\geq\sum_k\frac{\delta_k}{4}\mathrm{Var}_{\psi}(D_k).
```

For each cut, $`f=\langle D_k\rangle`$ must pass from $`+1`$ to $`-1`$. The control budget implies $`|\dot f|\leq2\Omega\sqrt{1-f^2}`$, and integration gives a cost at least $`\pi/(4\Omega)`$. Summing therefore gives $`\pi d/(16\Omega)`$.

These cuts certify arbitrary coherent paths; they do not restrict the state to adjacent graph vertices. The scalar crossing optimum is credited to Lu and collaborators. The new connection developed here is the all-control graph certificate and its saturating path, proved in [Geometry](../science/geometry.md).

### Step D: Control optimization over noisy and long protocols

The fixed-trajectory expansion cannot by itself justify optimization over durations that grow as noise decreases. For the actual mixed state, the exact identity is

```math
-\frac{d}{dt}\mathrm{Tr}\rho^2
=\epsilon\sum_a\gamma_a
\lVert[L_a,\rho]\rVert_2^2.
```

Here $`\lVert A\rVert_2^2=\mathrm{Tr}(A^\dagger A)`$ is the Hilbert–Schmidt norm. Final overlap $`1-q`$ implies $`P(T)\geq(1-q)^2`$. Since purity cannot increase, that endpoint information bounds purity throughout the path. A state with high purity and substantial populations on both sides of a cut must carry coherence across that cut.

The mixed-state block estimates and their integration give

```math
q\geq\frac{\pi\epsilon d}{16\Omega+8\pi\epsilon d}.
```

Combining this uniform converse with one fixed saturating path proves the sharp optimized leading coefficient. The rational expression is a finite-noise lower bound, not an exact finite-noise optimum. The full argument is in [Finite noise](../science/finite_noise.md), with the optimization quantifiers in [Geometry, Section 5](../science/geometry.md#5-optimization-at-nonzero-noise).

### Step E: Turn the path into an operation

A shortest path provides a sequence of pair rotations that attains the bound for one basis transfer. An endpoint logical swap uses the forward path followed by the first edges in reverse order. Both logical basis inputs then have the optimal leading population error, while arbitrary superpositions can accumulate phase error.

The [worked example and gate comparison](README.md#4-a-good-basis-transfer-is-only-part-of-a-quantum-gate) display that tradeoff. [Constructions](../science/constructions.md) supplies exact finite-noise probabilities, phase and leakage weights, and the charged controlled extension. The graph theorem alone does not establish simultaneous attainability for every column of an arbitrary permutation.

## 5. From reduced states to retained-workspace consequences

The composite-system distinction in Chapter 2 is operational here. The data marginal $`\rho_D=\mathrm{Tr}_W\rho_{DW}`$ can be accurate while the retained work $`W`$ stores a syndrome. A pure target for the joint state is a stricter requirement.

For target $`\lvert b\rangle_D\lvert w_0\rangle_W`$, define data error $`e`$, pure-work return error $`r`$, and joint target error $`q`$. Their target projectors commute, giving $`q\leq e+r`$. For binary data jumps with actual rates $`\kappa_a`$ and changed-label mixing budgets $`h_a`$, write

```math
R=\sum_{a\in C}\frac{\kappa_a}{h_a}.
```

The project then proves

```math
e+r\geq\frac{\pi R}{4+8\pi R}.
```

This is supplied locally by applying the mixed-state crossing proof to the complete retained system. Adding noiseless work duplicates noise signatures; it does not create intermediate signatures. Allowing that work to remain mixed changes the final task.

The further entropy consequence is also a project derivation. Forced joint purity loss is transferred to a bound on work purity when the data error is small, and then to entropy. With natural logarithms, the accurate-data regime $`e=o(R)`$ satisfies

```math
\liminf_{R\to0}
\frac{S(W)}{R\ln(1/R)}\geq\frac{\pi}{4}.
```

The [workspace proof](../science/workspace.md) gives the finite inequalities and permits correlations between data and work. This is an entropy requirement after the stated initialized operation. Converting it into an erasure-work or heat cost requires a thermodynamic model.

### What the trajectory chapters add

For the coherent repetition-correction example, each physical jump is $`\sqrt{\gamma}Z_j`$, so its squared amplitude operator is $`\gamma I`$. The total jump intensity for four qubits is therefore the state-independent value $`4\gamma`$. Over the gadget duration $`T_g`$, the jump count is Poisson with mean $`\mu=4\gamma T_g`$.

The circuit corrects the population effect of zero or one jump without using a measured record. Consequently,

```math
e_{\mathrm{data}}\leq\Pr(N\geq2)
=1-e^{-\mu}(1+\mu).
```

Chapter 6 supplies the trajectory viewpoint; the circuit propagation and its correction property are proved locally in [Workspace, Section 4](../science/workspace.md#4-an-explicit-coherent-escape-from-a-data-only-linear-floor). The trajectory representation is bookkeeping for the unconditional channel, not permission for feedback or postselection.

Chapter 7 provides context for stochastic numerical methods. The repository's current [verification suite](../verification/README.md) instead uses deterministic finite-dimensional propagation and matrix-exponential derivatives. Either type of numerical method checks specified cases; the universal optimality statement rests on the analytical proof.

## 6. Foundation, attribution and authoritative routes

Breuer–Petruccione is the single educational anchor. Research papers cited in [Related work](../references/RELATED_WORK.md) identify inherited ingredients and scientific comparisons; they are not additional educational prerequisites.

| Question after consulting the anchor | Authoritative project account |
|---|---|
| Which dynamics and optimization are actually claimed? | [Model](../science/model.md) |
| Why does a shortest-path distance constrain arbitrary superpositions? | [Geometry](../science/geometry.md) |
| Why do long, noise-dependent protocols obey the same leading limit? | [Finite noise](../science/finite_noise.md) |
| Which pulses attain the bound, and what happens to phase and leakage? | [Constructions](../science/constructions.md) |
| What do selective controls and additional levels cost? | [Control resources](../science/control_resources.md) |
| How does retained syndrome information change the error statement? | [Workspace](../science/workspace.md) |
| How do the assumptions and resources fit together? | [Interpretation](../science/interpretation.md) |

The bridge supplies the connections between the foundation and these results. The scientific pages remain the authoritative homes of their exact assumptions, proofs and limiting cases.
