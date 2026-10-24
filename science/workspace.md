# Coherent workspace: return error and entropy

Coherent ancillary degrees of freedom can suppress population errors on the data while retaining error information themselves. This page distinguishes that task from returning the entire controlled system to a prescribed pure state. It proves a local-control version of the finite-noise bound, a dimension-independent work-entropy consequence, and an explicit coherent correction circuit showing why a data-only linear error floor would be false.

The repetition-code mechanism used in the example is established prior work. Benito, Velázquez-Reséndiz, and Bermudez introduce a temporary repetition encoding, transversal CNOT, decoding, and measured majority feedforward in their bias-filtering gadget ([Benito2026](https://arxiv.org/html/2606.17709v1), Section IV and Fig. 5). Repetition-based noise reshaping is also developed by Ma et al. ([Ma2025](https://doi.org/10.1103/16gx-m7kg)). The continuous-pulse coherent implementation below is specified and proved explicitly so that its role as a boundary example does not depend on assuming ideal instantaneous recovery gates.

## 1. Model with local mixing budgets

Let D be the data register and W all retained controlled workspace. Initially,

**(W1)**

```math
\rho(0)=|x\rangle\langle x|_D\otimes|w_0\rangle\langle w_0|_W.
```

The data input is a computational basis state. The workspace state is an arbitrary pure state, and its finite dimension is unrestricted. In this page, $`\kappa_a`$ denotes an **actual** noise rate: an overall weak-noise parameter, when used, is already included in it.

Let the dissipator contain commuting diagonal data involutions $`D_a`$, tensored with identity on W:

**(W2)**

```math
\dot\rho=-i[H(t),\rho]
+\sum_a\kappa_a(D_a\rho D_a-\rho)
+\mathcal K_t(\rho).
```

Here $`D_a^2=I`$. A qubit Z channel in this convention damps its coherence at rate $`2\kappa_a`$. All time-dependent generators are assumed measurable and locally bounded on the finite system, so the state is absolutely continuous on every finite interval. The bounds below charge only the specified mixing blocks, not a separate uniform bound on internal workspace dynamics.

The extra generator is required to be unital and to preserve each counted data label:

**(W3)**

```math
\mathcal K_t(I)=0,
\qquad \mathcal K_t^\dagger(D_a)=0.
```

A sufficient choice is a unital dissipator whose jump operators commute with the counted labels. Independent unital noise acting only on W satisfies these conditions, as does noiseless W. Unitality alone would not suffice if extra noise changed a counted label's expectation.

Fix a desired data output $`|b\rangle`$. Let C contain labels whose eigenvalues differ between x and b. Change their signs, if necessary, so that

**(W4)**

```math
D_a|x\rangle=|x\rangle,
\qquad D_a|b\rangle=-|b\rangle,
\qquad a\in C.
```

For $`P_{a,\pm}=(I\pm D_a)/2`$, assume the mixing-block budgets

**(W5)**

```math
\|P_{a,+}H(t)P_{a,-}\|_\infty\leq h_a,
\qquad h_a>0,
\qquad
R=\sum_{a\in C}\frac{\kappa_a}{h_a}.
```

Only these blocks are bounded. Arbitrary internal workspace Hamiltonians and arbitrary terms commuting with the counted labels do not enter the budgets. If a changed label has zero mixing budget, it cannot change expectation under (W2)–(W3), and accurate transfer is impossible. Such a case is treated directly rather than by dividing by zero in R.

The bounds are on the total mixing blocks, including all couplings to helpers. Adding many terms of individually bounded strength can increase $`h_a`$; it is not a comparison at fixed control resources unless their aggregate block remains bounded.

All workspace is retained during the interval. There is no measurement conditioning, discard, reset, or supply of fresh initialized degrees of freedom outside W. The uncontrolled Markov environment is already traced out in (W2). The Hamiltonian and duration may depend on the rates, and no upper bound on the duration is imposed.

## 2. Full pure-state return

Define the joint target error

**(W6)**

```math
q=1-\langle b,w_0|\rho(T)|b,w_0\rangle.
```

**Theorem W1.** Under (W1)–(W5),

**(W7)**

```math
\boxed{q\geq\frac{\pi R}{4+8\pi R}.}
```

This includes any number of coherent helpers. It requires return to the specified pure workspace state under the actual noisy evolution. Ideal clean return alone is a weaker requirement.

### Proof

Let $`P(t)=\mathrm{Tr}\rho(t)^2`$. Unitality gives $`P(t)\geq P(T)`$, while the target overlap gives

**(W8)**

```math
P(T)\geq(1-q)^2\geq1-2q.
```

For each changed label set $`f_a(t)=\mathrm{Tr}(D_a\rho(t))`$. The two block estimates proved in [finite_noise.md](finite_noise.md) apply with $`\Omega`$ replaced by $`h_a`$:

**(W9)**

```math
|\dot f_a|\leq2h_a\sqrt{1-f_a^2},
\qquad
\|[D_a,\rho]\|_2^2\geq2(1-4q-f_a^2)_+.
```

The endpoint conditions are $`f_a(0)=1`$ and $`f_a(T)\leq-1+2q`$. For $`q<1/8`$, the scalar crossing argument therefore gives

**(W10)**

```math
\int_0^T\|[D_a,\rho(t)]\|_2^2\,dt
\geq\frac1{h_a}\left(\frac\pi2-4\pi q\right).
```

The exact counted-channel purity balance, with any extra unital contribution retained as nonnegative loss, yields

**(W11)**

```math
\begin{aligned}
2q\geq1-P(T)
&\geq\sum_{a\in C}\kappa_a
 \int_0^T\|[D_a,\rho(t)]\|_2^2\,dt\\
&\geq R\left(\frac\pi2-4\pi q\right).
\end{aligned}
```

Rearrangement proves (W7) for $`q<1/8`$. For larger q it is automatic, since its right-hand side is at most $`1/8`$. All estimates use the actual noisy state and are uniform in the duration and allowed control. No assumption on the noiseless action of the chosen control is needed.

### Separate data and workspace errors

Let

**(W12)**

```math
e=1-\langle b|\rho_D(T)|b\rangle,
\qquad
r=1-\langle w_0|\rho_W(T)|w_0\rangle.
```

The two target projectors commute. Their complement events obey

**(W13)**

```math
q=e+r-
\mathrm{Tr}\!\left[
 (I-|b\rangle\langle b|)\otimes(I-|w_0\rangle\langle w_0|)\rho(T)
\right]
\leq e+r.
```

Consequently,

**(W14)**

```math
\boxed{e+r\geq\frac{\pi R}{4+8\pi R}.}
```

Suppressing the data population error below first order in R therefore leaves a first-order defect in pure workspace return.

For a CNOT truth-table input with control 1, the target bit changes. Counting only target dephasing with rate $`\kappa`$ and target mixing budget h gives $`R=\kappa/h`$. Averaging the resulting joint-error bound over the four uniformly distributed CNOT basis inputs gives at least one half of (W7), because two inputs require that target transition. This statement concerns joint return, not the data channel after discarding work.

## 3. Work entropy without a clean-return requirement

Now impose only the data target and let W finish in an arbitrary state. Keep e from (W12), and write

**(W15)**

```math
p=\mathrm{Tr}\rho_{DW}(T)^2,
\qquad L=1-p.
```

### 3.1 Forced joint purity loss

Monotonicity gives $`P(t)\geq1-L`$. Applying the same block calculation to each counted label gives

**(W16)**

```math
\|[D_a,\rho(t)]\|_2^2
\geq2(1-2L-f_a(t)^2)_+.
```

The data success probability implies $`f_a(T)\leq2e-1`$. Combining the speed bound in (W9) with the total-variation argument for a primitive, now over the interval $`[2e-1,1]`$, yields

**(W17)**

```math
L\geq R J(L,e),
\qquad
J(L,e)=\int_{2e-1}^{1}
\frac{(1-2L-u^2)_+}{\sqrt{1-u^2}}\,du.
```

This is valid for all $`e\in[0,1]`$, including nonmonotone label trajectories. Endpoint integrals are defined by continuity; their singularities are integrable.

Dropping the positive part weakens the bound. Define

**(W18)**

```math
B(e)=\arccos(2e-1),
\qquad
A(e)=\frac{B(e)}2+(1-2e)\sqrt{e(1-e)}.
```

These are, respectively, the integrals of $`(1-u^2)^{-1/2}`$ and $`(1-u^2)^{1/2}`$ over $`[2e-1,1]`$. Therefore

**(W19)**

```math
L\geq R[A(e)-2LB(e)],
\qquad
\boxed{L\geq L_0(R,e):=\frac{RA(e)}{1+2RB(e)}.}
```

In particular,

**(W20)**

```math
L_0(R,0)=\frac{\pi R}{2+4\pi R}.
```

The case $`e=0`$ is a conditional resource bound. It makes no assertion that exact data output is achievable at finite duration for every nonzero-noise model.

### 3.2 Transfer the purity deficit to work

Take the data-target block and the sum of the other diagonal blocks,

**(W21)**

```math
A_W=\langle b|\rho_{DW}(T)|b\rangle,
\qquad
B_W=\sum_{d\neq b}\langle d|\rho_{DW}(T)|d\rangle.
```

Both are positive, with traces $`1-e`$ and e, and $`\rho_W=A_W+B_W`$. The joint purity is at least $`\mathrm{Tr}A_W^2`$. Also,

```math
\mathrm{Tr}A_WB_W\leq(1-e)e,
\qquad
\mathrm{Tr}B_W^2\leq e^2.
```

Hence

**(W22)**

```math
\begin{aligned}
\mathrm{Tr}\rho_W^2
&=\mathrm{Tr}A_W^2+2\mathrm{Tr}A_WB_W+\mathrm{Tr}B_W^2\\
&\leq\min\{1,p+2e-e^2\}\\
&\leq1-\ell(R,e),
\end{aligned}
```

where

**(W23)**

```math
\ell(R,e)=[L_0(R,e)-2e+e^2]_+.
```

No bound on the data or workspace dimension enters this step. Data-work coherences and correlations are allowed.

### 3.3 An elementary finite entropy bound

All logarithms below are natural, and $`h_2(z)=-z\ln z-(1-z)\ln(1-z)`$. Since $`A(e)\leq B(e)`$, one has $`L_0\leq1/2`$, and therefore $`0\leq\ell\leq1/2`$.

The largest eigenvalue of $`\rho_W`$ obeys

**(W24)**

```math
\lambda_{\max}(\rho_W)
\leq\sqrt{\mathrm{Tr}\rho_W^2}
\leq\sqrt{1-\ell}=:a.
```

Here $`a\geq1/2`$. The probability vector $`(a,1-a,0,\ldots)`$ majorizes every spectrum with largest eigenvalue at most a: the first partial sum is bounded by a, and every partial sum from the second onward is at most 1. Schur concavity of entropy then gives

**(W25)**

```math
\boxed{
S(W)\geq h_2\!\left(1-\sqrt{1-\ell(R,e)}\right).
}
```

This deliberately uses an elementary entropy estimate. It is not asserted to be the sharp entropy-versus-purity frontier.

### 3.4 Weak-noise consequence

Let the rates tend to zero so that $`R\to0`$, with fixed positive mixing budgets, and suppose $`e=o(R)`$. Equations (W18)–(W23) give

**(W26)**

```math
L_0(R,e)=\frac\pi2R+o(R),
\qquad
\ell(R,e)=\frac\pi2R+o(R),
\qquad
1-\sqrt{1-\ell(R,e)}=\frac\pi4R+o(R).
```

Using $`h_2(z)=z\ln(1/z)+O(z)`$,

**(W27)**

```math
\boxed{
\liminf_{R\to0}\frac{S(W)}{R\ln(1/R)}\geq\frac\pi4.
}
```

This conclusion is independent of both dimensions and of the protocol duration. It applies even when the controller, workspace dimension, and duration vary with the noise strength, provided the assumptions and the indicated budgets continue to hold.

It is a statement about the entropy of retained work after one operation. It is not automatically additive over repeated operations starting with correlated or mixed work. It is also not a heat or work-cost theorem. Existing syndrome-entropy and reset analyses, including [CzartowskiBinder2026](https://arxiv.org/html/2609.03825v2), address thermodynamic accounting for supplied noise and recovery models. The quantity established here is the minimum workspace mixing forced by a noisy, bounded-rate label transition when data population error is suppressed.

## 4. An explicit coherent escape from a data-only linear floor

The following four-qubit circuit has data $`C,T`$, work $`a,b`$, and initial work $`|00\rangle`$. Every physical qubit is subject, throughout gates and idles, to independent dephasing

**(W28)**

```math
\gamma\sum_{j\in\{C,T,a,b\}}(Z_j\rho Z_j-\rho).
```

There are no measurements or resets. The desired data operation is $`\mathrm{CX}_{C,T}`$, and the noiseless work returns to $`|00\rangle`$.

### 4.1 Continuous two-qubit pulses

For control c and target t, define

**(W29)**

```math
G_{c,t}=|1\rangle\langle1|_c\otimes(I-X_t),
\qquad U_{c,t}(\theta)=e^{-i\theta G_{c,t}}.
```

At $`\theta=\pi/2`$, this is exactly a CNOT. Define $`V=e^{-i\pi(I-X)/4}`$, so $`V^2=X`$; at $`\theta=\pi/4`$, (W29) is controlled V. Negative $`\theta`$ implements the inverse.

Use the Hamiltonian $`H=\mathrm{sgn}(\theta)\Omega G_{c,t}`$ for duration $`|\theta|/\Omega`$. G has eigenvalues 0 and 2, so every pulse has spectral half-width $`\Omega`$. Its target-Z mixing block has norm $`\Omega`$, and its control-Z mixing block vanishes. The pulses are finite and act on at most two qubits.

Apply the following gates in the listed temporal order:

| Stage | Gates |
|---|---|
| Encode T | $`\mathrm{CX}_{T,a},\ \mathrm{CX}_{T,b}`$ |
| Transversal CNOT | $`\mathrm{CX}_{C,T},\ \mathrm{CX}_{C,a},\ \mathrm{CX}_{C,b}`$ |
| Decode | $`\mathrm{CX}_{T,a},\ \mathrm{CX}_{T,b}`$ |
| Coherent majority correction | $`V_{b,T},\ \mathrm{CX}_{a,b},\ V_{b,T}^{\dagger},\ \mathrm{CX}_{a,b},\ V_{a,T}`$ |

The last five gates implement $`\mathrm{CCX}_{a,b;T}`$. To verify this without an ideal-Toffoli assumption, fix the incoming control bits a and b. The exponent of V accumulated on T is

**(W30)**

```math
b-(b\mathbin{\oplus}a)+a=2ab.
```

Both control bits are restored. Therefore the action on T is $`V^{2ab}=X^{ab}`$, on every control basis state, and hence on their superpositions by linearity.

There are nine CNOT pulses and three controlled-half pulses. The total duration is

**(W31)**

```math
T_g=9\frac\pi{2\Omega}+3\frac\pi{4\Omega}
=\frac{21\pi}{4\Omega}.
```

### 4.2 Propagation of one dephasing jump during a pulse

A control Z commutes with (W29). For a target Z, conjugation by a remaining pulse angle r gives

**(W32)**

```math
U_{c,t}(r)Z_tU_{c,t}(r)^\dagger
=P_{0,c}Z_t+
 P_{1,c}\bigl(\cos(2r)Z_t+\sin(2r)Y_t\bigr).
```

Since $`Y_t=iX_tZ_t`$, this has the form

**(W33)**

```math
D_0+X_tD_1,
```

where $`D_0,D_1`$ are diagonal in the computational basis. Thus a single Z jump inside a pulse, propagated to that pulse's end, is a coherent sum of a diagonal error and one target-bit flip times a diagonal error. It never flips the control. Jumps on qubits outside the active pulse commute with it.

Every subsequent complete CNOT is a computational-basis permutation. It maps diagonal operators to diagonal operators under conjugation. Its action on possible bit flips can therefore be tracked independently of the diagonal amplitudes.

### 4.3 Encoding, transversal operation, and decoding

For an input basis state $`|c,t,0,0\rangle`$, the encoded target block is $`(t,t,t)`$. The transversal operation sends it to $`(y,y,y)`$, where $`y=t\oplus c`$.

A jump during encoding can create at most one flip on a or b: those are the only active targets, while T is a control. A jump during the transversal stage can create at most one flip in $`T,a,b`$. Earlier single flips are not spread by the other transversal gates because C is their common, unflipped control.

Immediately before decoding, the possible population errors are therefore the identity or one target-block flip, multiplied by diagonal amplitudes. Their exact decoded populations are:

| Error on the encoded block | Decoded $`(T,a,b)`$ | After $`\mathrm{CCX}_{a,b;T}`$ |
|---|---|---|
| I | $`(y,0,0)`$ | $`(y,0,0)`$ |
| $`X_T`$ | $`(y\oplus1,1,1)`$ | $`(y,1,1)`$ |
| $`X_a`$ | $`(y,1,0)`$ | $`(y,1,0)`$ |
| $`X_b`$ | $`(y,0,1)`$ | $`(y,0,1)`$ |

Thus each possible single flip is corrected on data, with its syndrome left in work.

If the sole jump instead occurs during decoding, there is no earlier bit error. Equation (W33) can flip only the active target a or b. The remaining decoding cannot spread this into T. The final syndrome is at most 10 or 01, so majority correction does not spuriously flip T. Diagonal parts cause no population change.

### 4.4 Jumps during the compiled correction

If the sole jump occurs in the final five-pulse block, its input syndrome is 00. Every continuous pulse of that block annihilates the syndrome-00 subspace through its control projector. The two intermediate CNOTs also have control a equal to zero. Hence the no-jump trajectory throughout this block retains $`a=b=0`$.

A Z jump on a or b acts as a scalar on this subspace. A Z jump on C or T is diagonal and leaves the syndrome unchanged. It cannot activate a subsequent correction pulse. Thus a single jump anywhere during this finite-duration compiled correction also leaves the data populations correct.

### 4.5 The argument applies to quantum inputs

For every zero- or one-jump operator, the preceding cases show that every computational input x is sent to its correct CNOT output, with an input-dependent workspace vector and amplitude. Taking a workspace matrix element therefore gives a data Kraus operator of the form

**(W34)**

```math
K_w=\sum_x a_w(x)|\mathrm{CX}(x)\rangle\langle x|.
```

After composing with the inverse ideal data CNOT,

**(W35)**

```math
U_{\mathrm{CX}}^\dagger K_w
=\sum_xa_w(x)|x\rangle\langle x|
```

is diagonal. This proves absence of first-order non-Z error in the data channel for arbitrary superpositions. It does not remove phase noise: the diagonal Kraus amplitudes can dephase the data.

### 4.6 Exact bound from two or more jumps

The jump operators are $`\sqrt\gamma Z_j`$, so $`L_j^\dagger L_j=\gamma I`$. The no-jump effective Hamiltonian is the applied Hamiltonian plus the scalar imaginary term $`-2i\gamma I`$. Accordingly, the total jump intensity is the state-independent constant $`4\gamma`$, and the number of jumps during the gadget is Poisson with mean $`4\gamma T_g`$.

Zero- and one-jump trajectories have correct data populations. Every other trajectory contributes at most its probability. For every computational data input,

**(W36)**

```math
\boxed{
e_{\mathrm{data}}\leq
\Pr(N\geq2)
=1-e^{-4\gamma T_g}(1+4\gamma T_g)
=O\!\left((\gamma/\Omega)^2\right).
}
```

The jump representation is mathematical bookkeeping for the unconditional channel; no monitoring of the environment is used by the circuit.

One can equivalently define the non-Z weight of the data error channel by the diagonal entries $`\chi_{PP}`$ of its Pauli process matrix. With the convention $`\mathcal N(\rho)=\sum_{P,Q}\chi_{PQ}P\rho Q^\dagger`$ and $`\mathrm{Tr}(P^\dagger Q)=d_D\delta_{PQ}`$,

**(W37)**

```math
\frac1{d_D}\sum_x
\left[1-\langle x|\mathcal N(|x\rangle\langle x|)|x\rangle\right]
=\sum_{P\notin\{I,Z\}^{\otimes2}}\chi_{PP}.
```

This follows by orthogonality of the diagonal Pauli characters when summing over x. Therefore (W36) also bounds this non-Z weight, without applying a Pauli twirl.

## 5. Consistency with the return and entropy bounds

For control-1 basis inputs of the gadget, the data target flips, its counted dephasing rate is $`\gamma`$, and its mixing-block budget is $`\Omega`$. Thus $`R=\gamma/\Omega`$. The other three dephasing channels are unital and preserve this counted target label, so they are permitted extra noise in (W3).

Equation (W36) gives $`e=O(R^2)`$, while (W14) forces a workspace-return defect of order R. The explicit syndrome table shows where that defect resides. This is why the joint-return theorem cannot be replaced by a data-only first-order lower bound.

The same example has matching entropy scaling, up to constants. Its zero-jump work output is exactly $`|00\rangle`$, and the probability of at least one jump is

**(W38)**

```math
p_J=1-e^{-4\gamma T_g}=O(R).
```

Hence $`1-\langle00|\rho_W|00\rangle\leq p_J`$. Dephasing $`\rho_W`$ in a basis containing $`|00\rangle`$ cannot lower entropy, and the largest entropy with a fixed total probability p on the other three basis states is $`h_2(p)+p\ln3`$. This function is increasing for $`p\leq3/4`$. For sufficiently small R,

**(W39)**

```math
S(W)\leq h_2(p_J)+p_J\ln3=O(R\ln(1/R)).
```

Combining with (W27), the accurate-data regime is realized with work entropy of order $`R\ln(1/R)`$. This establishes the order of the entropy requirement, not attainability of the lower-bound coefficient $`\pi/4`$. The circuit uses ordinary repetition correction, finite coherent pulses, and retained syndrome work; measurement and reset would supply a different resource model.

For bibliography and the relation to earlier correction and control results, see [Related work](../references/RELATED_WORK.md).
