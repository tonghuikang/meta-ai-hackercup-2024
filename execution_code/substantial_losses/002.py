MOD = 998244353

def solve():
    import sys
    T=int(sys.stdin.readline())
    for tc in range(1,T+1):
        W,G,L = map(int, sys.stdin.readline().split())
        D = W - G
        if L ==0:
            E = D
        else:
            E = (2 * L +1) * D
        E = E % MOD
        print(f"Case #{tc}: {E}")