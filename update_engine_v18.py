import re

with open('engine.py', 'r') as f:
    content = f.read()

router_replacement = """
class StatelessFSORouter:
    \"\"\"
    Generalized FSO Router supporting arbitrary dimensions k.
    Follows the Law of Dimensional Parity Harmony.
    \"\"\"
    def __init__(self, m, k=3, r_vector=None):
        self.m = m
        self.k = k
        if m % 2 == 0 and k % 2 != 0:
            raise ValueError(f"Topological Obstruction: Grid size {m} (even) requires dimension {k} to be even.")

        self.P = [list(range(k)) for _ in range(m)]

        if m % 2 != 0:
            if k == 3:
                for s in range(m):
                    if s == m - 2: self.P[s][1], self.P[s][2] = 2, 1
                    elif s == m - 1: self.P[s][0], self.P[s][1] = 1, 0
            else:
                for s in range(m):
                    if s == m - 1: self.P[s][0], self.P[s][1] = 1, 0
        else:
            for s in range(m):
                if s == m - 1: self.P[s][0], self.P[s][1] = 1, 0

    def lookup(self, coords, color=0):
        s = sum(coords) % self.m
        p = list(self.P[s])
        j = coords[1] if self.k >= 2 else 0

        # The Universal Spike: Apply symmetry break at j=0 for odd m, k=3
        if self.m % 2 != 0 and self.k == 3:
            if j == 0 and s != self.m - 2:
                v0, v2 = p.index(0), p.index(2)
                p[v0], p[v2] = 2, 0

        return p[color]

def closed_form_spike_rule(m, k=3):
    router = StatelessFSORouter(m, k)
    n = m**k
    sigma = np.zeros((n, k), dtype=np.int32)
    for idx in range(n):
        coords = []
        temp = idx
        for d in reversed(range(k)):
            coords.append(temp % m)
            temp //= m
        coords.reverse()
        sigma[idx] = [router.lookup(coords, c) for c in range(k)]
    return sigma
"""

content = re.sub(r'class StatelessFSORouter:.*?return sigma', router_replacement, content, flags=re.DOTALL)
with open('engine.py', 'w') as f:
    f.write(content)
