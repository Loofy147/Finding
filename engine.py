import itertools, random, math, time, numpy as np
from math import gcd

# ============================================================
# NUMPY-accelerated scoring
# ============================================================
def build_succ_np(perm_arr, m, k):
    n = m**k
    strides = np.array([m**(k-1-d) for d in range(k)], dtype=np.int32)
    succ = np.zeros((n, k), dtype=np.int32)

    for c in range(k):
        dims = perm_arr[:, c]
        for v_idx in range(n):
            dim = dims[v_idx]
            old_coord = (v_idx // strides[dim]) % m
            succ[v_idx, c] = v_idx - (old_coord * strides[dim]) + ((old_coord + 1) % m) * strides[dim]

    return succ

def score_np(succ, n, k):
    """Count (total_cycles - k) across all colors"""
    total_cycles = 0
    for c in range(k):
        visited = np.zeros(n, dtype=bool)
        for start in range(n):
            if visited[start]:
                continue
            total_cycles += 1
            v = start
            while not visited[v]:
                visited[v] = True
                v = succ[v, c]
    return total_cycles - k

# ============================================================
# FAST SA with numpy
# ============================================================
def fast_sa(m, k=3, max_iter=500_000, T_start=5.0, T_end=0.001, seed=42):
    random.seed(seed)
    np.random.seed(seed)
    n = m**k

    perms = list(itertools.permutations(range(k)))
    n_perms = len(perms)
    perms_np = np.array(perms, dtype=np.int32)

    strides = np.array([m**(k-1-d) for d in range(k)], dtype=np.int32)

    # Initialize: fiber-structured
    perm_idx = np.zeros(n, dtype=np.int32)
    for i in range(n):
        fiber_val = 0
        for d in range(1, k):
            coord_d = (i // strides[d]) % m
            fiber_val += coord_d * (m**(d-1))
        perm_idx[i] = fiber_val % n_perms

    perm_arr = perms_np[perm_idx]
    succ = build_succ_np(perm_arr, m, k)

    curr_score = score_np(succ, n, k)
    best_score = curr_score
    best_perm = perm_arr.copy()

    cooling = (T_end / T_start) ** (1.0 / max_iter)
    T = T_start

    scores = [(0, best_score)]
    t0 = time.perf_counter()

    for it in range(1, max_iter + 1):
        v_idx = random.randrange(n)
        old_pidx = perm_idx[v_idx]
        new_pidx = random.randrange(n_perms - 1)
        if new_pidx >= old_pidx:
            new_pidx += 1

        old_succ_row = succ[v_idx].copy()
        new_p = perms[new_pidx]
        for c in range(k):
            dim = new_p[c]
            old_coord = (v_idx // strides[dim]) % m
            succ[v_idx, c] = v_idx - (old_coord * strides[dim]) + ((old_coord + 1) % m) * strides[dim]

        s = score_np(succ, n, k)
        delta = s - curr_score

        if delta <= 0 or (T > 1e-9 and random.random() < math.exp(-delta / T)):
            curr_score = s
            perm_idx[v_idx] = new_pidx
            if s < best_score:
                best_score = s
                best_perm = perms_np[perm_idx].copy()
                scores.append((it, best_score))
                if best_score == 0:
                    break
        else:
            succ[v_idx] = old_succ_row

        T *= cooling

    elapsed = time.perf_counter() - t0
    return best_perm, best_score, elapsed, scores

# ============================================================
# CLOSED-FORM UNIVERSAL SPIKE RULE (Theorem 7.1 Extension)
# ============================================================
def closed_form_spike_rule(m):
    """
    Universal O(m) construction for all odd m >= 3.
    """
    identity = (0, 1, 2)
    swap12 = (0, 2, 1)
    swap01 = (1, 0, 2)
    def swap02(p): return (p[2], p[1], p[0])

    P = [identity]*(m-2) + [swap12, swap01]

    n = m**3
    strides = [m**2, m, 1]
    perm_arr = np.zeros((n, 3), dtype=np.int32)
    for i in range(m):
        for j in range(m):
            for l in range(m):
                idx = i*strides[0] + j*strides[1] + l*strides[2]
                s = (i + j + l) % m
                perm = P[s]
                if j == 0 and s != m-2:
                    perm = swap02(perm)
                perm_arr[idx] = perm

    return perm_arr

# ============================================================
# CANONICAL SPIKE GENERATOR (Theorem 7.1 Extension)
# ============================================================
def canonical_spike_rule(m, k=3):
    if m % 2 == 0:
        raise ValueError("Canonical Spike requires odd m.")

    n = m**k
    strides = [m**(k-1-d) for d in range(k)]
    perm_arr = np.zeros((n, k), dtype=np.int32)

    # Canonical r=(1, m-2, 1) and delta=1
    # We choose perms that shift the correct dimensions
    # Color 0: dim 1
    # Color 1: dim 2
    # Color 2: dim 0
    # This is an illustrative simplified construction.
    for idx in range(n):
        j = (idx // strides[1]) % m
        p = [1, 2, 0]
        if j == 0:
            p = [2, 0, 1] # Rotate
        perm_arr[idx] = p

    return perm_arr
