import sys
import math
import sys
import sys
from math import comb
import sys
import sys
MOD = 10**9 +7

def precompute_factorials(max_n, MOD):
    factorial = [1] * (max_n +1)
    for i in range(1, max_n +1):
        factorial[i] = factorial[i-1] * i % MOD
    inv_fact = [1] * (max_n +1)
    inv_fact[max_n] = pow(factorial[max_n], MOD-2, MOD)
    for i in range(max_n, 0, -1):
        inv_fact[i-1] = inv_fact[i] * i % MOD
    return factorial, inv_fact

def binom(n, k, factorial, inv_fact):
    if k <0 or k >n:
        return 0
    return factorial[n] * inv_fact[k] % MOD * inv_fact[n -k] % MOD

def partial_binomial_sum(n, k, a, factorial, inv_fact):
    # Computes sum_{c=0}^k C(n, c) * a^c mod MOD
    # Using iterative approach
    result = 0
    term = 1  # C(n,0) * a^0
    for c in range(0, k+1):
        result = (result + term) % MOD
        if c ==k:
            break
        # Compute term * (n -c) / (c+1) *a mod MOD
        term = term * (n -c) % MOD
        inv = pow(c +1, MOD-2, MOD)
        term = term * inv % MOD
        term = term * a % MOD
    return result

def compute_f_H(A, H, M1, M2, S, factorial, inv_fact):
    f =0
    min_x = max(0, H - M1, H - M2)
    max_x = min(A, M1, M2)
    for x in range(0, max_x +1):
        if x > M1 or x > M2:
            continue
        C_Ax = binom(A, x, factorial, inv_fact) * pow(S-1, x, MOD) % MOD
        # Calculate lower_a and lower_b
        L_a = max(H - (M1 -x), 0)
        L_b = max(H - (M2 -x), 0)
        if L_a + L_b > H:
            continue
        K = H - L_a - L_b
        if K <0:
            continue
        # Now sum over a from L_a to H - L_b
        # and for each a, sum over c=0 to K
        # where c = H -a -b and b >= L_b
        # which implies c <= H -a -L_b
        sum_B =0
        for a in range(L_a, H - L_b +1):
            C_H_a = binom(H, a, factorial, inv_fact)
            n = H -a
            k = K
            if k <0:
                continue
            partial_sum = partial_binomial_sum(n, k, S -2, factorial, inv_fact)
            sum_B = (sum_B + C_H_a * partial_sum) % MOD
        f = (f + C_Ax * sum_B) % MOD
    return f

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 <<25)
    T = int(sys.stdin.readline())
    test_cases = []
    max_N =0
    for _ in range(T):
        parts = sys.stdin.readline().strip().split()
        N, M1, M2, H, S = map(int, parts)
        test_cases.append( (N, M1, M2, H, S))
        if N > max_N:
            max_N =N
    factorial, inv_fact = precompute_factorials(max_N, MOD)
    for idx, (N, M1, M2, H, S) in enumerate(test_cases,1):
        if H > N or H <0:
            total =0
            print(f"Case #{idx}: {total}")
            continue
        A = N - H
        f_H = compute_f_H(A, H, M1, M2, S, factorial, inv_fact)
        # Now, compute S^N * C(N, H) * (S -1)^H * f_H mod MOD
        S_N = pow(S, N, MOD)
        C_N_H = binom(N, H, factorial, inv_fact)
        S_1_H = pow(S -1, H, MOD)
        total = S_N * C_N_H % MOD
        total = total * S_1_H % MOD
        total = total * f_H % MOD
        print(f"Case #{idx}: {total}")

if __name__ == "__main__":
    main()