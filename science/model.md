# Model and results

Dephasing leaves populations unchanged when no gate is being applied. A coherent transfer between distinguishable noise eigenstates must temporarily create coherence, and dephasing during that motion can turn into population error. This account determines the smallest possible error at leading order in the noise, allowing arbitrary coherent trajectories and arbitrary durations.

The answer depends on the available noise eigenvalues. Pairwise dephasing rates define edge costs on a finite graph. Their shortest-path distance gives both a lower bound for every control and the cost of an explicit sequence of rotations. The [geometry proof](geometry.md), [finite-noise converse](finite_noise.md), and [constructions](constructions.md) establish these statements. [Control resources](control_resources.md) and [workspace](workspace.md) explain their operational boundaries.

## Dynamics and conventions

Let the retained system have finite Hilbert space $`\mathcal H=\mathbb C^N`$. Fix mutually commuting Hermitian operators $`L_a`$ and reference rates $`\gamma_a\ge0`$. Choose a common orthonormal eigenbasis,

```math
L_a\lvert i\rangle=\lambda_{ai}\lvert i\rangle.
```

With $`\hbar=1`$, the density matrix evolves according to

```math
\dot\rho_\epsilon(t)
=-i[H(t),\rho_\epsilon(t)]
+\epsilon\sum_a\gamma_a\mathcal D[L_a](\rho_\epsilon(t)),
\qquad
\mathcal D[L](\rho)=L\rho L-\frac12\{L^2,\rho\}.
```

The nonnegative number $`\epsilon`$ scales all noise rates. The operators, reference rates, finite dimension, initial state and target are held fixed when taking the weak-noise limit. The noise is Markovian and fixed in this basis. Controls are deterministic, piecewise continuous, or more generally measurable and bounded on each finite interval. No intermediate measurements, resets, discarded subsystems or conditioning on an observed noise record are included in this model.

The control resource is a bound on the instantaneous spectral halfwidth,

```math
h(H(t))
=\min_{c\in\mathbb R}\|H(t)-cI\|_\infty
=\frac{\lambda_{\max}(H(t))-\lambda_{\min}(H(t))}{2}
\le\Omega,
\qquad \Omega>0.
```

A scalar energy shift is immaterial. This is a global budget for the complete retained system, not a bound on each term in a sum of simultaneous controls. The lower bound also admits a more local formulation in terms of the Hamiltonian blocks crossing specified cuts; see [the finite-noise proof](finite_noise.md).

For the primary transfer problem, initialize $`\rho_\epsilon(0)=\lvert s\rangle\langle s\rvert`$ and target $`\lvert t\rangle`$. Define

```math
q_\epsilon(H,T)
=1-\langle t\lvert\rho_\epsilon(T)\rvert t\rangle,
\qquad
q_*(\epsilon;s,t)
=\inf_{\substack{T<\infty\\h(H(\cdot))\le\Omega}}
q_\epsilon(H,T).
```

Every outcome other than the desired basis state counts as failure. In an encoded gate this includes population outside the logical subspace. The target may differ from the noiseless endpoint of a candidate control: the infimum permits controls optimized directly at nonzero noise. It also permits families whose durations grow as $`\epsilon`$ decreases.

The initial and final *basis* states are stationary under the noise alone. The error arises during the intervening coherent motion. Reliability on arbitrary superpositions is a separate channel property, evaluated explicitly for the logical gate construction.

## The dephasing graph

Define the symmetric matrix

```math
Q_{ij}
=\sum_a\gamma_a(\lambda_{ai}-\lambda_{aj})^2.
```

The weighted noise signature of level $`i`$ is $`(\sqrt{\gamma_a}\lambda_{ai})_a`$. Equality of these signatures requires equal eigenvalues only for active jumps with $`\gamma_a>0`$; a zero-rate jump has no physical effect. References below to distinct noise signatures use this weighted definition.

When $`H=0`$, the corresponding coherence obeys

```math
\dot\rho_{ij}=-\frac{\epsilon Q_{ij}}2\rho_{ij}.
```

Thus $`\epsilon Q_{ij}/2`$ is the physical coherence-decay rate. This convention fixes all factors of two in the results. In particular, $`\kappa\mathcal D[Z](\rho)=\kappa(Z\rho Z-\rho)`$ gives coherence decay rate $`2\kappa`$.

The representation of dephasing rates through squared differences of jump eigenvalues is established background; see [Fagnola et al. in the related-work account](../references/RELATED_WORK.md). Here it serves as the input to a control optimization.

Build the complete undirected graph on the available common eigenstates, with edge weights $`Q_{ij}`$. Its shortest-path distance is

```math
d_Q(s,t)
=\min_{\substack{i_0=s,\ i_m=t\\m\ge1}}
\sum_{k=1}^{m}Q_{i_{k-1}i_k}.
```

Repeated vertices can be removed, so a finite minimizing path exists. Zero-cost vertices may be identified. The resulting distance is a pseudometric on the original basis and a metric on distinct noise signatures.

The matrix $`Q`$ itself need not satisfy the triangle inequality. An intermediate state can have a noise signature close to both endpoints, making two shorter transitions less costly than their direct connection. The distance $`d_Q`$ is the metric closure of $`Q`$.

These costs can be specified through coherence-decay rates without selecting a particular Lindblad representation. Real shifts of individual Hermitian jumps and orthogonal changes among the weighted jumps preserve $`Q`$. Adding an extra dephasing channel can only increase the distance. Adding available states while retaining the old costs can only decrease it.

## Exact claims and their domains

### Arbitrary-strength lower bound

For every finite duration, every admissible Hamiltonian and every $`\epsilon\ge0`$,

```math
q_\epsilon(H,T)
\ge
\frac{\pi\epsilon d_Q(s,t)}
{16\Omega+8\pi\epsilon d_Q(s,t)}.
```

The proof is [nonperturbative](finite_noise.md). It uses the monotonicity of global purity and a comparison with binary cuts of a shortest-path potential. It does not assume an accurate noiseless control, a fixed duration, or a perturbatively pure trajectory. The rational expression is a lower bound, not the exact optimum at finite noise.

### Sharp weak-noise optimum

When arbitrary selective two-level rotations are available within the stated global budget,

```math
q_*(\epsilon;s,t)
=
\frac{\pi d_Q(s,t)}{16\Omega}\epsilon
+O(\epsilon^2),
\qquad \epsilon\longrightarrow0.
```

The constant in the remainder may depend on the fixed finite model. The lower bound holds even for restricted hardware. Equality additionally requires access to the rotations on a minimizing path.

The optimization over noise-dependent controls is justified by the uniform finite-noise lower bound and one fixed constructive upper bound. It is not obtained by exchanging an infimum with a perturbative expansion. [The geometry account](geometry.md) gives the complete argument.

If $`d_Q(s,t)=0`$, the endpoints have identical weighted noise signatures. A rotation inside their common eigenspace for the active jumps transfers the state with exactly zero noise error.

### Logical gates and spectral refinement

A path with $`m`$ edges produces an endpoint logical swap using $`2m-1`$ selective rotations. Both logical basis inputs attain the same leading coefficient. A controlled form implements an exact ideal CNOT on a control qubit and the endpoint logical qubit, provided the specified conditional controls and diagonal shifts are available.

For one Hermitian noise operator with ordered eigenvalues between the endpoints,

```math
d_Q(s,t)
=\gamma\sum_{k}(\lambda_k-\lambda_{k-1})^2.
```

A fixed span $`\Delta`$ divided into $`m`$ uniform gaps gives $`d_Q=\gamma\Delta^2/m`$. The optimal endpoint population error then has a sharp $`1/m`$ asymptotic even at fixed noise strength. The construction takes time $`(2m-1)\pi/(2\Omega)`$, and its fixed-$`m`$ first-order phase-error coefficient grows with $`m`$. Exact probabilities, channel components and a separate fixed-noise coherence estimate are derived in [constructions](constructions.md).

### Retained and disposable workspace

The pure-transfer bound concerns the complete retained state. A clean workspace can be included by treating it as part of that state and charging the full Hamiltonian. If auxiliary states merely duplicate the data's noise signatures, they do not change the graph distance.

A protocol may instead leave a mixed syndrome in its workspace while preserving the data more accurately. [The workspace theorem](workspace.md) quantifies this possibility through a tradeoff between data error and pure-work return, and through a lower bound on residual work entropy. It does not assert a data-only error floor when auxiliary entropy may be discarded.

## Reading and verification

| Scientific question | Authoritative account |
|---|---|
| Why a shortest path gives the exact leading optimum | [Geometry and optimality](geometry.md) |
| Why arbitrarily long or noise-dependent controls cannot evade the converse | [Finite-noise bound](finite_noise.md) |
| How the optimal path becomes a logical gate | [Constructions and exact probabilities](constructions.md) |
| What selective control, phase error and additional levels cost | [Control resources](control_resources.md) |
| How syndrome storage changes the data-only conclusion | [Workspace and entropy](workspace.md) |
| What the combined results imply | [Physical interpretation](interpretation.md) |
| Which ingredients are inherited | [Related work](../references/RELATED_WORK.md) |
| Which finite calculations were reproduced | [Verification](../verification/README.md) |

The analytical proofs establish the unrestricted statements. Finite checks test normalization, exact pulse formulas, the graph certificate and logical channel bookkeeping. They do not replace the proofs or establish an experimental implementation.
