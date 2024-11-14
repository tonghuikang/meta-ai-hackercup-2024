MOD = 998244353

def solve():
    import sys
    T,*rest = map(int, sys.stdin.read().split())
    for tc in range(1, T+1):
        W, G, L = rest[3*(tc-1):3*tc]
        D = W - G
        if L ==0:
            E = D % MOD
        elif L >= D:
            E = (D % MOD) * ((2 * L) % MOD +1 ) % MOD
        else:
            E = (L % MOD) * ((2 * L) % MOD +1 ) % MOD
        print(f"Case #{tc}: {E}")

MOD = 998244353

def solve():
    import sys
    T,*rest = map(int, sys.stdin.read().split())
    for tc in range(1, T+1):
        W, G, L = rest[3*(tc-1):3*tc]
        D = W - G
        if L ==0:
            E = D % MOD
        elif L >= D:
            E = (D % MOD) * ((2 * L) % MOD +1 ) % MOD
        else:
            E = (L % MOD) * ((2 * L) % MOD +1 ) % MOD
        print(f"Case #{tc}: {E}")