import itertools, random, math, time, numpy as np
from math import gcd

# ============================================================
# NUMPY-accelerated scoring
# ============================================================
def build_succ_np(perm_arr, m, k):
    n = m**k
    strides = np.array([m**(k-1-d) for d in range(k)], dtype=np.int32)
    succ = np.zeros((n, k), dtype=np.int32)
    coords = np.zeros((n, k), dtype=np.int32)
    for i in range(n):
        temp = i
        for d in reversed(range(k)):
            coords[i, d] = temp % m
            temp //= m
    for v_idx in range(n):
        perm = perm_arr[v_idx]
        for c in range(k):
            dim = perm[c]
            old_coord = coords[v_idx, dim]
            succ[v_idx, c] = v_idx - (old_coord * strides[dim]) + ((old_coord + 1) % m) * strides[dim]
    return succ

def score_np(succ, n, k):
    total_cycles = 0
    for c in range(k):
        visited = np.zeros(n, dtype=bool)
        for start in range(n):
            if visited[start]: continue
            total_cycles += 1
            v = start
            while not visited[v]:
                visited[v] = True
                v = succ[v, c]
    return total_cycles - k

# ============================================================
# SEARCH ENGINES
# ============================================================
def fast_sa(m, k=3, max_iter=500_000, T_start=5.0, T_end=0.001, seed=42):
    random.seed(seed)
    np.random.seed(seed)
    n = m**k
    perms = list(itertools.permutations(range(k)))
    n_perms = len(perms)
    perms_np = np.array(perms, dtype=np.int32)
    strides = np.array([m**(k-1-d) for d in range(k)], dtype=np.int32)
    perm_idx = np.zeros(n, dtype=np.int32)
    for i in range(n): perm_idx[i] = random.randrange(n_perms)
    perm_arr = perms_np[perm_idx]
    succ = build_succ_np(perm_arr, m, k)
    curr_score = score_np(succ, n, k)
    best_score = curr_score
    best_perm = perm_arr.copy()
    cooling = (T_end / T_start) ** (1.0 / max_iter)
    T = T_start
    t0 = time.perf_counter()
    coords = np.zeros((n, k), dtype=np.int32)
    for i in range(n):
        temp = i
        for d in reversed(range(k)):
            coords[i, d] = temp % m
            temp //= m
    for it in range(1, max_iter + 1):
        v_idx = random.randrange(n)
        old_pidx = perm_idx[v_idx]
        new_pidx = random.randrange(n_perms - 1)
        if new_pidx >= old_pidx: new_pidx += 1
        old_succ_row = succ[v_idx].copy()
        new_p = perms[new_pidx]
        for c in range(k):
            dim = new_p[c]
            old_coord = coords[v_idx, dim]
            succ[v_idx, c] = v_idx - (old_coord * strides[dim]) + ((old_coord + 1) % m) * strides[dim]
        s = score_np(succ, n, k)
        delta = s - curr_score
        if delta <= 0 or (T > 1e-9 and random.random() < math.exp(-delta / T)):
            curr_score = s
            perm_idx[v_idx] = new_pidx
            if s < best_score:
                best_score = s
                best_perm = perms_np[perm_idx].copy()
                if best_score == 0: break
        else:
            succ[v_idx] = old_succ_row
        T *= cooling
    elapsed = time.perf_counter() - t0
    return best_perm, best_score, elapsed

def stratified_sa(m, k=3, max_iter=500_000, T_start=5.0, T_end=0.001, seed=42):
    random.seed(seed)
    np.random.seed(seed)
    n = m**k
    perms = list(itertools.permutations(range(k)))
    n_perms = len(perms)
    perms_np = np.array(perms, dtype=np.int32)
    strides = np.array([m**(k-1-d) for d in range(k)], dtype=np.int32)
    all_coords = np.zeros((n, k), dtype=np.int32)
    for i in range(n):
        temp = i
        for d in reversed(range(k)):
            all_coords[i, d] = temp % m
            temp //= m
    sums = np.sum(all_coords, axis=1) % m
    js = all_coords[:, 1]
    ks = all_coords[:, 2] if k >= 4 else np.zeros(n, dtype=np.int32)

    if k == 3: table_idx = np.zeros((m, m), dtype=np.int32)
    else: table_idx = np.zeros((m, m, m), dtype=np.int32)

    def get_v_indices(idxs):
        if k == 3: return np.where((sums == idxs[0]) & (js == idxs[1]))[0]
        else: return np.where((sums == idxs[0]) & (js == idxs[1]) & (ks == idxs[2]))[0]

    def update_succ(v_indices, table_idx_val, succ):
        perm = perms_np[table_idx_val]
        for v_idx in v_indices:
            for c in range(k):
                dim = perm[c]
                old_coord = all_coords[v_idx, dim]
                succ[v_idx, c] = v_idx - (old_coord * strides[dim]) + ((old_coord + 1) % m) * strides[dim]

    succ = np.zeros((n, k), dtype=np.int32)
    for s in range(m):
        for j in range(m):
            if k == 3: update_succ(get_v_indices((s, j)), table_idx[s, j], succ)
            else:
                for l in range(m): update_succ(get_v_indices((s, j, l)), table_idx[s, j, l], succ)

    curr_score = score_np(succ, n, k)
    best_score = curr_score
    best_table = table_idx.copy()
    cooling = (T_end / T_start) ** (1.0 / max_iter)
    T = T_start
    t0 = time.perf_counter()
    for it in range(1, max_iter + 1):
        if k == 3: idxs = (random.randrange(m), random.randrange(m))
        else: idxs = (random.randrange(m), random.randrange(m), random.randrange(m))
        old_pidx = table_idx[idxs]
        new_pidx = random.randrange(n_perms - 1)
        if new_pidx >= old_pidx: new_pidx += 1
        affected_v = get_v_indices(idxs)
        old_succ_rows = succ[affected_v].copy()
        table_idx[idxs] = new_pidx
        update_succ(affected_v, table_idx[idxs], succ)
        s = score_np(succ, n, k)
        delta = s - curr_score
        if delta <= 0 or (T > 1e-9 and random.random() < math.exp(-delta / T)):
            curr_score = s
            if s < best_score:
                best_score = s
                best_table = table_idx.copy()
                if best_score == 0: break
        else:
            table_idx[idxs] = old_pidx
            succ[affected_v] = old_succ_rows
        T *= cooling
    elapsed = time.perf_counter() - t0
    final_perm_arr = np.zeros((n, k), dtype=np.int32)
    for i in range(n):
        if k == 3: final_perm_arr[i] = perms_np[best_table[sums[i], js[i]]]
        else: final_perm_arr[i] = perms_np[best_table[sums[i], js[i], ks[i]]]
    return final_perm_arr, best_score, elapsed

# ============================================================
# CLOSED-FORM UNIVERSAL SPIKE RULE (Theorem 7.1)
# ============================================================
def closed_form_spike_rule(m):
    """
    Universal O(m) construction for all odd m >= 3.
    See THEORY.md Section 5 for details.
    """
    if m % 2 == 0: raise ValueError("Spike rule requires odd m.")
    n = m**3
    sigma = np.zeros((n, 3), dtype=np.int32)
    for i in range(m):
        for j in range(m):
            for l in range(m):
                idx = i*m**2 + j*m + l
                s = (i + j + l) % m
                if s < m - 2: p = [0, 1, 2]
                elif s == m - 2: p = [0, 2, 1]
                else: p = [1, 0, 2]
                if j == 0 and s != m - 2:
                    new_p = []
                    for val in p:
                        if val == 0: new_p.append(2)
                        elif val == 2: new_p.append(0)
                        else: new_p.append(val)
                    p = new_p
                sigma[idx] = p
    return sigma
