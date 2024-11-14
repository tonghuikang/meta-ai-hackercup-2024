MOD = 998244353

T = int(input())
for tc in range(1, T +1):
    W, G, L = map(int, input().split())
    if L ==0:
        E = W - G
    else:
        D = W - G
        E = 2 * D * L + L * L
    res = E % MOD
    print(f"Case #{tc}: {res}")