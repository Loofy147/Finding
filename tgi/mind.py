from .core import CognitiveManifold
from .deduction import O1InferenceEngine
from .verification import TruthOracle

class TopologicalGeneralIntelligence:
    """
    The primary TGI class (The Algebraic Mind).
    Orchestrates O(1) deduction and geometric truth verification.
    """
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.manifold = CognitiveManifold(m, k)
        self.engine = O1InferenceEngine(m, k)
        self.oracle = TruthOracle(m, k)

    def process_hypothesis(self, premise, verbose=True):
        """
        Processes a logical hypothesis by generating a reasoning chain
        and verifying its geometric consistency.
        """
        if verbose:
            print(f"\n[TGI MIND] Processing Hypothesis: Z_{self.m}^{self.k}")
            print(f" - Initial Premise: {premise}")

        # 1. Deductive Reasoning (O(1) Jumps)
        chain = self.engine.reason(premise)

        # 2. Geometric Verification
        report = self.oracle.evaluate_consistency(chain)

        if verbose:
            print(f" - Reasoning Chain Length: {len(chain)}")
            print(f" - Verification Status:    {report['status']}")
            print(f" - Mathematical Proof:     {report['proof']}")

        return {
            "chain": chain,
            "report": report
        }

    def solve_np_hard_logic(self, problem_input):
        """
        Leverages SES reduction to solve complex problems in the base space.
        """
        # Lift to Base Space
        reduced = self.manifold.reduce_problem(problem_input)

        # O(1) Solution in Quotient Space
        base_sol = self.manifold.solve_base(reduced)

        # Lift to High-Dim space via Closure Lemma
        full_sol = self.manifold.lift_solution(base_sol, problem_input[1:])

        return full_sol
