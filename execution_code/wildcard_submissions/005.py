import sys
import threading
from itertools import combinations
from collections import defaultdict

MOD = 998244353

def main():
    import sys
    import math
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N = int(sys.stdin.readline())
        S = [sys.stdin.readline().strip() for _ in range(N)]
        # Collect possible characters at each position for each string
        C_i = []  # List of list of sets of possible characters per string
        maxlen = 0
        for s in S:
            maxlen = max(maxlen, len(s))
        for s in S:
            C_s = []
            for ch in s:
                if ch == '?':
                    C_s.append(set(chr(ord('A') + i) for i in range(26)))
                else:
                    C_s.append(set([ch]))
            C_i.append(C_s)
        # Precompute per-string prefix counts
        Pi = []
        for C_s in C_i:
            len_s = len(C_s)
            prefix_counts = []
            total = 0
            prod = 1
            for k in range(len_s):
                prod = (prod * len(C_s[k])) % MOD
                total = (total + prod) % MOD
            Pi.append(total)
        # Compute overlaps between pairs
        Pij = {}
        for (i, Ci), (j, Cj) in combinations(enumerate(C_i), 2):
            min_len = min(len(Ci), len(Cj))
            total = 0
            prod = 1
            for k in range(min_len):
                Ci_k = Ci[k]
                Cj_k = Cj[k]
                intersection = Ci_k & Cj_k
                len_intersection = len(intersection)
                if len_intersection == 0:
                    break
                prod = (prod * len_intersection) % MOD
                total = (total + prod) % MOD
            Pij[(i, j)] = total
        # Compute overlaps between triplets
        Pijk = {}
        for (i, Ci), (j, Cj), (k, Ck) in combinations(enumerate(C_i), 3):
            min_len = min(len(Ci), len(Cj), len(Ck))
            total = 0
            prod = 1
            for idx in range(min_len):
                intersection = Ci[idx] & Cj[idx] & Ck[idx]
                len_intersection = len(intersection)
                if len_intersection == 0:
                    break
                prod = (prod * len_intersection) % MOD
                total = (total + prod) % MOD
            Pijk[(i, j, k)] = total
        # Compute overlaps between quadruplets if necessary
        Pijkl = {}
        for (i, Ci), (j, Cj), (k, Ck), (l, Cl) in combinations(enumerate(C_i), 4):
            min_len = min(len(Ci), len(Cj), len(Ck), len(Cl))
            total = 0
            prod = 1
            for idx in range(min_len):
                intersection = Ci[idx] & Cj[idx] & Ck[idx] & Cl[idx]
                len_intersection = len(intersection)
                if len_intersection == 0:
                    break
                prod = (prod * len_intersection) % MOD
                total = (total + prod) % MOD
            Pijkl[(i, j, k, l)] = total
        # Compute total nodes using inclusion-exclusion principle
        total_nodes = sum(Pi) % MOD
        total_nodes = (total_nodes - sum(Pij.values())) % MOD
        total_nodes = (total_nodes + sum(Pijk.values())) % MOD
        total_nodes = (total_nodes - sum(Pijkl.values())) % MOD
        # Since we can proceed further if needed, but given N<=25, going up to quadruplets is acceptable
        print(f"Case #{case_num}: {total_nodes}")
if __name__ == '__main__':
    threading.Thread(target=main).start()