MOD = 10**9 + 7

import sys
import sys
import sys

def main():
    import sys
    import sys
    sys.setrecursionlimit(1000000)
    T = int(sys.stdin.readline())
    test_cases = []
    max_N = 0
    for _ in range(T):
        N, M1, M2, H, S = map(int, sys.stdin.readline().split())
        test_cases.append((N, M1, M2, H, S))
        if N > max_N:
            max_N = N
    # Precompute factorial and inv_fact up to max_N
    factorial = [1] * (max_N +1)
    for i in range(1, max_N +1):
        factorial[i] = factorial[i -1] * i % MOD
    inv_fact = [1] * (max_N +1)
    inv_fact[max_N] = pow(factorial[max_N], MOD -2, MOD)
    for i in range(max_N, 0, -1):
        inv_fact[i -1] = inv_fact[i] * i % MOD
    # Precompute inv[y} for y =1 to max_N
    inv = [0] * (max_N +2)
    for y in range(1, max_N +1):
        inv[y] = pow(y, MOD -2, MOD)
    case_num =1
    for N, M1, M2, H, S in test_cases:
        if H > N:
            answer =0
        else:
            answer =0
            min_x =0
            max_x = min(N - H, M1, M2)
            for x in range(min_x, max_x +1):
                C_x = factorial[N - H] * inv_fact[x] % MOD
                C_x = C_x * inv_fact[N - H -x] % MOD
                A = M1 -x
                B = M2 -x
                if A <0 or B <0:
                    continue
                sum_per_x =0
                max_w = min(A, B, H)
                for w in range(0, max_w +1):
                    C_hw = factorial[H] * inv_fact[w] % MOD
                    C_hw = C_hw * inv_fact[H -w] % MOD
                    n = H -w
                    y_min = max(0, H +x - M2)
                    y_max = min(A -w, n)
                    if y_max < y_min:
                        continue
                    # Compute sum_C = sum(C(n,y) for y=y_min..y_max) % MOD
                    if y_min ==0:
                        C_current =1
                    else:
                        if y_min > n:
                            continue
                        C_current = factorial[n] * inv_fact[y_min] % MOD
                        C_current = C_current * inv_fact[n - y_min] % MOD
                    sum_C = C_current
                    for y in range(y_min +1, y_max +1):
                        # C(n,y) = C(n,y-1) * (n - (y-1)) / y
                        C_current = C_current * (n - (y -1)) % MOD
                        C_current = C_current * inv[y] % MOD
                        sum_C = (sum_C + C_current) % MOD
                    p = pow(S -2, w, MOD)
                    term = C_hw * sum_C % MOD
                    term = term * p % MOD
                    sum_per_x = (sum_per_x + term) % MOD
                answer = (answer + C_x * sum_per_x % MOD) % MOD
        print(f"Case #{case_num}: {answer}")
        case_num +=1

if __name__ == "__main__":
    main()