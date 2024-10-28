import sys
import bisect
from itertools import combinations_with_replacement, product

def generate_non_decreasing_sequences(length, max_digit):
    if length == 0:
        return [()]
    return list(combinations_with_replacement(range(1, max_digit + 1), length))

def generate_non_increasing_sequences(length, max_digit):
    if length == 0:
        return [()]
    return list(combinations_with_replacement(range(1, max_digit + 1), length))[::-1]

def generate_non_increasing_sequences_recursive(length, max_digit):
    if length == 0:
        return [()]
    sequences = []
    def backtrack(seq, last):
        if len(seq) == length:
            sequences.append(tuple(seq))
            return
        for digit in range(last, 0, -1):
            backtrack(seq + [digit], digit)
    backtrack([], max_digit)
    return sequences

def generate_non_decreasing_sequences_recursive(length, max_digit):
    if length == 0:
        return [()]
    sequences = []
    def backtrack(seq, last):
        if len(seq) == length:
            sequences.append(tuple(seq))
            return
        for digit in range(last, max_digit +1):
            backtrack(seq + [digit], digit)
    backtrack([], 1)
    return sequences

def main():
    import sys
    import threading
    def run():
        T = int(sys.stdin.readline())
        test_cases = []
        max_length = 1
        for _ in range(T):
            A, B, M = map(int, sys.stdin.readline().split())
            test_cases.append((A, B, M))
            max_length = max(max_length, len(str(B)))
        mountain_numbers = []
        # Precompute all mountain numbers
        for k in range(0, 10):
            l = 2 * k +1
            if l > 19:
                continue
            for mid in range(1,10):
                if k >0 and mid <=1:
                    continue
                if k ==0:
                    # Single digit numbers
                    mountain_numbers.append(mid)
                    continue
                max_digit_prefix = mid -1
                if max_digit_prefix <1:
                    continue
                # Generate all non-decreasing prefixes of length k with digits from 1 to mid-1
                prefixes = generate_non_decreasing_sequences_recursive(k, max_digit_prefix)
                # Generate all non-increasing suffixes of length k with digits from 1 to mid-1
                suffixes = generate_non_increasing_sequences_recursive(k, max_digit_prefix)
                for prefix in prefixes:
                    for suffix in suffixes:
                        # Assemble the number
                        num_digits = list(prefix) + [mid] + list(suffix)
                        num = 0
                        for d in num_digits:
                            num = num *10 + d
                        mountain_numbers.append(num)
        mountain_numbers = sorted(mountain_numbers)
        # Now process each test case
        for idx, (A, B, M) in enumerate(test_cases,1):
            # Find the range in mountain_numbers
            left = bisect.bisect_left(mountain_numbers, A)
            right = bisect.bisect_right(mountain_numbers, B)
            count = 0
            for num in mountain_numbers[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{idx}: {count}")
    threading.Thread(target=run).start()

# Example usage:
# To run this code, input should be provided via standard input.
# For example, you can test it with the sample input provided in the problem statement.

# Sample Input:
# 6
# 121 121 11
# 0 100 2
# 0 132 1
# 121 132 1
# 121 131 1
# 22322 22322 1

# Expected Output:
# Case #1: 1
# Case #2: 4
# Case #3: 12
# Case #4: 3
# Case #5: 2
# Case #6: 1