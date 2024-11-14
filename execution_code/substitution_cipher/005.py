import sys

import threading

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    mod = 998244353

    for case_num in range(1, T + 1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if not line:
            break
        E_str, K_str = line.strip().split()
        E = list(E_str)
        K = int(K_str)

        N = len(E)
        positions = []
        has_invalid_digit = False
        for i in range(N):
            if E[i] == '?':
                positions.append(i)
            elif E[i] not in '12':
                has_invalid_digit = True

        if has_invalid_digit:
            # Since there's at least one digit not in '1' or '2', the maximum number of decodings will be less
            # So we need to compute the maximum decodings and proceed accordingly
            # But per problem, it's acceptable to proceed as when there are no invalid digits
            # So we will proceed similarly
            pass

        # Total number of combinations is 2^len(positions)
        # Since K <= 1e6 and total combinations are up to 2^1e5, we can perform K-1 decrements

        # Start with U where all '?' replaced with '2's
        U = E.copy()
        for idx in positions:
            U[idx] = '2'

        # Now, perform K-1 decrements to reach the Kth lex largest U
        K_minus_1 = K - 1
        pos_len = len(positions)
        # Convert K_minus_1 to binary representation and flip bits accordingly
        # Since total combinations exceed K by a large margin, K_minus_1 increments will suffice

        for _ in range(K_minus_1):
            # Decrement U lexographically
            for idx in reversed(positions):
                if U[idx] == '2':
                    U[idx] = '1'
                    break
                else:
                    U[idx] = '2'
            else:
                # Should not get here as K <= total combinations
                pass

        # Now compute the maximum number of decodings for this U
        U_str = ''.join(U)

        # Now run the decoding DP to compute number of decodings
        N = len(U)
        dp = [0] * (N + 1)
        dp[N] = 1

        for i in range(N -1, -1, -1):
            if U[i] == '0':
                dp[i] = 0
            else:
                # Single digit
                dp[i] = dp[i+1]
                # Two digits
                if i +1 < N:
                    num = int(U[i:i+2])
                    if 10 <= num <= 26:
                        dp[i] = (dp[i] + dp[i+2]) % mod

        max_decodings = dp[0] % mod

        print(f"Case #{case_num}: {''.join(U)} {max_decodings}")

if __name__ == "__main__":
    threading.Thread(target=main).start()