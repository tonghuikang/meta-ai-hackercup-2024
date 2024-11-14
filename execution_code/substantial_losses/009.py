MOD = 998244353

def solve():
    import sys
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        W, G, L = map(int, sys.stdin.readline().split())
        D = W - G
        if L ==0:
            E = D % MOD
        else:
            N = D + L
            # Compute (N * (N +1)) //2 % MOD
            # To compute (N mod MOD) * ((N +1) mod MOD) * inv2 mod MOD
            N_mod = N % MOD
            N_plus1_mod = (N +1) % MOD
            inv2 = (MOD +1)//2
            E = (N_mod * N_plus1_mod) % MOD
            E = (E * inv2) % MOD
        print(f"Case #{tc}: {E}")

MOD = 998244353

def solve():
    import sys
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        W, G, L = map(int, sys.stdin.readline().split())
        D = W - G
        if L ==0:
            E = D % MOD
        else:
            N = D + L
            # Compute (N * (N +1)) //2 % MOD
            # To compute (N mod MOD) * ((N +1) mod MOD) * inv2 mod MOD
            N_mod = N % MOD
            N_plus1_mod = (N +1) % MOD
            inv2 = (MOD +1)//2
            E = (N_mod * N_plus1_mod) % MOD
            E = (E * inv2) % MOD
        print(f"Case #{tc}: {E}")