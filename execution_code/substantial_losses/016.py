MOD = 998244353

def solve():
    import sys
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        W, G, L = map(int, sys.stdin.readline().split())
        if L == 0:
            E = W - G
        else:
            E = (W - G) * (L + 1) + L * L
        result = E % MOD
        print(f"Case #{case}: {result}")