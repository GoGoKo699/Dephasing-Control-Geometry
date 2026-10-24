# Controls that attain the dephasing-distance bound

This document supplies explicit state-transfer and logical-gate constructions for the model in [model.md](model.md). Their optimality follows from [geometry.md](geometry.md) and the duration-uniform converse in [finite_noise.md](finite_noise.md). The physical meaning of the control budget is discussed separately in [control_resources.md](control_resources.md).

We set $\hbar=1$, write the noise as

```math
\epsilon\sum_a\gamma_a\mathcal D[L_a],
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\},
```

and use commuting Hermitian $L_a$. In their common eigenbasis,

```math
Q_{ij}=\sum_a\gamma_a(\lambda_{ai}-\lambda_{aj})^2.
```

Thus $\epsilon Q_{ij}/2$ is the uncontrolled decay rate of $\rho_{ij}$. The symbol $d_Q$ denotes the shortest-path distance with edge costs $Q_{ij}$. All weak-noise expansions below take $\epsilon\to0$ with a fixed finite model unless another limit is stated explicitly.

## 1. A phase-free elementary transposition

For two levels $i,j$, define

```math
X_{ij}=|i\rangle\langle j|+|j\rangle\langle i|,
\qquad P_{ij}=|i\rangle\langle i|+|j\rangle\langle j|.
```

The pulse

```math
H_{ij}=\Omega(X_{ij}-P_{ij}),
\qquad \tau=\frac{\pi}{2\Omega},
\tag{1}
```

has spectrum contained in $\{-2\Omega,0\}$, so its spectral halfwidth is $\Omega$. Its propagator is exactly the transposition

```math
e^{-i\tau H_{ij}}=I-P_{ij}+X_{ij}.
\tag{2}
```

Equation (1) requires both a selective coupling and a common energy shift on the active pair. The latter is included in the spectral-width accounting. It is not assumed to be available automatically in a particular device.

If only the coupling $H_{ij}^{\mathrm c}=\Omega X_{ij}$ is available, the same pulse produces $-iX_{ij}$ on the active pair. All population-error formulas below remain unchanged. State transfer then has a known phase, and an endpoint logical swap has a common phase $(-i)^m$. That phase matters when the operation is controlled by another register. The phase-free construction avoids an uncharged correction gate.

## 2. Transfer along a shortest path

Choose a simple shortest path

```math
s=i_0,i_1,\ldots,i_m=t,
\qquad \sum_{k=1}^m Q_{i_{k-1}i_k}=d_Q(s,t).
```

Apply (1) to its edges in order. The noiseless protocol transfers $|s\rangle$ to $|t\rangle$ in

```math
T_{\mathrm{tr}}=\frac{m\pi}{2\Omega}.
```

During an edge pulse, its ideal state has probabilities $\cos^2(\Omega u)$ and $\sin^2(\Omega u)$ on the active pair. Consequently,

```math
\sum_a\gamma_a\operatorname{Var}_{\psi(u)}(L_a)
=\frac{Q_{ij}}4\sin^2(2\Omega u),
```

and the first-order error contributed by that edge is

```math
\epsilon\int_0^\tau\sum_a\gamma_a\operatorname{Var}(L_a)\,du
=\frac{\pi\epsilon Q_{ij}}{16\Omega}.
```

The full transfer therefore attains

```math
q_{s\to t}=\frac{\pi\epsilon d_Q(s,t)}{16\Omega}+O(\epsilon^2).
\tag{3}
```

The duration-uniform lower bound applies even to controls and durations that depend on $\epsilon$. Together with this fixed finite sequence, it proves the optimized asymptotic value without exchanging optimization and differentiation.

The binary two-level integrated-variance bound underlying this construction is already present in Lu et al., *Physical Review A* **88**, 033406 (2013), Eqs. 22–26, [arXiv:1305.6127](https://arxiv.org/abs/1305.6127). The metric-closure optimization and its scope are stated in [geometry.md](geometry.md).

## 3. Exact success probability at finite noise

Each active two-level principal block evolves autonomously. After removing an irrelevant scalar part of each jump on that block, its dissipator is

```math
\kappa_{ij}(Z\rho Z-\rho),
\qquad \kappa_{ij}=\frac{\epsilon Q_{ij}}4.
```

Starting in one endpoint, the population difference obeys

```math
\ddot z+2\kappa_{ij}\dot z+4\Omega^2z=0,
\qquad z(0)=1,\quad\dot z(0)=0.
```

For the pulse duration $\tau$ in (1), the exact transfer probability is

```math
p_{ij}(\epsilon)=\frac12\left[
1-e^{-\kappa_{ij}\tau}
\left(\cos(\omega_{ij}\tau)
+\frac{\kappa_{ij}}{\omega_{ij}}\sin(\omega_{ij}\tau)\right)
\right],
\quad
\omega_{ij}=\sqrt{4\Omega^2-\kappa_{ij}^2}.
\tag{4}
```

At critical damping, use $\sin(\omega\tau)/\omega\to\tau$; above critical damping, use the corresponding hyperbolic functions. This is the transfer probability at the *noiseless* $\pi$-pulse duration. It is not asserted to optimize finite-noise transfer time.

For a simple forward path, the next level has zero population before it is addressed. Positivity then makes its initial coherences zero as well. Previously abandoned populations and coherences do not enter the active principal block. Each step therefore multiplies the population that continues along the path:

```math
P_{s\to t}=\prod_{k=1}^m p_{i_{k-1}i_k},
\qquad q_{s\to t}=1-P_{s\to t}.
\tag{5}
```

This argument concerns the specified basis input. It does not turn the entire quantum channel into a classical stochastic walk. Equation (5) also avoids a perturbation expansion in the full duration.

## 4. A coherent logical $X$ with internal helper levels

Encode a qubit in $\mathcal C=\operatorname{span}\{|s\rangle,|t\rangle\}$. Apply the path transpositions forward, followed by the first $m-1$ transpositions in reverse order:

```math
(i_0i_1),(i_1i_2),\ldots,(i_{m-1}i_m),
(i_{m-2}i_{m-1}),\ldots,(i_0i_1).
\tag{6}
```

There are $2m-1$ pulses. With (1), the exact ideal unitary swaps $s,t$ and fixes every interior level. It implements logical $X$ on arbitrary superpositions in $\mathcal C$, in time

```math
T_X=\frac{(2m-1)\pi}{2\Omega}.
\tag{7}
```

For input $s$, successful population reaches $t$ during the forward sequence; subsequent pulses exclude $t$. For input $t$, the early pulses leave it unchanged, and the final forward pulse followed by the backward sequence carries it to $s$. Thus both endpoint truth errors are exactly (5), and both attain (3).

The interior levels are internal states of the same controlled system. They are unoccupied at the endpoints of the ideal logical protocol. At nonzero noise, population can remain in them; this is counted as error. No reset, postselection, or disposal of that population is hidden in the construction. The separate case of a tensor-product work register that retains entropy is addressed in [workspace.md](workspace.md).

The construction does not establish simultaneous optimality for a general permutation acting on every basis input.

### Controlled extension

With a control qubit, replace each pulse by

```math
H_{ij}^{\mathrm{ctrl}}=|1\rangle\langle1|_C\otimes H_{ij}.
\tag{8}
```

Its spectral halfwidth remains $\Omega$. The sequence (6) implements an exact controlled logical $X$ when the conditioned pair couplings and conditioned pair energy shifts are available. For target noise $I_C\otimes L_a$, the control-zero truth-table rows have zero population error; the control-one rows have error (5). Their uniform average is therefore $q_{s\to t}/2$.

An additional control dephasing channel $\epsilon\gamma_C\mathcal D[Z_C]$ also leaves these basis populations unchanged. It nevertheless degrades coherent controlled-gate action. For the single scalar target jump of span $\Delta$ considered below, a conservative full-channel bound is

```math
\frac12\|\mathcal E_{\mathrm{CX}}-\mathcal U_{\mathrm{CX}}\|_\diamond
\leq\epsilon T_X\left(\frac{\gamma\Delta^2}{4}+\gamma_C\right).
```

The control contribution is therefore at most $\epsilon\gamma_C T_X$. The detailed single-logical-qubit Pauli coefficients in Section 6 are not asserted to be the Pauli coefficients of this controlled gate. No claim of a free entangling interaction or of unchanged coherent fidelity accompanies (8).

## 5. A uniformly refined noise spectrum

For one jump $L$ with ordered eigenvalues $\lambda_0<\cdots<\lambda_m$, an edge spanning several consecutive gaps costs at least the sum of their squares. A path between the extreme eigenvalues must cross every gap. Hence

```math
d_Q(0,m)=\gamma\sum_{k=1}^m(\lambda_k-\lambda_{k-1})^2.
\tag{9}
```

For equal gaps $\delta=\Delta/m$ within a fixed span $\Delta$,

```math
d_Q(0,m)=\frac{\gamma\Delta^2}{m},
\qquad
q_{\mathrm{bad}}=\frac{\pi\epsilon\gamma\Delta^2}{16\Omega m}+O(\epsilon^2).
\tag{10}
```

Here $q_{\mathrm{bad}}$ includes wrong logical output and leakage. Refinement uses $m-1$ helper levels and the duration (7). The fixed comparison quantity is the endpoint dephasing rate $\epsilon\gamma\Delta^2/2$.

At fixed $\epsilon\gamma,\Delta,\Omega$ and $m\to\infty$, each edge has $\kappa=\epsilon\gamma\Delta^2/(4m^2)$. The exact product (5) gives

```math
q_{\mathrm{bad}}=
\frac{\pi\epsilon\gamma\Delta^2}{16\Omega m}+O(m^{-2}).
\tag{11}
```

The finite-noise converse has the same leading term. This joint dimension-and-duration limit is therefore controlled for basis errors, even though the total duration grows. It does not preserve arbitrary phase coherence at fixed noise and arbitrarily large $m$.

## 6. Logical phase, transverse, and leakage weights

Let $V:\mathbb C^2\to\mathcal H$ embed the endpoint code, and remove the ideal logical $X$ from the noisy output. The projected logical map is

```math
\mathcal F_\epsilon(A)=X\,V^\dagger\mathcal E_\epsilon(VAV^\dagger)V\,X.
```

It is completely positive and can decrease trace. Define its Choi matrix using a normalized maximally entangled input:

```math
J_\epsilon=(\mathcal F_\epsilon\otimes\mathrm{id})(|\Phi^+\rangle\langle\Phi^+|),
\qquad |\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2.
```

For $P\in\{I,X,Y,Z\}$, set

```math
p_P=\langle\Phi_P|J_\epsilon|\Phi_P\rangle,
\qquad |\Phi_P\rangle=(P\otimes I)|\Phi^+\rangle,
```

and $p_{\mathrm{leak}}=1-\operatorname{tr}J_\epsilon$. The latter is the leakage averaged over a maximally mixed logical input. These are **unconditioned** weights; they are not divided by the probability of remaining in the code. In particular, a postselected fidelity is not being substituted for the original task.

For the phase-free uniform-ladder construction, first-order symmetry makes leakage independent of the logical input, and the projected logical map is Pauli diagonal to this order. Its coefficients are

```math
\begin{aligned}
p_Z&=\frac{\pi\epsilon\gamma\Delta^2(8m^3+m-3)}{96\Omega m^2}+O(\epsilon^2),\\
p_Y&=\frac{\pi\epsilon\gamma\Delta^2}{16\Omega m^2}+O(\epsilon^2),\\
p_X&=O(\epsilon^2),\\
p_{\mathrm{leak}}&=\frac{\pi\epsilon\gamma\Delta^2(m-1)}{16\Omega m^2}+O(\epsilon^2).
\end{aligned}
\tag{12}
```

The coupling-only pulse convention instead gives the transverse weight on $X$ for even $m$, and on $Y$ for odd $m$; its magnitude and all other displayed coefficients agree. The original truth error is

```math
q_{\mathrm{bad}}=p_X+p_Y+p_{\mathrm{leak}}
```

to this order (and as an averaged identity for the corresponding Choi weights).

### Derivation of the phase coefficient

During an outer pulse the two ideal logical branches have disjoint supports. The projected interaction-picture jump has diagonal means $\mu_0,\mu_1$; its $Z$ coefficient is $(\mu_0-\mu_1)/2$. Each of the forward and backward outer pulses indexed by $r=2,\ldots,m$ contributes

```math
\frac{\epsilon\gamma\delta^2\tau}{4}
\left(r^2-r+\frac38\right)
```

to $p_Z$, using the average of $(r-\sin^2\Omega u)^2$. The central pulse has both branches in the active pair and contributes $\epsilon\gamma\delta^2\tau/8$ to each of $p_Z$ and $p_Y$. The mixed $Z,Y$ contribution integrates to zero. Each outer pulse contributes average leakage $\epsilon\gamma\delta^2\tau/16$. Summing the $2(m-1)$ outer pulses proves (12).

The first-order ratio is

```math
\frac{p_Z}{q_{\mathrm{bad}}}
=\frac{4m^2}{3}+\frac16-\frac{1}{2m}+O(\epsilon),
\tag{13}
```

at fixed $m$. Population errors decrease with refinement while the phase weight grows as $\pi\epsilon\gamma\Delta^2m/(12\Omega)$. Total gate fidelity is therefore a separate resource constraint.

## 7. A rigorous fixed total-channel-error budget

For a Hermitian jump, adding a scalar multiple of the identity does not change $\mathcal D[L]$. Center $L$ so $\|L\|=\Delta/2$. Submultiplicativity gives

```math
\|\mathcal D[L]\|_\diamond\leq2\|L\|^2=\Delta^2/2.
```

A variation-of-constants argument, using that both propagating channels have diamond norm one, then gives

```math
\frac12\|\mathcal E_\epsilon-\mathcal U\|_\diamond
\leq\frac{\epsilon\gamma\Delta^2T_X}{4}
=\frac{\pi\theta(2m-1)}8,
\qquad \theta=\frac{\epsilon\gamma\Delta^2}{\Omega}.
\tag{14}
```

This bound is on the full channel and includes leakage. For a fixed positive error budget $\eta$, choose

```math
m=\left\lfloor\frac{4\eta}{\pi\theta}\right\rfloor\geq1.
```

Then half the full-channel diamond distance is at most $\eta$, while the exact population formula yields

```math
q_{\mathrm{bad}}=
\frac{\pi^2\theta^2}{64\eta}[1+o(1)]
\quad(\theta\to0).
\tag{15}
```

The helper count is $\Theta(\eta/\theta)$, and the duration is $\Theta(\eta/(\Omega\theta))$. This is a constructive guarantee within the stated control model, not an optimal tradeoff at fixed total error. It uses the exact product, so it does not substitute $m\sim1/\epsilon$ into an uncontrolled fixed-dimension perturbation remainder. Equation (14), rather than the first-order phase coefficient alone, supplies the finite-budget guarantee.

## 8. Executable checks

The focused suite in [verification/README.md](../verification/README.md) checks three independent aspects of this construction: the multiple-jump graph example and exact product, the logical Choi derivatives for small uniform ladders, and the exact controlled-gate action with its spectral-width accounting. Dense Lindblad propagators and matrix-exponential derivatives are compared with the formulas above. These finite examples check constants and channel conventions; the general optimality claim rests on the analytic converse.
