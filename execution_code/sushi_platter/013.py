import sys
import threading
from functools import lru_cache

MOD = 10**9 + 7

def main():
    import sys
    import math
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, M, L = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))
        A_sorted = sorted(A)
        B_sorted = sorted(B)
        # Combine all pieces with type
        pieces = [('A', val) for val in A_sorted] + [('B', val) for val in B_sorted]
        n = N + M
        # Precompute all possible differences
        diffs = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                diffs[i][j] = abs(pieces[i][1] - pieces[j][1])
        # Assign indices to A and B
        A_indices = list(range(N))
        B_indices = list(range(N, n))
        # Initialize DP
        from collections import defaultdict
        dp = [{} for _ in range(n+1)]  # dp[k][last][mask] = count
        # Initialize for first piece
        for i in range(n):
            mask = 1 << i
            dp[1][i] = {diffs[i][i]: 1}  # S(P) starts at 0, but since there's no previous, differences start from 0
        # Iterate over the permutation
        for k in range(1, n):
            next_dp = {}
            for last in dp[k]:
                for s, cnt in dp[k][last].items():
                    for nxt in range(n):
                        if not (k < n and (s >> nxt) & 1):
                            if ((s + (1 << nxt)) <= L):
                                # Update state
                                new_s = s + diffs[last][nxt]
                                if new_s <= L:
                                    if nxt not in dp[k+1]:
                                        dp[k+1][nxt] = {}
                                    dp[k+1][nxt][new_s] = (dp[k+1][nxt].get(new_s, 0) + cnt) % MOD
            # dp[k+1] = next_dp
        # Sum up all valid permutations
        total = 0
        for last in dp[n]:
            for s, cnt in dp[n][last].items():
                if s <= L:
                    total = (total + cnt) % MOD
        print(f"Case #{test_case}: {total}")

threading.Thread(target=main).start()