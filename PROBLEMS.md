# Open Problems in Hamiltonian Decomposition of Cayley Graphs

## P1-k4: m=4, k=4
- **Status:** RESOLVED.
- **Result:** Found in 47.8M iterations.
- **Note:** Proves that $k=4$ dimensions bypasses the parity obstruction for even $m$.

## P2: m=6, k=3
- **Status:** Open (High Convergence).
- **Best Score:** 1 (Basin Escape SA v3.3).
- **Note:** Score 1 indicates a single edge-swap required to close all cycles. The $H^2$ obstruction makes this landscape extremely rugged.

## P3: m=8, k=3
- **Status:** Open.
- **Best Known Score:** 17.

## Scoring Metric
The competition score is defined as `total_cycles_across_colors - k`.
A score of 0 indicates that each of the $k$ colors forms a single Hamiltonian cycle of length $m^k$.
