MOD = 998244353

def solve():
    T = int(input())
    for case_num in range(1, T+1):
        W_str, G_str, L_str = input().split()
        W = int(W_str)
        G = int(G_str)
        L = int(L_str)
        delta = W - G
        two_L_plus_one = 2 * L + 1
        E = delta * two_L_plus_one
        E_mod = E % MOD
        print(f"Case #{case_num}: {E_mod}")