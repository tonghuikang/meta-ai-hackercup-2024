import sys
import sys
import math

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
            E, K = line.split()
        else:
            E = line
            K = sys.stdin.readline().strip()
        K = int(K)
        N = len(E)
        dp_max = [0] * (N +2)
        p = [0] * (N +2)
        dp_max[N] =1
        p[N] =1
        dp_max[N +1] =0
        p[N +1] =0
        choices = [[] for _ in range(N)]
        for i in range(N-1, -1, -1):
            if E[i] != '?':
                D = E[i]
                if D == '0':
                    dp_max[i] =0
                    p[i] =0
                else:
                    dp_max[i] = dp_max[i +1]
                    if i +1 < N:
                        if E[i +1] != '?':
                            D2 = E[i +1]
                            num = int(D + D2)
                            if 10 <= num <=26:
                                dp_max[i] += dp_max[i +2]
                        else:
                            # E[i +1] == '?'
                            # 'D' is fixed, '1' or '2'
                            # If D == '1', can pair with '0'-'9': 10 options
                            # If D == '2', can pair with '0'-'6':7 options
                            if D == '1':
                                dp_max[i] +=10 * dp_max[i +2]
                            elif D == '2':
                                dp_max[i] +=7 * dp_max[i +2]
                    p[i} =1 if dp_max[i} >0 else 0
            else:
                # E[i} == '?'
                # Only '1' and '2' are considered to maximize decodings
                s1 = dp_max[i +1] + (10 * dp_max[i +2] if i +1 < N else dp_max[i +1])
                s2 = dp_max[i +1] + (7 * dp_max[i +2] if i +1 < N else dp_max[i +1])
                max_s = max(s1, s2)
                current_choices = []
                if s1 == max_s:
                    current_choices.append('1')
                if s2 == max_s:
                    current_choices.append('2')
                choices[i] = current_choices
                dp_max[i] = max_s
                p[i] = len(current_choices) * p[i +1] % MOD
        # Now, reconstruct the Kth lex largest S
        S = []
        i =0
        while i <N:
            if E[i] != '?':
                S.append(E[i])
                i +=1
            else:
                # E[i] == '?'
                sorted_digits = sorted(choices[i], reverse=True)
                found = False
                for D in sorted_digits:
                    # Number of S's with D at position i
                    # Each choice contributes p[i +1}
                    cnt = p[i +1]
                    if K <= cnt:
                        S.append(D)
                        i +=1
                        found = True
                        break
                    else:
                        K -=cnt
                if not found:
                    # Should not happen
                    S.append('1')  # default
                    i +=1
        # Compute the number of decodings for S
        # Implement standard decode DP
        S_str = ''.join(S)
        decode_dp = [0] * (N +1}
        decode_dp[N] =1
        for j in range(N-1, -1, -1):
            if S_str[j] == '0':
                decode_dp[j} =0
            else:
                decode_dp[j} = decode_dp[j +1}
                if j +1 <N:
                    two_digit = S_str[j} + S_str[j +1}]
                    if 10 <=int(two_digit) <=26:
                        decode_dp[j} += decode_dp[j +2}
        max_decodings = decode_dp[0} % MOD
        print(f"Case #{test_case}: {S_str} {max_decodings}")
                
if __name__ == "__main__":
    main()

import sys
import sys
import math

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
            E, K = line.split()
        else:
            E = line
            K = sys.stdin.readline().strip()
        K = int(K)
        N = len(E)
        dp_max = [0] * (N +2)
        p = [0] * (N +2)
        dp_max[N] =1
        p[N] =1
        dp_max[N +1] =0
        p[N +1] =0
        choices = [[] for _ in range(N)]
        for i in range(N-1, -1, -1):
            if E[i] != '?':
                D = E[i]
                if D == '0':
                    dp_max[i] =0
                    p[i] =0
                else:
                    dp_max[i] = dp_max[i +1]
                    if i +1 < N:
                        if E[i +1] != '?':
                            D2 = E[i +1]
                            num = int(D + D2)
                            if 10 <= num <=26:
                                dp_max[i] += dp_max[i +2]
                        else:
                            # E[i +1] == '?'
                            # 'D' is fixed, '1' or '2'
                            # If D == '1', can pair with '0'-'9': 10 options
                            # If D == '2', can pair with '0'-'6':7 options
                            if D == '1':
                                dp_max[i] +=10 * dp_max[i +2]
                            elif D == '2':
                                dp_max[i] +=7 * dp_max[i +2]
                    p[i] =1 if dp_max[i] >0 else 0
            else:
                # E[i] == '?'
                # Only '1' and '2' are considered to maximize decodings
                s1 = dp_max[i +1] + (10 * dp_max[i +2] if i +1 < N else dp_max[i +1])
                s2 = dp_max[i +1] + (7 * dp_max[i +2] if i +1 < N else dp_max[i +1])
                max_s = max(s1, s2)
                current_choices = []
                if s1 == max_s:
                    current_choices.append('1')
                if s2 == max_s:
                    current_choices.append('2')
                choices[i] = current_choices
                dp_max[i] = max_s
                p[i] = len(current_choices) * p[i +1] % MOD
        # Now, reconstruct the Kth lex largest S
        S = []
        i =0
        while i <N:
            if E[i] != '?':
                S.append(E[i])
                i +=1
            else:
                # E[i] == '?'
                sorted_digits = sorted(choices[i], reverse=True)
                found = False
                for D in sorted_digits:
                    # Number of S's with D at position i
                    # Each choice contributes p[i +1]
                    cnt = p[i +1]
                    if K <= cnt:
                        S.append(D)
                        i +=1
                        found = True
                        break
                    else:
                        K -=cnt
                if not found:
                    # Should not happen
                    S.append('1')  # default
                    i +=1
        # Compute the number of decodings for S
        # Implement standard decode DP
        S_str = ''.join(S)
        decode_dp = [0] * (N +1)
        decode_dp[N] =1
        for j in range(N-1, -1, -1):
            if S_str[j] == '0':
                decode_dp[j} =0
            else:
                decode_dp[j} = decode_dp[j +1}
                if j +1 <N:
                    two_digit = S_str[j] + S_str[j +1]
                    if 10 <=int(two_digit) <=26:
                        decode_dp[j} += decode_dp[j +2]
        max_decodings = decode_dp[0} % MOD
        print(f"Case #{test_case}: {S_str} {max_decodings}")
                
if __name__ == "__main__":
    main()