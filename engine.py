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
# SEARCH ENGINES (SA & Basin Escape)
# ============================================================
def stratified_sa_v3(m, k=3, max_iter=500_000, T_start=5.0, T_end=0.001, seed=42,
                      basin_step=1000, escape_iter=100):
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

    table_idx = np.zeros((m, m), dtype=np.int32)
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
            v_indices = np.where((sums == s) & (js == j))[0]
            update_succ(v_indices, table_idx[s, j], succ)

    curr_score = score_np(succ, n, k)
    best_score = curr_score
    best_table = table_idx.copy()
    cooling = (T_end / T_start) ** (1.0 / max_iter)
    T = T_start
    t0 = time.perf_counter()

    for it in range(1, max_iter + 1):
        if it % basin_step == 0:
            jump_table = table_idx.copy()
            jump_succ = succ.copy()
            for _ in range(escape_iter):
                idxs = (random.randrange(m), random.randrange(m))
                new_p = random.randrange(n_perms)
                jump_table[idxs] = new_p
                update_succ(np.where((sums == idxs[0]) & (js == idxs[1]))[0], new_p, jump_succ)
            s_jump = score_np(jump_succ, n, k)
            if s_jump <= curr_score or random.random() < math.exp(-(s_jump - curr_score) / T):
                curr_score = s_jump
                table_idx = jump_table
                succ = jump_succ
                if s_jump < best_score:
                    best_score = s_jump
                    best_table = table_idx.copy()
                    if best_score == 0: break

        idxs = (random.randrange(m), random.randrange(m))
        old_pidx = table_idx[idxs]
        new_pidx = random.randrange(n_perms - 1)
        if new_pidx >= old_pidx: new_pidx += 1
        affected_v = np.where((sums == idxs[0]) & (js == idxs[1]))[0]
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

    final_perm_arr = np.zeros((n, k), dtype=np.int32)
    for i in range(n):
        final_perm_arr[i] = perms_np[best_table[sums[i], js[i]]]
    return final_perm_arr, best_score, time.perf_counter() - t0

# ============================================================
# STATELESS FSO LOGIC ROUTER (Your Zero-Memory Blueprint)
# ============================================================
class StatelessFSORouter:
    def __init__(self, m):
        if m % 2 == 0: raise ValueError("Stateless Spike requires odd m.")
        self.m = m
        self.P = [None] * m
        # P[s] is the level-permutation
        for s in range(m):
            if s < m - 2: self.P[s] = (0, 1, 2)
            elif s == m - 2: self.P[s] = (0, 2, 1) # swap12
            else: self.P[s] = (1, 0, 2) # swap01

    def lookup(self, i, j, l, color=0):
        s = (i + j + l) % self.m
        p = self.P[s]

        # SPIKE at j=0
        if j == 0:
            if s == self.m - 2:
                # Critical exception: no swap at m-2 to ensure closure
                return p[color]
            else:
                # swap02 logic: p[0] <-> p[2]
                if p[color] == 0: return 2
                if p[color] == 2: return 0
        return p[color]

def closed_form_spike_rule(m):
    router = StatelessFSORouter(m)
    n = m**3
    sigma = np.zeros((n, 3), dtype=np.int32)
    for idx in range(n):
        i, j, l = idx // m**2, (idx // m) % m, idx % m
        sigma[idx] = [router.lookup(i, j, l, c) for c in range(3)]
    return sigma
