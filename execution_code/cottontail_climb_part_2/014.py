import sys
import math
from itertools import product

def generate_mountain_numbers(max_digits):
    mountains = []
    # Only odd lengths
    for length in range(1, max_digits + 1, 2):
        k = length // 2
        # Generate all possible first k+1 digits (non-decreasing, no zeros)
        def backtrack(prefix, last_digit, pos):
            if pos == k + 1:
                # Now, the middle digit must be unique
                for mid_digit in range(1, 10):
                    if mid_digit != prefix[-1]:
                        # Now, generate the last k digits (non-increasing)
                        def backtrack_suffix(suffix, last, p):
                            if p == k:
                                mountain = int(''.join(map(str, prefix + [mid_digit] + suffix)))
                                mountains.append(mountain)
                                return
                            for d in range(1, last + 1):
                                backtrack_suffix(suffix + [d], d, p + 1)
                        backtrack_suffix([], mid_digit, 0)
                return
            for d in range(last_digit, 10):
                backtrack(prefix + [d], d, pos + 1)
        # Initialize backtracking with first digit from 1 to 9
        for first_digit in range(1, 10):
            backtrack([first_digit], first_digit, 1)
    return mountains

def main():
    T = int(sys.stdin.readline())
    test_cases = [tuple(map(int, sys.stdin.readline().split())) for _ in range(T)]
    max_B = max(b for _, b, _ in test_cases)
    max_digits = len(str(max_B)) if max_B > 0 else 1
    mountains = generate_mountain_numbers(max_digits)
    mountains = sorted(mountains)
    # Precompute prefixes for mountains
    for idx, (A, B, M) in enumerate(test_cases, 1):
        # Binary search to find the relevant mountains
        left = 0
        right = len(mountains)
        # Find the first mountain >= A
        while left < right:
            mid = (left + right) // 2
            if mountains[mid] < A:
                left = mid + 1
            else:
                right = mid
        start = left
        # Find the first mountain > B
        left = 0
        right = len(mountains)
        while left < right:
            mid = (left + right) // 2
            if mountains[mid] <= B:
                left = mid + 1
            else:
                right = mid
        end = left
        count = 0
        for num in mountains[start:end]:
            if num % M == 0:
                count += 1
        print(f"Case #{idx}: {count}")

if __name__ == "__main__":
    main()