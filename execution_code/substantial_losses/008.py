import sys

MOD = 998244353

def main():
    import sys
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        W_str, G_str, L_str = sys.stdin.readline().strip().split()
        W = int(W_str)
        G = int(G_str)
        L = int(L_str)
        delta = W - G
        if L ==0:
            E = delta
        else:
            E = delta * (2 * L +1)
        E %= MOD
        print(f"Case #{case}: {E}")

if __name__ == "__main__":
    main()