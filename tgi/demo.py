from tgi.mind import TopologicalGeneralIntelligence

def run_tgi_oracle_demo():
    print("\n" + "="*80)
    print("      TOPOLOGICAL GENERAL INTELLIGENCE (TGI) v1.0: THE ALGEBRAIC MIND")
    print("="*80)

    # SCENARIO 1: THE PARADOXICAL HYPOTHESIS
    # m=4 (even), k=3 (odd)
    # Statistical AI might guess a conclusion, but TGI detects the H^2 obstruction.
    tgi_obs = TopologicalGeneralIntelligence(4, 3)
    tgi_obs.process_hypothesis((0,0,0))

    # SCENARIO 2: THE HARMONIOUS TRUTH
    # m=3, k=3
    # Logical chain perfectly reconstructs to the origin.
    tgi_har = TopologicalGeneralIntelligence(3, 3)
    tgi_har.process_hypothesis((0,0,0))

    # SCENARIO 3: HYPER-DIMENSIONAL REASONING
    # m=4, k=2
    # TGI proves consistency in manifolds where dimensionality and parity align.
    tgi_hyper = TopologicalGeneralIntelligence(4, 2)
    tgi_hyper.process_hypothesis((0,0))

    print("\n" + "="*80)
    print("CONCLUSION: TGI replaces probabilistic inference with geometric certainty.")
    print("The Algebraic Mind identifies Truth as a closed Hamiltonian loop.")
    print("="*80 + "\n")

if __name__ == "__main__":
    run_tgi_oracle_demo()
