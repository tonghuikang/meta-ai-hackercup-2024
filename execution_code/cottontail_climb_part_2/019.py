import sys
import math
from bisect import bisect_left, bisect_right

def generate_mountain_numbers():
    from itertools import combinations_with_replacement, product
    mountain_numbers = []

    # For lengths 1,3,5,...,19
    for k in range(0, 10):  # k from 0 to 9, length=2k+1 up to 19
        length = 2 * k + 1
        if k == 0:
            # Single-digit mountain numbers: 1 to 9
            for d in range(1, 10):
                mountain_numbers.append(d)
            continue
        # For k >=1, generate mountain numbers
        for middle in range(1, 10):
            # Digits to the left: k digits, non-decreasing, digits from 1 to middle-1
            if middle ==1:
                continue  # No digits less than 1
            max_digit = middle -1
            # Generate all non-decreasing sequences of length k with digits from1 to max_digit
            # Equivalent to combinations with replacement
            # The number of such sequences is C(max_digit +k -1, k)
            # Since generating all is time-consuming, use recursion
            def generate_prefix(current, last, remaining):
                if remaining ==0:
                    prefixes.append(current)
                    return
                for d in range(last, max_digit+1):
                    generate_prefix(current *10 +d, d, remaining -1)
            prefixes = []
            generate_prefix(0,1, k)
            # Similarly, generate all non-increasing sequences of length k with digits from1 to max_digit
            def generate_suffix(current, last, remaining):
                if remaining ==0:
                    suffixes.append(current)
                    return
                for d in range(1, last+1):
                    generate_suffix(current *10 +d, d, remaining -1)
            suffixes = []
            generate_suffix(0, max_digit, k)
            # Combine prefixes and suffixes with the middle digit
            for p in prefixes:
                for s in suffixes:
                    number = p * (10**(k +1)) + middle * (10**k) + s
                    mountain_numbers.append(number)
    mountain_numbers.sort()
    return mountain_numbers

def main():
    import sys
    import threading

    def run():
        T = int(sys.stdin.readline())
        test_cases = []
        for _ in range(T):
            A, B, M = map(int, sys.stdin.readline().split())
            test_cases.append( (A, B, M) )
        # Generate all mountain numbers
        mountain_numbers = generate_mountain_numbers()
        # Sort mountain numbers
        mountain_numbers.sort()
        # For each test case, count numbers in [A,B] divisible by M
        for idx, (A, B, M) in enumerate(test_cases, 1):
            left = bisect_left(mountain_numbers, A)
            right = bisect_right(mountain_numbers, B)
            count =0
            for num in mountain_numbers[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{idx}: {count}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()