import itertools
from math import gcd
import numpy as np

def is_single_cycle(Q, m):
    """Checks if a transformation Q on Z_m x Z_m is a single cycle of length m^2."""
    n = m * m
    vis = set()
    cur = (0, 0)
    while cur not in vis:
        vis.add(cur)
        cur = Q[cur]
    return len(vis) == n

def make_canonical_spike_Q(m, r, delta=1, v=0, j0=0):
    """Returns the transformation Q(i,j) = (i + b(j), j + r) mod m."""
    Q = {}
    for i in range(m):
        for j in range(m):
            b = (v + delta) if j == j0 else v
            Q[(i, j)] = ((i + b) % m, (j + r) % m)
    return Q

def verify_canonical_spike(m):
    """Verifies Theorem 7.1: Canonical r=(1, m-2, 1) and delta=1 yield single cycles."""
    r_triple = (1, m - 2, 1)
    results = []
    for r in r_triple:
        Q = make_canonical_spike_Q(m, r, delta=1)
        results.append(is_single_cycle(Q, m))
    return all(results)

if __name__ == "__main__":
    for m in [3, 5, 7, 9]:
        print(f"m={m}: Canonical Spike Verified = {verify_canonical_spike(m)}")
