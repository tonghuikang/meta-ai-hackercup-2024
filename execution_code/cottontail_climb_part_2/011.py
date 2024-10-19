import sys
import bisect
from itertools import combinations_with_replacement, combinations, product

def generate_non_decreasing_sequences(length, max_digit):
    """Generates all non-decreasing sequences of a given length with digits <= max_digit."""
    # Using combinations_with_replacement since digits can repeat and order is non-decreasing
    return list(combinations_with_replacement(range(1, max_digit), length))

def generate_non_increasing_sequences(length, max_digit):
    """Generates all non-increasing sequences of a given length with digits <= max_digit."""
    # Using combinations_with_replacement and reversing for non-increasing
    return [tuple(reversed(seq)) for seq in combinations_with_replacement(range(1, max_digit), length)]

def generate_mountain_numbers():
    mountain_numbers = set()

    # k from 0 to 9 (since 2*9+1=19 digits)
    for k in range(0, 10):
        num_digits = 2 * k + 1
        if k == 0:
            # Single-digit numbers
            for d in range(1, 10):
                mountain_numbers.add(d)
            continue
        # For k >=1
        # Choose peak digit from 2 to 9
        for peak in range(2, 10):
            # Generate all possible left sequences (non-decreasing, digits < peak)
            left_sequences = generate_non_decreasing_sequences(k, peak)
            # Generate all possible right sequences (non-increasing, digits < peak)
            right_sequences = generate_non_increasing_sequences(k, peak)
            # Combine left, peak, and right
            for left in left_sequences:
                for right in right_sequences:
                    # Convert to integer
                    number = 0
                    for d in left:
                        number = number * 10 + d
                    number = number * 10 + peak
                    for d in right:
                        number = number * 10 + d
                    mountain_numbers.add(number)
    # Convert to sorted list
    mountain_numbers = sorted(mountain_numbers)
    return mountain_numbers

def main():
    import sys
    import threading
    def run():
        mountain_numbers = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for test_case in range(1, T + 1):
            A_str, B_str, M_str = sys.stdin.readline().strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find the lower and upper indices using bisect
            left_idx = bisect.bisect_left(mountain_numbers, A)
            right_idx = bisect.bisect_right(mountain_numbers, B)
            # Slice the relevant mountain numbers
            relevant = mountain_numbers[left_idx:right_idx]
            # Count how many are divisible by M
            count = 0
            if M == 1:
                count = len(relevant)
            else:
                for num in relevant:
                    if num % M == 0:
                        count +=1
            print(f"Case #{test_case}: {count}")
    threading.Thread(target=run,).start()

if __name__ == "__main__":
    main()