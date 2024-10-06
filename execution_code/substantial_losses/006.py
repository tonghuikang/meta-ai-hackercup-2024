MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T=int(data[0])
    inv2 = pow(2, MOD-2, MOD)
    for tc in range(1, T+1):
        W, G, L = map(int, data[3*(tc-1)+1: 3*tc+1])
        d = W - G
        if L ==0:
            E = d % MOD
        elif L >=d:
            E = (d * (2*L +1)) % MOD
        else:
            p = (d * (d +2*L)) % MOD
            E = (p * inv2) % MOD
        print(f"Case #{tc}: {E}")

if __name__ == "__main__":
    main()