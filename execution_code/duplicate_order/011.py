import sys
import math
import sys
import sys
MOD = 10**9 + 7

def readints():
    import sys
    return list(map(int, sys.stdin.read().split()))

def precompute_combinations(max_n):
    comb = [ [0]*(max_n+1) for _ in range(max_n+1) ]
    for n in range(max_n+1):
        comb[n][0] = 1
        for k in range(1, n+1):
            comb[n][k] = (comb[n-1][k-1] + comb[n-1][k]) % MOD
    return comb

def precompute_combinations_pascal(max_n):
    # Since N can be up to 10000, and we need combinations upto N,
    # but storing C(N,k) for N=10000 is too much (10000*10000)
    # Instead, we can compute combinations on the fly using factorial and inverse factorial
    factorial = [1]*(max_n+1)
    for i in range(1, max_n+1):
        factorial[i] = factorial[i-1]*i % MOD
    inv_fact = [1]*(max_n+1)
    inv_fact[max_n] = pow(factorial[max_n], MOD-2, MOD)
    for i in range(max_n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1]*(i+1) % MOD
    return factorial, inv_fact

def comb(n, k, factorial, inv_fact):
    if k < 0 or k > n:
        return 0
    return factorial[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def solve():
    import sys
    import sys
    T, *rest = map(int, sys.stdin.read().split())
    test_cases = rest
    max_N = 0
    for i in range(T):
        N, M1, M2, H, K = test_cases[i*5:(i+1)*5]
        max_N = max(max_N, N)
    factorial, inv_fact = precompute_combinations_pascal(max_N)
    for t in range(1, T+1):
        N, M1, M2, H, K = test_cases[(t-1)*5:t*5]
        C = N - H
        if H > N or C <0:
            res = 0
            print(f"Case #{t}: {res}")
            continue
        # Now, for fixed H, C = N - H
        # The number of S1,S2 pairs with hamming distance H is K^N * C(N,H)*(K-1)^H
        # However, since s is summed over all possible strings, we need to compute
        # the number of triples (s, S1, S2) with h(S1,S2)=H, h(s,S1)<=M1, h(s,S2)<=M2
        # To compute this, fix s, and count number of S1,S2 with h(S1,S2)=H, h(s,S1)<=M1, h(s,S2)<=M2
        # Then multiply by K^N
        # So total sum = K^N * [number of S1,S2 with hamming distance H and within M1,M2 from s]
        # We need to compute the number of S1,S2 given s, with hamming distance H and hamming distances <=M1,M2
        
        # The number of S1 with hamming distance w to s is C(N, w)*(K-1)^w
        # Similarly for S2 with hamming distance v to s
        # Given S1 with hamming distance w and S2 with hamming distance v,
        # the hamming distance between S1 and S2 must satisfy |w - v| <= H <= w + v
        # But we need hamming distance exactly H
        
        # However, computing this directly is too slow
        # Instead, use the inclusion-exclusion based on overlap
        # Another way is to think of the intersection of two Hamming balls
        # where the centers are Hamming distance H apart

        # Alternatively, consider the generating function approach

        # The number of s that satisfy h(s,S1)<=M1 and h(s,S2)<=M2 for each S1,S2 with h(S1,S2)=H
        # can be computed using the overlap of two balls of radius M1 and M2 separated by H

        # Using the principle of inclusion, the number can be expressed as:
        # sum_{a=0}^C C(C,a)*(K-1)^a * sum_{b=0}^min(H,M1 - (C - a))} C(H,b)*(1 + (K-2))^{H-b} * something with M2
        # This is too vague, instead, use a more concrete combinatorial approach

        # Model the positions where S1=S2 (C positions)
        # and where S1 != S2 (H positions)
        # For positions S1=S2:
        #   s matches S1/S2: contributes 0 to hamming distances
        #   s differs: contributes 1 to both hamming distances
        # For positions S1 != S2:
        #   s matches S1: contributes 0 to hamming distance to S1, 1 to S2
        #   s matches S2: contributes 1 to S1, 0 to S2
        #   s differs from both: contributes 1 to both hamming distances

        # Let a: number of positions where S1=S2 and s matches them
        # Let b: number of positions where S1 != S2 and s matches S1
        # Let c: number of positions where S1 != S2 and s matches S2
        # Let d: number of positions where S1 != S2 and s differs from both
        # Then:
        #   a <= C
        #   b + c + d = H
        #   (C - a) + (H - b) <= M1
        #   (C - a) + (H - c) <= M2
        # We need to count all (a, b, c, d) satisfying above constraints

        res = 0

        # Iterate over a
        min_a = max(0, C + H - M1 - H, C + H - M2 - H, C + H - min(M1, M2) - H)
        min_a = max(C + H - M1, C + H - M2, 0)
        max_a = min(C, N)
        # To keep it simple, iterate a from max(C + H - M1, C + H - M2, 0) to min(C, N)
        # Note that:
        # (C - a) + (H - b) <= M1 => a >= (C + H - M1) - b
        # Similarly for M2

        # To make it efficient, precompute possible a
        lower_a = max(C + H - M1, C + H - M2, 0)
        upper_a = C
        for a in range(lower_a, upper_a +1):
            # Now, given a, we have (C - a) + (H - b) <= M1
            #                (C - a) + (H - c) <= M2
            # Let's rearrange:
            # b >= C + H - M1 - a
            # c >= C + H - M2 - a
            min_b = max(0, C + H - M1 - a)
            min_c = max(0, C + H - M2 - a)
            # Also, b + c <= H + d = H
            # So c <= H - b
            # Similarly, b <= H - c
            # Iterate over b
            max_b = min(H, M1 - (C - a))
            for b in range(min_b, min(H, M1 - (C - a)) +1):
                # For each b, c must be >= max(C + H - M2 - a, 0)
                # and <= min(H - b, M2 - (C - a))
                current_min_c = max(min_c, C + H - M2 -a - b)
                current_min_c = max(current_min_c, 0)
                current_max_c = min(H - b, M2 - (C - a))
                if current_max_c < 0 or current_min_c > current_max_c:
                    continue
                # Number of c is current_max_c - current_min_c +1
                # But need to iterate over c
                for c in range(max(current_min_c, 0), min(current_max_c, M2 - (C - a)) +1):
                    d = H - b - c
                    if d <0 or (C - a) + (H - b) > M1 or (C - a) + (H - c) > M2:
                        continue
                    ways_a = comb(C, a, factorial, inv_fact) * pow(K-1, C -a, MOD) % MOD
                    ways_b = comb(H, b, factorial, inv_fact)
                    ways_c = comb(H - b, c, factorial, inv_fact)
                    ways_d = pow(K - 2, d, MOD)
                    total_ways = ways_a * ways_b % MOD
                    total_ways = total_ways * ways_c % MOD
                    total_ways = total_ways * ways_d % MOD
                    res = (res + total_ways) % MOD
        # Number of S1,S2 pairs with hamming distance H is C(N,H)*(K-1)^H
        total_pairs = comb(N, H, factorial, inv_fact) * pow(K -1, H, MOD) % MOD
        # Each s is counted res times, but we have K^N possible s
        # From the analysis, res is the number of s for fixed s, but total sum is K^N * total_pairs * (res / K^N)
        # So final answer is total_pairs * res
        # Wait, not exactly: res is the number of S1,S2 for fixed s, and sum over s is k^N * res
        # But the total sum we want is sum_{S1,S2} |{s}|
        # Which is k^N * (number of S1,S2 with hamming distance H and s within both Hamming balls)
        # But res is the number of S1,S2 with hamming distance H and s within both Hamming balls for fixed s
        # So total sum is K^N * res
        answer = res
        print(f"Case #{t}: {answer}")

# The Python code is provided above within the code block.