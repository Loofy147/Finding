# Learnings from FSO Development v2.3

## 1. Dimensionality Reduction
The Short Exact Sequence (SES) framework allows reducing the search space for Hamiltonian cycles on $\mathbb{Z}_m^k$ from $O((2k)!^{m^k})$ to $O((k!)^{m^2})$ by stratifying into fibers.

## 2. Closure Lemma
In a k-dimensional system, defining the routing for k-1 colors often determines the k-th color move algebraically if the fiber bijection is maintained. This is a powerful constraint for both search and deterministic generation.

## 3. Parity Obstruction
The $H^2$ parity obstruction for even $m$ and $k=3$ is a fundamental topological barrier. It requires breaking fiber-uniformity (i.e., making the mapping coordinate-dependent beyond just the fiber sum).

## 4. Basin Escape
For rugged search landscapes (like $m=6$), standard Simulated Annealing often gets trapped. Integrating a "Basin Escape" (Basin Hopping) step—where multiple random moves are taken simultaneously—significantly improves convergence.
