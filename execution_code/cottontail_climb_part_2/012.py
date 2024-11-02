import sys
import bisect
from itertools import combinations_with_replacement, combinations
from math import comb

def generate_mountain_numbers():
    mountains = []
    # L = 2k+1 from 1 to 19
    for L in range(1, 20, 2):
        k = (L -1)//2
        if k ==0:
            # single digit numbers
            for d in range(1,10):
                mountains.append(d)
            continue
        for D_peak in range(1,10):
            # First k digits: non-decreasing, digits from 1 to D_peak -1
            if D_peak ==1:
                continue  # No digits less than 1
            # Number of non-decreasing sequences of length k with digits 1 to D_peak-1
            # Equivalent to combinations with replacement
            # We need to generate all possible sequences
            # Using combinations_with_replacement
            # Possible digits for first k digits: 1 to D_peak-1
            digits_first = list(range(1, D_peak))
            if not digits_first:
                continue
            # Generate all non-decreasing sequences of length k from digits_first
            # Use combinations_with_replacement
            first_sequences = list(combinations_with_replacement(digits_first, k))
            # Similarly for last k digits: non-increasing sequences from 1 to D_peak-1
            last_sequences = list(combinations_with_replacement(digits_first, k))
            # For each combination in last_sequences, since it's non-increasing, reverse it
            last_sequences = [seq[::-1] for seq in last_sequences]
            # Now, for each first_sequence and last_sequence, combine with D_peak
            for first in first_sequences:
                for last in last_sequences:
                    # Ensure that the last digit of first <= D_peak
                    # But since first is non-decreasing and last is non-increasing, D_peak is the peak
                    # Also, need to ensure that D_peak does not appear in first and last sequences
                    # Which is already ensured since first and last sequences are from 1 to D_peak-1
                    # Now, construct the number
                    num_digits = list(first) + [D_peak] + list(last)
                    num = 0
                    for d in num_digits:
                        num = num *10 + d
                    mountains.append(num)
    mountains = sorted(set(mountains))
    return mountains

def main():
    mountains = generate_mountain_numbers()
    input = sys.stdin.read().split()
    T = int(input[0])
    index =1
    for tc in range(1, T+1):
        A = int(input[index])
        B = int(input[index+1])
        M = int(input[index+2])
        index +=3
        # Find mountains in [A,B]
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{tc}: {count}")

if __name__ == "__main__":
    main()