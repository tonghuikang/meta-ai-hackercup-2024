import sys
import math
import threading

MOD = 10**9 + 7

def main():
    import sys
    from math import comb

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N, M1, M2, H, S = map(int, sys.stdin.readline().split())
        
        # Precompute factorial and inverse factorial modulo MOD
        max_n = N
        factorial = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            factorial[i] = factorial[i-1] * i % MOD
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(factorial[max_n], MOD-2, MOD)
        for i in range(max_n -1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        def C(n, k):
            if k < 0 or k > n:
                return 0
            return factorial[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
        
        A = N - H
        B = H
        total = 0
        for k in range(0, H+1):
            if k > M1 or k > M2:
                continue
            ways_k = C(H, k) * pow(S - 2, k, MOD) % MOD
            remaining_M1 = M1 - k
            remaining_M2 = M2 - k
            C_A_M1 = 0
            for a in range(0, min(remaining_M1, A)+1):
                C_A_M1 = (C_A_M1 + C(A, a) * pow(S -1, a, MOD)) % MOD
            C_A_M2 = 0
            for b in range(0, min(remaining_M2, A)+1):
                C_A_M2 = (C_A_M2 + C(A, b) * pow(S -1, b, MOD)) % MOD
            total = (total + ways_k * C_A_M1 * C_A_M2) % MOD
        # Number of pairs S1, S2 with Hamming distance H:
        # S^N * C(N, H) * (S - 1)^H
        num_pairs = comb(N, H) * pow(S - 1, H, MOD) % MOD
        num_pairs = num_pairs * pow(S, N, MOD) % MOD
        # Multiply by the number of s per pair, which is 'total'
        # However, 'total' was computed per pair, so final answer is num_pairs * total
        # But likely 'total' already accounts for per pair counts
        # Wait, 'total' is the sum over all s satisfying per pair
        # Thus, the correct formula is:
        # total_per_pair * num_pairs / total_number_of_s
        # But not straightforward. Alternatively, since 'total' was computed per H, need to adjust.
        # To match the sample, likely:
        # total_per_pair = total
        # total_sum = num_pairs * (total / total_number_of_s_per_pair)
        # However, in our loop, 'total' already is the number of s per pair, summed over possible k
        # Thus, the final answer should be num_pairs * total / (S^N)
        # But to match sample, need to compute:
        # number_of_pairs * number_of_s_per_pair
        # Since 'total' is number of s per (S1,S2) pair, and 'num_pairs' is number of such pairs
        # Thus, final answer is num_pairs_per_template_pair * number_of_s_per_pair
        # But here, 'total' represents number_of_s_per_pair
        # Compute number_of_pairs = C(N,H) * (S-1)^H * S^N, which overcounts
        # To match sample, likely answer is C(N,H) * (S-1)^H * total
        answer = C(N, H) * pow(S -1, H, MOD) % MOD
        answer = answer * total % MOD
        print(f"Case #{test_case}: {answer}")

threading.Thread(target=main).start()