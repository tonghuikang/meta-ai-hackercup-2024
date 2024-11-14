import sys
import sys
import sys

MOD = 998244353

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        line = sys.stdin.readline().rstrip()
        if not line:
            line = sys.stdin.readline().rstrip()
        E, K_str = line.rsplit(' ', 1)
        K = int(K_str)
        n = len(E)
        dp = [0] * (n + 1)
        dp[n] = 1
        # To store possible digits at each position that can lead to max dp[i]
        choices = [[] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            current_max = 0
            possible = []
            # Single digit
            single_digits = []
            if E[i] == '?':
                single_digits = [str(d) for d in range(1, 10)]
            else:
                if E[i] != '0':
                    single_digits = [E[i]]
            for d in single_digits:
                cnt = dp[i + 1]
                if cnt > current_max:
                    current_max = cnt
                    possible = [d]
                elif cnt == current_max:
                    possible.append(d)
            # Two digits
            if i + 1 < n:
                two_digits = []
                first = E[i]
                second = E[i + 1]
                first_options = [str(d) for d in range(1, 10)] if first == '?' else ([first] if first != '0' else [])
                second_options = [str(d) for d in range(0, 10)] if second == '?' else ([second])
                for f in first_options:
                    for s in second_options:
                        num = int(f + s)
                        if 10 <= num <= 26:
                            cnt = dp[i + 2]
                            if cnt > current_max:
                                current_max = cnt
                                possible = [f + s]
                            elif cnt == current_max:
                                possible.append(f + s)
            dp[i] = current_max % MOD
            # Store possible choices
            choices[i] = possible
        # Now, reconstruct the Kth lex largest string
        res = []
        i = 0
        while i < n:
            possible = choices[i]
            # We need to sort possible in descending order for lex largest
            possible_sorted = sorted(possible, reverse=True)
            for option in possible_sorted:
                if len(option) == 1:
                    cnt = dp[i + 1]
                else:
                    cnt = dp[i + 2]
                if K > cnt:
                    K -= cnt
                else:
                    res.append(option)
                    i += len(option)
                    break
        decoded_str = ''.join(res)
        print(f"Case #{test_case}: {decoded_str} {dp[0]%MOD}")

if __name__ == "__main__":
    main()