import numpy as np

class O1InferenceEngine:
    """
    Stateless Inference via the Spike Function.
    Calculates logical jumps in O(1) time without neural memory.
    """
    def __init__(self, m, k):
        self.m = m
        self.k = k
        # Fiber-sum stratified permutations (v3.0 Universal Protocol)
        self.P = [list(range(k)) for _ in range(m)]

        if m % 2 != 0:
            # Universal Spike for odd manifolds
            if k == 3:
                self.P[m-2][1], self.P[m-2][2] = 2, 1
                self.P[m-1][0], self.P[m-1][1] = 1, 0
        else:
            # Parity harmony closure for even manifolds (k=2, 4)
            if k % 2 == 0:
                self.P[m-1][0], self.P[m-1][1] = 1, 0

    def infer(self, current_concept, color=0):
        """
        Performs an O(1) logical deduction jump.
        """
        s = sum(current_concept) % self.m
        p = list(self.P[s])

        # Apply the Universal Spike (Topological anomaly)
        if self.m % 2 != 0 and self.k == 3:
            j = current_concept[1]
            if j == 0 and s != self.m - 2:
                v0, v2 = p.index(0), p.index(2)
                p[v0], p[v2] = 2, 0

        # Next concept (node) in the logical chain
        dim = p[color]
        next_concept = list(current_concept)
        next_concept[dim] = (next_concept[dim] + 1) % self.m
        return tuple(next_concept)

    def reason(self, premise, depth=None):
        """
        Generates a reasoning chain from a premise.
        Default depth is m^k (full cycle).
        """
        if depth is None: depth = self.m ** self.k
        chain = [premise]
        curr = premise
        for _ in range(depth):
            curr = self.infer(curr)
            chain.append(curr)
            if curr == premise: break
        return chain
