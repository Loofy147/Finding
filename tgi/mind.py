from .core import CognitiveManifold
from .deduction import O1InferenceEngine
from .verification import TruthOracle
from .grounding import KnowledgeGrounding

class SymbolicMapper:
    """
    Translates between symbolic concepts and manifold coordinates.
    """
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.concept_to_coord = {}
        self.coord_to_concept = {}

    def map_concept(self, concept_name, coords):
        if len(coords) != self.k:
            raise ValueError(f"Coords must have length {self.k}")
        self.concept_to_coord[concept_name] = tuple(coords)
        self.coord_to_concept[tuple(coords)] = concept_name

    def get_coord(self, concept_name):
        return self.concept_to_coord.get(concept_name)

    def get_concept(self, coord):
        return self.coord_to_concept.get(tuple(coord), f"Node{coord}")

class TopologicalGeneralIntelligence:
    """
    The primary TGI class (The Algebraic Mind).
    Orchestrates O(1) deduction and geometric truth verification.
    """
    def __init__(self, m, k, hf_token=None):
        self.m = m
        self.k = k
        self.manifold = CognitiveManifold(m, k)
        try:
            self.engine = O1InferenceEngine(m, k)
            self.obstructed = False
        except ValueError as e:
            self.engine = None
            self.obstructed = True
            self.obstruction_msg = str(e)
        self.oracle = TruthOracle(m, k)
        self.mapper = SymbolicMapper(m, k)
        self.grounding = KnowledgeGrounding(token=hf_token)

    def process_hypothesis(self, premise, verbose=True):
        """
        Processes a logical hypothesis by generating a reasoning chain
        and verifying its geometric consistency.
        """
        premise_coord = premise
        if isinstance(premise, str):
            premise_coord = self.mapper.get_coord(premise)
            if premise_coord is None:
                # Use grounding if concept is not in the mapper
                premise_coord = self.grounding.ground_to_manifold(premise, self.m, self.k)
                self.mapper.map_concept(premise, premise_coord)

        if verbose:
            print(f"\n[TGI MIND] Processing Hypothesis: Z_{self.m}^{self.k}")
            concept_name = self.mapper.get_concept(premise_coord)
            print(f" - Initial Premise: {concept_name} {premise_coord}")

        # 1. Deductive Reasoning (O(1) Jumps)
        if self.obstructed:
            report = {
                "status": "PARADOX_DETECTED",
                "proof": self.obstruction_msg,
                "valid": False
            }
            chain = [premise_coord]
        else:
            chain = self.engine.reason(premise_coord)
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

    def ground_and_process(self, natural_language_query):
        """
        Neuro-Symbolic Pipeline:
        1. LLM Extraction (Mocked)
        2. Grounding to Manifold
        3. FSO Verification
        """
        concepts = self.grounding.extract_concepts(natural_language_query)
        # We use the main concept for the premise
        premise = concepts[0]
        return self.process_hypothesis(premise)

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
