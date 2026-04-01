import numpy as np
from engine import StatelessFSORouter

class O1InferenceEngine:
    """
    Stateless Inference via the Spike Function.
    Powered by the core SES StatelessFSORouter.
    Calculates logical jumps in O(1) time without neural memory.
    """
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.router = StatelessFSORouter(m, k)

    def infer(self, current_concept, color=0):
        """
        Performs an O(1) logical deduction jump.
        """
        dim = self.router.lookup(current_concept, color)

        # Next concept (node) in the logical chain
        next_concept = list(current_concept)
        next_concept[dim] = (next_concept[dim] + 1) % self.m
        return tuple(next_concept)

    def reason(self, premise, depth=None):
        """
        Generates a reasoning chain from a premise.
        Default depth is m^k (full cycle).
        """
        if depth is None: depth = self.m ** self.k
        chain = [tuple(premise)]
        curr = tuple(premise)
        for _ in range(depth):
            curr = self.infer(curr)
            chain.append(curr)
            if curr == tuple(premise): break
        return chain
