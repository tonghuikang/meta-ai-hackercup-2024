MOD = 998244353

def solve():
    import sys
    T=int(sys.stdin.readline())
    for tc in range(1,T+1):
        W,G,L=map(int, sys.stdin.readline().split())
        d=W-G
        e = (d % MOD) * ((2*(L % MOD) +1) % MOD) % MOD
        print(f"Case #{tc}: {e}")