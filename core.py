import itertools
from math import gcd
import numpy as np

def verify_sigma(sigma, m):
    """
    Verifies if the given vertex-indexed permutation array (sigma)
    results in k Hamiltonian cycles on the Cayley graph Z_m^k.
    """
    n = sigma.shape[0]
    k = sigma.shape[1]
    strides = np.array([m**(k-1-d) for d in range(k)], dtype=np.int32)

    # Build successors
    succ = np.zeros((n, k), dtype=np.int32)
    for idx in range(n):
        coords = []
        temp = idx
        for d in reversed(range(k)):
            coords.append(temp % m)
            temp //= m
        coords.reverse()

        for c in range(k):
            dim = sigma[idx, c]
            new_coords = list(coords)
            new_coords[dim] = (new_coords[dim] + 1) % m
            new_idx = sum(new_coords[d] * strides[d] for d in range(k))
            succ[idx, c] = new_idx

    # Check for single cycles
    for c in range(k):
        vis = np.zeros(n, dtype=bool)
        curr = 0
        count = 0
        while not vis[curr]:
            vis[curr] = True
            curr = succ[curr, c]
            count += 1
        if count != n:
            return False, c, count
    return True, None, n

def table_to_sigma(table, m):
    """
    Converts a level-table (s, j) -> permutation into a vertex-indexed array.
    """
    n = m**3
    sigma = np.zeros((n, 3), dtype=np.int32)
    for i in range(m):
        for j in range(m):
            for l in range(m):
                idx = i*m**2 + j*m + l
                s = (i + j + l) % m
                sigma[idx] = table[s][j]
    return sigma
