MOD = 10**9 + 7

import sys
import threading

def main():
    import sys

    import math

    T=int(sys.stdin.readline())
    max_N=0
    test_cases=[]
    for _ in range(T):
        line=""
        while line.strip()=="":
            line = sys.stdin.readline()
        N,M1,M2,H,C = map(int,line.strip().split())
        test_cases.append( (N,M1,M2,H,C) )
        if N > max_N:
            max_N=N
    # Precompute factorial and inv factorial
    max_fact = max_N *2 +10
    fact = [1]*(max_fact +1)
    for i in range(1, max_fact +1):
        fact[i] = fact[i-1]*i % MOD
    inv_fact = [1]*(max_fact +1)
    inv_fact[max_fact] = pow(fact[max_fact], MOD -2, MOD)
    for i in range(max_fact -1, -1, -1):
        inv_fact[i] = inv_fact[i+1]*(i+1) % MOD
    def comb(n,k):
        if n <0 or k <0 or k >n:
            return 0
        return fact[n]* inv_fact[k] % MOD * inv_fact[n -k] % MOD
    for tc, (N,M1,M2,H,C) in enumerate(test_cases,1):
        if C==1:
            if H==0:
                # All S1=S2, and s must be equal to S1=S2.
                # Number of S1,S2 with H=0 is |Sigma|^N =1
                # |{s}|=1
                answer=1 if M1 >=0 and M2 >=0 else 0
            else:
                # C=1 and H>0 impossible
                answer=0
            print(f"Case #{tc}: {answer}")
            continue
        if H >N:
            print(f"Case #{tc}: 0")
            continue
        # Calculate sum_terms
        sum_terms=0
        max_a = min(N - H, M1)
        for a in range(0, max_a +1):
            comb_A = comb(N - H, a)
            pow_A = pow(C -1, a, MOD)
            c_min = max(0, a + H - M2)
            c_max = min(H, M1 -a)
            if c_min > c_max:
                continue
            comb_A_pow_A = comb_A * pow_A % MOD
            for c in range(c_min, c_max +1):
                comb_c = comb(H, c)
                K = H -c
                d_max = min(M1 -a -c, K)
                if d_max <0:
                    continue
                # Compute sum_d = sum_{d=0}^{d_max} C(K,d) * (C-2)^d
                # This can be done iteratively
                sum_d =0
                C_minus_2 = C -2
                if C_minus_2 ==0:
                    if d_max >=0:
                        sum_d =1 if K >=0 else 0
                else:
                    # Compute (1 + (C-2))^K up to d_max
                    # Which is sum_{d=0}^{d_max} C(K,d) * (C-2)^d
                    # Use iterative approach
                    current =1
                    sum_d =1
                    for d in range(1, d_max +1):
                        current = current * (K - d +1) % MOD
                        current = current * pow(d, MOD -2, MOD) % MOD
                        current = current * (C -2) % MOD
                        sum_d = (sum_d + current) % MOD
                term = comb_A_pow_A * comb_c % MOD
                term = term * sum_d % MOD
                sum_terms = (sum_terms + term) % MOD
        # Now, how to relate sum_terms to the required sum
        # Number of S1,S2 with h(S1,S2}=H} is pow(C, N} ) * comb(N,H} ) * pow(C-1, H} ) / pow(C, N} ) ?
        # No, it's |Sigma|^N * comb(N,H} ) * pow(C-1, H} ).
        # We need to multiply sum_terms with comb(N,H} ) * pow(C-1, H} )
        number_S1_S2 = comb(N, H) * pow(C -1, H, MOD) % MOD
        # Also, each Type A position has C choices, but already accounted in a
        # Thus, answer is sum_terms * pow(C, N - H} ) * number_S1_S2
        # But this double counts, hence:
        # Each a corresponds to certain configurations
        # To match the sample, when sum_terms=3, number_S1_S2=2,
        # and |Sigma|^N=4,
        # sum_terms * number_S1_S2=6 !=24
        # Need to multiply by pow(C, N -H} )
        answer = sum_terms * pow(C, N - H, MOD) % MOD
        answer = answer * number_S1_S2 % MOD
        print(f"Case #{tc}: {answer}")

threading.Thread(target=main).start()