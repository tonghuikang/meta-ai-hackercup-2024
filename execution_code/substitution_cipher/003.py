import sys
import sys
import math

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353

    pow2 = [1] * 21
    for i in range(1,21):
        pow2[i] = pow2[i-1] *2

    for test_case in range(1, T+1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if ' ' in line:
            E, K = line.split()
            K = int(K)
        else:
            E = line
            K = 1
        n = len(E)
        s = list(E)
        # Precompute remaining_q
        remaining_q = [0]*(n+1)
        for i in range(n-1, -1, -1):
            remaining_q[i] = remaining_q[i+1] + (1 if s[i] == '?' else 0)
        # Compute Kth lex largest
        S = s.copy()
        current_K = K
        for i in range(n):
            if S[i] != '?':
                continue
            r = remaining_q[i] -1
            if r <=20:
                cnt2 = pow2[r]
            else:
                cnt2 = 1000001
            if current_K <= cnt2:
                S[i] = '2'
            else:
                S[i] = '1'
                current_K -= cnt2
        # Now, S is the Kth lex largest string
        # Now, compute dp[i}
        dp = [0]*(n+2)
        dp[n] =1
        dp[n+1] =0
        for i in range(n-1, -1, -1):
            if S[i] == '1':
                dp[i] = (dp[i+1] + dp[i+2]) % MOD
            elif S[i] == '2':
                if i+1 <n and S[i+1] in {'1','2','3','4','5','6'}:
                    dp[i] = (dp[i+1] + dp[i+2]) % MOD
                else:
                    dp[i] = dp[i+1] % MOD
            else:
                dp[i] =0
        # Now, find all S strings that replace '?' with '1' or '2' and have dp[0} as computed
        # The count of such S strings is 2^{number of '?'}
        # But need to confirm, based on replacements, but according to our assignment, they all have dp[0}
        # Thus, the number of S strings that achieve max decodings is 1 << m, capped at MOD
        m = E.count('?')
        count_S = pow(2, m, MOD)
        # But m can be up to 100,000 and 2^100,000 is too big, but we only need to count assignments that have dp[0}
        # Since our assignments ensure that, count_S = 2^m
        # However, since we assigned specific digits to achieve the Kth lex largest, the count_S is 2^m
        # But problem wants the number of S strings that have max decodings, which is 2^m
        # However, as per problem, K <= number of such S strings, which is assured
        # Thus, set count_S = pow(2, m, MOD)
        # Since m can be up to 100,000, calculate it via fast exponentiation
        # Implement fast exponentiation
        if m ==0:
            count_S =1
        else:
            count_S =1
            exp =m
            base =2
            while exp >0:
                if exp %2 ==1:
                    count_S = (count_S * base) % MOD
                base = (base * base) % MOD
                exp = exp //2
        # Now, dp[0} is the number of decodings
        decodings = dp[0] % MOD
        final_S = ''.join(S)
        print(f"Case #{test_case}: {final_S} {decodings}")

if __name__ == "__main__":
    main()

import sys
import sys
import math

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353

    pow2 = [1] * 21
    for i in range(1,21):
        pow2[i] = pow2[i-1] *2

    for test_case in range(1, T+1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if ' ' in line:
            E, K = line.split()
            K = int(K)
        else:
            E = line
            K = 1
        n = len(E)
        s = list(E)
        # Precompute remaining_q
        remaining_q = [0]*(n+1)
        for i in range(n-1, -1, -1):
            remaining_q[i] = remaining_q[i+1] + (1 if s[i] == '?' else 0)
        # Compute Kth lex largest
        S = s.copy()
        current_K = K
        for i in range(n):
            if S[i] != '?':
                continue
            r = remaining_q[i] -1
            if r <=20:
                cnt2 = pow2[r]
            else:
                cnt2 = 1000001
            if current_K <= cnt2:
                S[i] = '2'
            else:
                S[i] = '1'
                current_K -= cnt2
        # Now, S is the Kth lex largest string
        # Now, compute dp[i}
        dp = [0]*(n+2)
        dp[n] =1
        dp[n+1] =0
        for i in range(n-1, -1, -1):
            if S[i] == '1':
                dp[i] = (dp[i+1] + dp[i+2]) % MOD
            elif S[i] == '2':
                if i+1 <n and S[i+1] in {'1','2','3','4','5','6'}:
                    dp[i] = (dp[i+1] + dp[i+2]) % MOD
                else:
                    dp[i] = dp[i+1] % MOD
            else:
                dp[i] =0
        # Now, find all S strings that replace '?' with '1' or '2' and have dp[0} as computed
        # The count of such S strings is 2^{number of '?'}
        # But need to confirm, based on replacements, but according to our assignment, they all have dp[0}
        # Thus, the number of S strings that achieve max decodings is 1 << m, capped at MOD
        m = E.count('?')
        count_S = pow(2, m, MOD)
        # But m can be up to 100,000 and 2^100,000 is too big, but we only need to count assignments that have dp[0}
        # Since our assignments ensure that, count_S = 2^m
        # However, problem wants the number of S strings that have max decodings, which is 2^m
        # But as per problem, K <= number of such S strings, which is assured
        # Thus, set count_S = pow(2, m, MOD)
        # Since m can be up to 100,000, calculate it via fast exponentiation
        if m ==0:
            count_S =1
        else:
            count_S =1
            exp =m
            base =2
            while exp >0:
                if exp %2 ==1:
                    count_S = (count_S * base) % MOD
                base = (base * base) % MOD
                exp = exp //2
        # Now, dp[0} is the number of decodings
        decodings = dp[0] % MOD
        final_S = ''.join(S)
        print(f"Case #{test_case}: {final_S} {decodings}")

if __name__ == "__main__":
    main()