import sys
import bisect
from itertools import combinations_with_replacement, product

def generate_non_decreasing_sequences(length, max_digit):
    """Generate all non-decreasing sequences of given length with digits <= max_digit."""
    if length == 0:
        return [[]]
    sequences = []
    def backtrack(start, seq):
        if len(seq) == length:
            sequences.append(seq.copy())
            return
        for digit in range(start, max_digit+1):
            seq.append(digit)
            backtrack(digit, seq)
            seq.pop()
    backtrack(1, [])
    return sequences

def generate_non_increasing_sequences(length, max_digit):
    """Generate all non-increasing sequences of given length with digits <= max_digit."""
    if length == 0:
        return [[]]
    sequences = []
    def backtrack(start, seq):
        if len(seq) == length:
            sequences.append(seq.copy())
            return
        for digit in range(start, 0, -1):
            if digit <= max_digit:
                seq.append(digit)
                backtrack(digit, seq)
                seq.pop()
    backtrack(max_digit, [])
    return sequences

def precompute_mountains():
    mountains = []
    # For k from 0 to 9 (1 to 19 digits)
    for k in range(0, 10):
        num_digits = 2 * k +1
        if num_digits == 1:
            # Single-digit mountains
            for d in range(1,10):
                mountains.append(d)
            continue
        # For k >=1
        # Middle digit from 2 to 9
        for peak in range(2,10):
            # Generate all non-decreasing left sequences of length k with digits <= peak -1
            left_seqs = generate_non_decreasing_sequences(k, peak -1)
            # Generate all non-increasing right sequences of length k with digits <= peak -1
            right_seqs = generate_non_increasing_sequences(k, peak -1)
            for left in left_seqs:
                for right in right_seqs:
                    number_digits = left + [peak] + right
                    # Convert to integer
                    number = 0
                    for d in number_digits:
                        number = number *10 + d
                    mountains.append(number)
    mountains = sorted(mountains)
    return mountains

def main():
    import sys
    import math
    from sys import stdin
    mountains = precompute_mountains()
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        A,B,M = map(int, sys.stdin.readline().split())
        # Find the indices using bisect
        left_idx = bisect.bisect_left(mountains, A)
        right_idx = bisect.bisect_right(mountains, B)
        count = 0
        # Iterate through the relevant mountain numbers and count divisible by M
        for num in mountains[left_idx:right_idx]:
            if num % M ==0:
                count +=1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()