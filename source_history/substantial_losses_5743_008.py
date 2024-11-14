import sys

MOD = 998244353

def main():
    import sys
    import math
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        W_str, G_str, L_str = sys.stdin.readline().strip().split()
        W = int(W_str)
        G = int(G_str)
        L = int(L_str)
        delta = W - G
        factor = (2 * L + 1) % MOD
        delta_mod = delta % MOD
        expected = (delta_mod * factor) % MOD
        print(f"Case #{case}: {expected}")

if __name__ == "__main__":
    main()