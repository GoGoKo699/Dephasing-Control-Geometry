# A duration-uniform finite-noise lower bound

This page proves the finite-noise counterpart of the [noise-metric control law](geometry.md). The proof uses the actual noisy state throughout. It therefore applies to controls and durations chosen as functions of the noise strength, without a perturbation expansion of those controls.

## 1. Model and theorem

Let the Hilbert space be finite dimensional. Fix commuting Hermitian operators $`L_a`$, with a common orthonormal eigenbasis $`\{|i\rangle\}`$, eigenvalues $`\lambda_{ai}`$, and reference rates $`\gamma_a\geq0`$. In units with $`\hbar=1`$, let

**(F1)**

```math
\dot\rho(t)=-i[H(t),\rho(t)]
+\epsilon\sum_a\gamma_a\left(
 L_a\rho(t)L_a-\frac12\{L_a^2,\rho(t)\}
\right),
\qquad \epsilon\geq0.
```

The noise operators and rates are fixed in the laboratory frame. The symbols $`\|\cdot\|_\infty`$, $`\|\cdot\|_1`$, and $`\|\cdot\|_2`$ denote the operator, trace, and Hilbert–Schmidt norms, respectively. The controls are measurable and locally bounded after subtracting a scalar multiple of the identity. Assume the spectral half-width bound

**(F2)**

```math
\min_{c\in\mathbb R}\|H(t)-cI\|_\infty\leq\Omega,
\qquad \Omega>0,
```

for almost every t. These conditions give an absolutely continuous density matrix on every finite time interval. A scalar part of H has no effect on the master equation.

Define the reference edge weights

**(F3)**

```math
Q_{ij}=\sum_a\gamma_a(\lambda_{ai}-\lambda_{aj})^2,
```

and let $`d_Q(i,j)`$ be the shortest-path distance in the complete graph with weights Q. In this convention, free coherence $`\rho_{ij}`$ decays at rate $`\epsilon Q_{ij}/2`$. The distance is a pseudometric: vertices with identical noise labels can have zero distance.

Start from $`\rho(0)=|s\rangle\langle s|`$, choose a target eigenstate $`|t\rangle`$, and define the actual terminal population error

**(F4)**

```math
q=1-\langle t|\rho(T)|t\rangle\in[0,1].
```

**Theorem F1.** For every finite duration $`T\geq0`$ and every admissible control,

**(F5)**

```math
\boxed{
q\geq
\frac{\pi\epsilon d_Q(s,t)}
     {16\Omega+8\pi\epsilon d_Q(s,t)}.
}
```

The control need not implement the desired transfer when its noise is set to zero. The theorem is a lower bound at finite noise, not a formula for the exact finite-noise optimum.

When $`d_Q(s,t)=0`$ or $`\epsilon=0`$, the bound is zero. Otherwise its right-hand side lies strictly between zero and $`1/8`$. The rest of the proof treats $`d=d_Q(s,t)>0`$.

## 2. A family of cuts certified by the noise distance

Set

**(F6)**

```math
\phi_i=\min\{d_Q(s,i),d\}.
```

The triangle inequality for $`d_Q`$, followed by the fact that the direct edge is an admissible path, gives

**(F7)**

```math
\phi_s=0,\qquad \phi_t=d,\qquad
|\phi_i-\phi_j|\leq d_Q(i,j)\leq Q_{ij}.
```

List the distinct values of $`\phi`$ as

```math
0=v_0<v_1<\cdots<v_K=d,
\qquad \delta_k=v_k-v_{k-1}>0.
```

For each k, define a diagonal involution $`D_k`$ by

**(F8)**

```math
D_k|i\rangle=
\begin{cases}
 |i\rangle,&\phi_i\leq v_{k-1},\\
-|i\rangle,&\phi_i\geq v_k.
\end{cases}
```

There are no values of $`\phi_i`$ between these two thresholds. Every cut has $`D_k|s\rangle=|s\rangle`$ and $`D_k|t\rangle=-|t\rangle`$. Moreover,

**(F9)**

```math
|\phi_i-\phi_j|
=\sum_{k:D_k(i)\neq D_k(j)}\delta_k,
\qquad \sum_k\delta_k=d.
```

For every density matrix, an entrywise calculation now proves the Dirichlet-form comparison

**(F10)**

```math
\begin{aligned}
\sum_a\gamma_a\|[L_a,\rho]\|_2^2
&=\sum_{i,j}Q_{ij}|\rho_{ij}|^2\\
&\geq\sum_{i,j}|\phi_i-\phi_j|\,|\rho_{ij}|^2\\
&=\sum_k\frac{\delta_k}{4}\|[D_k,\rho]\|_2^2.
\end{aligned}
```

The factor $`1/4`$ appears because opposite eigenvalues of an involution differ by 2. Equation (F10) is an inequality between quadratic forms. It does not assert that the difference between the corresponding Lindblad generators is a completely positive generator.

## 3. Two block estimates for a mixed state

Let D be any Hermitian involution, with spectral projections $`P_+`$ and $`P_-`$. Relative to these two subspaces, write

**(F11)**

```math
\rho=\begin{pmatrix}A&C\\C^\dagger&B\end{pmatrix},
\qquad
H=\begin{pmatrix}H_+&V\\V^\dagger&H_-\end{pmatrix},
\qquad f=\mathrm{Tr}(D\rho).
```

Then $`A,B`$ are positive, $`\mathrm{Tr}A=(1+f)/2`$, and $`\mathrm{Tr}B=(1-f)/2`$.

### 3.1 Speed of the label expectation

Suppose that the dissipative generator leaves the expectation of D unchanged, as it does here because D and all $`L_a`$ are diagonal. The Hamiltonian contribution gives

**(F12)**

```math
|\dot f|\leq4\|V\|_\infty\|C\|_1.
```

To bound $`\|C\|_1`$, decompose $`\rho=\sum_r p_r|\psi_r\rangle\langle\psi_r|`$ and write $`|\psi_r\rangle=u_r\oplus v_r`$. Then

**(F13)**

```math
\begin{aligned}
\|C\|_1
&\leq\sum_r p_r\|u_r\|\,\|v_r\|\\
&\leq
\left(\sum_rp_r\|u_r\|^2\right)^{1/2}
\left(\sum_rp_r\|v_r\|^2\right)^{1/2}\\
&=\sqrt{\mathrm{Tr}A\mathrm{Tr}B}.
\end{aligned}
```

Condition (F2) implies $`\|V\|_\infty\leq\Omega`$, since the off-diagonal block of $`cI`$ is zero. Therefore

**(F14)**

```math
\boxed{|\dot f|\leq2\Omega\sqrt{1-f^2}}
```

almost everywhere. At $`f=\pm1`$, positivity forces C to vanish, consistently giving zero instantaneous derivative.

### 3.2 Coherence forced by high joint purity

For $`P=\mathrm{Tr}\rho^2`$, positivity and $`\mathrm{Tr}A^2\leq(\mathrm{Tr}A)^2`$ give

**(F15)**

```math
P=\mathrm{Tr}A^2+\mathrm{Tr}B^2+2\|C\|_2^2
\leq\frac{1+f^2}{2}+2\|C\|_2^2.
```

Since $`\|[D,\rho]\|_2^2=8\|C\|_2^2`$, this implies

**(F16)**

```math
\|[D,\rho]\|_2^2\geq4P-2(1+f^2).
```

The left side is nonnegative, so the positive part of the right side may always be used.

For (F1), the exact purity balance is

**(F17)**

```math
-\dot P(t)=\epsilon\sum_a\gamma_a\|[L_a,\rho(t)]\|_2^2\geq0.
```

The final overlap gives

**(F18)**

```math
P(T)\geq\langle t|\rho(T)|t\rangle^2=(1-q)^2\geq1-2q.
```

Combining monotonicity, (F16), and (F18), for every cut and every time,

**(F19)**

```math
\boxed{
\|[D_k,\rho(t)]\|_2^2
\geq2(1-4q-f_k(t)^2)_+,
}
\qquad f_k(t)=\mathrm{Tr}(D_k\rho(t)).
```

Here $`x_+=\max\{x,0\}`$. This estimate is for the noisy state, rather than for an ideal trajectory.

## 4. The scalar crossing integral

The endpoint conditions are

**(F20)**

```math
f_k(0)=1,\qquad f_k(T)\leq-1+2q.
```

The second inequality follows because the entire target population lies in the negative eigenspace of $`D_k`$.

Suppose first that $`0\leq q<1/8`$, and set $`a=\sqrt{1-4q}`$. Then

**(F21)**

```math
-1+2q\leq-a,
```

because $`1-2q\geq0`$ and $`(1-2q)^2\geq1-4q`$. Each cut trajectory must therefore cross the whole interval $`[-a,a]`$.

Define

**(F22)**

```math
g_q(u)=(1-4q-u^2)_+,
\qquad
w_q(u)=\frac{g_q(u)}{\sqrt{1-u^2}}.
```

Define $`w_q(\pm1)=0`$. For $`q=0`$, this is $`\sqrt{1-u^2}`$; for $`q>0`$, its support is away from the endpoints. Thus $`w_q`$ is continuous on $`[-1,1]`$, including the noiseless endpoint case.

Equations (F14) and (F19) yield

**(F23)**

```math
\begin{aligned}
\int_0^T\|[D_k,\rho(t)]\|_2^2\,dt
&\geq2\int_0^Tg_q(f_k(t))\,dt\\
&\geq\frac1\Omega\int_0^T
 w_q(f_k(t))|\dot f_k(t)|\,dt\\
&\geq\frac1\Omega\int_{-a}^{a}
 \frac{1-4q-u^2}{\sqrt{1-u^2}}\,du.
\end{aligned}
```

The last inequality requires no monotonicity. To see this directly, take a primitive $`W_q(u)=\int_0^u w_q(v)\,dv`$. Absolute continuity and the chain rule imply that the total variation of $`W_q(f_k(t))`$ is at least the absolute difference of its endpoint values. By (F20)–(F21), that difference contains the full integral over $`[-a,a]`$. Extra excursions cannot reduce it.

The exact scalar integral in (F23) is

**(F24)**

```math
J(q)=(1-8q)\arcsin\sqrt{1-4q}
      +2\sqrt{q(1-4q)}.
```

A simpler bound suffices. Extending the signed numerator to $`[-1,1]`$ adds only nonpositive contributions outside $`[-a,a]`$, so

**(F25)**

```math
\begin{aligned}
J(q)
&\geq\int_{-1}^{1}
 \frac{1-4q-u^2}{\sqrt{1-u^2}}\,du\\
&=\frac\pi2-4\pi q.
\end{aligned}
```

Consequently,

**(F26)**

```math
\int_0^T\|[D_k,\rho(t)]\|_2^2\,dt
\geq\frac1\Omega\left(\frac\pi2-4\pi q\right).
```

The underlying pure-state two-level crossing kernel is established prior work: Lu et al., *Physical Review A* **88**, 033406 (2013), Section IV, derive the dephasing sensitivity and the amplitude-constrained flat-$`\pi`$-pulse optimum in their Rabi-frequency convention ([Lu2013](https://arxiv.org/abs/1305.6127)). Equations (F19)–(F26) supply the mixed-state, finite-noise estimate used here; the factor conventions are specified in (F1)–(F3).

## 5. Assemble the finite-noise bound

Integrating (F17), applying the cut comparison (F10), and summing (F26) gives

**(F27)**

```math
\begin{aligned}
1-P(T)
&\geq\epsilon\sum_k\frac{\delta_k}{4}
 \int_0^T\|[D_k,\rho(t)]\|_2^2\,dt\\
&\geq\frac{\epsilon d}{4\Omega}
 \left(\frac\pi2-4\pi q\right).
\end{aligned}
```

On the other hand, (F18) gives $`1-P(T)\leq2q-q^2\leq2q`$. Put $`R=\epsilon d/(4\Omega)`$. For $`q<1/8`$,

**(F28)**

```math
2q\geq R\left(\frac\pi2-4\pi q\right),
\qquad
q\geq\frac{\pi R}{4+8\pi R}.
```

Substituting R proves (F5) in this range. If $`q\geq1/8`$, (F5) is automatic because its right-hand side is less than $`1/8`$. This completes the proof for every $`q\in[0,1]`$.

Keeping (F24) instead of (F25) provides the stronger implicit constraint $`2q\geq R J(q)`$ in the small-error range. The explicit rational form is convenient because it is uniform and immediately displays the leading coefficient.

## 6. Uniformity over noisy optimization

For a fixed finite noise model, endpoints, and control budget, define

**(F29)**

```math
q_{\mathrm{opt}}(\epsilon)
=\inf_{T,H}\left[1-\langle t|\rho_{\epsilon,H}(T)|t\rangle\right],
```

where the infimum ranges over all finite durations and admissible Hamiltonians. Both H and T may depend arbitrarily on $`\epsilon`$. Every member of this class satisfies (F5), so the infimum does too.

If the pair-selective couplings on a shortest path are available, the fixed finite protocol in [constructions](constructions.md) gives

**(F30)**

```math
q_{\mathrm{opt}}(\epsilon)
\leq\frac{\pi\epsilon d_Q(s,t)}{16\Omega}+O(\epsilon^2).
```

Expanding only the explicit lower bound, for this fixed model,

```math
\frac{\pi\epsilon d_Q}{16\Omega+8\pi\epsilon d_Q}
=\frac{\pi\epsilon d_Q}{16\Omega}+O(\epsilon^2).
```

The two inequalities imply

**(F31)**

```math
\boxed{
q_{\mathrm{opt}}(\epsilon)
=\frac{\pi\epsilon d_Q(s,t)}{16\Omega}+O(\epsilon^2).
}
```

No exchange of a derivative and an infimum is used. The constants in this remainder are for the fixed finite model; a growing-dimension or changing-spectrum limit requires its own uniform estimates. The exact path formulas provide such estimates for the ladder construction.

## 7. Weaker sufficient control assumptions and additional noise

The converse uses (F2) only to ensure

**(F32)**

```math
\|P_{k,+}H(t)P_{k,-}\|_\infty\leq\Omega
```

for the certificate cuts $`D_k`$. Thus (F32) alone suffices for (F5). Arbitrarily large terms that are block diagonal across every certificate cut are harmless to this proof. In particular, an arbitrarily large Hamiltonian diagonal in the noise eigenbasis does not change these crossing budgets. The global spectral half-width remains the specified budget for the matching unrestricted-control optimization.

The same lower bound also survives an added time-dependent GKSL generator $`\mathcal K_t`$ if, for almost every t,

**(F33)**

```math
\mathcal K_t(I)=0,
\qquad
\mathcal K_t^\dagger(D_k)=0\quad\text{for every certificate cut}.
```

Unital completely positive dynamics contracts the Hilbert–Schmidt norm of a density matrix: the Kadison inequality gives $`\Phi(\rho)^2\leq\Phi(\rho^2)`$, and trace preservation then gives $`\mathrm{Tr}\Phi(\rho)^2\leq\mathrm{Tr}\rho^2`$. Its infinitesimal form shows that $`\mathcal K_t`$ adds a nonnegative purity-loss contribution. The second condition in (F33) leaves the label speed equation unchanged. A sufficient concrete choice is a unital extra dissipator whose jump operators commute with every $`D_k`$.

Unitality alone is insufficient for this extension: an extra channel that changes a cut expectation would invalidate (F14). Likewise, discarding or resetting controlled degrees of freedom, conditioning on a measurement record, nonunital cooling, or drive-dependent changes to the specified noise require a different model. The [workspace bounds](workspace.md) state explicitly how retained coherent ancillas fit within the present assumptions.
