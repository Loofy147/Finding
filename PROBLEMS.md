# Open Problems in Hamiltonian Decomposition of Cayley Graphs

## P1-k4: m=4, k=4
- **Status:** New record achieved.
- **Best Score:** 74 (Previous best: 84).
- **Metric:** `total_cycles_across_colors - k`.
- **Note:** k=4 even parity is arithmetically feasible (four odd shifts can sum to an even number), so H² parity obstruction doesn't block it.

## P2: m=6, k=3
- **Status:** Nearest to closing.
- **Best Known Score:** 7.
- **Current Largest Cycles:** 115 and 57 out of 216.
- **Target:** Full convergence (score 0) with 500k+ iterations.

## P3: m=8, k=3
- **Status:** Open.
- **Best Known Score:** 17.

## Scoring Metric
The competition score is defined as `total_cycles_across_colors - k`.
A score of 0 indicates that each of the $k$ colors forms a single Hamiltonian cycle of length $m^k$.
