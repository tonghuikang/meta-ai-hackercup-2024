MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T+1):
        W, G, L = map(int, data[3*(i-1)+1:3*i+1])
        k = W - G
        E = k * (2 * L +1)
        result = E % MOD
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()