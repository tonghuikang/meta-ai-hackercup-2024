import sys
import sys
import sys
import sys
def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353
    for test_case in range(1, T +1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if not line:
            E, K = '',0
        else:
            parts = line.split()
            E = parts[0]
            K = int(parts[1])
        N = len(E)
        dp = [0]*(N+1)
        dp[N] =1
        choices = [[] for _ in range(N)]
        for i in range(N-1, -1, -1):
            if E[i] == '?':
                max_count =0
                possible_digits = []
                for d in '1','2','3','4','5','6','7','8','9':
                    cnt =0
                    if d != '0':
                        cnt += dp[i+1]
                    if i +1 < N:
                        if d == '1':
                            if E[i+1] == '?':
                                cnt += 10 * dp[i+2]
                            else:
                                val = int(d + E[i+1])
                                if 10 <= val <=19:
                                    cnt += dp[i+2]
                        elif d == '2':
                            if E[i+1] == '?':
                                cnt +=7 * dp[i+2]
                            else:
                                val = int(d + E[i+1])
                                if 20 <= val <=26:
                                    cnt += dp[i+2]
                    if cnt > max_count:
                        max_count = cnt
                        possible_digits = [d]
                    elif cnt == max_count:
                        possible_digits.append(d)
                dp[i] = min(max_count,1_000_001)
                choices[i] = possible_digits
            else:
                if E[i] == '0':
                    dp[i] =0
                else:
                    cnt = dp[i+1]
                    if i +1 <N:
                        if E[i+1] == '?':
                            d1 = E[i]
                            if d1 == '1':
                                cnt +=10 * dp[i+2]
                            elif d1 == '2':
                                cnt +=7 * dp[i+2]
                        else:
                            val = int(E[i] + E[i+1])
                            if 10 <= val <=26:
                                cnt +=dp[i+2]
                    dp[i] = min(cnt,1_000_001)
        # Now reconstruct
        s = []
        i =0
        K_current = K
        while i <N:
            if E[i] == '?':
                # Choose digits from '9' to '0' that are in choices[i]
                for d in sorted(choices[i], reverse=True):
                    cnt =0
                    if d != '0':
                        cnt += dp[i+1]
                    if i +1 <N:
                        if d == '1':
                            if E[i+1] == '?':
                                cnt +=10 * dp[i+2]
                            else:
                                val = int(d + E[i+1])
                                if 10 <= val <=19:
                                    cnt +=dp[i+2]
                        elif d == '2':
                            if E[i+1] == '?':
                                cnt +=7 * dp[i+2]
                            else:
                                val = int(d + E[i+1])
                                if 20 <= val <=26:
                                    cnt +=dp[i+2]
                    cnt = min(cnt,1_000_001)
                    if K_current <= cnt:
                        s.append(d)
                        i +=1
                        break
                    else:
                        K_current -= cnt
            else:
                s.append(E[i])
                i +=1
        # Now compute the total number of decodings for s
        # To compute dp_final for s
        s_str = ''.join(s)
        dp_final = [0]*(N+1)
        dp_final[N] =1
        for i in range(N-1, -1, -1):
            if s_str[i] == '0':
                dp_final[i] =0
            else:
                dp_final[i] = dp_final[i+1]
                if i +1 <N:
                    val = int(s_str[i:i+2])
                    if 10 <= val <=26:
                        dp_final[i] += dp_final[i+2]
                if dp_final[i] >1_000_000:
                    dp_final[i] =1_000_001
        total_decodings = dp_final[0] % MOD
        print(f"Case #{test_case}: {s_str} {total_decodings}")
if __name__ == "__main__":
    main()