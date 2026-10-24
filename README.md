# Dephasing Control Geometry

**How does the spectrum of dephasing noise determine the least population error required for a controlled quantum transition?**

For a finite-dimensional system with fixed, commuting Hermitian dephasing operators and a bounded Hamiltonian spectral width, the leading optimal error is a shortest-path distance between the initial and final noise signatures. Selective two-level rotations attain the bound. A separate finite-noise inequality holds for every admissible control and every finite duration, including protocols chosen as a function of the noise strength.

The account also constructs coherent endpoint gates, charges their phase error and leakage, and distinguishes additional noise eigenvalues from a workspace that retains error syndromes.

## Main result

Work in units with $`\hbar=1`$. The dynamics and control budget are

```math
\begin{aligned}
\dot\rho&=-i[H(t),\rho]+\epsilon\sum_a\gamma_a\mathcal D[L_a](\rho),\\
\mathcal D[L](\rho)&=L\rho L-\tfrac12\{L^2,\rho\},\\
\min_{c\in\mathbb R}\|H(t)-cI\|_\infty&\leq\Omega.
\end{aligned}
```

The $`L_a`$ commute and are Hermitian. Write $`L_a|i\rangle=\lambda_{ai}|i\rangle`$ in a common eigenbasis, and assign each pair the cost

```math
\begin{aligned}
Q_{ij}&=\sum_a\gamma_a(\lambda_{ai}-\lambda_{aj})^2,\\
d_Q(s,t)&=\min_{s=i_0,\ldots,i_m=t}\sum_{k=1}^{m}Q_{i_{k-1}i_k}.
\end{aligned}
```

The uncontrolled coherence-decay rate is $`\epsilon Q_{ij}/2`$. For initial state $`|s\rangle`$ and terminal error $`q=1-\langle t|\rho(T)|t\rangle`$,

```math
q\geq\frac{\pi\epsilon d_Q(s,t)}{16\Omega+8\pi\epsilon d_Q(s,t)}.
```

For a fixed finite noise model, when selective rotations on a shortest path are available,

```math
\inf_{H,T<\infty}q
=\frac{\pi d_Q(s,t)}{16\Omega}\epsilon+O(\epsilon^2).
```

The infimum allows arbitrary many-level coherent controls and noise-dependent durations. The finite-noise expression is a lower bound; the matching equality concerns the leading weak-noise coefficient. [Model and assumptions](science/model.md) · [Geometric proof](science/geometry.md) · [Finite-noise proof](science/finite_noise.md)

## Consequences and resource costs

| Setting | Result | Resource or operational boundary |
|---|---|---|
| Several commuting dephasing channels | The metric closure of their squared noise-distance matrix gives the optimal leading transfer cost. | The complete graph describes noise costs; hardware connectivity may restrict which saturating pulses are available. |
| One scalar spectrum with $`m`$ equal gaps in fixed span $`\Delta`$ | The distance is $`\gamma\Delta^2/m`$. | The endpoint gate uses $`m-1`$ helper levels and $`2m-1`$ pulses. Its leading phase-error coefficient grows with $`m`$. |
| Binary dephasing labels | The costs already form a weighted Hamming metric. | Adding noiseless copies of the same labels cannot shorten the distance to a prescribed joint pure target. |
| Coherent work register with data error $`e=o(R)`$ as $`R\to0`$ | Suppressed data error requires imperfect pure-work return and work entropy of order at least $`R\ln(1/R)`$. | A finite coherent repetition circuit attains the entropy order while leaving syndromes in work. A data-only linear error floor would therefore be false. |

Here $`R`$ is the sum of the relevant actual dephasing rates divided by their label-mixing budgets; its precise local-control definition is in [workspace.md](science/workspace.md).

As a small example, noise signatures $`(-1,0)`$ and $`(1,0)`$ have direct squared-distance cost $`4`$. An available level with signature $`(0,1/2)`$ gives a two-edge path of cost $`5/2`$; adding a fourth level at $`(0,2)`$ gives no shorter route. The optimal leading population error is therefore 37.5% smaller than that of the direct rotation, with twice the transfer duration. The lower bound certifies the improvement against arbitrary coherent controls in this four-level example. [Interpretation and examples](science/interpretation.md)

## Learning route

The educational anchor is **Breuer and Petruccione, *The Theory of Open Quantum Systems***, Oxford University Press, 2007 paperback, ISBN 9780199213900. The learning route connects its open-system foundations to this project's control law and resource distinctions.

- [Start with the physical example](learning/README.md): a complete three-level comparison, followed by the graph theorem, phase costs and workspace interpretation.
- [Follow the 30-milestone map](learning/MILESTONES.md): 14 background/preliminaries milestones and 16 narrative/innovation milestones, progressing from local concepts to the full scientific account in each phase.
- [Use the Breuer–Petruccione bridge](learning/BREUER_PETRUCCIONE_BRIDGE.md): verified chapter pointers, notation and rate conventions, assumptions, and the steps supplied by the project.

The map is common to all readers. The source bridge supports targeted reading; the complete book is not a prerequisite for beginning the examples.

## Scientific account

Read the files in this order for a complete derivation:

1. [Model and theorem](science/model.md): noise normalization, task, control budget, quantifiers and scope.
2. [Geometry](science/geometry.md): distance certificates, binary crossings and the exact weak-noise optimum.
3. [Finite noise](science/finite_noise.md): mixed-state proof uniform in duration and noise-dependent controls.
4. [Constructions](science/constructions.md): phase-free pulses, exact finite-noise products, logical gates, leakage and phase weights.
5. [Control resources](science/control_resources.md): selective and conditional access, hardware restrictions, spectrum normalization and additional noise.
6. [Coherent workspace](science/workspace.md): return-error bound, entropy consequence and continuous-pulse correction example.
7. [Interpretation](science/interpretation.md): what spectral refinement changes and which comparisons it supports.

[Related work](references/RELATED_WORK.md) distinguishes the contribution from established two-level optimality, dephasing geometry, purity methods, relaxation-aware control and repetition filtering. It also identifies comparisons limited by source access. The [BibTeX bibliography](references/references.bib) contains the primary references.

In particular, the scalar two-level optimum is credited to [Lu et al. (2013)](https://doi.org/10.1103/PhysRevA.88.033406), and the squared-distance representation of Markovian dephasing to [Fagnola et al. (2019)](https://doi.org/10.1088/1751-8121/ab38ec). The graph optimization, its saturating construction and its duration-uniform consequences are the results developed here.

## Reproduce the finite-dimensional checks

The verification suite compares dense Lindblad propagators and matrix-exponential derivatives with the analytic predictions. From the repository root:

```sh
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The [verification guide](verification/README.md) states the examples, numerical conventions, tested dependencies, tolerances and limits. The checks detect normalization, phase, leakage and control-budget errors in representative finite systems. The analytic proofs establish the general optimality and duration-uniform claims.

## Scope

The exact optimization assumes a fixed finite model, commuting Hermitian Markovian jumps and the specified aggregate control budget. Achievability requires the stated selective pair controls; controlled gates also require conditional access. The result concerns population transfer and truth errors, including leakage. Coherent phase noise, duration, helper count and additional physical noise are accounted for separately. It does not establish a hardware advantage, an exact finite-noise optimum, or an optimal total-fidelity tradeoff under arbitrary device constraints.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT License](LICENSE).
