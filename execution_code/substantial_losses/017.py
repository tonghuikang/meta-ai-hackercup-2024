MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    T_and_cases = input().split()
    T = int(T_and_cases[0])
    for tc in range(1, T+1):
        W_str, G_str, L_str = T_and_cases[3*(tc-1)+1:3*tc+1]
        W = int(W_str)
        G = int(G_str)
        L = int(L_str)
        d = W - G
        E = (d % MOD) * ((2 * (L % MOD) +1) % MOD) % MOD
        print(f"Case #{tc}: {E}")

if __name__ == "__main__":
    main()