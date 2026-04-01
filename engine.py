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
# BASIN ESCAPE SA (v3.3)
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
        if it % basin_step == 0:
            jump_table = table_idx.copy()
            jump_succ = succ.copy()
            for _ in range(escape_iter):
                if k == 3: idxs = (random.randrange(m), random.randrange(m))
                else: idxs = (random.randrange(m), random.randrange(m), random.randrange(m))
                new_p = random.randrange(n_perms)
                jump_table[idxs] = new_p
                update_succ(get_v_indices(idxs), new_p, jump_succ)
            s_jump = score_np(jump_succ, n, k)
            if s_jump <= curr_score or random.random() < math.exp(-(s_jump - curr_score) / T):
                curr_score = s_jump
                table_idx = jump_table
                succ = jump_succ
                if s_jump < best_score:
                    best_score = s_jump
                    best_table = table_idx.copy()
                    if best_score == 0: break

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

    final_perm_arr = np.zeros((n, k), dtype=np.int32)
    for i in range(n):
        if k == 3: final_perm_arr[i] = perms_np[best_table[sums[i], js[i]]]
        else: final_perm_arr[i] = perms_np[best_table[sums[i], js[i], ks[i]]]
        elapsed = time.perf_counter() - t0
    elapsed = time.perf_counter() - t0
    return final_perm_arr, best_score, elapsed

# ============================================================
# STATELESS FSO LOGIC ROUTER (Zero-RAM lookup)
# ============================================================




class StatelessFSORouter:
    """
    Generalized FSO Router supporting arbitrary dimensions k.
    Follows the Law of Dimensional Parity Harmony.
    """
    def __init__(self, m, k=3, r_vector=None):
        self.m = m
        self.k = k
        if m % 2 == 0 and k % 2 != 0:
            raise ValueError(f"Topological Obstruction: Grid size {m} (even) requires dimension {k} to be even.")

        self.P = [list(range(k)) for _ in range(m)]

        if m % 2 != 0:
            # Solomon Spike Construction (Verified for odd m, k=3)
            if k == 3:
                for s in range(m):
                    if s == m - 2: self.P[s][1], self.P[s][2] = 2, 1
                    elif s == m - 1: self.P[s][0], self.P[s][1] = 1, 0
            else:
                # Generalized boundary shift for odd m
                for s in range(m):
                    if s == m - 1: self.P[s][0], self.P[s][1] = 1, 0

    def lookup(self, coords, color=0):
        s = sum(coords) % self.m
        p = list(self.P[s])
        j = coords[1] if self.k >= 2 else 0

        if self.m % 2 != 0 and self.k == 3:
            # Universal Spike at j=0 column for odd m, k=3
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




# ============================================================
# UNIVERSAL FSO ENGINE v2.4 (Generalized k)
# ============================================================
def verify_universal_router(m, k):
    """
    Verifies if the stateless router for a given (m, k) produces single cycles.
    """
    try:
        sigma = closed_form_spike_rule(m, k)
        n = m**k
        strides = np.array([m**(k-1-d) for d in range(k)], dtype=np.int32)

        # Successor mapping
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
                succ[idx, c] = sum(new_coords[d] * strides[d] for d in range(k))

        # Check for Hamiltonian cycles
        for c in range(k):
            vis = np.zeros(n, dtype=bool)
            curr = 0
            count = 0
            while not vis[curr]:
                vis[curr] = True
                curr = succ[curr, c]
                count += 1
            if count != n:
                return False, f"Cycle failure for color {c}: {count}/{n}"
        return True, "Verified SUCCESS"
    except ValueError as e:
        return False, str(e)
