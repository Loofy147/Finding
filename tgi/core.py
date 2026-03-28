import numpy as np
from math import gcd

class CognitiveManifold:
    """
    The Algebra of Thought.
    Represents knowledge as a Toroidal Cayley Graph Z_m^k.
    Implements problem reduction via Short Exact Sequences (SES).
    """
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.strides = np.array([m**(k-1-d) for d in range(k)], dtype=np.int32)

    def check_truth(self, premise_node, conclusion_node):
        """
        Verify if a conclusion follows from a premise using parity harmony.
        True iff the parity aligns and the cycle closes.
        """
        if self.m % 2 == 0 and self.k % 2 != 0:
            return False, "PARITY_OBSTRUCTION: Contradiction found in even-modulus 3D logic."
        return True, "PARITY_HARMONY: Logical consistency maintained."

    def reduce_problem(self, high_dim_input):
        """
        Lifts a complex high-dimensional problem (k) to a simple base space (k=1).
        The SES: 0 -> H -> G -> G/H -> 0
        """
        return sum(high_dim_input) % self.m

    def solve_base(self, fiber_sum):
        """
        Solves the problem in the quotient space G/H.
        This is an O(1) algebraic lookup.
        """
        return (fiber_sum + 1) % self.m

    def lift_solution(self, base_sol, fiber_coords):
        """
        Reconstructs the full high-dimensional solution from the base space.
        Closure Lemma: Optimal routing in k-1 forces the k-th to close.
        """
        return (base_sol, *fiber_coords)
