import sys
import sys
import sys
sys.setrecursionlimit(1 << 25)
from sys import stdin
MOD = 998244353

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.read().splitlines()
    T = int(input[0])
    for tc in range(1, T+1):
        E, K = input[tc].split()
        K = int(K)
        n = len(E)
        dp = [0] * (n+1)
        dp[n] = 1
        # To store max decodings from each position
        for i in range(n-1, -1, -1):
            if E[i] == '?':
                digits = [str(d) for d in range(10)]
            else:
                digits = [E[i]]
            total = 0
            for d in digits:
                if d == '0':
                    continue
                total += dp[i+1] if i+1 <= n else 0
            # Check two-digit
            if i+1 < n:
                if E[i] == '?' and E[i+1] == '?':
                    possible = [str(two) for two in range(10,27)]
                elif E[i] == '?':
                    possible = [str(int(E[i+1])+10) for E_i_plus1 in [E[i+1]] for two in [int(E[i+1])+10] if 10 <= two <= 26]
                elif E[i+1] == '?':
                    if E[i] == '1':
                        possible = [str(two) for two in range(10,27)]
                    elif E[i] == '2':
                        possible = [str(two) for two in range(20,27)]
                    else:
                        possible = []
                else:
                    two = int(E[i:i+2])
                    if 10 <= two <= 26:
                        possible = [E[i:i+2]]
                    else:
                        possible = []
                total += len(possible) * dp[i+2]
            dp[i] = total % MOD
        # Now, find the maximum number of decodings
        max_decodings = dp[0] % MOD
        # Now, need to find all uncorrupted strings that achieve max_decodings
        # To find the Kth lex largest, we'll traverse the string, at each '?' pick digits that can lead to max_decodings, in descending order
        res = []
        i = 0
        current_k = K
        while i < n:
            choices = []
            if E[i] == '?':
                digits = [str(d) for d in range(10)]
            else:
                digits = [E[i]]
            # Collect possible choices that can lead to max_decodings
            for d in digits:
                if d == '0':
                    continue
                # Check one-digit
                cnt = dp[i+1] if i+1 <= n else 0
                # Check two-digit
                cnt2 = 0
                if i+1 < n:
                    c1 = d
                    c2 = E[i+1]
                    if c2 == '?':
                        possible_next = []
                        # c1 is fixed
                        if c1 == '1':
                            possible_next = [str(two) for two in range(0,10)]
                        elif c1 == '2':
                            possible_next = [str(two) for two in range(0,7)]
                        else:
                            possible_next = []
                        for pc in possible_next:
                            two = c1 + pc
                            if 10 <= int(two) <= 26:
                                cnt2 += dp[i+2]
                    else:
                        two = c1 + c2
                        if 10 <= int(two) <= 26:
                            cnt2 += dp[i+2]
                total_cnt = (cnt + cnt2) % MOD
                if total_cnt == dp[i]:
                    choices.append(d)
            # Now, sort choices in descending order to get lex largest
            choices.sort(reverse=True)
            # Now, iterate over choices to find which digit to take based on K
            for d in choices:
                # Now, simulate choosing d and calculate the number of strings that follow
                temp = 0
                # One-digit
                cnt = dp[i+1] if i+1 <= n else 0
                # Two-digit
                cnt2 = 0
                if i+1 < n:
                    c1 = d
                    c2 = E[i+1]
                    if c2 == '?':
                        possible_next = []
                        if c1 == '1':
                            possible_next = [str(two) for two in range(0,10)]
                        elif c1 == '2':
                            possible_next = [str(two) for two in range(0,7)]
                        else:
                            possible_next = []
                        for pc in possible_next:
                            two = c1 + pc
                            if 10 <= int(two) <= 26:
                                cnt2 += dp[i+2]
                    else:
                        two = c1 + c2
                        if 10 <= int(two) <= 26:
                            cnt2 += dp[i+2]
                total = (cnt + cnt2) % MOD
                if total >= current_k:
                    res.append(d)
                    i +=1
                    break
                else:
                    current_k -= total
            else:
                # No valid choice found, should not happen
                res.append('0')
                i +=1
        final_str = ''.join(res)
        print(f"Case #{tc}: {final_str} {max_decodings}")

if __name__ == "__main__":
    main()