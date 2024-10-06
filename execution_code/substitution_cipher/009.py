import sys
import sys
import sys
sys.setrecursionlimit(1 << 25)

MOD = 998244353

def main():
    import sys
    from functools import lru_cache
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        E, K = sys.stdin.readline().strip().split()
        K = int(K)
        n = len(E)
        
        # dp[i] will store the number of ways from i to end
        dp = [0] * (n + 1)
        dp[n] = 1  # Base case
        # To maximize the number of decodings, we need to allow as many options as possible
        for i in range(n -1, -1, -1):
            current_char = E[i]
            total = 0
            # Single digit
            if current_char == '?':
                single_digits = range(1,10)
            else:
                if current_char == '0':
                    single_digits = []
                else:
                    single_digits = [int(current_char)]
            total_single = len(single_digits)
            # Two digits
            if i+1 < n:
                next_char = E[i+1]
                if current_char == '?':
                    first_digits = range(1, 10)
                else:
                    if current_char == '0':
                        first_digits = []
                    else:
                        first_digits = [int(current_char)]
                if next_char == '?':
                    second_digits = range(0,10)
                else:
                    second_digits = [int(next_char)]
                valid_two = 0
                for d1 in first_digits:
                    for d2 in second_digits:
                        num = d1 *10 + d2
                        if 10 <= num <=26:
                            valid_two +=1
                total_two = valid_two
            else:
                total_two =0
            dp[i] = ( (total_single * dp[i+1]) + (total_two * dp[i+2] if i+1 < n else 0) ) % MOD
        max_decodings = dp[0]
        
        # Now, find all S that achieve this max_decodings
        # And find the Kth lex largest among them
        # We need to construct the string greedily from left to right, choosing the largest possible digit
        # that allows enough sequences to reach K
        res = []
        i = 0
        remaining = K
        while i < n:
            candidates = []
            current_char = E[i]
            if current_char == '?':
                possible_digits = [str(d) for d in range(0,10)]
            else:
                possible_digits = [current_char]
            for d in sorted(possible_digits, reverse=True):
                if d == '0':
                    # Single digit '0' is invalid
                    single_valid = False
                else:
                    single_valid = True
                # Check single digit
                single_count = 0
                if single_valid:
                    single_count = dp[i+1]
                # Check two digits
                if i+1 < n:
                    next_char = E[i+1]
                    if next_char == '?':
                        possible_next = [str(d2) for d2 in range(0, 10)]
                    else:
                        possible_next = [next_char]
                    if d == '?':
                        first_digits = range(1,10)
                    else:
                        if d == '0':
                            first_digits = []
                        else:
                            first_digits = [int(d)]
                    valid_two = 0
                    if d != '?':
                        d1 = int(d)
                        if d1 ==0:
                            valid_two =0
                        else:
                            if next_char == '?':
                                valid_two = 17 if d1 ==1 else (6 if d1 ==2 else 0)
                            else:
                                d2 = int(next_char)
                                num = d1 *10 + d2
                                valid_two = 1 if 10 <= num <=26 else 0
                    else:
                        # d is '?', which cannot be, since we're iterating over possible d
                        # Which are 0-9
                        d1 = int(d)
                        if d1 ==0:
                            valid_two =0
                        else:
                            if next_char == '?':
                                valid_two = 17 if d1 ==1 else (6 if d1 ==2 else 0)
                            else:
                                d2 = int(next_char)
                                num = d1 *10 + d2
                                valid_two = 1 if 10 <= num <=26 else 0
                    two_count = valid_two * dp[i+2]
                else:
                    two_count =0
                total_count = single_count + two_count
                if total_count >= remaining:
                    res.append(d)
                    # Now decide if we took single or two
                    # Prefer single first since we are constructing lex largest
                    if single_valid and (single_count >= remaining):
                        i +=1
                    else:
                        remaining -= single_count
                        i +=2
                    break
                else:
                    remaining -= total_count
            else:
                # No valid digit found, should not happen
                res.append('0')
                i +=1
        final_S = ''.join(res)
        print(f"Case #{test_case}: {final_S} {max_decodings}")

if __name__ == "__main__":
    main()