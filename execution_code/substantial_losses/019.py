MOD = 998244353

T = int(input())
for test_case in range(1, T +1):
    W_str, G_str, L_str = input().split()
    W = int(W_str)
    G = int(G_str)
    L = int(L_str)
    if L ==0:
        E = (W - G) % MOD
    else:
        a = (W - G) % MOD
        b = (2 * L +1) % MOD
        E = (a * b) % MOD
    print(f"Case #{test_case}: {E}")