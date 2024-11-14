import sys
import threading
def main():
    import sys
    import bisect

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if not line:
            break
        if ' ' in line:
            E, K = line.strip().split()
            K = int(K)
        else:
            E = line.strip()
            line = sys.stdin.readline().strip()
            K = int(line)
        s = E
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        mod = 998244353

        # For positions with '?', we store the digits that can be used to maximize decodings
        choices = [''] * n  # Possible choices at each position
        max_decodings = None

        # First pass to compute the maximum number of decodings and fill choices
        from collections import defaultdict
        dp_choices = [set() for _ in range(n + 1)]
        dp_choices[0].add('')
        for i in range(n):
            dp[i + 1] = 0
            temp_set = set()
            if s[i] == '?':
                single_digits = [str(d) for d in range(1, 10)]
            else:
                if s[i] == '0':
                    single_digits = []
                else:
                    single_digits = [s[i]]

            for d in single_digits:
                if dp[i] > 0:
                    dp[i + 1] = (dp[i + 1] + dp[i]) % mod
                    # Update choices
                    for prev in dp_choices[i]:
                        temp_set.add(prev + d)

            if i >= 1:
                if s[i - 1] == '?' and s[i] == '?':
                    two_digit_nums = [(str(a), str(b)) for a in range(1, 3) for b in range(10) if 10 <= int(f"{a}{b}") <= 26]
                elif s[i - 1] == '?':
                    b = s[i]
                    two_digit_nums = [(str(a), b) for a in range(1, 3) if 10 <= int(f"{a}{b}") <= 26]
                elif s[i] == '?':
                    a = s[i - 1]
                    two_digit_nums = [(a, str(b)) for b in range(10) if 10 <= int(f"{a}{b}") <= 26]
                else:
                    num = int(s[i - 1:i + 1])
                    if s[i - 1] != '0' and 10 <= num <= 26:
                        two_digit_nums = [(s[i - 1], s[i])]
                    else:
                        two_digit_nums = []
                if dp[i - 1] > 0 and two_digit_nums:
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % mod
                    # Update choices
                    for num in two_digit_nums:
                        for prev in dp_choices[i - 1]:
                            temp_set.add(prev + ''.join(num))
            dp_choices[i + 1] = temp_set.copy()
        max_decodings = dp[n] % mod

        possible_strings = list(dp_choices[n])
        possible_strings.sort()
        total_strings = len(possible_strings)

        if K > total_strings:
            # As per constraints, K will not be larger than the number of uncorrupted strings
            print(f"Case #{case_num}: IMPOSSIBLE")
            continue

        result_string = possible_strings[K - 1]
        print(f"Case #{case_num}: {result_string} {max_decodings}")
if __name__ == "__main__":
    threading.Thread(target=main).start()