import sys
import math

MOD = 10**9 + 7

def precompute_factorials(max_n):
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i-1] * i % MOD
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
    for i in range(max_n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    return fact, inv_fact

def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    idx = 1
    max_N = 0
    test_cases = []
    for _ in range(T):
        N, M1, M2, H, Sigma = map(int, data[idx:idx+5])
        test_cases.append((N, M1, M2, H, Sigma))
        max_N = max(max_N, N)
        idx += 5
    fact, inv_fact = precompute_factorials(max_N)
    for tc_num, (N, M1, M2, H, S) in enumerate(test_cases, 1):
        if H > N:
            result = 0
            print(f"Case #{tc_num}: {result}")
            continue
        # Number of S1, S2 pairs with Hamming distance H
        # For fixed S1, number of S2 with Hamming distance H is comb(N, H) * (S-1)^H
        total_S1_S2 = (pow(S, N, MOD) * comb(N, H, fact, inv_fact) % MOD) * pow(S-1, H, MOD) % MOD
        # Now for each such pair, number of s within M1 of S1 and M2 of S2
        # We need to compute a function f(H) where H is the Hamming distance between S1 and S2
        # For positions where S1 and S2 are same, s must match S1/S2 or differ
        # For positions where S1 and S2 differ, s can match S1, match S2, or differ from both
        # Let k be the number of positions where s matches S1 in the H difference positions (i.e., matches S1 but differs from S2)
        # Similarly, l be the number where s matches S2 but differs from S1
        # m = H - k - l are the positions where s differs from both S1 and S2
        # Total differences from S1: k + m' where m' is number of positions where s differs from S1 in the H differ positions
        # Wait, let's think differently:
        # Let x be the number of positions where s differs from S1 and s differs from S2 among the H differing positions
        # In the other N-H positions, s can either match S1/S2 or differ from both
        # So total differences from S1: (s differs from S1 in H differing positions) + (s differs from S1 in N-H same positions)
        # Similarly for S2
        # It might be better to iterate over possible number of matches in differing and same positions
        # Let's iterate over a: number of differing positions where s matches S1
        # b: number of differing positions where s matches S2
        # c: number of differing positions where s differs from both
        # Then in same positions (N - H), let d: number of same positions where s differs
        # Constraints:
        # a + b + c = H
        # d ≤ N - H
        # Total differences from S1: c + d ≤ M1
        # Total differences from S2: c + d ≤ M2
        # Number of ways:
        # choose a, b, c such that a + b + c = H
        # choose d such that c + d ≤ min(M1, M2)
        # For each a, b, c, d:
        # Ways to choose a, b, c: comb(H, a, b, c) = comb(H, a) * comb(H - a, b)
        # For a given a, b, c, d can be from 0 to min(M1, M2) - c and ≤ N - H
        # For same positions, if s differs, it can be any of S -1 options
        # If s matches, 1 option
        # For differing positions:
        # If s matches S1 (a): 1 option
        # If s matches S2 (b): 1 option
        # If s differs from both (c): S - 2 options
        # For same positions:
        # If s matches (N - H - d positions): 1 option each
        # If s differs (d positions): S -1 options each
        # The total number of s for given a, b, c, d:
        # (1^a) * (1^b) * (S-2)^c * comb(N - H, d) * (S-1)^d
        # We need to sum over a + b + c = H and d such that c + d ≤ min(M1, M2)
        # To optimize, we can iterate over c from 0 to H
        # Then a + b = H - c
        # The number of ways to choose a and b is (H - c + 1) since a can be 0 to H -c and b = H -c -a
        # Then for each c, d can be 0 to min(M1, M2) - c and ≤ N - H
        min_MM = min(M1, M2)
        result = 0
        for c in range(0, H+1):
            max_d = min(min_MM - c, N - H)
            if max_d < 0:
                continue
            # Number of a, b: H - c +1
            num_a_b = H - c +1
            # binomial for c from H
            ways_ab = comb(H, c, fact, inv_fact) * pow(2, H - c, MOD) % MOD
            # but actually a and b are independent (a + b <= H -c), but need a + b = H -c
            # Actually, for fixed c, a + b = H -c, and number of (a,b) is H -c +1
            # For each a,b, same calculation, but since s matches S1 or S2, each pair (a,b) gives same number of s
            # So ways_ab = (H -c +1) ways
            ways_ab = comb(H, c, fact, inv_fact) * pow(S - 2, c, MOD) % MOD
            # Now sum over d
            # Number of choices for d: d from 0 to max_d
            # For each d, comb(N - H, d) * (S -1)^d
            # This is a partial sum of binomial coefficients
            sum_d = 0
            for d in range(0, max_d +1):
                sum_d = (sum_d + comb(N - H, d, fact, inv_fact) * pow(S -1, d, MOD)) % MOD
            # Number of s for this c: (1)^a * (1)^b * (S-2)^c * sum_d
            # Number of s: (S-2)^c * sum_d
            ways_s = pow(S -2, c, MOD) * sum_d % MOD
            # Number of (a,b) is H -c +1
            ways_ab = H - c +1
            contrib = ways_ab * ways_s % MOD
            result = (result + contrib) % MOD
        # Now total_S1_S2 * result
        # Wait, double check:
        # Actually, the number of s is already per pair S1, S2, and total_S1_S2 counts all such pairs
        # So the total sum over S1, S2, and s is total_S1_S2 * number of s per pair
        # However, the number of s per pair depends on H, so we compute:
        # total_S1_S2 is the number of (S1, S2)
        # For each such pair, number of s is computed as above
        # So the total answer is total_S1_S2 * ways_s per pair
        # But in the above loop, result computed ways_s multiplied by ways_ab, which counts for all s
        # Since all pairs with distance H are symmetric, result is the number of s per pair multiplied by total_S1_S2 / number_of_pairs?
        # Wait, confusion here.
        # Rethink:
        # For a fixed H, the total number is number of S1,S2 with h(S1,S2)=H multiplied by number of s for each S1,S2
        # Since for all pairs with same H, number of s is the same (depends only on H)
        # So actually, compute the number of s for a single S1,S2 with h(S1,S2)=H, then multiply by total_S1_S2
        # To compute number of s for given H:
        # Similar to result above without multiplying by ways_ab
        # So redo:
        # Compute number of s for a given H
        # Using the previous approach without ways_ab
        # So let's compute separate
        # Redefine:
        num_s = 0
        for c in range(0, H+1):
            max_d = min(min_MM - c, N - H)
            if max_d < 0:
                continue
            # Number of ways to choose a and b: a + b = H -c, which is H -c +1
            # Number of s for this c: (S-2)^c * sum_{d=0}^{max_d} comb(N - H, d) * (S -1)^d
            ways_s_c = pow(S -2, c, MOD) * 1
            # sum_d = sum_{d=0}^{max_d} comb(N - H, d) * (S -1)^d
            # which is the same as sum_d computed earlier
            sum_d = 0
            for d in range(0, max_d +1):
                sum_d = (sum_d + comb(N - H, d, fact, inv_fact) * pow(S -1, d, MOD)) % MOD
            ways_s_c = pow(S -2, c, MOD) * sum_d % MOD
            # Number of (a,b) with a + b = H -c: H -c +1
            num_a_b = H -c +1
            num_s = (num_s + num_a_b * ways_s_c) % MOD
        total = (comb(N, H, fact, inv_fact) * pow(S -1, H, MOD) % MOD) * num_s % MOD
        # But this needs to be multiplied by S^N for S1 choices, divided by S^N since total_S1_S2 counts S1 and S2
        # It's unclear, let's refer to the initial total_S1_S2 and multiplier
        # Alternatively, refer to the preanalyse: total_S1_S2 = S^N * comb(N, H) * (S-1)^H
        # And num_s is the number of s for a given pair
        # So total answer is total_S1_S2 * num_s * pow(S, -N, MOD) modulo MOD
        # Because for each S1, there are comb(N, H) * (S-1)^H S2
        # And num_s is for each S1, S2 pair
        # So the final answer is S^N * comb(N, H) * (S-1)^H * num_s modulo MOD
        total = (pow(S, N, MOD) * comb(N, H, fact, inv_fact) % MOD) * pow(S -1, H, MOD) % MOD
        total = total * num_s % MOD
        print(f"Case #{tc_num}: {total}")