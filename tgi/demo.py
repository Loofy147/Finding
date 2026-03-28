import os
from tgi.mind import TopologicalGeneralIntelligence

def run_tgi_advanced_demo():
    print("\n" + "="*80)
    print("      TOPOLOGICAL GENERAL INTELLIGENCE (TGI) v1.2: THE NEURO-SYMBOLIC MIND")
    print("="*80)

    # Use the token from env if available
    hf_token = os.getenv("HF_TOKEN")

    # SCENARIO 1: THE LIAR PARADOX (Topological Obstruction)
    print("\n[SCENARIO 1] Investigating the 'Liar Paradox' in an Obstructed Manifold.")
    tgi_liar = TopologicalGeneralIntelligence(4, 3)
    tgi_liar.mapper.map_concept("Liar: 'This statement is false'", (0, 0, 0))
    tgi_liar.process_hypothesis("Liar: 'This statement is false'")

    # SCENARIO 2: NEURO-SYMBOLIC GROUNDING (Z_3^3)
    # Using natural language to generate a manifold premise
    print("\n[SCENARIO 2] Neuro-Symbolic Grounding of Natural Language.")
    tgi_ground = TopologicalGeneralIntelligence(3, 3, hf_token=hf_token)

    query = "All men are mortal. Socrates is a man. Therefore, Socrates is mortal."
    print(f" - Natural Language Query: '{query}'")
    tgi_ground.ground_and_process(query)

    # SCENARIO 3: HYPER-DIMENSIONAL REASONING (Z_4^2)
    print("\n[SCENARIO 3] Resolving Logic in a Parity-Aligned 2D Manifold.")
    tgi_hyper = TopologicalGeneralIntelligence(4, 2)
    tgi_hyper.mapper.map_concept("Temporal Root", (0,0))
    tgi_hyper.process_hypothesis("Temporal Root")

    print("\n" + "="*80)
    print("CONCLUSION: TGI bridges LLM probabilistic reasoning with FSO geometric truth.")
    print("Neuro-Symbolic TGI identifies Universal Truth as a closed Hamiltonian loop.")
    print("="*80 + "\n")

if __name__ == "__main__":
    run_tgi_advanced_demo()
