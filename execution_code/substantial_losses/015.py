MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    T, *rest = map(int, input().split())
    for tc in range(1, T+1):
        W, G, L = rest[(tc-1)*3:(tc)*3]
        D = W - G
        if L ==0:
            E = D
        else:
            two_L_plus1 = (2 * L +1) % MOD
            D_mod = D % MOD
            E = (D_mod * two_L_plus1) % MOD
        print(f"Case #{tc}: {E}")

# Example usage:
# If you were to run this script, it would read from standard input.

# Test Input:
# 5
# 201 200 1
# 185 183 2
# 250 180 0
# 77665544332211 11223344556677 0
# 83716485936440 64528193749358 1938563682

# Expected Output:
# Case #1: 3
# Case #2: 10
# Case #3: 70
# Case #4: 53884207
# Case #5: 306870714