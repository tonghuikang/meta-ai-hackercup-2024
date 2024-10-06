MOD = 998244353

T = int(input())
for case_num in range(1, T + 1):
    W_str, G_str, L_str = input().split()
    W = int(W_str)
    G = int(G_str)
    L = int(L_str)
    N = W - G
    K = 2 * L + 1
    E = (N % MOD) * (K % MOD) % MOD
    print(f"Case #{case_num}: {E}")