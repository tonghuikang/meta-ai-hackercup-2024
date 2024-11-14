MOD = 998244353

T = int(input())
for tc in range(1, T+1):
    W_str, G_str, L_str = input().strip().split()
    W = int(W_str)
    G = int(G_str)
    L = int(L_str)
    diff = (W - G) % MOD
    if L ==0:
        ans = diff
    else:
        twoL_plus1 = (2 * L +1) % MOD
        ans = (diff * twoL_plus1) % MOD
    print(f"Case #{tc}: {ans}")