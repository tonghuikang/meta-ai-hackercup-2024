import sys
import math

MOD = 10**9 + 7

def precompute_factorials(max_n):
    factorial = [1] * (max_n + 1)
    for i in range(1, max_n +1):
        factorial[i] = factorial[i-1] * i % MOD
    inv_fact = [1] * (max_n +1)
    inv_fact[max_n] = pow(factorial[max_n], MOD-2, MOD)
    for i in range(max_n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    return factorial, inv_fact

def comb(n, k, factorial, inv_fact):
    if n < 0 or k < 0 or k > n:
        return 0
    return factorial[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def solve():
    import sys
    from math import comb as math_comb
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
        idx +=5
    factorial, inv_fact = precompute_factorials(max_N)
    for tc in range(1, T+1):
        N, M1, M2, H, Sigma = test_cases[tc-1]
        if H > N or M1 > N or M2 > N:
            print(f"Case #{tc}: 0")
            continue
        K = N - H
        S = Sigma
        # Total number of S1
        total_S1 = pow(S, N, MOD)
        # Number of S2 for each S1 with hamming distance H
        total_pairs = pow(S, N, MOD) * comb(N, H, factorial, inv_fact) % MOD
        total_pairs = comb(N, H, factorial, inv_fact) * pow(S-1, H, MOD) % MOD * pow(S, K, MOD) % MOD
        # Now, for each pair (S1, S2) with hamming distance H, compute the number of s
        # Due to symmetry, we can fix S1 and S2 and compute the count, then multiply by total_pairs / (S^N)
        # But to avoid floating division, we compute directly
        # The number of valid s for a given (S1,S2) is sum over a=0 to K, y=0 to H, w=0 to H
        # such that a + H - y <= M1 and a + H - w <= M2, and y + w <= H + min(M1, M2) - a
        # This is complex, so we'll use inclusion over the possible overlaps
        # Essentially, iterate over z, which is the number of positions where S1=S2 and s differs
        result = 0
        for z in range(0, K+1):
            if z > K:
                break
            # s differs from S1/S2 in z positions where S1=S2
            # Thus, a = z
            max_e = min(H, M1 - z, M2 - z)
            if max_e < 0:
                continue
            # At H differing positions, s can match S1, match S2, or match neither
            # Let e be the number of positions where s matches neither
            for e in range(0, max_e+1):
                # Now, y + w + e = H
                # Also, hamming distance to S1: z + (H - y) <= M1 => y >= H - (M1 - z)
                # hamming distance to S2: z + (H - w) <= M2 => w >= H - (M2 - z)
                y_min = max(0, H - (M1 - z))
                w_min = max(0, H - (M2 - z))
                y_max = H - e
                w_max = H - e
                if y_min > y_max or w_min > w_max:
                    continue
                # y can range from y_min to y_max
                # Similarly for w
                # Number of ways to choose y and w such that y + w + e = H
                # with y >= y_min and w >= w_min and y + w = H - e
                # So y >= y_min, w >= w_min, y + w = H - e
                # Thus y >= y_min and y <= H - e - w_min
                y_start = max(y_min, H - e - w_max)
                y_end = min(y_max, H - e - w_min)
                if y_start > y_end:
                    continue
                count = (y_end - y_start +1)
                # Now, number of ways to choose s for the differing positions:
                # Choose z positions out of K to differ: C(K, z)
                C1 = comb(K, z, factorial, inv_fact)
                # Choose e positions out of H to match neither S1 nor S2: C(H, e)
                C2 = comb(H, e, factorial, inv_fact)
                # For these e positions, s can take (S-2) values
                power_S_minus_2 = pow(S-2, e, MOD)
                # For the remaining H - e positions, s matches S1 or S2
                # Which can be arranged in 2^{H - e} ways
                power_2 = pow(2, H - e, MOD)
                # For z positions, s differs from S1/S2: (S-1)^z
                power_S_minus_1 = pow(S-1, z, MOD)
                total = C1 * C2 % MOD
                total = total * power_S_minus_2 % MOD
                total = total * power_2 % MOD
                total = total * power_S_minus_1 % MOD
                result = (result + total) % MOD
        print(f"Case #{tc}: {result}")
                

if __name__ == "__main__":
    solve()