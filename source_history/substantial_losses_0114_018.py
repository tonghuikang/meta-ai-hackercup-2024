import sys

MOD = 998244353

def readints():
    return list(map(int, sys.stdin.read().split()))

def main():
    data = readints()
    T = data[0]
    for tc in range(1, T+1):
        W, G, L = data[3*(tc-1)+1 : 3*tc+1]
        D = W - G
        if L == 0:
            E = D % MOD
        else:
            E = (D % MOD) * ((2 * L +1) % MOD) % MOD
        print(f"Case #{tc}: {E}")

if __name__ == "__main__":
    main()