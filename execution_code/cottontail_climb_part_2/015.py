import sys
import bisect
from itertools import combinations_with_repetition

def generate_non_decreasing_sequences(length, exclude_digit):
    if length == 0:
        return [()]
    digits = [d for d in range(1, 10) if d != exclude_digit]
    # Use combinations_with_repetition to generate non-decreasing sequences
    return list(combinations_with_repetition(digits, length))

def generate_non_increasing_sequences(length, exclude_digit):
    if length == 0:
        return [()]
    digits = [d for d in range(1, 10) if d != exclude_digit]
    # Generate non-increasing sequences by reversing combinations_with_repetition
    return [tuple(sorted(seq, reverse=True)) for seq in combinations_with_repetition(digits, length)]

def generate_mountains():
    mountains = []
    for total_length in range(1, 20, 2):  # Odd lengths from 1 to 19
        k = (total_length - 1) // 2
        for peak in range(1, 10):
            if k == 0:
                mountains.append(peak)
            else:
                left_sequences = generate_non_decreasing_sequences(k, peak)
                right_sequences = generate_non_increasing_sequences(k, peak)
                for left in left_sequences:
                    for right in right_sequences:
                        # Combine left, peak, and right into a single number
                        number_digits = left + (peak,) + right
                        # Convert tuple of digits to integer
                        number = int(''.join(map(str, number_digits)))
                        mountains.append(number)
    mountains.sort()
    return mountains

def main():
    mountains = generate_mountains()
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for case in range(1, T + 1):
        A = int(input[idx])
        B = int(input[idx + 1])
        M = int(input[idx + 2])
        idx += 3
        # Find the left and right indices using bisect
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M == 0:
                count += 1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()