import sys
import bisect
from itertools import combinations_with_replacement, product

def generate_non_decreasing_sequences(k, max_digit):
    """
    Generate all non-decreasing sequences of length k with digits from 1 to max_digit -1
    """
    if k == 0:
        return [()]
    # Use combinations with replacement
    return list(combinations_with_replacement(range(1, max_digit), k))

def generate_non_increasing_sequences(k, max_digit):
    """
    Generate all non-increasing sequences of length k with digits from 1 to max_digit -1
    """
    if k == 0:
        return [()]
    # Generate combinations with replacement in reverse order
    sequences = list(combinations_with_replacement(range(1, max_digit), k))
    # For each combination, sort descending to make non-increasing
    return [tuple(sorted(seq, reverse=True)) for seq in sequences]

def generate_all_mountains():
    mountains = []
    # Lengths: 1,3,5,...,19
    for n in range(1, 20, 2):
        k = (n -1)//2
        if k ==0:
            # Single-digit mountains
            for d in range(1,10):
                mountains.append(d)
        else:
            # For k >=1, generate mountains
            for peak in range(2,10):
                # First k digits: non-decreasing sequences with digits < peak
                first_half_seqs = generate_non_decreasing_sequences(k, peak)
                if not first_half_seqs:
                    continue
                # Last k digits: non-increasing sequences with digits < peak
                last_half_seqs = generate_non_increasing_sequences(k, peak)
                if not last_half_seqs:
                    continue
                # Combine all possible sequences
                for first in first_half_seqs:
                    for last in last_half_seqs:
                        # To ensure that peak appears only once, check that peak doesn't appear in first or last
                        if peak in first or peak in last:
                            continue
                        # Build the number
                        number_digits = first + (peak,) + last
                        # Convert to integer
                        number = 0
                        for d in number_digits:
                            number = number * 10 + d
                        mountains.append(number)
    # Sort the mountains
    mountains.sort()
    return mountains

def main():
    import sys
    import threading
    def run():
        mountains = generate_all_mountains()
        T = int(sys.stdin.readline())
        for case in range(1, T+1):
            A, B, M = map(int, sys.stdin.readline().split())
            # Find left index: first mountain >= A
            left = bisect.bisect_left(mountains, A)
            # Find right index: first mountain > B
            right = bisect.bisect_right(mountains, B)
            count =0
            # Iterate through mountain[left:right] and count divisible by M
            if M ==1:
                count = right - left
            else:
                # To optimize, iterate and count
                for num in mountains[left:right]:
                    if num % M ==0:
                        count +=1
            print(f"Case #{case}: {count}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()