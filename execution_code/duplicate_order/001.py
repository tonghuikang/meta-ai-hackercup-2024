#!/usr/bin/env python3
import sys
import threading

MOD = 10**9 + 7

def main():
    import sys
    import math
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T+1):
        N, M1, M2, H, S = map(int, sys.stdin.readline().split())
        T0 = N - H  # Number of positions where S1_i == S2_i
        T1 = H      # Number of positions where S1_i != S2_i

        # Initialize DP array
        # dp[delta1][delta2]: number of ways with total delta1 mistakes in S1 and delta2 in S2
        dp = [ [0]*(M2+2) for _ in range(M1+2) ]
        dp[0][0] = 1

        # Process Type 0 positions
        for _ in range(T0):
            next_dp = [ [0]*(M2+2) for _ in range(M1+2) ]
            for delta1 in range(M1+1):
                for delta2 in range(M2+1):
                    val = dp[delta1][delta2]
                    if val == 0:
                        continue
                    # Event A: delta1_i = 0, delta2_i = 0
                    next_dp[delta1][delta2] = (next_dp[delta1][delta2] + val) % MOD
                    # Event B: delta1_i = 1, delta2_i = 1
                    if delta1+1 <= M1 and delta2+1 <= M2:
                        next_dp[delta1+1][delta2+1] = (next_dp[delta1+1][delta2+1] + val * (S-1)) % MOD
            dp = next_dp

        # Process Type 1 positions
        for _ in range(T1):
            next_dp = [ [0]*(M2+2) for _ in range(M1+2) ]
            for delta1 in range(M1+1):
                for delta2 in range(M2+1):
                    val = dp[delta1][delta2]
                    if val == 0:
                        continue
                    # Event C: delta1_i = 0, delta2_i = 1
                    if delta2+1 <= M2:
                        next_dp[delta1][delta2+1] = (next_dp[delta1][delta2+1] + val) % MOD
                    # Event D: delta1_i = 1, delta2_i = 0
                    if delta1+1 <= M1:
                        next_dp[delta1+1][delta2] = (next_dp[delta1+1][delta2] + val) % MOD
                    # Event E: delta1_i = 1, delta2_i = 1
                    if delta1+1 <= M1 and delta2+1 <= M2:
                        next_dp[delta1+1][delta2+1] = (next_dp[delta1+1][delta2+1] + val * (S-2)) % MOD
            dp = next_dp

        # Sum up all valid configurations
        total_ways = 0
        for delta1 in range(M1+1):
            for delta2 in range(M2+1):
                total_ways = (total_ways + dp[delta1][delta2]) % MOD

        # Compute the total number of pairs (S1, S2) with hamming distance H
        # Number of ways to choose H positions where S1_i != S2_i: C(N, H)
        total_pairs = math.comb(N, H)
        # For positions where S1_i == S2_i (N - H positions), S1_i can be any of S letters: S^{N - H}
        # For positions where S1_i != S2_i (H positions), S1_i can be any of S letters, S2_i can be any of S - 1 letters (excluding S1_i): (S * (S - 1))^H
        total_pairs = (total_pairs * pow(S, N - H, MOD) * pow(S * (S - 1), H, MOD)) % MOD

        # The final answer is total_pairs * total_ways mod MOD
        answer = (total_pairs * total_ways) % MOD
        print(f"Case #{case_num}: {answer}")

threading.Thread(target=main).start()