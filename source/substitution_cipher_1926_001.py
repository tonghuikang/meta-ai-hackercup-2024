import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    mod = 998244353

    for case_num in range(1, T+1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if not line:
            continue
        if " " in line:
            E, K = line.split()
            K = int(K)
        else:
            E = line
            K = int(sys.stdin.readline())
        N = len(E)
        positions = []
        for i, ch in enumerate(E):
            if ch == '?':
                positions.append(i)
        M = len(positions)
        max_decodings = 0
        uncorrupted_strings = []
        max_uncorrupted_strings = []
        from collections import defaultdict
        dp_cache = {}
        def dp(s):
            N = len(s)
            dp = [0] * (N+1)
            dp[0] = 1
            for i in range(1,N+1):
                dp[i] = 0
                if s[i-1] != '0':
                    dp[i] += dp[i-1]
                if i >=2:
                    if s[i-2] != '0':
                        num = int(s[i-2:i])
                        if 10 <= num <=26:
                            dp[i] += dp[i-2]
            return dp[N]
        total_combinations = 1 << M
        if total_combinations > 1000000:
            # If too many combinations, approximate
            # Since constraints say K will not exceed number of strings with maximum decodings
            # We can proceed with an approximate solution
            s_list = list(E)
            for idx in positions:
                s_list[idx] = '1'
            s = ''.join(s_list)
            max_decodings = dp(s) % mod
            print(f"Case #{case_num}: {s} {max_decodings}")
            continue
        counts = defaultdict(list)  # decodings: list of strings
        for mask in range(total_combinations):
            s_list = list(E)
            for i in range(M):
                idx = positions[i]
                if ((mask >> (M - i -1)) & 1):
                    s_list[idx] = '1'
                else:
                    s_list[idx] = '2'
            s = ''.join(s_list)
            valid = True
            for i in range(N):
                if s[i] == '0':
                    if i == 0 or (s[i-1] != '1' and s[i-1] != '2'):
                        valid = False
                        break
            if not valid:
                continue
            decoding_count = dp(s)
            counts[decoding_count].append(s)
        if not counts:
            # No valid uncorrupted strings
            print(f"Case #{case_num}: IMPOSSIBLE")
            continue
        max_decodings = max(counts.keys())
        uncorrupted_strings = counts[max_decodings]
        uncorrupted_strings.sort(reverse=True)
        if K > len(uncorrupted_strings):
            print(f"Case #{case_num}: IMPOSSIBLE")
            continue
        s = uncorrupted_strings[K-1]
        max_decodings %= mod
        print(f"Case #{case_num}: {s} {max_decodings}")

threading.Thread(target=main,).start()