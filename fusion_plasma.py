import numpy as np

class FusionPlasmaRouter:
    def __init__(self, m):
        self.m = m
        self.P = [list(range(3)) for _ in range(m)]
        # Solomon's Spike (verified construction for odd m)
        self.P[m-2][1], self.P[m-2][2] = 2, 1
        self.P[m-1][0], self.P[m-1][1] = 1, 0

    def get_field_line(self, start_coords):
        curr = list(start_coords)
        visited = set()
        while tuple(curr) not in visited:
            visited.add(tuple(curr))
            s = sum(curr) % self.m
            j = curr[1]
            p = list(self.P[s])
            if j == 0 and s != self.m - 2:
                # Value-based swap: 0 <-> 2
                v0, v2 = p.index(0), p.index(2)
                p[v0], p[v2] = 2, 0
            dim = p[0]
            curr[dim] = (curr[dim] + 1) % self.m
        return len(visited)

def demo_fusion():
    print("--- Fusion Plasma Router: Magnetic Field Winding (Spike-Enabled) ---")

    for m in [3, 5, 11]:
        router = FusionPlasmaRouter(m)
        coverage = router.get_field_line((0, 0, 0))
        total = m**3
        print(f"\n[TOKAMAK M={m:<2}] Coverage: {coverage}/{total} ({coverage/total*100:.2f}%)")

if __name__ == "__main__":
    demo_fusion()
