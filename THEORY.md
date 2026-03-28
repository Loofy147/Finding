# Theoretical Foundations of Hamiltonian Decomposition in Cayley Graphs

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

### Verification:
- $m=3$: $N_b(3) = 3^{3-1} \cdot \varphi(3) = 9 \cdot 2 = 18$.
- $m=5$: $N_b(5) = 5^4 \cdot \varphi(5) = 625 \cdot 4 = 2500$.

## 2. Gauge Orbit and Torsor Count
The count of 648 for the $m=3, k=3$ case can be understood through the gauge orbit decomposition:
- Base count (triples with $b_0 + b_1 + b_2 = 0$): 162.
- Multiplied by 2 for base-shift directions.
- Multiplied by 2 for the choice of the "fixed last" color.
Total: $162 \times 2 \times 2 = 648$.

## 3. Extension to $k > 3$
For $k$ colors, the base-shift balance condition is:
$$\sum_{c=0}^{k-1} r_c \equiv 0 \pmod m$$
This ensures the combined action over all dimensions is balanced, preventing premature cycle closure.

## 4. Canonical Spike and Single m²-Cycles (Theorem 7.1)
The construction $Q_c(i,j) = (i + b_c(j), j + r_c) \pmod m$ is a single $m^2$-cycle on $\mathbb{Z}_m \times \mathbb{Z}_m$ if:
- $\gcd(r_c, m) = 1$
- $\gcd(\sum b_c, m) = 1$

### Proof of the Canonical Spike:
For the canonical choice $b_c(j) = \delta$ if $j=j_0$, else $0$:
1. $\sum b_c = (m-1) \cdot 0 + 1 \cdot \delta = \delta$.
2. The condition $\gcd(\sum b_c, m) = 1$ becomes $\gcd(\delta, m) = 1$.
3. For any odd $m$, $\delta = 1$ always works.
4. The canonical $r$-triple $(1, m-2, 1)$ satisfies $\gcd(r_c, m) = 1$ for all odd $m$.
5. Thus, the construction always produces a single $m^2$-cycle.
