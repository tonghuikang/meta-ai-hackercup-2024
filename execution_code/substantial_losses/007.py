import sys

MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    T, *rest = input().split()
    T = int(T)
    for tc in range(1, T+1):
        W, G, L = map(int, rest[(tc-1)*3:tc*3])
        if L ==0:
            E = W - G
        else:
            E = (W - G) * (W + 2 * L - G)
        E_mod = E % MOD
        print(f"Case #{tc}: {E_mod}")

if __name__ == "__main__":
    main()

import sys

MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    T, *rest = input().split()
    T = int(T)
    for tc in range(1, T+1):
        W, G, L = map(int, rest[(tc-1)*3:tc*3])
        if L ==0:
            E = W - G
        else:
            E = (W - G) * (W + 2 * L - G)
        E_mod = E % MOD
        print(f"Case #{tc}: {E_mod}")

if __name__ == "__main__":
    main()