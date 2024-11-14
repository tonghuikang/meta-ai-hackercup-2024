To solve this problem efficiently, we need to approach it in two main phases: determining the maximum number of decoded strings and then finding the lexicographically \(K\)th largest uncorrupted string that achieves this maximum.

**Key Findings:**

1. **Dynamic Programming for Decoding Count:**
   - We can use dynamic programming (DP) to calculate the number of ways to decode the string.
   - Let `dp[i]` represent the number of ways to decode the substring starting from index `i`.
   - The recurrence relation considers both single-digit and two-digit possibilities, ensuring they fall within the range 1 to 26 and avoiding leading zeros.

2. **Handling Wildcards ('?'):**
   - Each '?' can be replaced by any digit from '0' to '9'. We need to consider all valid replacements that maximize the number of decoding ways.
   - During the DP computation, for each '?', we iterate through all possible digit substitutions that lead to valid decoding segments.

3. **Maximizing Decoding Ways:**
   - Our goal is to choose replacements for '?' such that the total number of decoding ways is maximized.
   - This involves selecting digits that allow for the most flexible partitioning of the string into valid chunks.

4. **Reconstructing the \(K\)th Lexicographical String:**
   - After determining the maximum number of decoding ways, we need to find the lexicographically \(K\)th largest string among all possible uncorrupted strings that achieve this maximum.
   - We perform a greedy construction of the string by choosing the largest possible digit at each position that still allows for the remaining string to achieve the maximum number of decodings, decrementing \(K\) accordingly until we construct the desired string.

5. **Efficient Implementation:**
   - Given the constraints (e.g., string length up to 100,000 and multiple test cases), the solution must be optimized for both time and space.
   - We ensure that the DP and reconstruction phases run in linear time relative to the string length.

6. **Modular Arithmetic:**
   - Since the number of decoding ways can be large, we compute it modulo \(998{,}244{,}353\) to keep the numbers manageable and to meet the problem's output requirements.

By combining these strategies, we can efficiently determine the required uncorrupted string and the corresponding number of decoding ways for each test case.

```python
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
```