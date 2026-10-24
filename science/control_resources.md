# Control resources and physical interpretation

The theorem concerns a controlled finite-dimensional open system with explicitly specified noise operators. Its lower bound and its achievable upper bound use different kinds of information: the converse needs a bound on how quickly population can cross certain partitions, while the construction needs selective access to the edges of a chosen path. This document states those requirements and the resources paid by spectral refinement.

The mathematical conventions are in [model.md](model.md), the distance theorem in [geometry.md](geometry.md), and the pulse sequences and channel costs in [constructions.md](constructions.md).

## 1. What is bounded

With $\hbar=1$, the global budget is the instantaneous spectral halfwidth

```math
\omega(H)=\min_{c\in\mathbb R}\|H-cI\|
=\frac{\lambda_{\max}(H)-\lambda_{\min}(H)}2
\leq\Omega.
\tag{1}
```

Adding a scalar to the entire Hamiltonian changes only a global phase. It is therefore appropriate that this budget is invariant under that operation. It differs from a laboratory power bound and from a bound on each separately driven term.

For any projector $P_S$,

```math
\|P_SH(I-P_S)\|
=\|P_S(H-cI)(I-P_S)\|\leq\Omega.
\tag{2}
```

The proof uses (2) for the threshold cuts in its distance certificate. Hence the global halfwidth bound is sufficient, but the converse remains valid whenever those particular off-diagonal blocks obey the same bound. Large diagonal terms that commute with the noise do not speed population across a cut.

A known diagonal drift may be removed in a diagonal interaction frame. Such a transformation leaves the noise operators unchanged and preserves the norms of the cross-cut blocks. It need not preserve the global spectral-halfwidth budget, because changing frame subtracts a generally nonscalar drift. The invariant cross-cut budgets suffice for the converse; achievability must still be checked against the actual control constraint. This observation does not establish the accuracy of a rotating-wave approximation, selective resonance driving, or any other device implementation. Their errors must be charged separately.

### Pulse conventions

| Elementary control | Spectral halfwidth | Operator norm in the displayed frame | Ideal active-pair action at $\pi/(2\Omega)$ |
|---|---:|---:|---|
| $\Omega X_{ij}$ | $\Omega$ | $\Omega$ | $-iX$ |
| $\Omega(X_{ij}-P_{ij})$ | $\Omega$ | $2\Omega$ | $X$ |
| $\lvert1\rangle\langle1\rvert_C\otimes\Omega(X_{ij}-P_{ij})$ | $\Omega$ | $2\Omega$ | Controlled $X$ |

The second and third rows use a selective common energy shift on the active pair. Under a different resource constraint, such as $\|H\|\leq\Omega$ in a fixed laboratory frame, their time and amplitude accounting must be revised. They cannot simply inherit the first row's resource interpretation.

## 2. Access required for achievability

The unrestricted optimum is attained when the controller can address every edge of a shortest path in the noise-cost graph with a pulse of the form above. A physical implementation must supply:

- Resolved levels with known joint noise signatures $(\lambda_{ai})_a$, sufficient to define the relevant costs $Q_{ij}$.
- Selective coherent coupling of each chosen pair, with its actual cross-cut amplitude and duration included in $\Omega$ and $T$.
- Selective pair energy shifts for the phase-free gate construction, or explicit time and error costs for the alternative phase corrections.
- Conditional versions of those controls if a controlled logical gate is claimed.
- An error model that includes additional noise, leakage to omitted levels, imperfect selectivity, switching, and calibration errors when they are material.

The theorem grants ideal controls satisfying its mathematical assumptions. It makes no hardware-specific claim that all these operations can be realized at the same strength or in the same time on a given platform. In particular, the conditional control is an interaction resource; adding a control qubit does not provide it automatically.

The noise signatures and path are finite classical specifications. The construction has one pulse per traversed edge for transfer and $2m-1$ pulses for the endpoint gate. No QRAM, state-loading oracle, or quantum algorithm for discovering the noise graph is part of the claim.

## 3. Restricted hardware graphs

Let $G$ describe the pairs that can actually be coupled selectively. A path in $G$ with edge cost sum $C_G$ gives the achievable weak-noise coefficient

```math
\frac{\pi C_G}{16\Omega}
```

when all of its edge pulses are available at the stipulated strength. The unrestricted converse still gives $\pi d_Q(s,t)/(16\Omega)$.

If a shortest noise path is available in $G$, these values coincide. If it is unavailable, there is a gap between this upper bound and the unrestricted lower bound. The theorem does **not** identify the exact restricted-control optimum with the shortest path in $G$: simultaneous coherent use of allowed edges need not be equivalent to a sequence of complete two-level swaps. A graph-restricted optimality statement would require another converse.

Likewise, per-edge amplitudes, locality, bounded slew rates, finite carrier bandwidth, or limits on simultaneous drives define different optimization problems. Replacing $\Omega$ by a convenient local amplitude without rechecking (2) would change the claim.

## 4. What spectral refinement pays for

For a uniform scalar spectrum with span $\Delta$, the endpoint dephasing rate is $\epsilon\gamma\Delta^2/2$. At that fixed rate, adding intermediate eigenvalues changes the geometry of the noise operator. It is a physical resource beyond adding extra Hilbert-space dimension.

| Quantity | Uniform ladder with $m$ gaps |
|---|---:|
| Dimension used | $m+1$ |
| Internal helper levels | $m-1$ |
| Gap between adjacent noise eigenvalues | $\Delta/m$ |
| Logical-gate pulse count | $2m-1$ |
| Logical-gate duration | $(2m-1)\pi/(2\Omega)$ |
| Leading truth error | $\pi\epsilon\gamma\Delta^2/(16\Omega m)$ |
| Large-$m$ behavior of the fixed-$m$ first-order logical phase weight | $\pi\epsilon\gamma\Delta^2m/(12\Omega)$ |

The improvement concerns truth errors, including leakage. Arbitrary logical superpositions accumulate phase noise during the longer gate. The last table row describes a perturbative coefficient, not a phase probability that remains linear at fixed noise as $m\to\infty$. [Constructions, Section 7](constructions.md#7-a-rigorous-fixed-total-channel-error-budget) gives an explicit regime in which total channel error is bounded while truth error is reduced, with the dimension and duration charged.

Adding noise-degenerate copies of existing states does not refine the spectrum. For example, replacing each binary dephasing operator $D_a$ by $D_a\otimes I_W$ repeats its existing noise labels. Its cost remains a weighted Hamming metric, so the metric closure cannot decrease. This is distinct from allowing a work register to retain syndrome entropy; that possibility is treated in [workspace.md](workspace.md).

## 5. A finite-spin model, with its normalization explicit

A concrete mathematical ladder is a spin $J$ with noise operator

```math
L=\frac{J_z}{J}.
```

Its $2J+1$ eigenvalues run from $-1$ to $1$ in steps of $1/J$. Thus $m=2J$, $\Delta=2$, and

```math
d_Q=\frac{2\gamma}{J},
\qquad
q_{\mathrm{bad}}=\frac{\pi\epsilon\gamma}{8\Omega J}+O(\epsilon^2).
\tag{3}
```

Equation (3) is conditional on the selective adjacent-level controls specified above. A bare field proportional to $J_x$ drives many adjacent transitions and does not equal the assumed single-pair Hamiltonian. Merely identifying a spin multiplet therefore does not demonstrate the construction experimentally. A diagonal anharmonic drift can be included in a proposed control model, but the resulting selective-drive times and errors would still need to be established.

The normalization also matters. At fixed coefficient of $\mathcal D[J_z]$, the spectral span grows with $J$, the gaps remain one, and the path cost is $2\gamma J$. That model gives increasing absolute error under the same global control budget. Holding the endpoint dephasing rate fixed while increasing $J$ corresponds to changing the coupling normalization as in $J_z/J$. The two comparisons describe different physical resources.

This example is a finite Hamiltonian/noise specification, not a claim that a particular atomic, nuclear, or superconducting device supplies the required controls or scaling.

## 6. Additional noise changes the graph

All relevant commuting noise contributions belong in $Q$. As a simple diagnostic, supplement the scalar ladder with separate level-resolving jumps $|k\rangle\langle k|$, each with reference rate $\kappa$. Every pair of distinct levels then acquires an additional edge cost $2\kappa$. The fully adjacent route has cost

```math
C_{\mathrm{adj}}=\frac{\gamma\Delta^2}{m}+2\kappa m.
```

Consequently, that route ceases to improve indefinitely as levels are added. It need not remain the shortest route; the metric-closure theorem uses the full graph and can select a path that skips levels. This example illustrates why suppressing one population-error contribution is not a complete noise budget.

Noncommuting jumps, relaxation, control-dependent noise, measurements, resets, and omitted levels are not covered merely by retaining the same scalar $\gamma$. Their treatment requires an appropriate enlarged model or a separate analysis.

## 7. Scope of the claim

The main result determines an exact weak-noise population-transfer coefficient and supplies a finite-noise lower bound uniform in duration. The pulse constructions show that this coefficient is attainable in the stated access model and that endpoint logical gates can share it. They do not establish an exact finite-noise optimum, a universal advantage in total fidelity, or unrestricted optimality under a particular device's control constraints.
