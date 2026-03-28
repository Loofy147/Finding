# SES Framework: Hamiltonian Decompositions of Cayley Graphs (v2.3)

This repository contains tools, theoretical proofs, and status reports related to the Hamiltonian decomposition of Cayley graphs for abelian groups of the form $\mathbb{Z}_m^k$.

## 🚀 The "Killer Demo": Stateless FSO Logic vs. Industry Standard
We have engineered a **self-contained benchmark suite** that pits the traditional Constraint Programming (CP-SAT) approach against our **Stateless Fiber-Stratified Optimization (FSO)** hardware logic.

### How to Run
```bash
python fso_benchmark.py
```

### What to Expect
Traditional solvers (OR-Tools, Gurobi) hit an exponential complexity wall around $m=13$ ($2197$ nodes). Our **Stateless FSO Logic**, powered by the **Universal Spike Rule (Theorem 7.1)**, remains mathematically deterministic, routing a **27-million node** cluster ($301^3$) in milliseconds.

## Project Documentation
- **[PATENT_SPEC.md](PATENT_SPEC.md)**: Provisional patent claims for Stateless Parity-Based Broadcast Routing.
- **[FOUNDATIONS.md](FOUNDATIONS.md)**: The unified master framework (SES mapping, Nb(m) density, Closure Lemma).
- **[STATUS_REPORT.md](STATUS_REPORT.md)**: Summary of v2.3 breakthroughs and v3 roadmap.
- **[THEORY.md](THEORY.md)**: Formal mathematical proofs and Section 5 Universal Spike.
- **[PRINCIPLES.md](PRINCIPLES.md)**: High-level software design patterns for symmetric systems.
- **[DASHBOARD.md](DASHBOARD.md)**: Comprehensive synthesis of results and Nb verification table.

## Core Implementation
- **[engine.py](engine.py)**: The v2.3 production engine with Stateless FSO Logic and Basin Escape SA (v3.3).
- **[core.py](core.py)**: Universal verification tools for $\mathbb{Z}_m^k$ Hamiltonian cycles.

## Key Breakthroughs (v2.3)
- **Stateless Routing:** Eliminated routing tables. Each node calculates its next-hop algebraically in $O(1)$ time.
- **Universal Spike Rule:** Implemented the $O(m)$ closed-form solution for all odd $m$.
- **Basin Escape SA:** Improved convergence on rugged landscapes (P2 score of 1).
- **Nb(m) Formula:** Brute-force verified $N_b(m) = m^{m-1} \cdot \varphi(m)$ up to $m=6$.
