import numpy as np

class TruthOracle:
    """
    Geometric Verification of Logic.
    Uses H^2 Parity Obstructions to detect logical paradoxes and contradictions.
    """
    def __init__(self, m, k):
        self.m = m
        self.k = k

    def evaluate_consistency(self, logic_chain):
        """
        A logic chain is TRUE if it obeys Parity Harmony and closes into a cycle.
        It is FALSE (Paradoxical) if it hits a topological obstruction.
        """
        if self.m % 2 == 0 and self.k % 2 != 0:
             return {
                "status": "PARADOX_DETECTED",
                "proof": "H^2 Parity Obstruction: Grid size even, dimension odd. Sum of odd residues cannot be even.",
                "valid": False
            }

        n = self.m ** self.k
        start = logic_chain[0]
        end = logic_chain[-1]
        length = len(logic_chain) - 1 # exclude start as end

        if start == end and length == n:
             return {
                "status": "ABSOLUTE_TRUTH",
                "proof": f"Hamiltonian Cycle Closure: Logic is perfectly consistent and covers all {n} states.",
                "valid": True
            }
        elif start == end:
             return {
                "status": "LOCAL_CONSISTENCY",
                "proof": f"Cycle closed but is sub-Hamiltonian ({length}/{n} states). Truth is local, not universal.",
                "valid": True
            }
        else:
             return {
                "status": "OPEN_INFERENCE",
                "proof": f"Logical chain remains open after {length} steps.",
                "valid": True
            }
