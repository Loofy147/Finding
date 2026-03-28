import sys

class FSOTheoreticalReasoner:
    def __init__(self):
        pass

    def check_parity_invariants(self, m, k):
        """
        Calculates the topological feasibility based on the Parity Harmony Law.
        """
        if m % 2 == 0:
            if k % 2 == 0:
                return "SOLVABLE", "Even m requires Even k. Parity Harmony maintained."
            else:
                return "OBSTRUCTED", f"H^2 Parity Block. Even m ({m}) with Odd k ({k}) forces an impossible coprime sum."
        else:
            return "SOLVABLE", f"Odd m ({m}) allows any dimension k. Parity Harmony maintained."

    def predict(self, m, k):
        status, reason = self.check_parity_invariants(m, k)
        return {
            "m": m,
            "k": k,
            "status": status,
            "reason": reason
        }

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 fso_reasoner.py <m> <k>")
        print("Example: python3 fso_reasoner.py 4 3")
        sys.exit(1)

    m = int(sys.argv[1])
    k = int(sys.argv[2])

    reasoner = FSOTheoreticalReasoner()
    result = reasoner.predict(m, k)

    print(f"\n[FSO REASONER v1.0] Analysing Topological Manifold Z_{m}^{k}...")
    print(f" - Grid Size (m): {result['m']}")
    print(f" - Dimension (k): {result['k']}")
    print(f" - Status:       {result['status']}")
    print(f" - Reasoning:    {result['reason']}\n")
