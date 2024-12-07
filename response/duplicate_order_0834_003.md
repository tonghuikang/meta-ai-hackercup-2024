To solve this problem, we analyze the relationship between the original string `s` and the two recorded strings `S1` and `S2` with a Hamming distance of `H`. The key idea is to calculate the number of valid original strings `s` that are within a Hamming distance of `M1` from `S1` and `M2` from `S2`, given that `S1` and `S2` differ in exactly `H` positions.

### Key Findings:

1. **Combinatorial Analysis**:
   - The total number of pairs `(S1, S2)` with Hamming distance `H` is given by:
     \[
     \text{Total Pairs} = \binom{N}{H} \times |\Sigma|^N \times (|\Sigma| - 1)^H
     \]
   - For each such pair, we need to count the number of possible original strings `s` that satisfy the Hamming distance constraints with both `S1` and `S2`.

2. **Counting Valid Strings `s`**:
   - Divide the positions into two categories:
     - **Common Positions**: Positions where `S1` and `S2` are identical.
     - **Differing Positions**: Positions where `S1` and `S2` differ.
   - For each position, determine how `s` can align with `S1` and `S2` to satisfy the Hamming distance constraints using combinatorial methods.
   
3. **Dynamic Programming**:
   - Precompute binomial coefficients and their cumulative sums to efficiently calculate the required counts.
   - Use nested loops to iterate over possible differences and accumulate the valid counts modulo \(10^9 + 7\) to handle large numbers.

4. **Optimization**:
   - Given the constraints (with `N` up to 10,000 and up to 100 test cases), it's crucial to implement the combinatorial calculations efficiently. Precomputing factorials and using dynamic programming for binomial coefficients helps achieve this.

### Python Implementation:

Below is the Python code that implements the above logic. The code precomputes the necessary binomial coefficients and cumulative sums, then iterates through each test case to calculate the required number of valid configurations.

```python
import sys
import threading

def main():
    import math
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 10**9 + 7

    T = int(sys.stdin.readline())
    test_cases = []
    max_N = 0
    for _ in range(T):
        N, M1, M2, H, S = map(int, sys.stdin.readline().split())
        test_cases.append((N, M1, M2, H, S))
        if N > max_N:
            max_N = N

    # Precompute factorial and inverse factorial
    max_n = max_N
    factorial = [1] * (max_n + 1)
    for i in range(1, max_n +1):
        factorial[i] = factorial[i-1] * i % MOD

    inv_fact = [1] * (max_n +1)
    inv_fact[max_n] = pow(factorial[max_n], MOD-2, MOD)
    for i in range(max_n, 0, -1):
        inv_fact[i-1] = inv_fact[i] * i % MOD

    # Function to compute C(n,k)
    def comb(n, k):
        if k <0 or k >n:
            return 0
        return factorial[n] * inv_fact[k] % MOD * inv_fact[n -k] % MOD

    # Precompute cumulative sums P[n][k] = sum_{a=0}^k C(n,a)
    # Since n and k up to 10000, we store P as a list of lists
    # To save memory and time, compute P row by row
    P = [ [0]*(max_n +1) for _ in range(max_n +1)]
    for n in range(max_n +1):
        P[n][0] = comb(n,0)
        for k in range(1, n+1):
            P[n][k] = (P[n][k-1] + comb(n,k)) % MOD
        for k in range(n+1, max_n +1):
            P[n][k] = P[n][n]

    for idx, (N, M1, M2, H, S) in enumerate(test_cases, 1):
        if H > N:
            result =0
            print(f"Case #{idx}: {result}")
            continue
        c_H =0
        # Precompute powers
        pow_S_minus_1 = [1] * (N - H +1)
        for x in range(1, N - H +1):
            pow_S_minus_1[x] = pow_S_minus_1[x-1] * (S -1) % MOD
        pow_S_minus_2 = [1] * (H +1)
        for c in range(1, H +1):
            pow_S_minus_2[c] = pow_S_minus_2[c-1] * (S -2) % MOD
        for x in range(0, N - H +1):
            C_NH_x = comb(N - H, x)
            ways_A = C_NH_x * pow_S_minus_1[x] % MOD
            # Now iterate over c
            for c in range(0, H +1):
                K = H -c
                a_min = max(0, H - M1 + x)
                a_max = min(K, M2 -x -c)
                if a_min > a_max:
                    continue
                sum_C = P[K][a_max]
                if a_min >0:
                    sum_C = (sum_C - P[K][a_min -1]) % MOD
                C_H_c = comb(H, c)
                ways_B = C_H_c * pow_S_minus_2[c] % MOD
                c_H = (c_H + ways_A * ways_B % MOD * sum_C % MOD) % MOD
        # Total number of S1,S2 pairs with hamming distance H:
        total_pairs = comb(N, H) * pow(S -1, H, MOD) % MOD
        total_pairs = total_pairs * pow(S, N, MOD) * pow(S, -N, MOD)
        # To compute |Sigma|^N * C(N, H) * (|Sigma| -1)^H modulo MOD
        # Which is pow(S, N, MOD) * comb(N, H) % MOD * pow(S -1, H, MOD) % MOD
        total_pairs = comb(N, H) * pow(S, N, MOD) % MOD
        total_pairs = total_pairs * pow(S -1, H, MOD) % MOD
        # Now multiply by c_H
        answer = c_H * total_pairs % MOD
        print(f"Case #{idx}: {answer}")

threading.Thread(target=main).start()
```