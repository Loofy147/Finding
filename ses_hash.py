import numpy as np

class SESHash:
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.P = [list(range(k)) for _ in range(m)]
        if m % 2 != 0:
            if k == 3:
                self.P[m-2][1], self.P[m-2][2] = 2, 1
                self.P[m-1][0], self.P[m-1][1] = 1, 0
        else:
            if k == 2:
                self.P[m-1][0], self.P[m-1][1] = 1, 0

    def get_cycle_length(self, start_coords):
        curr = list(start_coords)
        visited = {tuple(curr)}
        steps = 0
        while True:
            s = sum(curr) % self.m
            dim = self.P[s][0]
            curr[dim] = (curr[dim] + 1) % self.m
            steps += 1
            if tuple(curr) in visited:
                break
            visited.add(tuple(curr))
        return steps

def demo_trapdoor():
    print("--- SES-Hash: The Parity Trapdoor Cycle Analysis ---")

    # CASE 1: OBSTRUCTED (m=4, k=3) - Small m for fast check
    m_obs, k_obs = 4, 3
    hasher_obs = SESHash(m_obs, k_obs)
    len_obs = hasher_obs.get_cycle_length((0, 0, 0))
    print(f"\n[OBSTRUCTED] Z_{m_obs}^{k_obs}: Cycle Length = {len_obs} (Expected m=4)")

    # CASE 2: HARMONIOUS (m=4, k=2)
    m_har, k_har = 4, 2
    hasher_har = SESHash(m_har, k_har)
    len_har = hasher_har.get_cycle_length((0, 0))
    print(f"[HARMONIOUS] Z_{m_har}^{k_har}: Cycle Length = {len_har} (Expected m^2=16)")

if __name__ == "__main__":
    demo_trapdoor()
