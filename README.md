# SES Framework: Hamiltonian Decompositions of Cayley Graphs

This repository contains tools, theoretical proofs, and status reports related to the Hamiltonian decomposition of Cayley graphs for abelian groups of the form $\mathbb{Z}_m^k$.

## Project Documentation
- **[PROBLEMS.md](PROBLEMS.md)**: Open challenges (P1-k4, P2, P3) and current scoring records.
- **[STATUS_REPORT.md](STATUS_REPORT.md)**: A summary of the latest results, session progress, and next steps.
- **[THEORY.md](THEORY.md)**: Formal mathematical proofs, including $N_b(m)$, torsor counts, and canonical spikes.
- **[PRINCIPLES.md](PRINCIPLES.md)**: High-level principles and software design patterns derived from the mathematical theorems.
- **[DASHBOARD.md](DASHBOARD.md)**: A comprehensive synthesis of results, including $N_b$ verification and torsor predictions.

## Core Implementation
- **[engine.py](engine.py)**: Optimized SA engine (v3) with NumPy-accelerated scoring and canonical spike generators.
- **[core.py](core.py)**: Verification tools for single cycles and canonical spikes.

## Key Results
- **P1-k4 Record:** Score 74 achieved for $m=4, k=4$.
- **P2 Progress:** Score 16 achieved for $m=6, k=3$.
- **$N_b(m)$ Formula:** Derived and verified $N_b(m) = m^{m-1} \cdot \varphi(m)$.
- **Torsor Resolution:** Resolved the $648$ count for $m=3, k=3$.
- **Canonical Spike:** Verified single-cycle construction for any odd $m$.
