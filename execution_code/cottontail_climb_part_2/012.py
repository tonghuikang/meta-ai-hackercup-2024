import sys
import bisect
from itertools import combinations_with_replacement, product

def generate_mountain_numbers():
    mountain_numbers = set()
    
    # Lengths: 1,3,5,...,19
    for l in range(1, 20, 2):
        k = (l - 1) // 2
        # Central digit from 1 to 9
        for c in range(1, 10):
            # Generate first k digits: non-decreasing, each < c
            if k == 0:
                first_parts = ['']
            else:
                # digits from 1 to c-1, non-decreasing
                # use combinations with replacement
                first_digit_options = list(range(1, c))
                first_combinations = combinations_with_replacement(first_digit_options, k)
                first_parts = [''.join(map(str, comb)) for comb in first_combinations]
            # Generate last k digits: non-increasing, each < c
            if k == 0:
                last_parts = ['']
            else:
                # digits from 1 to c-1, non-increasing
                # similar to first, but non-increasing
                last_digit_options = list(range(1, c))
                # To generate non-increasing sequences, generate combinations with replacement and sort in reverse
                last_combinations = combinations_with_replacement(last_digit_options, k)
                last_parts = [''.join(map(str, sorted(comb, reverse=True))) for comb in last_combinations]
            # Combine first_parts, central digit, last_parts
            for fp in first_parts:
                for lp in last_parts:
                    number_str = fp + str(c) + lp
                    number = int(number_str)
                    mountain_numbers.add(number)
    # Convert to sorted list
    mountain_list = sorted(mountain_numbers)
    return mountain_list

def main():
    import sys
    import threading
    def run():
        mountain_list = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for case in range(1, T+1):
            A_str, B_str, M_str = sys.stdin.readline().strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find the range in mountain_list
            left = bisect.bisect_left(mountain_list, A)
            right = bisect.bisect_right(mountain_list, B)
            count = 0
            if M == 1:
                count = right - left
            else:
                # Iterate through the subset and count divisible by M
                subset = mountain_list[left:right]
                # To speed up, use list comprehension
                count = sum(1 for num in subset if num % M == 0)
            print(f"Case #{case}: {count}")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()