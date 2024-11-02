import sys
import bisect
import itertools

def generate_non_decreasing_sequences(k, max_digit):
    if k == 0:
        return [[]]
    # Generate all non-decreasing sequences of length k with digits from 1 to max_digit
    return list(itertools.combinations_with_replacement(range(1, max_digit +1), k))

def generate_non_increasing_sequences(k, max_digit):
    if k == 0:
        return [[]]
    # Generate all non-decreasing sequences and reverse them to get non-increasing
    non_decreasing = generate_non_decreasing_sequences(k, max_digit)
    non_increasing = [seq[::-1] for seq in non_decreasing]
    return non_increasing

def generate_mountain_numbers():
    mountains = []
    # Handle l=1 separately
    for d in range(1,10):
        mountains.append(d)
    # Handle l=3,5,...,19
    for k in range(1, 10):
        l = 2*k +1
        if l > 19:
            break
        for D in range(2,10):  # D from 2 to 9
            # Generate all non-decreasing sequences of length k with digits from 1 to D-1
            if D-1 <1:
                continue
            first_seqs = generate_non_decreasing_sequences(k, D-1)
            if not first_seqs:
                continue
            # Generate all non-increasing sequences of length k with digits from 1 to D-1
            last_seqs = generate_non_increasing_sequences(k, D-1)
            if not last_seqs:
                continue
            # Combine all combinations
            for first in first_seqs:
                for last in last_seqs:
                    # Build the number: first + D + last
                    num_digits = list(first) + [D] + list(last)
                    # Convert to integer
                    num = 0
                    for digit in num_digits:
                        num = num *10 + digit
                    mountains.append(num)
    mountains.sort()
    return mountains

def main():
    mountains = generate_mountain_numbers()
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        A,B,M = map(int,line.strip().split())
        # Find the indices of A and B in mountains
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        # Iterate from left to right-1
        for num in mountains[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()