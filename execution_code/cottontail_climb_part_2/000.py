import sys
import math
from bisect import bisect_left, bisect_right

def generate_mountain_numbers():
    mountains = []
    # Maximum number of digits is 19 (since 10^18 has 19 digits)
    for length in range(1, 20, 2):  # Only odd lengths
        k = length // 2
        # Generate first k+1 digits (non-decreasing, digits 1-9)
        def dfs(prefix, last_digit, depth):
            if depth == k + 1:
                # Now generate the decreasing part
                peak = prefix[-1]
                def dfs_decr(suffix, current_digit, depth_decr):
                    if depth_decr == k:
                        mountains.append(int(prefix + suffix))
                        return
                    for d in range(1, current_digit + 1):
                        dfs_decr(suffix + str(d), d, depth_decr + 1)
                dfs_decr("", peak, 0)
                return
            for d in range(last_digit, 10):
                if d == 0:
                    continue
                dfs(prefix + str(d), d, depth + 1)
        dfs("", 1, 0)
    mountains.sort()
    return mountains

def main():
    mountains = generate_mountain_numbers()
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        A_str, B_str, M_str = sys.stdin.readline().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        # Find mountains within [A, B]
        left = bisect_left(mountains, A)
        right = bisect_right(mountains, B)
        count = 0
        # Iterate through the relevant mountains and count those divisible by M
        for num in mountains[left:right]:
            if num % M == 0:
                count += 1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()