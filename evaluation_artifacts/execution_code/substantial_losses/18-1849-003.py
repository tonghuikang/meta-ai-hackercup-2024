# Python code to solve the problem

MOD = 998244353

def solve():
    import sys
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        W_str, G_str, L_str = sys.stdin.readline().strip().split()
        W = int(W_str)
        G = int(G_str)
        L = int(L_str)
        delta = W - G
        E = delta * (2 * L +1)
        result = E % MOD
        print(f"Case #{tc}: {result}")