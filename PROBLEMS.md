# Open Problems in Hamiltonian Decomposition of Cayley Graphs

## P1-k4: m=4, k=4
- **Status:** Open.
- **Best Score:** 74 (Basin Escape SA).
- **Metric:** `total_cycles_across_colors - k`.
- **Note:** k=4 even parity is arithmetically feasible, so H² parity obstruction doesn't block it.

## P2: m=6, k=3
- **Status:** Open.
- **Best Score:** 16 (SA v3 Final).
- **Target:** Full convergence (score 0).
- **Note:** Stalls around score 16-20 due to depth-3 barrier in $Z_2 \times Z_3$.

## P3: m=8, k=3
- **Status:** Open.
- **Best Known Score:** 17.

## Scoring Metric
The competition score is defined as `total_cycles_across_colors - k`.
A score of 0 indicates that each of the $k$ colors forms a single Hamiltonian cycle of length $m^k$.
