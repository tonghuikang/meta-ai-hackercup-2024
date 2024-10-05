import sys

MOD = 998244353

def mod_mul(a, b, mod):
    return (a % mod) * (b % mod) % mod

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T=int(data[0])
    for tc in range(1,T+1):
        W=int(data[3*(tc-1)+1])
        G=int(data[3*(tc-1)+2])
        L=int(data[3*(tc-1)+3])
        D = W - G
        if L <0:
            L=0
        two_L_plus_one = (2 * L +1) % MOD
        D_mod = D % MOD
        E = mod_mul(D_mod, two_L_plus_one, MOD)
        print(f"Case #{tc}: {E}")

if __name__ == "__main__":
    main()