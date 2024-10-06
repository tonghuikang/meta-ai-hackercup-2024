import sys

MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    for test_case in range(1, T + 1):
        W = int(data[3 * (test_case - 1) + 1])
        G = int(data[3 * (test_case - 1) + 2])
        L = int(data[3 * (test_case - 1) + 3])
        
        if L == 0:
            E = W - G
        else:
            E = (W - G) * (2 * L + 1)
        
        E_mod = E % MOD
        print(f"Case #{test_case}: {E_mod}")

if __name__ == "__main__":
    main()