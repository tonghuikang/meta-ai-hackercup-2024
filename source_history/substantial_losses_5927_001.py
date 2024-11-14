MOD = 998244353

T = int(input())  # Number of test cases

for case_num in range(1, T + 1):
    W_str, G_str, L_str = input().split()
    W = int(W_str)
    G = int(G_str)
    L = int(L_str)

    # Compute (W - G) % MOD
    A = (W - G) % MOD

    # Compute (2 * L + 1) % MOD
    B = (2 * L + 1) % MOD

    # Compute Expected Time E = (A * B) % MOD
    E = (A * B) % MOD

    print(f"Case #{case_num}: {E}")