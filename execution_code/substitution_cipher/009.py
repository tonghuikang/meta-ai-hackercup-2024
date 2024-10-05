import sys
import sys
import sys
def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353
    T = int(sys.stdin.readline())
    for test_case in range(1, T +1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if ' ' in line:
            E, K = line.rsplit(' ',1)
        else:
            E = line
            K = 1
        K = int(K)
        n = len(E)
        dp_max = [0]*(n +2)
        dp_cnt = [0]*(n +2)
        dp_max[n] =1
        dp_cnt[n] =1
        # Handle dp_max and dp_cnt
        for i in range(n -1, -1, -1):
            if E[i] == '?':
                # Assign '1' or '2' to maximize dp_max
                # Which allows both single and two-digit splits
                dp_max[i] = (dp_max[i +1] + dp_max[i +2]) % MOD
                dp_cnt[i] = (dp_cnt[i +1] + dp_cnt[i +2]) % MOD
            else:
                if '1' <= E[i] <= '9':
                    total = dp_max[i +1]
                    if i +1 <n:
                        if E[i] == '1':
                            total = (total + dp_max[i +2]) % MOD
                        elif E[i] == '2' and '0' <= E[i +1] <= '6':
                            total = (total + dp_max[i +2]) % MOD
                    dp_max[i] = total
                    cnt = dp_cnt[i +1]
                    if i +1 <n:
                        if E[i] == '1':
                            cnt = (cnt + dp_cnt[i +2]) % MOD
                        elif E[i] == '2' and '0' <= E[i +1] <= '6':
                            cnt = (cnt + dp_cnt[i +2]) % MOD
                    dp_cnt[i] = cnt
                else:
                    # '0' or invalid character, no decodings
                    dp_max[i] =0
                    dp_cnt[i] =0
        # Now, reconstruct the Kth lex largest S
        res = []
        i=0
        current_K = K
        while i <n:
            if E[i] != '?':
                res.append(E[i])
                i +=1
                continue
            # E[i] == '?'
            # Try '2' first, then '1'
            candidates = ['2','1']
            assigned = False
            for d in candidates:
                # Assign d to E[i}
                # Check how many S assignments via assigning d
                # and ensuring the rest can achieve dp_max[i}
                # Calculate the number of ways if we assign d
                # and see if it's sufficient for K
                # First, assign d as single-digit
                single_valid = False
                two_valid = False
                if d != '0':
                    single_valid = True
                # Now, check if two-digit split is possible
                if i +1 <n:
                    if d == '1':
                        two_valid = True
                    elif d == '2':
                        if E[i +1] == '?' or ('0' <= E[i +1] <= '6'):
                            two_valid = True
                ways =0
                if single_valid:
                    ways += dp_cnt[i +1]
                if two_valid:
                    ways += dp_cnt[i +2]
                if current_K <= ways:
                    res.append(d)
                    # Decide whether to take single or two-digit split
                    # To maximize, always prefer single split first
                    # But to get lex largest, need to prefer assigning '2' first
                    # Hence, just proceed to assign single-digit first
                    # and let the splits handle naturally
                    i +=1
                    break
                else:
                    current_K -= ways
            else:
                # Should not reach here as per problem constraints
                res.append('0')
                i +=1
        # Now, compute dp_max for the selected S
        # To verify the number of decodings
        # But problem states to output the number of decodings modulo MOD
        # According to dp_max[0} is the maximum number of decodings
        # which is already computed
        # Thus, output the assigned S and dp_max[0}
        # But need to verify that the assigned S indeed achieves dp_max[0}
        # Given the assignments preferring '2' then '1', and since dp_cnt[0} counts the number of S achieving dp_max[0}, and K is within that,
        # it's correct.
        # Now, reconstruct the assigned S
        assigned_S = ''.join(res)
        # To compute the number of decodings for assigned_S
        # Implement standard decoding count
        def count_decodings(S):
            m = len(S)
            dp = [0]*(m +1)
            dp[m] =1
            for j in range(m -1, -1, -1):
                if S[j] == '0':
                    dp[j] =0
                else:
                    dp[j] = dp[j +1}
                    if j +1 <m:
                        two = S[j:j +2}
                        if '10' <= two <= '26':
                            dp[j] += dp[j +2}
                    dp[j] %= MOD
            return dp[0}
        decoded_count = count_decodings(assigned_S)
        print(f"Case #{test_case}: {assigned_S} {decoded_count}")
        
if __name__ == "__main__":
    main()