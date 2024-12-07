import sys
import math

MOD = 10**9 + 7
MAX = 10000

# Precompute factorial and inverse factorial
fact = [1] * (MAX + 1)
for i in range(1, MAX +1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (MAX +1)
inv_fact[MAX] = pow(fact[MAX], MOD-2, MOD)
for i in range(MAX, 0, -1):
    inv_fact[i-1] = inv_fact[i] * i % MOD

def comb(n, k):
    if n <k or k <0:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n -k] % MOD

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    idx =1
    for test_case in range(1, T+1):
        N = int(data[idx])
        M1 = int(data[idx+1])
        M2 = int(data[idx+2])
        H = int(data[idx+3])
        A = int(data[idx+4])
        idx +=5
        if H > N:
            ans=0
        else:
            t_min = max(H - M1, H - M2, 0)
            t_max = min(N - H, M1, M2)
            if t_min > t_max:
                ans=0
            else:
                total =0
                for t in range(t_min, t_max +1):
                    C_NH_t = comb(N - H, t)
                    pow_A1_t = pow(A -1, t, MOD)
                    u_min = max(H - M1 + t,0)
                    v_min = max(H - M2 + t,0)
                    if u_min + v_min > H:
                        continue
                    C_H_u = comb(H, u_min)
                    C_Hu_v = comb(H - u_min, v_min)
                    w = H - u_min - v_min
                    if A ==2:
                        if w ==0:
                            s_count = 1
                        else:
                            # For A=2, s must match S1 or S2 in all differing positions
                            # So when w >0, it's not possible to have valid s
                            continue
                    else:
                        s_count = pow(A -2, w, MOD)
                    term = C_NH_t * pow_A1_t % MOD
                    term = term * C_H_u % MOD
                    term = term * C_Hu_v % MOD
                    term = term * s_count % MOD
                    if A ==2:
                        # When A=2, and w=0, s can match S1 or S2 in H positions
                        # Each valid s corresponds to unique choices
                        # But in case A=2, s_count should actually be 2^{w} when A=2 and w=0 is 1
                        # To handle correctly, need to multiply by 1 when w=0
                        # Already done by s_count =1
                        pass
                    else:
                        pass
                    total = (total + term) % MOD
                # Now, handle A=2 separately for cases where w >0
                # In the primary loop, w >0 are skipped when A=2
                # However, in reality, when A=2 and w >0,
                # the number of s's is 0, so it's correct to skip
                ans = total
        print(f"Case #{test_case}: {ans}")