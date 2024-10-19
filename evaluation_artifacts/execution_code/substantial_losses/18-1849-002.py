import sys

def main():
    MOD = 998244353
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        W_str, G_str, L_str = sys.stdin.readline().strip().split()
        W = int(W_str)
        G = int(G_str)
        L = int(L_str)
        if L ==0:
            t = W - G
        else:
            M = W + L - G
            x = W - G
            t = x * (M +1)
        ans = t % MOD
        print(f"Case #{tc}: {ans}")

if __name__ == "__main__":
    main()

import sys

def main():
    MOD = 998244353
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        W_str, G_str, L_str = sys.stdin.readline().strip().split()
        W = int(W_str)
        G = int(G_str)
        L = int(L_str)
        if L ==0:
            t = W - G
        else:
            M = W + L - G
            x = W - G
            t = x * (M +1)
        ans = t % MOD
        print(f"Case #{tc}: {ans}")

if __name__ == "__main__":
    main()