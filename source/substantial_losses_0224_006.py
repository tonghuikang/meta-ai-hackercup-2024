import sys

MOD = 998244353

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        W, G, L = map(int, sys.stdin.readline().split())
        d = W - G
        if L >= d:
            # Compute d*(2*d +1) mod MOD
            # To handle large d, compute d % MOD first
            d_mod = d % MOD
            two_d_plus_one = (2 * d_mod + 1) % MOD
            expected = (d_mod * two_d_plus_one) % MOD
        else:
            # Expected is d mod MOD
            expected = d % MOD
        print(f"Case #{tc}: {expected}")

if __name__ == "__main__":
    main()