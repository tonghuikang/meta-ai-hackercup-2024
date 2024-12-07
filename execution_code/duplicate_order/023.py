import sys
import threading

def main():
    import sys
    import math

    MOD = 10**9 +7

    T=int(sys.stdin.readline())
    
    max_N=10000
    # Precompute binomial coefficients up to max_N
    C = [ [0]*(max_N+1) for _ in range(max_N+1)]
    for n in range(max_N+1):
        C[n][0]=1
        for k in range(1,n+1):
            C[n][k]=(C[n-1][k-1] + C[n-1][k])%MOD
    
    for test_case in range(1,T+1):
        line=''
        while line.strip()=='':
            line=sys.stdin.readline()
        N,M1,M2,H,S = map(int,line.strip().split())
        A=N - H
        if A <0 or H >N:
            print(f"Case #{test_case}: 0")
            continue
        min_c =0
        max_c = min(A,M1,M2)
        fH=0
        # Precompute powers
        pow_S1 = [1]*(max_c+1)
        for c in range(1,max_c+1):
            pow_S1[c]=pow_S1[c-1]*(S-1)%MOD
        pow_S2 = [1]*(H+1)
        for x in range(1,H+1):
            if S >=2:
                pow_S2[x]=pow_S2[x-1]*(S-2)%MOD
            else:
                pow_S2[x]=0
        for c in range(0, max_c+1):
            C_A_c=C[A][c]
            S1_p_c=pow_S1[c]
            temp_c = C_A_c * S1_p_c % MOD
            # Compute x_lower and x_upper
            x_low = max(0, H - (M1 + M2 - 2*c))
            x_low = max(x_low, 0)
            x_up = min(H, M1 -c, M2 -c)
            if x_up <0:
                continue
            x_up = min(x_up, H)
            if x_low > x_up:
                continue
            for x in range(x_low, x_up+1):
                K = H -x
                tmin = max(0, K - (M1 -c -x))
                tmax = min(K, M2 -c -x)
                if tmax < tmin:
                    continue
                number_t1_t2 = (tmax - tmin +1) % MOD
                C_H_x = C[H][x]
                if S >=2:
                    S2_p_x = pow_S2[x]
                else:
                    if x==0:
                        S2_p_x=1
                    else:
                        S2_p_x=0
                temp_contribution = C_H_x * S2_p_x % MOD
                temp_contribution = temp_contribution * number_t1_t2 % MOD
                fH = (fH + temp_c * temp_contribution) % MOD
        # Now, compute sum= C(N,H)*(S-1)^H * fH * S^{A} % MOD
        if H >N or A <0:
            total=0
        else:
            C_N_H = C[N][H]
            S1_term = pow(S-1, H, MOD)
            S_A_term = pow(S, A, MOD)
            total = C_N_H * S1_term % MOD
            total = total * fH % MOD
            total = total * S_A_term % MOD
        print(f"Case #{test_case}: {total}")

threading.Thread(target=main).start()