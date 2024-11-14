MOD = 998244353

def solve():
    import sys
    T,*rest = map(int, sys.stdin.read().split())
    for i in range(1, T+1):
        W, G, L = rest[(i-1)*3: i*3]
        delta = W - G
        if L >0:
            term1 = delta % MOD
            term2 = (2 * (L % MOD) +1) % MOD
            E = (term1 * term2) % MOD
        else:
            E = delta % MOD
        print(f"Case #{i}: {E}")