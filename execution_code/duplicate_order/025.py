MOD = 10**9 + 7

def precompute_factorials(max_n, MOD):
    fact = [1]*(max_n+1)
    for i in range(1, max_n+1):
        fact[i] = fact[i-1]*i % MOD
    inv_fact = [1]*(max_n+1)
    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
    for i in range(max_n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1]*(i+1) % MOD
    return fact, inv_fact

def binom(n, k, fact, inv_fact):
    if k <0 or k >n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n -k] % MOD

import sys

def main():
    import sys
    import threading

    def run():
        T = int(sys.stdin.readline())
        max_N = 10000
        fact, inv_fact = precompute_factorials(max_N, MOD)
        for test_case in range(1, T+1):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            N,M1,M2,H,S = map(int,line.strip().split())
            # Compute C(N,H)
            C_N_H = binom(N, H, fact, inv_fact)
            # Compute (S-1)^H
            pow_S_minus1_H = pow(S -1, H, MOD)
            # Compute F
            F =0
            c_min = max(0, H - M1 - M2)
            c_max = min(H, M1, M2)
            # Precompute binom(H,c) for all c
            binom_H_c = [binom(H, c, fact, inv_fact) for c in range(c_max+1)]
            # Precompute (S-2)^c for all c in range
            pow_S_minus2_c = [pow(S -2, c, MOD) for c in range(c_max+1)]
            for idx,c in enumerate(range(c_min, c_max+1)):
                if c > H:
                    continue
                C_H_c = binom(H, c, fact, inv_fact)
                if c >= len(binom_H_c):
                    C_H_c = binom(H, c, fact, inv_fact)
                else:
                    C_H_c = binom_H_c[c]
                term1 = C_H_c * pow(S -2, c, MOD) % MOD
                n = H -c
                a_min = max(H - M1, 0)
                a_max = min(M2 -c, n)
                if a_max < a_min:
                    continue
                # Compute sum_C = sum_{a=a_min}^{a_max} C(n,a)
                # Compute prefix sum on the fly
                sum_C = 0
                for a in range(a_min, a_max+1):
                    sum_C = (sum_C + binom(n, a, fact, inv_fact)) % MOD
                F = (F + term1 * sum_C) % MOD
            # Compute |Sigma|^N
            pow_S_N = pow(S, N, MOD)
            # Compute final answer
            answer = pow_S_N
            answer = answer * binom(N, H, fact, inv_fact) % MOD
            answer = answer * pow_S_minus1_H % MOD
            answer = answer * F % MOD
            print(f"Case #{test_case}: {answer}")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()