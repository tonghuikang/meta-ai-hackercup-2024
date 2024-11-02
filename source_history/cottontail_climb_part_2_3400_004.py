import sys
import bisect
from itertools import combinations_with_replacement

def generate_mountain_numbers():
    mountain_numbers = set()

    # Single-digit mountain numbers
    for d in range(1, 10):
        mountain_numbers.add(d)

    # Generate mountain numbers with length >=3
    for k in range(1, 9):  # k from 1 to8, L=2k+1 up to 17
        L = 2 * k + 1
        for D in range(2, 10):  # Middle digit from 2 to9
            # Generate all non-decreasing left sequences of length k with digits from 1 to D-1
            left_seqs = combinations_with_replacement(range(1, D), k)
            left_seqs = list(left_seqs)
            if not left_seqs:
                continue
            # Generate all non-increasing right sequences of length k with digits from 1 to D-1
            # To generate non-increasing, generate non-decreasing and reverse
            right_seqs = combinations_with_replacement(range(1, D), k)
            right_seqs = [seq[::-1] for seq in right_seqs]
            if not right_seqs:
                continue
            # Combine left and right sequences with middle digit D
            for left in left_seqs:
                left_part = ''.join(str(d) for d in left)
                for right in right_seqs:
                    right_part = ''.join(str(d) for d in right)
                    number_str = left_part + str(D) + right_part
                    number = int(number_str)
                    mountain_numbers.add(number)

    # Return sorted list of mountain numbers
    return sorted(mountain_numbers)

def main():
    mountain_numbers = generate_mountain_numbers()

    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        A_str, B_str, M_str = sys.stdin.readline().strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)

        # Find the indices of mountain numbers within [A, B]
        left_idx = bisect.bisect_left(mountain_numbers, A)
        right_idx = bisect.bisect_right(mountain_numbers, B)

        count = 0
        # Iterate through the relevant subset and count divisible by M
        for num in mountain_numbers[left_idx:right_idx]:
            if num % M == 0:
                count += 1

        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()