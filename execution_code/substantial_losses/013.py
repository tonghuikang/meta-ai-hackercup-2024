MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    T_and_cases = input().split()
    T = int(T_and_cases[0])
    for test in range(1, T +1):
        W, G, L = map(int, T_and_cases[3*(test-1)+1:3*(test-1)+4])
        D = W - G
        if L ==0:
            E = D % MOD
        else:
            N = D + L
            # Compute (N * (N +1) //2 ) % MOD
            # To prevent large numbers, compute N mod (2*MOD), since N*(N+1)//2 mod MOD
            N_mod = N % (2 * MOD)
            E = (N_mod * (N_mod +1) //2 ) % MOD
        print(f"Case #{test}: {E}")

if __name__ == "__main__":
    main()