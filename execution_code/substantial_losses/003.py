MOD = 998244353

def modinv(a):
    return pow(a, MOD-2, MOD)

T = int(input())
for tc in range(1, T+1):
    W, G, L = map(int, input().split())
    D = W - G
    if L ==0:
        p = D
        q =1
    else:
        p = D * (2*L +1)
        q =1
    # Since q=1, result is p modulo MOD
    result = p % MOD
    print(f"Case #{tc}: {result}")