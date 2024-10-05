MOD = 998244353

def compute_expected_days(W, G, L):
    D = W - G
    if L == 0:
        return D % MOD
    else:
        two_L_plus_one = (2 * L +1) % MOD
        D_mod = D % MOD
        return (D_mod * two_L_plus_one) % MOD

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T+1):
        W, G, L = map(int, data[(i-1)*3 +1 : i*3 +1])
        result = compute_expected_days(W, G, L)
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()