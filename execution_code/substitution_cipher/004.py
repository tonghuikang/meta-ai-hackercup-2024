import sys
import sys
import sys
sys.setrecursionlimit(1 << 25)
def main():
    import sys
    from collections import defaultdict
    T = int(sys.stdin.readline())
    MOD = 998244353
    for test_case in range(1, T+1):
        E, K = sys.stdin.readline().strip().split()
        K = int(K)
        n = len(E)
        dp = [0]*(n+1)
        dp[n] = 1
        # To track possible digits leading to max dp
        choices = [ [] for _ in range(n) ]
        for i in range(n-1, -1, -1):
            current = E[i]
            possible_digits = []
            if current == '?':
                possible_digits = [str(d) for d in range(10)]
            else:
                possible_digits = [current]
            max_count = -1
            digit_to_counts = {}
            for d in possible_digits:
                # Single digit
                if d != '0':
                    count = dp[i+1]
                else:
                    count = 0
                # Two digits
                if i+1 < n:
                    next_char = E[i+1]
                    if next_char == '?':
                        possible_next = [str(nd) for nd in range(10)]
                    else:
                        possible_next = [next_char]
                    for nd in possible_next:
                        num = int(d+nd)
                        if 10 <= num <= 26:
                            if d != '0':
                                count = (count + dp[i+2]) % MOD
                if count > max_count:
                    max_count = count
            dp[i] = max_count % MOD
        # Now, find replacements that maximize dp[0]
        # We need to reconstruct the choices
        # Start from the beginning, at each position, choose the digit that allows maximum dp
        # and collect the possible digits that achieve this
        dp_full = [0]*(n+1)
        dp_full[n] = 1
        info = [ [] for _ in range(n+1) ]
        for i in range(n-1, -1, -1):
            current = E[i]
            possible_digits = []
            if current == '?':
                possible_digits = [str(d) for d in range(10)]
            else:
                possible_digits = [current]
            total = 0
            temp = []
            for d in possible_digits:
                count = 0
                if d != '0':
                    count += dp_full[i+1]
                if i+1 < n:
                    next_char = E[i+1]
                    if next_char == '?':
                        possible_next = [str(nd) for nd in range(10)]
                    else:
                        possible_next = [next_char]
                    for nd in possible_next:
                        num = int(d+nd)
                        if 10 <= num <= 26:
                            if d != '0':
                                count += dp_full[i+2]
                temp.append((d, count))
                total = max(total, temp[-1][1])
            # Now, keep only digits that lead to the maximum
            info[i] = [d for d, cnt in temp if cnt == total]
            dp_full[i] = total
        # Now, reconstruct the Kth lex large string
        res = []
        i = 0
        while i < n:
            possible = []
            current = E[i]
            possible_digits = []
            if current == '?':
                possible_digits = [str(d) for d in range(10)]
            else:
                possible_digits = [current]
            candidates = []
            for d in sorted(possible_digits, reverse=True):
                valid = False
                # Simulate choosing d at position i
                # and check if d is in info[i]
                if d in info[i]:
                    valid = True
                if valid:
                    candidates.append(d)
            for d in candidates:
                # Choose d and see how many strings can be formed
                count = 0
                if d != '0':
                    count += dp_full[i+1]
                if i+1 < n:
                    next_char = E[i+1]
                    if next_char == '?':
                        possible_next = [str(nd) for nd in range(10)]
                    else:
                        possible_next = [next_char]
                    for nd in possible_next:
                        num = int(d+nd)
                        if 10 <= num <= 26:
                            if d != '0':
                                count += dp_full[i+2]
                count %= MOD
                if count >= K:
                    res.append(d)
                    if i+1 < n and d != '0':
                        if next_char := E[i+1] if i+1 < n else None:
                            if next_char == '?':
                                # Need to choose the lex largest
                                # But already handled by sorted descending
                                pass
                    if d != '0' and i+1 < n:
                        # Check if taking two digits is possible
                        if E[i+1] == '?':
                            # Choose the largest possible nd that makes a valid number
                            for nd in sorted([str(nd) for nd in range(10)], reverse=True):
                                num = int(d+nd)
                                if 10 <= num <=26:
                                    res.append(nd)
                                    i +=2
                                    break
                    i +=1
                    break
                else:
                    K -= count
            else:
                # Should not reach here
                res.append('0')
                i +=1
        decoded = ''.join(res)
        print(f"Case #{test_case}: {decoded} {dp_full[0]%MOD}")

if __name__ == "__main__":
    main()