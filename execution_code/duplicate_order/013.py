import sys
import math
import threading

MOD = 10**9 + 7

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    max_N = 10000
    # Precompute factorial and inverse factorial
    fact = [1] * (max_N + 1)
    for i in range(1, max_N + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact = [1] * (max_N + 1)
    inv_fact[max_N] = pow(fact[max_N], MOD - 2, MOD)
    for i in range(max_N, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def comb(n, k):
        if n < 0 or k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    for test_case in range(1, T + 1):
        N_str = sys.stdin.readline()
        while N_str.strip() == '':
            N_str = sys.stdin.readline()
        N, M1, M2, H, S = map(int, N_str.strip().split())
        C_N_H = N - H
        # Compute min_x
        min_x = max(0, H - M1 + 0, H - M2 + 0)
        max_x = min(C_N_H, M1 + M2 - H)
        A = 0
        for x in range(0, min(max_x, C_N_H) +1):
            # y_low = max(H - M1 + x, 0)
            y_low = max(H - M1 + x, 0)
            y_high = min(M2 - x, H)
            if y_high < y_low:
                continue
            B = (y_high - y_low + 1) % MOD
            C = comb(C_N_H, x)
            pow_S_minus1_x = pow(S -1, x, MOD)
            term = C * pow_S_minus1_x % MOD
            term = term * B % MOD
            A = (A + term) % MOD
        # Now compute the total number of S1,S2 pairs with hamming distance H
        total_S1_S2 = comb(N, H) * pow(S -1, H, MOD) % MOD
        total_S1_S2 = total_S1_S2 * pow(S, N - H, MOD) % MOD
        # Now the desired sum is total_S1_S2 * A
        # But in the sample, the answer is total_S1_S2 * A modulo MOD
        # So compute it
        result = total_S1_S2 * A % MOD
        print(f"Case #{test_case}: {result}")

threading.Thread(target=main,).start()