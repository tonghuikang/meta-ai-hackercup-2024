import sys
import sys
import sys

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    mod = 998244353
    for test_case in range(1, T + 1):
        line = sys.stdin.readline()
        if not line:
            line = sys.stdin.readline()
        E, K = line.strip().split()
        K = int(K)
        N = len(E)
        dp = [0] * (N + 1)
        dp[N] = 1
        choices = [[] for _ in range(N)]
        for i in range(N -1, -1, -1):
            if E[i] != '?':
                res = 0
                if E[i] != '0':
                    res += dp[i +1]
                if i +1 < N:
                    if E[i +1] != '?':
                        num = int(E[i] + E[i +1])
                        if 10 <= num <= 26:
                            res += dp[i +2]
                    else:
                        d = E[i]
                        if d == '1':
                            res += 9 * dp[i +2]
                        elif d == '2':
                            res += 6 * dp[i +2]
                dp[i] = res
            else:
                max_val = -1
                for d in '123456789':
                    temp_val = dp[i +1]  # since d != '0'
                    if i +1 < N:
                        if E[i +1] != '?':
                            num = int(d + E[i +1])
                            if 10 <= num <= 26:
                                temp_val += dp[i +2]
                        else:
                            if d == '1':
                                temp_val += 9 * dp[i +2]
                            elif d == '2':
                                temp_val += 6 * dp[i +2]
                    if temp_val > max_val:
                        max_val = temp_val
                dp[i] = max_val
                for d in '123456789':
                    temp_val = dp[i +1]
                    if i +1 < N:
                        if E[i +1] != '?':
                            num = int(d + E[i +1])
                            if 10 <= num <= 26:
                                temp_val += dp[i +2]
                        else:
                            if d == '1':
                                temp_val += 9 * dp[i +2]
                            elif d == '2':
                                temp_val += 6 * dp[i +2]
                    if temp_val == max_val:
                        choices[i].append(d)
        # Second pass: compute count[i]
        count = [0] * (N +1)
        count[N] = 1
        for i in range(N -1, -1, -1):
            if E[i] != '?':
                if E[i] != '0':
                    c = count[i +1]
                    if i +1 < N:
                        if E[i +1] != '?':
                            num = int(E[i] + E[i +1])
                            if 10 <= num <= 26:
                                c += count[i +2]
                        else:
                            d = E[i]
                            if d == '1':
                                c += 9 * count[i +2]
                            elif d == '2':
                                c += 6 * count[i +2]
                    count[i] = c % mod
                else:
                    count[i] = 0
            else:
                c = 0
                for d in choices[i]:
                    temp = 0
                    if d != '0':
                        temp += count[i +1]
                    if i +1 < N:
                        if E[i +1] != '?':
                            num = int(d + E[i +1])
                            if 10 <= num <= 26:
                                temp += count[i +2]
                        else:
                            if d == '1':
                                temp += 9 * count[i +2]
                            elif d == '2':
                                temp += 6 * count[i +2]
                    c += temp
                    if c >= mod:
                        c -= mod
                count[i] = c % mod
        # Reconstruct the Kth lex largest S
        S = []
        i = 0
        while i < N:
            if E[i] == '?':
                valid_digits = sorted(choices[i], reverse=True)
                for d in valid_digits:
                    temp = 0
                    if d != '0':
                        temp += count[i +1]
                    if i +1 < N:
                        if E[i +1] != '?':
                            num = int(d + E[i +1])
                            if 10 <= num <= 26:
                                temp += count[i +2]
                        else:
                            if d == '1':
                                temp += 9 * count[i +2]
                            elif d == '2':
                                temp += 6 * count[i +2]
                    temp %= mod
                    if temp >= K:
                        S.append(d)
                        i +=1
                        break
                    else:
                        K -= temp
            else:
                S.append(E[i])
                i +=1
        S_str = ''.join(S)
        print(f"Case #{test_case}: {S_str} {dp[0] % mod}")

if __name__ == "__main__":
    main()