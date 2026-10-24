# The optimal transfer cost is a shortest-path distance

This page proves the exact leading population-error cost under the [fixed dephasing model](model.md). The argument has two components. A shortest-path potential converts arbitrary dephasing into a weighted collection of binary cuts. Each cut carries an unavoidable integrated variance. A sequence of rotations along a minimizing path attains the sum.

The scalar two-level sensitivity bound is inherited from [Lu et al.](../references/RELATED_WORK.md). The result here is its exact optimization over arbitrary coherent trajectories in a finite common-noise eigenbasis, together with a [uniform finite-noise converse](finite_noise.md).

## 1. First-order error of a fixed exact transfer

Let $`U(t)`$ solve the noiseless Schrödinger equation, with $`U(0)=I`$, and suppose that $`U(T)\lvert s\rangle=e^{i\phi}\lvert t\rangle`$. Write $`\lvert\psi(t)\rangle=U(t)\lvert s\rangle`$.

In the interaction picture, the jump operators are $`\widetilde L_a(t)=U(t)^\dagger L_aU(t)`$. For this fixed finite protocol, variation of constants gives

```math
\widetilde\rho_\epsilon(T)
=\lvert s\rangle\langle s\rvert
+\epsilon\sum_a\gamma_a
\int_0^T
\mathcal D[\widetilde L_a(t)]
(\lvert s\rangle\langle s\rvert)\,dt
+O(\epsilon^2).
```

Taking the initial-state matrix element yields

```math
q_\epsilon(H,T)
=\epsilon C[H]+O(\epsilon^2),
\qquad
C[H]
=\int_0^T\sum_a\gamma_a
\mathrm{Var}_{\psi(t)}(L_a)\,dt.
```

The remainder follows from bounded finite-dimensional generators over a fixed finite interval. It is not asserted uniform over arbitrary protocol durations. The later optimized-control theorem uses the nonperturbative converse precisely to avoid that issue.

For probabilities $`p_i=|\langle i\vert\psi\rangle|^2`$ in the common eigenbasis,

```math
\sum_a\gamma_a\mathrm{Var}_{\psi}(L_a)
=\sum_{i\lt j}p_ip_jQ_{ij}.
```

The expression depends on the noise signatures and populations of the instantaneous pure state. All phases and all Hamiltonian interference mechanisms are still allowed.

## 2. A certificate from graph distances

Fix $`d=d_Q(s,t)>0`$. Define

```math
u_i=\min\{d_Q(s,i),d\}.
```

The triangle inequality for $`d_Q`$ and the fact that truncation is a contraction give

```math
|u_i-u_j|\le d_Q(i,j)\le Q_{ij}.
```

Moreover, $`u_s=0`$ and $`u_t=d`$. List the distinct values of $`u`$ as

```math
0=v_0\lt v_1\lt\cdots\lt v_K=d,
\qquad
\delta_k=v_k-v_{k-1}.
```

Let $`D_k`$ be the diagonal Hermitian involution equal to $`+1`$ when $`u_i\le v_{k-1}`$ and $`-1`$ otherwise. Every such cut separates the initial and target states. For any pair of vertices,

```math
|u_i-u_j|
=\sum_{\{k:D_k(i)\ne D_k(j)\}}\delta_k.
```

For a pure state, $`\mathrm{Var}(D_k)=4p_{k,+}p_{k,-}`$. Therefore

```math
\sum_a\gamma_a\mathrm{Var}_{\psi}(L_a)
\ge
\sum_{k=1}^K
\frac{\delta_k}{4}\mathrm{Var}_{\psi}(D_k).
```

This is a pointwise inequality for every pure state. It does not constrain the path to visit the graph vertices in sequence.

The corresponding mixed-state statement is

```math
\sum_a\gamma_a\|[L_a,\rho]\|_2^2
\ge
\sum_{k=1}^K
\frac{\delta_k}{4}\|[D_k,\rho]\|_2^2.
```

To verify it, expand both sides entry by entry. The coefficient of $`|\rho_{ij}|^2`$ on the left is $`Q_{ij}`$; on the right it is $`|u_i-u_j|`$. This Dirichlet-form comparison is all that is needed. The difference of the corresponding formal generators is not assumed to be completely positive.

## 3. The binary crossing cost

Let $`D=P_+-P_-`$ be any Hermitian involution. Define $`f(t)=\langle\psi(t)|D|\psi(t)\rangle`$. The two components $`P_\pm\lvert\psi\rangle`$ have squared norms $`(1\pm f)/2`$. The control budget implies

```math
\|P_+H(t)P_-\|_\infty\le\Omega,
\qquad
|\dot f(t)|
\le
4\Omega\|P_+\psi(t)\|\|P_-\psi(t)\|
=
2\Omega\sqrt{1-f(t)^2}.
```

If $`D`$ separates the initial and final basis states, orient it so that $`f(0)=1`$ and $`f(T)=-1`$. For almost every $`t`$,

```math
1-f(t)^2
\ge
\frac{|\dot f(t)|}{2\Omega}\sqrt{1-f(t)^2}.
```

Integration and total variation give

```math
\int_0^T\mathrm{Var}_{\psi(t)}(D)\,dt
\ge
\frac1{2\Omega}
\int_{-1}^{1}\sqrt{1-z^2}\,dz
=
\frac{\pi}{4\Omega}.
```

Monotonicity of $`f`$ is unnecessary. Backtracking contributes additional nonnegative variation. Equivalently, apply the chain rule to a primitive of $`\sqrt{1-z^2}`$ and use the endpoint difference.

A maximal-strength two-level rotation has $`f(t)=\cos(2\Omega t)`$ for $`0\le t\le\pi/(2\Omega)`$ and saturates the bound. Lu et al.'s Rabi-frequency convention is $`\Omega_{\mathrm{Rabi}}=2\Omega`$; their scalar optimum is the same constant after this conversion.

Applying the inequality to each distance cut gives

```math
C[H]
\ge
\sum_k\frac{\delta_k}{4}\frac{\pi}{4\Omega}
=
\frac{\pi d_Q(s,t)}{16\Omega}.
```

## 4. A path that attains the lower bound

Take a minimizing simple path $`s=i_0,i_1,\ldots,i_m=t`$. During step $`k`$, couple only $`i_{k-1}`$ and $`i_k`$ with strength $`\Omega`$, for time $`\tau=\pi/(2\Omega)`$.

The state has support on those two vertices and populations $`\cos^2(\Omega t)`$ and $`\sin^2(\Omega t)`$. Its weighted variance is

```math
\sum_a\gamma_a\mathrm{Var}(L_a)
=
\frac{Q_{i_{k-1}i_k}}4\sin^2(2\Omega t).
```

The integrated contribution is $`\pi Q_{i_{k-1}i_k}/(16\Omega)`$. Summing over the path gives exactly

```math
C[H_{\mathrm{path}}]
=\frac{\pi d_Q(s,t)}{16\Omega}.
```

Each pulse respects the global halfwidth budget. The construction requires independently selectable pair couplings; it supplies the upper bound only in that control model. The [gate construction](constructions.md) removes endpoint phase conventions explicitly.

This proves that the minimum first-order sensitivity among fixed exact-transfer protocols is attained and equals the graph distance coefficient.

## 5. Optimization at nonzero noise

The fixed-protocol argument alone would not control an optimizing family whose duration or pulse shape depends on $`\epsilon`$. The [finite-noise theorem](finite_noise.md) supplies, uniformly over every candidate,

```math
q_\epsilon(H,T)
\ge
\frac{\pi\epsilon d}
{16\Omega+8\pi\epsilon d}.
```

Let $`K=\pi d/(16\Omega)`$. Taking the infimum preserves this bound,

```math
q_*(\epsilon;s,t)
\ge\frac{K\epsilon}{1+8K\epsilon}
=K\epsilon+O(\epsilon^2).
```

The fixed finite path construction gives $`q_*(\epsilon;s,t)\le K\epsilon+O(\epsilon^2)`$. These two inequalities imply

```math
q_*(\epsilon;s,t)
=K\epsilon+O(\epsilon^2).
```

There is no assumption that an optimizer exists, that an optimizer has bounded duration uniformly in $`\epsilon`$, or that an optimizing control would be exact with the noise switched off.

If $`d=0`$, all vertices on a zero-cost connecting path share the eigenvalue of every active jump with $`\gamma_a>0`$, and hence so do $`s`$ and $`t`$. Equivalently, their weighted noise signatures coincide. The dissipator vanishes on the common eigenspace of those active jumps. A pair rotation there gives $`q_*=0`$ exactly.

## 6. Two useful geometries

### One Hermitian jump

For $`L`$ with ordered distinct eigenvalues $`\lambda_0<\cdots<\lambda_m`$ between the endpoints, let $`\Delta_k=\lambda_k-\lambda_{k-1}`$. An edge crossing several ordered gaps satisfies

```math
(\lambda_j-\lambda_i)^2
=
\left(\sum_{k=i+1}^{j}\Delta_k\right)^2
\ge
\sum_{k=i+1}^{j}\Delta_k^2.
```

Any path between the endpoints must cross each intervening cut at least once. Its total cost is therefore at least $`\gamma\sum_k\Delta_k^2`$. The monotone adjacent path attains that value. Excursions outside the endpoint interval cannot lower it.

For fixed span $`\Delta`$ and $`m`$ gaps, Cauchy–Schwarz gives

```math
\sum_{k=1}^m\Delta_k^2\ge\frac{\Delta^2}{m},
```

with equality for uniform spacing. This identifies both the optimal route for a given spectrum and the best spacing when the endpoints and number of intermediate noise values are specified.

### Binary jump labels

If every $`L_a`$ is a diagonal involution, then

```math
Q_{ij}=4\sum_{\{a:\lambda_{ai}\ne\lambda_{aj}\}}\gamma_a.
```

Each coordinate mismatch indicator satisfies a triangle inequality. Their nonnegative weighted sum does too, so $`d_Q(s,t)=Q_{st}`$. A detour through additional binary signatures cannot lower the leading cost. Repeating signatures through extra degeneracy also leaves the distance unchanged.

This includes independent local Pauli-$`Z`$ noise and commuting correlated Pauli-$`Z`$ strings. It does not include changing the physical jumps during the protocol or discarding a syndrome register.

## 7. What the optimization does not imply

The graph is defined by noise rates over the full common eigenbasis, not by the adjacency matrix of an available control Hamiltonian. Hardware selection rules may prevent the saturating sequence. Replacing forbidden edges by infinite costs does not automatically give a valid converse: the Dirichlet-form comparison constrains all coherences, including coherences between states without a direct allowed coupling.

A general permutation requires one Hamiltonian to act correctly on every input. Applying the bound to each column gives valid lower bounds, but their simultaneous attainability is not established in general. The endpoint swap has a separate construction that attains both relevant column bounds.

The graph has $`N`$ explicitly specified states. Standard shortest-path algorithms compute its distances efficiently in $`N`$; this is not a claim of efficient input access or polynomial complexity in $`\log N`$ for arbitrary many-qubit descriptions.

The [physical interpretation](interpretation.md) connects these boundaries to gate design, and the [related-work account](../references/RELATED_WORK.md) distinguishes the result from earlier geometric noise descriptions and numerical control methods.
