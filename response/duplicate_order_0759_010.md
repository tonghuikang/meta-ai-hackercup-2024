To solve the problem, let's break it down step by step.

**Key Findings:**

1. **Combinatorial Analysis:**
   - We need to count the number of ways to choose two strings \( S_1 \) and \( S_2 \) of length \( N \) from the alphabet \( \Sigma \) such that their Hamming distance is exactly \( H \).
   - For each such pair \( (S_1, S_2) \), we need to determine the number of possible original strings \( s \) that are within \( M_1 \) Hamming distance from \( S_1 \) and within \( M_2 \) Hamming distance from \( S_2 \).
   
2. **Generating Functions Approach:**
   - We consider the positions where \( S_1 \) and \( S_2 \) are the same and where they differ.
   - For positions where \( S_1 \) and \( S_2 \) are the same, \( s \) can either match or differ from them.
   - For positions where \( S_1 \) and \( S_2 \) differ, \( s \) can match \( S_1 \), match \( S_2 \), or differ from both.
   - Using combinatorial coefficients and powers, we derive a formula to count all valid configurations.

3. **Efficient Computation:**
   - To handle large values of \( N \) and \( H \), we precompute factorials and inverse factorials modulo \( 10^9+7 \).
   - We iteratively compute the contributions for different values of \( a \) and \( b \), which correspond to how \( s \) matches \( S_1 \) and \( S_2 \) respectively.
   - We also precompute partial sums for efficient calculation of certain binomial coefficients multiplied by powers of \( |\Sigma| - 1 \).

4. **Edge Cases Handling:**
   - Special attention is given to cases where \( H = 0 \) or when \( |\Sigma| = 2 \) to ensure that the counts are accurate.

The final implementation follows these steps, efficiently handling all given constraints and computing the required sum modulo \( 10^9+7 \).

```python
import sys
import threading

def main():
    import sys

    MOD = 10**9 +7
    import math

    T = int(sys.stdin.readline())
    test_cases = []
    max_N = 0
    for _ in range(T):
        line = sys.stdin.readline()
        while line.strip() == '':
            line = sys.stdin.readline()
        N, M1, M2, H, Sigma = map(int, line.strip().split())
        test_cases.append( (N, M1, M2, H, Sigma) )
        if N > max_N:
            max_N = N
    # Precompute factorial and inverse factorial up to max_N
    max_fact = max_N
    factorial = [1]*(max_fact +1)
    for i in range(1, max_fact +1):
        factorial[i] = factorial[i -1]*i % MOD
    inv_fact = [1]*(max_fact +1)
    inv_fact[max_fact] = pow(factorial[max_fact], MOD -2, MOD)
    for i in range(max_fact -1, -1, -1):
        inv_fact[i] = inv_fact[i +1]*(i +1) % MOD
    def C(n,k):
        if n <0 or k <0 or k >n:
            return 0
        return factorial[n] * inv_fact[k] % MOD * inv_fact[n -k] % MOD

    for tc_idx, (N, M1, M2, H, Sigma) in enumerate(test_cases,1):
        if H > N:
            total_sum =0
            print(f"Case #{tc_idx}: {total_sum}")
            continue
        comb_N_H = C(N,H)
        sigma_pow_N = pow(Sigma, N, MOD)
        sigma_minus1_pow_H = pow(Sigma -1, H, MOD)
        # Prepare list_d and prefix_sum_d
        list_d = [0]*(N - H +1)
        for d in range(0, N - H +1):
            list_d[d] = C(N - H, d) * pow(Sigma -1, d, MOD) % MOD
        prefix_sum_d = [0]*(N - H +1)
        prefix_sum_d[0] = list_d[0]
        for d in range(1, N - H +1):
            prefix_sum_d[d] = (prefix_sum_d[d -1] + list_d[d]) % MOD
        # Compute sum_total
        sum_total =0
        a_min = max(H - M1, 0)
        a_max = min(H, M2)
        for a in range(a_min, a_max +1):
            b_min = max(H - M2, 0)
            b_max = min(H -a, M1 - H +a)
            if b_max < b_min:
                continue
            for b in range(b_min, b_max +1):
                c = H -a -b
                if Sigma >=2:
                    if c >=0:
                        sigma_minus2_pow_c = pow(Sigma -2, c, MOD)
                    else:
                        continue
                else:
                    if c ==0:
                        sigma_minus2_pow_c =1
                    else:
                        sigma_minus2_pow_c =0
                d_max_candidate1 = M1 - H +a
                d_max_candidate2 = M2 - H +b
                d_max = min(d_max_candidate1, d_max_candidate2, N - H)
                if d_max <0:
                    continue
                sum_d = prefix_sum_d[d_max]
                term1 = C(H, a) * C(H -a, b) % MOD
                term2 = term1 * sigma_minus2_pow_c % MOD
                term3 = term2 * sum_d % MOD
                sum_total = (sum_total + term3) % MOD
        # Now, total_sum = Sigma^N * C(N,H) * (Sigma -1)^H * sum_total % MOD
        total_sum = sigma_pow_N
        total_sum = total_sum * comb_N_H % MOD
        total_sum = total_sum * sigma_minus1_pow_H % MOD
        total_sum = total_sum * sum_total % MOD
        print(f"Case #{tc_idx}: {total_sum}")

threading.Thread(target=main).start()
```