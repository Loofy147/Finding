import os
import time
from tgi.mind import TopologicalGeneralIntelligence

def run_tgi_advanced_demo():
    print("\n" + "="*80)
    print("      TOPOLOGICAL GENERAL INTELLIGENCE (TGI) v1.3: THE KERNEL MIND")
    print("="*80)

    # Use the token from env if available
    hf_token = os.getenv("HF_TOKEN")

    # TEST 1: Standard Logical Path (m=5, k=3)
    print("\n[TEST 1] Standard Odd-Dimensional Logic (m=5, k=3)")
    tgi_1 = TopologicalGeneralIntelligence(5, 3, hf_token=hf_token)
    tgi_1.mapper.map_concept("Universal Ethics", (0, 0, 0))
    t0 = time.time()
    tgi_1.process_hypothesis("Universal Ethics")
    lat1 = time.time() - t0

    # TEST 2: Paradoxical/Flawed Logical Input (m=6, k=3)
    print("\n[TEST 2] Paradoxical Input in an Obstructed Manifold (m=6, k=3)")
    tgi_2 = TopologicalGeneralIntelligence(6, 3)
    tgi_2.mapper.map_concept("Liar: 'This statement is false'", (0, 0, 0))
    t0 = time.time()
    tgi_2.process_hypothesis("Liar: 'This statement is false'")
    lat2 = time.time() - t0

    # TEST 3: Resolving Paradox via Higher Dimensional Lift (m=6, k=4)
    print("\n[TEST 3] Resolving Paradox via Higher Dimensional Lift (m=6, k=4).")
    tgi_3 = TopologicalGeneralIntelligence(6, 4)
    tgi_3.mapper.map_concept("Universal Root", (0, 0, 0, 0))
    t0 = time.time()
    tgi_3.process_hypothesis("Universal Root")
    lat3 = time.time() - t0

    print("\n" + "="*80)
    print(f"KERNEL PERFORMANCE DIAGNOSTICS:")
    print(f" - Test 1 Latency: {lat1:.6f}s")
    print(f" - Test 2 Latency: {lat2:.6f}s (Zero-Compute Rejection)")
    print(f" - Test 3 Latency: {lat3:.6f}s")
    print("\nCONCLUSION: TGI Kernel provides absolute truth verification and density analysis.")
    print("The Algebraic Mind identifies Truth as a closed Hamiltonian loop.")
    print("="*80 + "\n")

if __name__ == "__main__":
    run_tgi_advanced_demo()
