import sys
import threading
def main():
    MOD = 998244353
    import sys
    import math
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for ttt in range(1, T +1 ):
        line = sys.stdin.readline().strip()
        while line == '':
            line = sys.stdin.readline().strip()
        if ' ' in line:
            E_str, K_str = line.split()
        else:
            E_str = line
            K_str = sys.stdin.readline().strip()
        E = list(E_str)
        K = int(K_str)
        N = len(E)
        # First pass: compute dp[i] with E[i] == '?' replaced by '1'
        S = [c if c != '?' else '1' for c in E]
        dp = [0] * (N + 1)  # dp[i] represents ways to decode up to position i-1
        dp[0] = 1
        for i in range(1, N + 1):
            dp[i] = 0
            # Single digit
            if S[i-1] != '0':
                dp[i] += dp[i-1]
            # Two-digit number
            if i >=2:
                if S[i-2] != '0':
                    num = int(S[i-2] + S[i-1])
                    if 10 <= num <=26:
                        dp[i] += dp[i-2]
            dp[i] %= MOD
        MAX_dp = dp[N]
        # Now, for positions where E[i] == '?', find possible digits
        possible_digits = [''] * N  # List of possible digits per position
        # Work backwards to collect possible digits that lead to MAX_dp
        # Initialize dp_positions[i]: set of (dp[i], digits at position i)
        dp_positions = [{} for _ in range(N+1)]
        dp_positions[0][()] = 1  # Empty sequence
        for i in range(1, N+1):
            dp_current = {}
            if E[i-1] != '?':
                ci = E[i-1]
                if ci != '0':
                    for key in dp_positions[i-1]:
                        dp_current[key + (ci,)] = (dp_current.get(key + (ci,), 0) + dp_positions[i-1][key]) % MOD
                if i >=2 and E[i-2] != '?':
                    c_prev = E[i-2]
                    if c_prev != '0':
                        num = int(c_prev + ci)
                        if 10 <= num <=26:
                            for key in dp_positions[i-2]:
                                dp_current[key + (c_prev, ci)] = (dp_current.get(key + (c_prev, ci), 0) + dp_positions[i-2][key]) % MOD
            else:
                digits_i = set()
                for ci in '123456789':
                    total_dp = 0
                    temp_dp = {}
                    # Single digit
                    if ci != '0':
                        for key in dp_positions[i-1]:
                            temp_dp[key + (ci,)] = (temp_dp.get(key + (ci,), 0) + dp_positions[i-1][key]) % MOD
                    # Two-digit numbers
                    if i >=2:
                        if E[i-2] != '?':
                            c_prev = E[i-2]
                            if c_prev != '0':
                                num = int(c_prev + ci)
                                if 10 <= num <=26:
                                    for key in dp_positions[i-2]:
                                        temp_dp[key + (c_prev, ci)] = (temp_dp.get(key + (c_prev, ci), 0) + dp_positions[i-2][key]) % MOD
                        else:
                            for c_prev in '123456789':
                                if c_prev != '0':
                                    num = int(c_prev + ci)
                                    if 10 <= num <=26:
                                        for key in dp_positions[i-2]:
                                            temp_dp[key + (c_prev, ci)] = (temp_dp.get(key + (c_prev, ci), 0) + dp_positions[i-2][key]) % MOD

                    total_dp = sum(temp_dp.values()) % MOD
                    if total_dp > 0:
                        dp_current.update(temp_dp)
                        digits_i.add(ci)
                possible_digits[i-1] = sorted(digits_i, reverse=True)
            dp_positions[i] = dp_current
        # Now, collect possible digits per position
        positions = []
        for i in range(N):
            if E[i] == '?':
                if possible_digits[i]:
                    positions.append((i, possible_digits[i]))
                else:
                    positions.append((i, ['1']))  # Default to '1'
        total_strings = 1
        for pos, digits in positions:
            total_strings *= len(digits)
        if K > total_strings:
            print(f"Case #{ttt}: Impossible {dp[N]%MOD}")
            continue
        # Now, generate the lex Kth largest uncorrupted string among the ones with maximum dp[N]
        # We can generate it by calculating the positions one by one
        K -=1  # Make it zero-based
        result = list(E)
        for pos, digits in positions:
            num_options = len(digits)
            idx = K // (total_strings // num_options)
            result[pos] = digits[idx]
            K = K % (total_strings // num_options)
            total_strings = total_strings // num_options
        uncorrupted_string = ''.join(c if c != '?' else '1' for c in result)
        print(f"Case #{ttt}: {uncorrupted_string} {dp[N]%MOD}")

threading.Thread(target=main).start()