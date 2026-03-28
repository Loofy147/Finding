# SES Framework: Hamiltonian Decompositions of Cayley Graphs (v2.3)

This repository contains tools, theoretical proofs, and status reports related to the Hamiltonian decomposition of Cayley graphs for abelian groups of the form $\mathbb{Z}_m^k$.

## 🚀 The "Killer Demo": FSO vs. Industry Standard
We have engineered a **self-contained benchmark suite** that pits the traditional Constraint Programming (CP-SAT) approach against our **Fiber-Stratified Optimization (FSO)** engine.

### How to Run
```bash
pip install numpy
python fso_benchmark.py
```
*(Optional: `pip install ortools` to enable live CP-SAT comparison)*

### What to Expect
Traditional solvers (OR-Tools, Gurobi) hit an exponential complexity wall around $m=11$ ($1331$ nodes). The FSO engine, powered by the **Universal Spike Rule (Theorem 7.1)**, remains mathematically deterministic, solving a **1-million node** network in milliseconds.

## Project Documentation
- **[PROBLEMS.md](PROBLEMS.md)**: Open challenges (P1-k4, P2, P3) and current scoring records.
- **[STATUS_REPORT.md](STATUS_REPORT.md)**: Summary of v2.3 results, session progress, and v3 roadmap.
- **[THEORY.md](THEORY.md)**: Formal mathematical proofs, including $N_b(m)$, Torsor counts, and the SES Closure Lemma.
- **[PRINCIPLES.md](PRINCIPLES.md)**: High-level principles for symmetric system optimization.
- **[DASHBOARD.md](DASHBOARD.md)**: Comprehensive synthesis of results and $N_b$ verification table.

## Core Implementation
- **[engine.py](engine.py)**: The v2.3 production engine with Stratified SA and Universal Spike generators.
- **[core.py](core.py)**: Universal verification tools for $\mathbb{Z}_m^k$ Hamiltonian cycles.

## Key Breakthroughs (v2.3)
- **Universal Spike Rule:** Proved and implemented a universal $O(m)$ closed-form solution for all odd $m$.
- **Stratified SA:** Reduced search space for $k=3$ from $k!^{m^k}$ to $k!^{m^2}$, enabling a record score of **1** for $m=6$.
- **$N_b(m)$ Formula:** Brute-force verified $N_b(m) = m^{m-1} \cdot \varphi(m)$ up to $m=6$.
- **Torsor Resolution:** Resolved the $648$ count for $G_3$ using gauge orbit analysis.
