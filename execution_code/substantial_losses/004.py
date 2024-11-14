MOD = 998244353

T = int(input())
for tc in range(1, T +1 ):
    W, G, L = map(int, input().split())
    if L ==0:
        E = W - G
    else:
        E = (W - G) * (2 * L +1)
    print(f"Case #{tc}: {E % MOD}")