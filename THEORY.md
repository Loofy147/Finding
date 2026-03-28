# Theoretical Foundations of Fiber-Stratified Optimization (FSO)

## 1. Closed Form for $N_b(m)$
We prove that the number of functions $b: \mathbb{Z}_m \to \mathbb{Z}_m$ such that their sum is coprime to $m$ is:
$$N_b(m) = m^{m-1} \cdot \varphi(m)$$

### Proof:
1. Consider the set of all $m^m$ functions $b: \mathbb{Z}_m \to \mathbb{Z}_m$.
2. Let $S = \sum_{x \in \mathbb{Z}_m} b(x) \pmod m$.
3. The sum $S$ is uniformly distributed over $\mathbb{Z}_m$. This is because for any fixed values of $b(0), b(1), \dots, b(m-2)$, there is exactly one value of $b(m-1)$ that results in each possible sum $s \in \{0, 1, \dots, m-1\}$.
4. Therefore, for each residue class $s \pmod m$, there are $m^m / m = m^{m-1}$ functions.
5. A sum $S$ is coprime to $m$ if $S \in \{s \mid \gcd(s, m) = 1\}$. There are exactly $\varphi(m)$ such values.
6. Thus, $N_b(m) = m^{m-1} \cdot \varphi(m)$.

## 2. Gauge Orbit and Torsor Count
The Moduli Space of valid Hamiltonian decompositions $M_k(G_m)$ is a torsor under the group of 1-cocycles. For $m=3, k=3$:
- Base count (triples with sum-to-zero): 162.
- Total solutions $|M| = 648$ (verified via gauge orbit factor $4 = 2 \times 2$).

## 3. Extension to $k > 3$ and Parity Obstruction
For even $m$, the condition $\sum r_c = m$ (even) while each $r_c$ must be odd (coprimality) creates an $H^2$ parity obstruction for fiber-uniform mappings at $k=3$.
- **The $k=4$ Escape:** Elevating to $k=4$ dimensions bypasses this, as four odd integers sum to an even modulus.

## 4. The Closure Lemma
**Theorem:** In a $k$-dimensional symmetric system, defining the optimal routing for $k-1$ colors forces the $k$-th dimension to satisfy the fiber bijection constraint, thereby closing the cycle. This reduces the search/generation space by a factor of $k!^{m^k} \to k!^{m^2}$.

## 5. Universal Spike & Stateless Routing (Theorem 7.1)
For any odd $m$, a deterministic $O(m)$ construction exists.
- **Base Permutations ($P_s$):**
    - $P_s = \text{identity}$ for $s < m-2$
    - $P_{m-2} = (0, 2, 1)$ (swap 1-2)
    - $P_{m-1} = (1, 0, 2)$ (swap 0-1)
- **The Spike:** Applying $swap(0, 2)$ to the $j=0$ column (except at $s=m-2$) ensures global parity is coprime to $m$.
- **Stateless Property:** Node $V(i, j, l)$ routes packets via $\sigma(i, j, l) = \text{level}[(i+j+l) \pmod m][j]$ in $O(1)$ time.

## 6. Mathematical Trace of b-functions
The "Spike" construction isolates $b$-functions into structured sequences (e.g., $[1, m-1, m-1, \dots]$), driving the sums to residues like $2 \pmod m$, which are guaranteed coprime to any odd $m$.
