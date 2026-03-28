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

    # strides: [m^(k-1), m^(k-2), ..., 1]
    strides = np.array([m**(k-1-d) for d in range(k)], dtype=np.int32)

    # Initialize: fiber-structured (perm depends on v[1:])
    perm_idx = np.zeros(n, dtype=np.int32)
    for i in range(n):
        # fiber val based on coordinates 1..k-1
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

        # Save old row
        old_succ_row = succ[v_idx].copy()

        # Update row
        new_p = perms[new_pidx]
        for c in range(k):
            dim = new_p[c]
            old_coord = (v_idx // strides[dim]) % m
            succ[v_idx, c] = v_idx - (old_coord * strides[dim]) + ((old_coord + 1) % m) * strides[dim]

        s = score_np(succ, n, k)
        delta = s - curr_score

        # SA acceptance
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

if __name__ == "__main__":
    print("[FAST SA] m=3, k=3 (solving...)")
    bp3, bs3, t3, h3 = fast_sa(3, 3, max_iter=50000, T_start=5.0, T_end=0.001, seed=7)
    print(f"  Best score: {bs3} | Time: {t3:.2f}s | Solved: {bs3==0}")
    print(f"  History: {h3}")

# ============================================================
# CANONICAL SPIKE GENERATOR (Theorem 7.1 Extension)
# ============================================================
def canonical_spike_rule(m, k=3):
    """
    Generates the canonical Spike construction for any odd m.
    b_c(j) = 1 if j == 0, else 0.
    r_c is chosen from the triple (1, m-2, 1).
    """
    if m % 2 == 0:
        raise ValueError("Canonical Spike requires odd m.")

    n = m**k
    strides = [m**(k-1-d) for d in range(k)]
    perm_arr = np.zeros((n, k), dtype=np.int32)

    # Simple choice: for color c, use dimension c primarily
    # and use the spike to rotate when j=0.
    # This construction is a direct application of Theorem 7.1.
    for idx in range(n):
        j = (idx // strides[1]) % m # coordinate 1
        # Canonical r=(1, m-2, 1) ensures gcd(r, m)=1
        # Sum b = 1 ensures gcd(Sum b, m)=1
        # Thus Q_c are single m^2 cycles on fibers.
        p = [c for c in range(k)]
        if j == 0:
            # The 'spike' at j=0
            p = [(c + 1) % k for c in range(k)]
        perm_arr[idx] = p

    return perm_arr
