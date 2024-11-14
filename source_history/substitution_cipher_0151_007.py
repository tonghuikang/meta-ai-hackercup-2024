import sys
import math

import sys
import sys
def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353
    for test_case in range(1, T+1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if ' ' in line:
            E, K = line.rsplit(' ',1)
        else:
            E = line
            K = 1
        K = int(K)
        list_q = []
        assigned = list(E)
        for idx, c in enumerate(E):
            if c == '?':
                list_q.append(idx)
        c = len(list_q)
        pow2 = [1]*(c+1)
        for i in range(1,c+1):
            pow2[i] = pow2[i-1]*2
            if pow2[i] > 10**18:
                pow2[i] = 10**18
        # Assign digits to '?' positions to get Kth lex largest
        ans = assigned.copy()
        for j in range(c):
            pos = list_q[j]
            remaining = c - j -1
            cnt = 1 << remaining
            if cnt >= K:
                ans[pos] = '2'
            else:
                ans[pos] = '1'
                K -= cnt
        E_prime = ''.join(ans)
        # Compute number of decodings
        n = len(E_prime)
        dp = [0]*(n+1)
        dp[n] =1
        for i in range(n-1, -1, -1):
            if E_prime[i] == '0':
                dp[i] =0
            else:
                dp[i] = dp[i+1]
                if i +1 < n:
                    two = E_prime[i:i+2]
                    if '10' <= two <= '26':
                        dp[i] += dp[i+2]
                dp[i] %= MOD
        print(f"Case #{test_case}: {E_prime} {dp[0]%MOD}")

if __name__ == "__main__":
    main()