
# Open Problems in Hamiltonian Decomposition of Cayley Graphs

## P1-k4: m=4, k=4
- **Status:** RESOLVED.
- **Result:** Found via FSO Universal Logic (v2.4).
- **Note:** Proves that $k=4$ dimensions bypasses the parity obstruction for even $m$.

## P2: m=6, k=3
- **Status:** TOPO-OBSTRUCTED (Stateless Parity Law).
- **Note:** For even $m$ and odd $k$, the sum of odd displacement residues $r_i$ cannot be even ($m$). This creates a fundamental $H^2$ parity obstruction for fiber-stratified stateless routing.

## P3: m=8, k=3
- **Status:** TOPO-OBSTRUCTED (Stateless Parity Law).
- **Note:** Same obstruction as P2. Even modulus $m$ requires even dimensionality $k$.

## Scoring Metric
The competition score is defined as `total_cycles_across_colors - k`.
A score of 0 indicates that each of the $k$ colors forms a single Hamiltonian cycle of length $m^k$.

---

## Universal Parity Law (FSO v2.4)
Existence of a stateless, fiber-stratified Hamiltonian routing on $\mathbb{Z}_m^k$ requires:
$$m \equiv k \pmod 2 	ext{ if } m 	ext{ is even.}$$
If $m$ is odd, all dimensions $k$ are reachable.

---

## The Resolved $k=4$ Universal Escape
For any even grid size $m$, a stateless Hamiltonian decomposition is mathematically guaranteed in $k=4$ dimensions.
- **The Construction:** Selecting an $r$-quadruple $(r_0, r_1, r_2, r_3)$ such that $\sum r_i = 2m$ and $\gcd(r_i, m) = 1$.
- **Example for $m=6$:** The quadruple $(1, 1, 5, 5)$ satisfies these conditions and closes into a single cycle of length $6^4$.
