MOD = 998244353

def solve():
    T = int(input())
    for case_num in range(1, T+1):
        W_str, G_str, L_str = input().strip().split()
        W = int(W_str)
        G = int(G_str)
        L = int(L_str)
        delta = (W - G) % MOD
        coef = (2 * L + 1) % MOD
        ans = (delta * coef) % MOD
        print(f"Case #{case_num}: {ans}")