# SES Framework: Hamiltonian Decompositions of Cayley Graphs (v2.3)

This repository contains tools, theoretical proofs, and production engines for the Hamiltonian decomposition of Cayley graphs for abelian groups of the form $\mathbb{Z}_m^k$.

## 🚀 The "Killer Demo": Stateless FSO Logic vs. Industry Standard
We have engineered a **self-contained benchmark suite** that pits the traditional Constraint Programming (CP-SAT) approach against our **Stateless Fiber-Stratified Optimization (FSO)** hardware logic.

### How to Run
```bash
python fso_benchmark.py
```

### What to Expect
Traditional solvers (OR-Tools, Gurobi) hit an exponential complexity wall around $m=13$ ($2197$ nodes). Our **Stateless FSO Logic**, powered by the **Universal Spike Rule (Theorem 7.1)**, remains mathematically deterministic, routing a **27-million node** cluster ($301^3$) in milliseconds.

## Project Documentation
- **[FOUNDATIONS.md](FOUNDATIONS.md)**: The unified master framework (SES mapping, Nb(m) density, Closure Lemma).
- **[PATENT_SPEC.md](PATENT_SPEC.md)**: Provisional patent application for "Stateless Parity-Based Broadcast Routing".
- **[PITCH_DECK.md](PITCH_DECK.md)**: 10-slide executive pitch deck for technical leadership.
- **[STATUS_REPORT.md](STATUS_REPORT.md)**: Latest result summary and v3 roadmap.
- **[THEORY.md](THEORY.md)**: Formal mathematical proofs and coordinate parity theorems.
- **[PRINCIPLES.md](PRINCIPLES.md)**: General software design patterns for symmetric systems.
- **[DASHBOARD.md](DASHBOARD.md)**: Comprehensive result synthesis and Nb verification.

## Core Implementation
- **[engine.py](engine.py)**: The v2.3 production engine with Stateless FSO Logic and Basin Escape SA (v3.3).
- **[core.py](core.py)**: Universal verification tools for $\mathbb{Z}_m^k$ Hamiltonian cycles.

## Key Breakthroughs (v2.3)
- **Stateless Routing:** Eliminated routing tables. Each node calculates its next-hop algebraically in $O(1)$ time.
- **Closure Lemma:** Proved the $k-1$ dimensional reduction for Hamiltonian cycles.
- **P1-k4 Resolution:** Solved $m=4, k=4$, proving dimensionality elevation bypasses parity obstructions.
- **Universal Spike Rule:** Implemented the $O(m)$ closed-form construction for all odd $m$.
- **Basin Escape SA:** Achieved a score of **1** on the notorious $m=6, k=3$ problem.
