import sys
import sys
import sys
from sys import stdin
import sys
import sys
from functools import lru_cache

def main():
    import sys
    import sys
    sys.setrecursionlimit(1000000)
    MOD = 998244353
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if not line:
            E, K = '', '1'
        else:
            parts = line.split()
            E = parts[0]
            K = int(parts[1])
        N = len(E)
        # First, find all possible digits replacements to maximize dp[N]
        # We need to calculate for each position, what digits can be assigned to maximize dp
        # To do this, we perform DP from left to right, keeping track of the number of ways,
        # and for each position, keep track of possible digits that can be assigned to maximize the DP
        dp = [0]*(N+1)
        dp[0] = 1
        # To store for each position, which digits are possible to assign to maximize dp[i]
        options = [set() for _ in range(N)]
        for i in range(1, N+1):
            current_options = set()
            # Single digit
            if E[i-1] == '?':
                possible_single = set(str(d) for d in range(1,10))
            else:
                if E[i-1] == '0':
                    possible_single = set()
                else:
                    possible_single = set(E[i-1])
            # Double digit
            if i >=2:
                if E[i-2] == '?':
                    possible_first = set(str(d) for d in range(1,3))  # '1' or '2'
                else:
                    possible_first = set([E[i-2]]) if E[i-2] in '12' else set()
                if E[i-1] == '?':
                    possible_second = set(str(d) for d in range(0,10))
                else:
                    possible_second = set([E[i-1]])
                possible_double = set()
                for d1 in possible_first:
                    for d2 in possible_second:
                        num = int(d1 + d2)
                        if 10 <= num <=26:
                            possible_double.add(d1 + d2)
                if E[i-2] == '?' and E[i-1] == '?':
                    possible_double = set(['10','11','12','13','14','15','16','17','18','19',
                                          '20','21','22','23','24','25','26'])
                elif E[i-2] == '?':
                    current_double = set()
                    d1 = E[i-2]
                    for d2 in possible_second:
                        num = int(d1 + d2)
                        if 10 <= num <=26:
                            current_double.add(d1 + d2)
                    possible_double = current_double
                elif E[i-1] == '?':
                    current_double = set()
                    for d1 in possible_first:
                        for d2 in range(0,10):
                            num = int(d1 + str(d2))
                            if 10 <= num <=26:
                                current_double.add(d1 + str(d2))
                    possible_double = current_double
                # else both are digits, already handled
            # Now, to maximize dp[i], we need to consider which choices maximize the sum
            # dp[i] = (single options) + (double options)
            # To maximize, for each possible single and double options, we need to maximize
            # the contributions
            # However, since dp[i] depends on dp[i-1] and dp[i-2], to maximize dp[i],
            # we need to maximize the number of options
            # So, to maximize dp[i], we should include all possible single and double options
            # Thus, the optimal is to have as many single and double options as possible
            # Therefore, for options at position i-1, we include all possible single digits
            # and for double digits, we mark the possible digits at i-2 and i-1 accordingly
            # But to assign digits later, we need to keep track of which digits can be assigned
            # at each '?'
            # To simplify, we'll assign all possible options and later choose digits that are compatible
            # with maximum dp
            # So here, we just compute dp[i]
            temp = 0
            if E[i-1] == '?':
                temp += dp[i-1] * 9
            elif E[i-1] != '0':
                temp += dp[i-1]
            if i >=2:
                if E[i-2] == '?' and E[i-1] == '?':
                    temp += dp[i-2] * 17  # '10'-'26', 17 options
                elif E[i-2] == '?':
                    if E[i-1] >= '0' and E[i-1] <= '9':
                        if '0' <= E[i-1] <= '6':
                            temp += dp[i-2] * 2  # '1' + d, '2' + d
                        elif '7' <= E[i-1] <= '9':
                            temp += dp[i-2] *1  # '1' + d
                elif E[i-1] == '?':
                    if E[i-2] == '1':
                        temp += dp[i-2] * 9  # '10' to '19'
                    elif E[i-2] == '2':
                        temp += dp[i-2] *6   # '20' to '26'
                else:
                    two = E[i-2:i]
                    if '10' <= two <= '26':
                        temp += dp[i-2]
            dp[i] = temp % MOD
        # Now, find the maximum dp[N]
        max_decodings = dp[N]
        # Now, need to find all S that can reach dp[N] by replacing '?', and select the Kth lex largest
        # To do this, we'll perform a backtracking with choices that can reach max_decodings
        # However, with large N and K up to 1e6, we need an efficient way
        # Instead, we'll reconstruct the possible digits by greedily choosing digits in reverse lex order
        # and use the counts to pick the Kth lex largest
        # To do that, we'll need to compute from left to right the possible digits and the number of ways from that point
        # So, let's compute the number of ways from each position given certain digit assignments
        # We need to do DP from end to start
        dp_rev = [0]*(N+1)
        dp_rev[N] = 1
        for i in range(N-1, -1, -1):
            total = 0
            # Single digit
            if E[i] == '?':
                single_digits = [str(d) for d in range(1,10)]
            else:
                if E[i] == '0':
                    single_digits = []
                else:
                    single_digits = [E[i]]
            for d in single_digits:
                total += dp_rev[i+1]
            # Double digit
            if i+1 < N:
                if E[i] == '?' and E[i+1] == '?':
                    double_digits = [str(a)+str(b) for a in ['1','2'] for b in range(0,10) if 10 <= int(str(a)+str(b)) <=26]
                elif E[i] == '?':
                    if E[i+1] >= '0' and E[i+1] <= '9':
                        if E[i+1] <= '6':
                            double_digits = ['1'+E[i+1], '2'+E[i+1]]
                        else:
                            double_digits = ['1'+E[i+1]]
                    else:
                        double_digits = []
                elif E[i+1] == '?':
                    if E[i] == '1':
                        double_digits = [E[i]+str(b) for b in range(0,10)]
                    elif E[i] == '2':
                        double_digits = [E[i]+str(b) for b in range(0,7)]
                    else:
                        double_digits = []
                else:
                    two = E[i:i+2]
                    if '10' <= two <= '26':
                        double_digits = [two]
                    else:
                        double_digits = []
                for two in double_digits:
                    total += dp_rev[i+2]
            dp_rev[i] = total
        # Now, the total number of ways should match max_decodings
        # Now, we need to reconstruct the lex Kth largest string
        # We'll build the string from left to right, choosing the largest possible digit at each '?'
        # that still allows us to reach the total K
        S = []
        i = 0
        current_dp = dp_rev
        while i < N:
            candidates = []
            # Single digit
            if E[i] == '?':
                single_digits = [str(d) for d in range(1,10)]
            else:
                if E[i] == '0':
                    single_digits = []
                else:
                    single_digits = [E[i]]
            # Double digit would affect this position and the next, handled later
            for d in single_digits:
                candidates.append((d, 'single'))
            # Now, if possible, also consider double digits
            double_candidates = []
            if i+1 < N:
                if E[i] == '?' and E[i+1] == '?':
                    double_digits = [str(a)+str(b) for a in ['1','2'] for b in range(0,10) if 10 <= int(str(a)+str(b)) <=26]
                elif E[i] == '?':
                    if E[i+1] >= '0' and E[i+1] <= '9':
                        if E[i+1] <= '6':
                            double_digits = ['1'+E[i+1], '2'+E[i+1]]
                        else:
                            double_digits = ['1'+E[i+1]]
                    else:
                        double_digits = []
                elif E[i+1] == '?':
                    if E[i] == '1':
                        double_digits = [E[i]+str(b) for b in range(0,10)]
                    elif E[i] == '2':
                        double_digits = [E[i]+str(b) for b in range(0,7)]
                    else:
                        double_digits = []
                else:
                    two = E[i:i+2]
                    if '10' <= two <= '26':
                        double_digits = [two]
                    else:
                        double_digits = []
                for two in double_digits:
                    double_candidates.append(two)
            # Now, sort candidates in reverse to get lex largest first
            candidates_sorted = sorted(candidates, key=lambda x: x[0], reverse=True)
            double_candidates_sorted = sorted(double_candidates, reverse=True)
            # Combine single and double, sorted in reverse
            combined = []
            p1, p2 = 0, 0
            while p1 < len(candidates_sorted) and p2 < len(double_candidates_sorted):
                if candidates_sorted[p1][0] > double_candidates_sorted[p2]:
                    combined.append(candidates_sorted[p1])
                    p1 +=1
                else:
                    combined.append((double_candidates_sorted[p2], 'double'))
                    p2 +=1
            while p1 < len(candidates_sorted):
                combined.append(candidates_sorted[p1])
                p1 +=1
            while p2 < len(double_candidates_sorted):
                combined.append((double_candidates_sorted[p2], 'double'))
                p2 +=1
            # Now, iterate through combined and choose the first that covers K
            for choice, kind in combined:
                if kind == 'single':
                    # Number of ways after choosing this digit
                    ways = dp_rev[i+1]
                    if ways >= K:
                        S.append(choice)
                        i +=1
                        break
                    else:
                        K -= ways
                else:
                    # double
                    ways = dp_rev[i+2]
                    if ways >= K:
                        S.append(choice)
                        i +=2
                        break
                    else:
                        K -= ways
            else:
                # If no break occurred, something is wrong
                break
        final_S = ''.join(S)
        print(f"Case #{test_case}: {final_S} {max_decodings}")

if __name__ == "__main__":
    main()