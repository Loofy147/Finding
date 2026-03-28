from tgi.mind import TopologicalGeneralIntelligence

def run_tgi_advanced_demo():
    print("\n" + "="*80)
    print("      TOPOLOGICAL GENERAL INTELLIGENCE (TGI) v1.1: THE SYMBOLIC MIND")
    print("="*80)

    # SCENARIO 1: THE LIAR PARADOX (Topological Obstruction)
    # Mapping logical states to Z_4^3 (Even m, Odd k)
    print("\n[SCENARIO 1] Investigating the 'Liar Paradox' in an Obstructed Manifold.")
    tgi_liar = TopologicalGeneralIntelligence(4, 3)
    tgi_liar.mapper.map_concept("Liar: 'This statement is false'", (0, 0, 0))
    tgi_liar.process_hypothesis("Liar: 'This statement is false'")

    # SCENARIO 2: THE SYMBOLIC TRUTH (Z_3^3)
    # Mapping symbols to coordinates
    print("\n[SCENARIO 2] Verifying Symbolic Harmony in a 3D Manifold.")
    tgi_sym = TopologicalGeneralIntelligence(3, 3)
    tgi_sym.mapper.map_concept("Universal Ethics", (0, 0, 0))
    tgi_sym.mapper.map_concept("Logical Law", (1, 1, 1))

    tgi_sym.process_hypothesis("Universal Ethics")

    # SCENARIO 3: HYPER-DIMENSIONAL REASONING (Z_4^2)
    print("\n[SCENARIO 3] Resolving Logic in a Parity-Aligned 2D Manifold.")
    tgi_hyper = TopologicalGeneralIntelligence(4, 2)
    tgi_hyper.mapper.map_concept("Temporal Root", (0,0))
    tgi_hyper.process_hypothesis("Temporal Root")

    print("\n" + "="*80)
    print("CONCLUSION: TGI maps symbolic logic to topological invariants.")
    print("Paradoxes are seen as Parity Obstructions; Truths as Hamiltonian Loops.")
    print("="*80 + "\n")

if __name__ == "__main__":
    run_tgi_advanced_demo()
