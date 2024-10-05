import sys
import sys
import sys
sys.setrecursionlimit(1 << 25)

MOD = 998244353

def solve():
    import sys
    import sys
    from sys import stdin
    from collections import defaultdict
    T = int(stdin.readline())
    for test_case in range(1, T+1):
        line = stdin.readline().strip()
        if not line:
            line = stdin.readline().strip()
        E, K = line.split()
        K = int(K)
        N = len(E)
        DP = [0]*(N+1)
        DP[N] =1
        choices = [set() for _ in range(N)]
        for i in range(N-1, -1, -1):
            if E[i] == '?':
                max_val = -1
                candidate_digits = set()
                # If E[i+1] is '?', set E[i] to '1' or '2'
                if i+1 < N and E[i+1] == '?':
                    # To maximize, choose '1' and '2'
                    possible_digits = ['1','2']
                    temp = DP[i+1] + DP[i+2] if i+2 <=N else DP[i+1]
                    choices[i].update(possible_digits)
                    DP[i] = DP[i+1] + DP[i+2]
                else:
                    # E[i+1] is a digit or out of range
                    max_temp = -1
                    for d in '123456789':
                        single = DP[i+1] if d != '0' else 0
                        two = 0
                        if i+1 <N:
                            if E[i+1] == '?':
                                if d == '1' or d == '2':
                                    two = DP[i+2] if i+2 <=N else 0
                            else:
                                two_digit = int(d + E[i+1])
                                if 10 <= two_digit <=26:
                                    two = DP[i+2] if i+2 <=N else 0
                        temp = single + two
                        if temp > max_temp:
                            max_temp = temp
                            candidate_digits = {d}
                        elif temp == max_temp:
                            candidate_digits.add(d)
                    DP[i] = max_temp
                    choices[i].update(candidate_digits)
            else:
                d = E[i]
                if d == '0':
                    single =0
                else:
                    single = DP[i+1]
                two =0
                if i+1 <N:
                    if E[i+1] == '?':
                        if d == '1' or d == '2':
                            two = DP[i+2] if i+2 <=N else 0
                    else:
                        two_digit = int(d + E[i+1])
                        if 10 <= two_digit <=26:
                            two = DP[i+2] if i+2 <=N else 0
                DP[i] = single + two
        # Now reconstruct the Kth lex largest string
        result = []
        i=0
        while i <N:
            if E[i] != '?':
                result.append(E[i])
                i +=1
            else:
                possible_digits = sorted(choices[i], reverse=True)
                for d in possible_digits:
                    # Calculate the number of decodings if we choose this digit
                    temp =0
                    if d != '0':
                        temp += DP[i+1]
                    if i+1 <N:
                        if E[i+1] == '?':
                            if d == '1' or d == '2':
                                temp += DP[i+2]
                        else:
                            two_digit = int(d + E[i+1])
                            if 10 <= two_digit <=26:
                                temp += DP[i+2]
                    if K <= temp:
                        result.append(d)
                        i +=1
                        break
                    else:
                        K -=temp
        # Now compute DP[0} modulo MOD
        max_decodings = DP[0] % MOD
        uncorrupted_string = ''.join(result)
        print(f"Case #{test_case}: {uncorrupted_string} {max_decodings}")

import sys
import sys
import sys
sys.setrecursionlimit(1 << 25)

MOD = 998244353

def solve():
    import sys
    import sys
    from sys import stdin
    from collections import defaultdict
    T = int(stdin.readline())
    for test_case in range(1, T+1):
        line = stdin.readline().strip()
        if not line:
            line = stdin.readline().strip()
        E, K = line.split()
        K = int(K)
        N = len(E)
        DP = [0]*(N+1)
        DP[N] =1
        choices = [set() for _ in range(N)]
        for i in range(N-1, -1, -1):
            if E[i] == '?':
                max_val = -1
                candidate_digits = set()
                # If E[i+1] is '?', set E[i] to '1' or '2'
                if i+1 < N and E[i+1] == '?':
                    # To maximize, choose '1' and '2'
                    possible_digits = ['1','2']
                    temp = DP[i+1] + DP[i+2] if i+2 <=N else DP[i+1]
                    choices[i].update(possible_digits)
                    DP[i] = DP[i+1] + DP[i+2]
                else:
                    # E[i+1] is a digit or out of range
                    max_temp = -1
                    for d in '123456789':
                        single = DP[i+1] if d != '0' else 0
                        two = 0
                        if i+1 <N:
                            if E[i+1] == '?':
                                if d == '1' or d == '2':
                                    two = DP[i+2] if i+2 <=N else 0
                            else:
                                two_digit = int(d + E[i+1])
                                if 10 <= two_digit <=26:
                                    two = DP[i+2] if i+2 <=N else 0
                        temp = single + two
                        if temp > max_temp:
                            max_temp = temp
                            candidate_digits = {d}
                        elif temp == max_temp:
                            candidate_digits.add(d)
                    DP[i] = max_temp
                    choices[i].update(candidate_digits)
            else:
                d = E[i]
                if d == '0':
                    single =0
                else:
                    single = DP[i+1]
                two =0
                if i+1 <N:
                    if E[i+1] == '?':
                        if d == '1' or d == '2':
                            two = DP[i+2] if i+2 <=N else 0
                    else:
                        two_digit = int(d + E[i+1])
                        if 10 <= two_digit <=26:
                            two = DP[i+2] if i+2 <=N else 0
                DP[i] = single + two
        # Now reconstruct the Kth lex largest string
        result = []
        i=0
        while i <N:
            if E[i] != '?':
                result.append(E[i])
                i +=1
            else:
                possible_digits = sorted(choices[i], reverse=True)
                for d in possible_digits:
                    # Calculate the number of decodings if we choose this digit
                    temp =0
                    if d != '0':
                        temp += DP[i+1]
                    if i+1 <N:
                        if E[i+1] == '?':
                            if d == '1' or d == '2':
                                temp += DP[i+2]
                        else:
                            two_digit = int(d + E[i+1])
                            if 10 <= two_digit <=26:
                                temp += DP[i+2]
                    if K <= temp:
                        result.append(d)
                        i +=1
                        break
                    else:
                        K -=temp
        # Now compute DP[0} modulo MOD
        max_decodings = DP[0] % MOD
        uncorrupted_string = ''.join(result)
        print(f"Case #{test_case}: {uncorrupted_string} {max_decodings}")