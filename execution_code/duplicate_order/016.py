import sys
import sys
import math

MOD = 10**9 +7

def precompute_fact_inv(max_n, mod):
    fact = [1]*(max_n +1)
    for i in range(1, max_n +1):
        fact[i] = fact[i-1]*i % mod
    inv_fact = [1]*(max_n +1)
    inv_fact[max_n] = pow(fact[max_n], mod -2, mod)
    for i in range(max_n -1, -1, -1):
        inv_fact[i] = inv_fact[i+1]*(i +1) % mod
    return fact, inv_fact

def comb(n, k, fact, inv_fact, mod):
    if k <0 or k >n:
        return 0
    return fact[n]*inv_fact[k]%mod * inv_fact[n -k]%mod

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    idx =1
    max_n =0
    test_cases = []
    for _ in range(T):
        N = int(data[idx])
        M1 = int(data[idx +1])
        M2 = int(data[idx +2])
        H = int(data[idx +3])
        S = int(data[idx +4])
        test_cases.append( (N, M1, M2, H, S))
        max_n = max(max_n, N)
        idx +=5
    fact, inv_fact = precompute_fact_inv(max_n, MOD)
    for tc in range(1, T +1):
        N, M1, M2, H, S = test_cases[tc -1]
        if H >N or H <0:
            total_sum =0
            print(f"Case #{tc}: {total_sum}")
            continue
        C = N - H
        D = H
        # Compute S^N
        S_N = pow(S, N, MOD)
        # Compute comb(N, H) * (S -1)^H
        comb_H = comb(N, H, fact, inv_fact, MOD) * pow(S -1, H, MOD) % MOD
        # Compute intersection_sum
        l_x = max(D - M1, D - M2, 0)
        u_x = (M1 + M2 - D) //2
        u_x = min(u_x, C)
        if (M1 + M2 >= D) and (l_x <= u_x):
            intersection_sum =0
            for x in range(l_x, u_x +1):
                # Compute factor
                fa = x + D - M1
                if fa <0:
                    fa =0
                fb = x + D - M2
                if fb <0:
                    fb =0
                factor = D - fa - fb +1
                if factor <0:
                    continue
                # Compute comb(C, x) * (S -1)^x % MOD
                comb_C_x = comb(C, x, fact, inv_fact, MOD)
                pow_Sm1_x = pow(S -1, x, MOD)
                term = comb_C_x * pow_Sm1_x % MOD
                term = term * factor % MOD
                intersection_sum = (intersection_sum + term) % MOD
        else:
            intersection_sum =0
        # Compute final answer
        total_sum = S_N * comb_H % MOD
        total_sum = total_sum * intersection_sum % MOD
        print(f"Case #{tc}: {total_sum}")

if __name__ == "__main__":
    main()