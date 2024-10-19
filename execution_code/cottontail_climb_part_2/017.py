import sys
import itertools
import bisect

def generate_mountains():
    mountains = []

    # Single-digit mountains (k=0)
    for m in range(1, 10):
        mountains.append(m)

    # For lengths >=3 (k=1 to9)
    for k in range(1, 10):
        for m in range(2, 10):
            max_digit = m - 1
            if max_digit < 1:
                continue  # No valid first or last digits
            # Generate first k digits: non-decreasing, digits 1 to m-1
            first_seqs = list(itertools.combinations_with_replacement(range(1, max_digit + 1), k))
            # Generate last k digits: non-increasing, digits 1 to m-1
            non_decreasing_seqs = list(itertools.combinations_with_replacement(range(1, max_digit + 1), k))
            last_seqs = [tuple(reversed(seq)) for seq in non_decreasing_seqs]
            # Combine first and last sequences with middle digit m
            for first in first_seqs:
                for last in last_seqs:
                    digits = list(first) + [m] + list(last)
                    num = 0
                    for d in digits:
                        num = num * 10 + d
                    mountains.append(num)

    mountains.sort()
    return mountains

def main():
    mountains = generate_mountains()
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for tc in range(1, T + 1):
        A = int(input[idx])
        B = int(input[idx + 1])
        M = int(input[idx + 2])
        idx += 3
        # Find left and right indices
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        if M == 1:
            count = right - left
        else:
            subset = mountains[left:right]
            count = sum(1 for num in subset if num % M == 0)
        print(f"Case #{tc}: {count}")

if __name__ == "__main__":
    main()