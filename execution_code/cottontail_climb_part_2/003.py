import sys
import math
import bisect
from itertools import combinations_with_replacement, product

def generate_non_decreasing_sequences(length, max_digit):
    """
    Generate all non-decreasing sequences of given length where each digit is <= max_digit
    and >=1.
    """
    sequences = []

    def backtrack(seq, start, remaining):
        if remaining == 0:
            sequences.append(seq.copy())
            return
        for digit in range(start, max_digit + 1):
            seq.append(digit)
            backtrack(seq, digit, remaining -1)
            seq.pop()
    
    backtrack([], 1, length)
    return sequences

def generate_non_increasing_sequences(length, max_digit):
    """
    Generate all non-increasing sequences of given length where each digit is <= max_digit
    and >=1.
    """
    sequences = []

    def backtrack(seq, start, remaining):
        if remaining == 0:
            sequences.append(seq.copy())
            return
        for digit in range(start, 0, -1):
            if digit > max_digit:
                continue
            seq.append(digit)
            backtrack(seq, digit, remaining -1)
            seq.pop()
    
    backtrack([], max_digit, length)
    return sequences

def precompute_mountain_numbers():
    mountain_numbers = set()

    # Iterate over possible odd digit lengths
    for total_digits in range(1, 19, 2):
        k = (total_digits -1)//2
        # For each possible middle digit
        for middle_digit in range(1,10):
            # Generate first k digits: non-decreasing, all < middle_digit
            if k ==0:
                first_parts = [[]]
            else:
                first_parts = generate_non_decreasing_sequences(k, middle_digit -1)
            # Generate last k digits: non-increasing, all < middle_digit
            if k ==0:
                last_parts = [[]]
            else:
                last_parts = generate_non_increasing_sequences(k, middle_digit -1)
            # Combine all possible combinations
            for fp in first_parts:
                for lp in last_parts:
                    number_digits = fp + [middle_digit] + lp
                    number = int(''.join(map(str, number_digits)))
                    mountain_numbers.add(number)
    # Remove numbers with leading zeros if any (though our generation shouldn't have)
    mountain_numbers = [num for num in mountain_numbers if len(str(num)) == len(str(num))]
    mountain_numbers.sort()
    return mountain_numbers

def main():
    import sys
    import threading

    def run():
        mountains = precompute_mountain_numbers()
        T = int(sys.stdin.readline())
        for case in range(1, T+1):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            A_str, B_str, M_str = line.strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find the index of first mountain >= A
            left = bisect.bisect_left(mountains, A)
            # Find the index of first mountain > B
            right = bisect.bisect_right(mountains, B)
            count = 0
            for num in mountains[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{case}: {count}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()