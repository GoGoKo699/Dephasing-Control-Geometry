# Physical interpretation

The central result assigns a control cost to a transition between noise eigenstates. It answers a concrete question: when coherent control moves population, how much of otherwise harmless dephasing must become an error in that population?

A basis state is unaffected by diagonal dephasing. During a gate, a superposition of states with different noise signatures exposes the population transfer to noise. The [shortest-path theorem](geometry.md) determines the minimum integrated exposure under a global bound on coherent control. The [finite-noise proof](finite_noise.md) shows that its sharp leading coefficient survives optimization over noise-dependent controls and durations.

## What can be inferred from measured dephasing rates

Suppose the common dephasing basis and all pairwise coherence-decay rates are known. Twice those reference rates form the matrix $Q$. The distance $d_Q(s,t)$ gives the leading minimum error for transferring $\lvert s\rangle$ to $\lvert t\rangle$.

There are two distinct tests for a proposed improvement.

First, ask whether a new physical level creates a route whose sum of edge costs is smaller than the existing distance. If it does, the unrestricted optimum improves. Second, ask whether the device can realize the required pair rotations within the same control budget. This determines whether the explicit upper bound is attainable.

A path is a control prescription as well as a lower-bound certificate. The certificate constrains arbitrary coherent trajectories, including trajectories with support on many levels. One protocol using successive pairwise superpositions attains the converse, so an optimum can be chosen in that form. The proof does not require every optimal protocol to have that form.

## A small multilevel example

Take four joint noise signatures,

```math
v_s=(-1,0),\qquad
v_t=(1,0),\qquad
v_b=(0,1/2),\qquad
v_e=(0,2),
```

where the two coordinates already include the square roots of the reference rates. Then $Q_{ij}=\|v_i-v_j\|^2$.

The direct endpoint edge has cost $4$. The route through $b$ has cost $5/4+5/4=5/2$, while the extra state $e$ gives no improvement. The optimal leading transfer error is therefore reduced by 37.5% relative to the direct endpoint rotation at the same $\Omega$.

This example uses two independent dephasing observables and is not restricted to points on a line. The [verification suite](../verification/README.md) compares exact Lindblad propagation, the analytic pulse-product formula, and the predicted leading coefficient. The same route can be used in the forward/back construction to swap the two logical endpoint states.

## Spectral refinement and the resources it consumes

For one dephasing operator, the shortest path visits intermediate noise eigenvalues in their sorted order. Splitting a fixed span $\Delta$ into $m$ equal gaps gives

```math
d_Q=\frac{\gamma\Delta^2}{m}.
```

For the endpoint logical swap, the leading undesirable population error is

```math
q_{\rm bad}
=\frac{\pi\epsilon\gamma\Delta^2}{16\Omega m}
+O(\epsilon^2)
```

at fixed $m$. It includes leakage as well as a wrong logical bit. The sequence uses $m+1$ levels and time $(2m-1)\pi/(2\Omega)$. Its phase-error weight grows as $\epsilon\gamma\Delta^2m/\Omega$ in the perturbative regime.

The exact transfer probabilities establish the $1/m$ population-error asymptotic even when the dimension increases at fixed noise strength. The conclusion concerns basis populations. At fixed positive noise, this ladder sequence loses logical phase coherence as $m\to\infty$; a separate [coherence estimate](constructions.md#coherence-at-fixed-noise-as-the-ladder-grows) establishes this limit without extrapolating a first-order probability.

This is relevant to noise-biased computation because different error components can have different correction costs. It does not establish that a larger value of $m$ improves total gate fidelity or a fault-tolerant threshold. Such a conclusion requires an explicit code, circuit, phase-error budget and implementation model.

### Fixed span and a fixed physical ladder

The normalization of the noise operator is a physical resource.

For $L=N=\operatorname{diag}(0,1,\ldots,m)$ with fixed coupling to the noise, the endpoint span grows with $m$. The direct transition has distance $\gamma m^2$, while adjacent routing has distance $\gamma m$. Routing improves the comparison by a factor of $m$, but the absolute error coefficient still grows.

For a fixed endpoint span divided into more intermediate values, the distance instead decreases as $1/m$. These are different families of devices. The latter comparison holds the logical endpoint coherence-decay rate fixed while increasing the available spectral resolution.

A three-level system already illustrates the distinction without an asymptotic extrapolation. For $L=\operatorname{diag}(-1,0,1)$, a direct transfer between the outer states costs $4\gamma$, while routing through the middle state costs $2\gamma$. The same physical noise operator is used in both protocols. Whether the direct and adjacent transitions are equally controllable is an additional assumption, addressed in [control resources](control_resources.md).

## Why binary dephasing behaves differently

For any collection of diagonal binary jumps, the edge costs form a weighted Hamming metric,

```math
Q_{ij}=4\sum_{\{a:\lambda_{ai}\ne\lambda_{aj}\}}\gamma_a.
```

There is no shorter route through existing binary signatures. Increasing their multiplicity by adding a noiseless workspace also leaves these distances unchanged.

The distinction concerns the physical noise signatures, not Hilbert-space dimension alone. More states can help when they supply intermediate signatures. Extra states with repeated signatures do not supply that resource.

For ordinary qubits this gives a quantitative counterpart to the known obstruction to exact continuous bias-preserving CNOT implementations. The exact obstruction is due to [Guillaud and Mirrahimi](../references/RELATED_WORK.md). The present bound specifies an unavoidable error scale under a control budget and states the role of auxiliary physical levels.

## How correction changes the conclusion

Error correction can preserve the data while transferring uncertainty into auxiliary systems. If those systems are discarded or reset, the final data is not the complete retained state to which the pure-transfer theorem applies.

The [workspace account](workspace.md) makes this boundary explicit. Under fixed binary data dephasing, a protocol starting with pure workspace must pay through data error, imperfect pure-work return, or residual work entropy. A coherent repetition-code construction suppresses leading data bit errors by storing a syndrome; it is a constructive escape from a data-only floor.

This entropy statement is not an additive heat charge for every gate. Correlations, reuse, compression, reset conditions and access to side information matter in a larger circuit. The bound concerns the stated initialized protocol and its final work register. A thermodynamic work cost would require a specified reset model.

## Scope of the resulting design principle

The graph distance is an exact leading-order optimum for the stated dephasing and control model. It distinguishes three resources:

| Resource | Effect in this model |
|---|---|
| Faster coherent mixing | Lowers the unavoidable error scale through $1/\Omega$ |
| Intermediate physical noise signatures | Can shorten the dephasing distance |
| Retaining or discarding a syndrome | Can protect data while leaving uncertainty in workspace |

Known diagonal drifts can be treated in a compatible interaction frame, and the lower proof can be expressed through the mixing blocks across the certificate cuts. Finite bandwidth, restricted selection rules, control-induced noise, noncommuting jumps and nonunital relaxation require their own resource model. The written converse remains useful wherever its assumptions hold; saturation should be claimed only when its required controls are actually available.

The [related-work account](../references/RELATED_WORK.md) separates the inherited scalar inequality, noise geometry and noise-aware control methods from the exact metric-closure optimization. The [verification account](../verification/README.md) specifies the finite calculations supporting the examples.
