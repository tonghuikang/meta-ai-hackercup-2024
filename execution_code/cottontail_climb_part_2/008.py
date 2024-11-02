import sys
import itertools
import numpy as np

def generate_mountain_numbers():
    mountain_numbers = []

    # Length 1
    for d in range(1,10):
        mountain_numbers.append(d)

    # Lengths 3,5,...,19
    for L in range(3, 20, 2):
        k = (L -1)//2
        for d in range(1,10):
            if d ==1 and k >0:
                continue  # No digits less than 1
            # Generate first k digits: non-decreasing from 1 to d-1
            if k ==0:
                first_seqs = [()]
            else:
                first_seqs = list(itertools.combinations_with_replacement(range(1,d), k))
                if not first_seqs:
                    continue
            # Generate last k digits: non-increasing from d-1 to 1
                # Which is reverse of non-decreasing from 1 to d-1
                last_seqs = [seq[::-1] for seq in itertools.combinations_with_replacement(range(1,d), k)]
                if not last_seqs:
                    continue
            for first in first_seqs:
                for last in last_seqs:
                    digits = first + (d,) + last
                    num = 0
                    for digit in digits:
                        num = num *10 + digit
                    mountain_numbers.append(num)
    return mountain_numbers

def main():
    mountain_numbers = generate_mountain_numbers()
    mountain_numbers_sorted = sorted(mountain_numbers)
    numbers = np.array(mountain_numbers_sorted, dtype=np.int64)

    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        A_str, B_str, M_str = line.strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        idx_a = np.searchsorted(numbers, A, side='left')
        idx_b = np.searchsorted(numbers, B, side='right')
        subset = numbers[idx_a:idx_b]
        if M ==1:
            count = subset.size
        else:
            # To handle large M, ensure M is within int64
            subset_mod = subset % M
            count = np.count_nonzero(subset_mod ==0)
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()