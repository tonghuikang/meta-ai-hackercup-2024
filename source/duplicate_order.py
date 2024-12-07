MOD = 10**9 + 7

import sys
import sys
import math

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    
    max_N = 0
    test_cases = []
    for _ in range(T):
        N, M1, M2, H, Sigma = map(int, sys.stdin.readline().split())
        test_cases.append((N, M1, M2, H, Sigma))
        if N > max_N:
            max_N = N
    
    # Precompute factorial and inverse factorial
    fact = [1] * (max_N + 1)
    for i in range(1, max_N +1):
        fact[i] = fact[i-1] * i % MOD
    inv_fact = [1] * (max_N +1)
    inv_fact[max_N] = pow(fact[max_N], MOD-2, MOD)
    for i in range(max_N-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    def comb(n, k):
        if k <0 or k >n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n -k] % MOD
    
    for tc in range(1, T+1):
        N, M1, M2, H, Sigma = test_cases[tc-1]
        if H > N:
            answer = 0
            print(f"Case #{tc}: {answer}")
            continue
        C_N_H = comb(N, H)
        total_S1_S2 = C_N_H * pow(Sigma, N, MOD) % MOD
        total_S1_S2 = total_S1_S2 * pow(Sigma -1, H, MOD) % MOD
        # Now compute the number of s for a given S1,S2 with hamming distance H
        # Which is sum over x=0 to N-H of C(N-H, x)*(Sigma-1)^x *
        # sum over y= max(x+H - M1,0) to min(M2 -x, H) of C(H,y)*(Sigma-2)^{H - y}
        # and ensure x + H - y <= M1 and x + y <= M2
        # Precompute powers
        sigma_minus1 = Sigma -1
        sigma_minus2 = Sigma -2
        pow_sigma_minus1 = [1]*(N - H +1)
        for i in range(1, N - H +1):
            pow_sigma_minus1[i] = pow_sigma_minus1[i-1] * sigma_minus1 % MOD
        pow_sigma_minus2 = [1]*(H +1)
        for i in range(1, H +1):
            pow_sigma_minus2[i] = pow_sigma_minus2[i-1] * sigma_minus2 % MOD
        result = 0
        for x in range(0, min(M1, N - H)+1):
            C_A_x = comb(N - H, x)
            term_A = C_A_x * pow_sigma_minus1[x] % MOD
            # y must satisfy:
            # x + (H - y) <= M1  => y >= x + H - M1
            # x + y <= M2        => y <= M2 - x
            lower_y = max(x + H - M1, 0)
            upper_y = min(M2 - x, H)
            if lower_y > upper_y:
                continue
            lower_y = max(lower_y, 0)
            upper_y = min(upper_y, H)
            if lower_y > upper_y:
                continue
            # Now sum C(H,y) * (Sigma -2)^{H - y} from y=lower_y to y=upper_y
            # Precompute C(H,y) * (Sigma-2)^{H - y}
            # To speed up, iterate y and accumulate
            sum_y = 0
            for y in range(lower_y, upper_y +1):
                C_H_y = comb(H, y)
                term_B = C_H_y * pow_sigma_minus2[H - y] % MOD
                sum_y = (sum_y + term_B) % MOD
            result = (result + term_A * sum_y) % MOD
        # Total sum is total_S1_S2 multiplied by result divided by total_S1_S2
        # But actually, since total_S1_S2 counts all S1,S2, and result counts s per S1,S2,
        # We just need to multiply total_S1_S2 with the ratio (number of s per S1,S2)
        # However, since result is already the number of s per S1,S2, and total_S1_S2 is the number of S1,S2,
        # the total sum is total_S1_S2's number times result
        # Wait no, need to think differently.
        # Actually, for each S1,S2, the number of s is 'result'.
        # So total sum is number of S1,S2 with hamming H multiplied by 'result'.
        # So answer = total_S1_S2_pairs * s_per_pair
        # But 'result' is the number of s per pair
        # So to compute it correctly:
        # 'result' is already the number of s per pair
        # So the total sum is number of S1,S2 with hamming H multiplied by 'result'
        # But 'result' was computed as the average number of s per pair, which is incorrect
        # Correction: 'result' is the number of s per fixed S1,S2
        # So total_sum = total_S1_S2 * s_per_pair
        # But 'result' was computed independently, so likely misinterpretation
        # Instead, 'result' should be the count of s for a single S1,S2
        # Thus, total_sum = total_S1_S2_pairs * s_per_pair
        # However, when we computed 'result', it was the number of s for a given S1,S2
        # So total_sum = C(N,H) * (Sigma)^N * (Sigma-1)^H * result
        # Wait no, 'result' was computed for a single S1,S2
        # So the total_sum is C(N,H) * (Sigma)^N * (Sigma-1)^H * result
        # But we need to make sure 'result' does not include any dependencies
        # It seems the result needs to be multiplied by 1
        # Upon further thought, 'result' was computed as the number of s for a fixed S1,S2,
        # So the total sum is the number of S1,S2 with hamming H multiplied by 'result'
        # Which is C(N,H) * Sigma^N * (Sigma-1)^H * s_per_pair
        # But 's_per_pair' is 'result', but 'result' was computed based on combinatorics
        # Thus the final answer is C(N,H) * Sigma^N * (Sigma-1)^H * s_factor
        # where s_factor is the normalized 'result'
        # It seems the correct final answer is C(N,H) * Sigma^N * (Sigma-1)^H * result
        # So multiply 'result' by the number of S1,S2 with hamming H
        # which is C(N,H) * Sigma^N * (Sigma-1)^H
        # and 'result' is the number of s per S1,S2
        # Therefore:
        total_pairs = C_N_H * pow(Sigma, N, MOD) % MOD
        total_pairs = total_pairs * pow(Sigma -1, H, MOD) % MOD
        answer = total_pairs * result % MOD
        print(f"Case #{tc}: {answer}")

if __name__ == "__main__":
    main()