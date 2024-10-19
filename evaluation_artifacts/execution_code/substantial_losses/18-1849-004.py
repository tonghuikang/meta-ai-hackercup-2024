MOD = 998244353

def solve():
    import sys
    T,*rest = map(int, sys.stdin.read().split())
    for i in range(1,T+1):
        W, G, L = rest[3*(i-1):3*i]
        if L ==0:
            E = (W - G) % MOD
        else:
            diff = W - G
            factor = (2 * L +1) % MOD
            E = (diff % MOD) * factor % MOD
        print(f"Case #{i}: {E}")