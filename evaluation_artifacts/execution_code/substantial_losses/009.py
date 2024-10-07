MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    for tc in range(1, T+1):
        W = int(data[3*(tc-1)+1])
        G = int(data[3*(tc-1)+2])
        L = int(data[3*(tc-1)+3])
        S = W - G
        E = (S % MOD) * ((2 * L +1) % MOD) % MOD
        print(f"Case #{tc}: {E}")