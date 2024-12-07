import sys
import math
import sys
import sys

MOD = 10**9 + 7

def precompute_factorials(max_n):
    fact = [1]*(max_n+1)
    for i in range(1, max_n+1):
        fact[i] = fact[i-1]*i % MOD
    inv_fact = [1]*(max_n+1)
    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
    for i in range(max_n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1]*(i+1) % MOD
    return fact, inv_fact

def binom(n, k, fact, inv_fact):
    if n < 0 or k <0 or k >n:
        return 0
    return fact[n]*inv_fact[k]%MOD * inv_fact[n -k]%MOD

def solve():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    idx = 1
    max_N = 0
    test_cases = []
    for _ in range(T):
        N = int(data[idx])
        M1 = int(data[idx+1])
        M2 = int(data[idx+2])
        H = int(data[idx+3])
        c = int(data[idx+4])
        test_cases.append( (N, M1, M2, H, c) )
        max_N = max(max_N, N)
        idx +=5
    fact, inv_fact = precompute_factorials(max_N)
    for tc in range(1, T+1):
        N, M1, M2, H, c = test_cases[tc-1]
        if H > N or H <0:
            result =0
            print(f"Case #{tc}: {result}")
            continue
        comb_N_H = binom(N, H, fact, inv_fact)
        comb_factor = pow(c-1, H, MOD)
        total = binom(N, H, fact, inv_fact)*pow(c-1, H, MOD) % MOD
        # Now iterate over k
        max_k = min(N - H, M1, M2)
        result =0
        for k in range(0, max_k+1):
            comb_A = binom(N - H, k, fact, inv_fact)
            term_A = comb_A * pow(c -1, k, MOD) % MOD
            m1_p = M1 -k
            m2_p = M2 -k
            z_max = min(H, m1_p, m2_p)
            if z_max <0:
                continue
            sum_z =0
            for z in range(0, z_max+1):
                comb_H_z = binom(H, z, fact, inv_fact)
                term_z = comb_H_z * pow(c -2, z, MOD) % MOD
                # Now t ranges from max(0, H - m1_p) to min(H - z, m2_p - z)
                t_min = max(0, H - m1_p)
                t_max = min(H - z, m2_p - z)
                if t_max < t_min:
                    continue
                # sum_{t=t_min}^{t_max} C(H - z, t)
                sum_t = 0
                for t in range(t_min, t_max+1):
                    sum_t = (sum_t + binom(H - z, t, fact, inv_fact)) % MOD
                sum_z = (sum_z + term_z * sum_t) % MOD
            result = (result + term_A * sum_z) % MOD
        print(f"Case #{tc}: {result}")