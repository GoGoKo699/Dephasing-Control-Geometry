# Learning Dephasing Control Geometry

The central question is concrete: a quantum system must move from one basis state to another while its environment dephases superpositions. How much population error is unavoidable when the coherent drive has a fixed strength? The answer depends on the available noise eigenvalues, the allowed controls, and which degrees of freedom must finish in the prescribed state.

This route uses one educational anchor: **Heinz-Peter Breuer and Francesco Petruccione, *The Theory of Open Quantum Systems***, Oxford University Press, 2007 paperback, ISBN 9780199213900. The [source bridge](BREUER_PETRUCCIONE_BRIDGE.md) identifies the relevant material and translates it into the repository's conventions. The [30-milestone map](MILESTONES.md) gives the project's complete conceptual route. Neither requires reading the entire book before beginning.

## Reading routes

| Reader's purpose | Route |
|---|---|
| Understand the physical mechanism | Work through the three-level example below, then read [Interpretation](../science/interpretation.md). |
| Build the prerequisite framework | Follow the background/preliminaries phase in [MILESTONES.md](MILESTONES.md), using the [anchor bridge](BREUER_PETRUCCIONE_BRIDGE.md). |
| Understand the contribution as a whole | Follow the narrative/innovation phase, from the graph certificate to the gate and workspace resource bounds. |
| Check an exact statement or proof | Start with [Model](../science/model.md), then [Geometry](../science/geometry.md) and [Finite noise](../science/finite_noise.md). |
| Reproduce finite examples | Follow [Verification](../verification/README.md); its observed channel calculations are compared with analytic expectations. |

The milestones describe common understanding targets. The scientific pages contain the complete proofs, including details that the conceptual route does not attempt to replace.

## 1. Why noise that preserves populations can spoil a transfer

For a density matrix $\rho$, the diagonal entry $\rho_{ii}$ is the probability of obtaining basis outcome $i$. An off-diagonal entry $\rho_{ij}$ describes coherence between two basis states. Fixed diagonal dephasing leaves the populations of a stationary state unchanged while damping its coherences.

Consider one Hermitian noise operator $L$ and the convention

```math
\begin{aligned}
\dot\rho&=-i[H(t),\rho]+\epsilon\gamma\mathcal D[L](\rho),\\
\mathcal D[L](\rho)&=L\rho L-\frac12\{L^2,\rho\}.
\end{aligned}
```

Here $\epsilon\geq0$ scales the noise, $\gamma\geq0$ is a fixed reference rate, and $\hbar=1$. If $L|i\rangle=\lambda_i|i\rangle$, turning off the Hamiltonian gives

```math
\dot\rho_{ij}=-\frac{\epsilon\gamma}{2}(\lambda_i-\lambda_j)^2\rho_{ij}.
```

The difference between the two noise eigenvalues determines how quickly their coherence decays. A basis state is protected against this dephasing while it remains a basis state. A coherent transfer, however, passes through superpositions. Noise during that passage changes the final population.

The Hamiltonian budget is its spectral halfwidth,

```math
\frac{\lambda_{\max}(H)-\lambda_{\min}(H)}2\leq\Omega.
```

This controls the maximum rate at which amplitude can cross a partition of the basis. It is a bound on the total Hamiltonian, and it is invariant under adding a scalar multiple of the identity. [Precise model](../science/model.md) · [Control resources](../science/control_resources.md)

## 2. A complete three-level example

Take three basis states $|0\rangle,|1\rangle,|2\rangle$ and

```math
L=\operatorname{diag}(-1,0,1).
```

The initial state is $|0\rangle$, the desired state is $|2\rangle$, and every other final outcome counts as failure. All pulses use the same noise operator and the same control budget. Assume that each required pair can be addressed selectively.

### Direct transfer

The coupling $H=\Omega(|0\rangle\langle2|+|2\rangle\langle0|)$ gives the ideal trajectory

```math
|\psi(u)\rangle=\cos(\Omega u)|0\rangle-i\sin(\Omega u)|2\rangle,
\qquad 0\leq u\leq\tau:=\frac\pi{2\Omega}.
```

Its noise variance is $\operatorname{Var}_{\psi(u)}(L)=\sin^2(2\Omega u)$. For a fixed protocol that transfers perfectly when $\epsilon=0$, the leading error is the integrated ideal variance multiplied by $\epsilon\gamma$. Thus

```math
q_{\mathrm{direct}}
=\epsilon\gamma\int_0^\tau\sin^2(2\Omega u)\,du+O(\epsilon^2)
=\frac{\pi\epsilon\gamma}{4\Omega}+O(\epsilon^2).
```

This first-order formula and its derivation are in [Geometry, Section 1](../science/geometry.md#1-first-order-error-of-a-fixed-exact-transfer). It is a fixed-duration expansion; using it alone would not justify optimizing over arbitrarily long protocols.

### Transfer through the middle level

Instead rotate $0\to1$, then $1\to2$. The noise eigenvalue difference on each edge is $1$, compared with $2$ for the direct edge. Squaring those differences gives costs

```math
Q_{02}=4\gamma,
\qquad Q_{01}=Q_{12}=\gamma.
```

Each adjacent rotation has one quarter of the direct rotation's integrated variance. Two such rotations therefore give

```math
q_{\mathrm{middle}}
=\frac{\pi\epsilon\gamma}{8\Omega}+O(\epsilon^2),
\qquad T_{\mathrm{middle}}=2\tau.
```

The longer path halves the leading population error. The improvement comes from crossing two smaller noise-eigenvalue gaps. Its cost is an extra controlled step and an extra physical level with the appropriate noise eigenvalue.

## 3. Why this route is optimal to leading order

For several commuting Hermitian jumps, level $i$ has a weighted noise signature $(\sqrt{\gamma_a}\lambda_{ai})_a$. The squared distance between signatures is

```math
Q_{ij}=\sum_a\gamma_a(\lambda_{ai}-\lambda_{aj})^2.
```

These squared distances need not obey the triangle inequality. The quantity that controls transfer is their shortest-path closure $d_Q$. In the three-level example, $d_Q(0,2)=2\gamma$.

The lower-bound proof does not assume that controls follow graph edges. It constructs a potential from the shortest distances and decomposes that potential into binary partitions. Every admissible transition must cross those partitions. The noise fixes a minimum integrated cost for each crossing, and summing the costs yields the graph distance. A sequence of selective rotations attains that value.

The actual noisy-state argument gives, for every finite duration and every allowed control,

```math
q\geq\frac{\pi\epsilon d_Q}{16\Omega+8\pi\epsilon d_Q}.
```

Together with one fixed saturating construction, this establishes

```math
q_{\mathrm{opt}}(\epsilon)
=\frac{\pi\epsilon d_Q}{16\Omega}+O(\epsilon^2)
```

for a fixed finite model with the required pair controls. The rational finite-noise bound and the leading-order equality are different statements. The proof remains valid even when the optimizing controls and durations depend on $\epsilon$. [Geometry](../science/geometry.md) · [Finite-noise proof](../science/finite_noise.md)

The scalar two-level optimum and the squared-distance description of dephasing have established antecedents. The [related-work account](../references/RELATED_WORK.md) explains their role in the graph theorem and identifies the source-access limits of the comparison.

## 4. A good basis transfer is only part of a quantum gate

A logical qubit may be encoded in the two endpoint states. To swap them coherently and return the middle basis state, use the sequence of transpositions $(01),(12),(01)$. The phase-free selective pulse

```math
H_{ij}=\Omega(X_{ij}-P_{ij}),
\quad
X_{ij}=|i\rangle\langle j|+|j\rangle\langle i|,
\quad
P_{ij}=|i\rangle\langle i|+|j\rangle\langle j|
```

implements an exact transposition in time $\tau$. It has spectral halfwidth $\Omega$ and requires a selective common energy shift as well as the coupling. The three-pulse sequence implements logical $X$ on arbitrary endpoint superpositions in the absence of noise.

For this same three-level model, the leading gate errors are:

| Endpoint logical gate | Duration | Population error, including leakage | Logical phase weight |
|---|---:|---:|---:|
| Direct endpoint pulse | $\tau$ | $\pi\epsilon\gamma/(4\Omega)$ | $\pi\epsilon\gamma/(4\Omega)$ |
| Three-pulse middle route | $3\tau$ | $\pi\epsilon\gamma/(8\Omega)$ | $21\pi\epsilon\gamma/(32\Omega)$ |

All error entries show the first-order term; each has an $O(\epsilon^2)$ remainder at this fixed dimension. The phase weight is an unconditioned diagonal entry of the ideal-corrected logical Choi matrix in the Bell/Pauli basis. For the middle route, the population-error term comprises equal contributions $\pi\epsilon\gamma/(16\Omega)$ from leakage and from a transverse logical error. These definitions and coefficients are derived in [Constructions, Section 6](../science/constructions.md#6-logical-phase-transverse-and-leakage-weights).

The table explains why lower truth error does not by itself establish a better full quantum gate. Longer routes preserve populations more accurately while exposing superpositions to more phase noise. Conditional gates additionally require conditional access to the stated controls. The [full-channel budget](../science/constructions.md#7-a-rigorous-fixed-total-channel-error-budget) provides a finite guarantee when total channel error is also constrained.

## 5. Extra levels and a work register are different resources

The middle level above changes the noise signatures available to the controller. A noiseless auxiliary register instead repeats the existing signatures. Repetition alone cannot shorten the distance to a prescribed joint pure target.

A work register can nevertheless change the task if it may retain an error syndrome. The data can end close to its desired output while the work remains mixed. The joint pure-state target then has a larger error than the data marginal. The [workspace analysis](../science/workspace.md) quantifies this distinction using the actual rates $\kappa_a$ and their label-mixing budgets $h_a$:

```math
R=\sum_{a\in C}\frac{\kappa_a}{h_a},
\qquad
e_{\mathrm{data}}+e_{\mathrm{work}}
\geq\frac{\pi R}{4+8\pi R}.
```

Here $C$ contains the dephasing labels that must change, and $e_{\mathrm{work}}$ measures failure to return to the specified pure work state. If $e_{\mathrm{data}}=o(R)$ as $R\to0$, retained work must acquire entropy of order at least $R\ln(1/R)$. A finite coherent repetition circuit realizes that order while suppressing data population errors to second order. The circuit preserves the resource distinction; it does not remove phase noise or provide free reusable pure work.

## Continue through the project

The [milestone map](MILESTONES.md) joins these local examples into the complete account: the open-system model, graph certificate, uniform noisy-state converse, gate constructions, and the physical resources that determine their interpretation. The [Breuer–Petruccione bridge](BREUER_PETRUCCIONE_BRIDGE.md) supplies the source route and convention translations. The authoritative proofs remain under [science/](../science/), and the finite numerical checks are documented under [verification/](../verification/README.md).
