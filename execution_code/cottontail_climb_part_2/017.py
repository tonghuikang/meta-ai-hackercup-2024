import sys
import itertools
import bisect

def generate_mountain_numbers():
    mountain_numbers = set()
    # k from 0 to 9 (2k+1 digits from 1 to19)
    for k in range(0, 10):
        num_digits = 2 * k +1
        if k ==0:
            for d in range(1,10):
                mountain_numbers.add(d)
            continue
        for D_mid in range(1,10):
            # First k digits: non-decreasing from 1 to D_mid -1
            if D_mid ==1:
                continue  # No digits <1
            max_first = D_mid -1
            # Generate all combinations with replacement of k digits from 1 to max_first, non-decreasing
            # Equivalent to combinations with replacement
            first_combinations = itertools.combinations_with_replacement(range(1, max_first +1), k)
            # Similarly, last k digits: non-increasing from D_mid -1 to1
            last_combinations = itertools.combinations_with_replacement(range(1, max_first +1), k)
            # To make last k digits non-increasing, sort each last_combination in reverse
            # To save memory, process combinations on the fly
            first_list = list(first_combinations)
            last_list = [tuple(sorted(last, reverse=True)) for last in last_combinations]
            for first in first_list:
                first_str = ''.join(str(d) for d in first)
                for last in last_list:
                    last_str = ''.join(str(d) for d in last)
                    full_number = int(first_str + str(D_mid) + last_str)
                    mountain_numbers.add(full_number)
    # Convert to sorted list
    mountain_numbers = sorted(mountain_numbers)
    return mountain_numbers

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    test_cases = []
    idx =1
    for _ in range(T):
        A = int(data[idx])
        B = int(data[idx+1])
        M = int(data[idx+2])
        test_cases.append( (A,B,M) )
        idx +=3
    # Generate all mountain numbers
    mountains = generate_mountain_numbers()
    # Sort them
    mountains = sorted(mountains)
    # For each test case, find the count
    for tc_num, (A, B, M) in enumerate(test_cases,1):
        # Find left and right indices
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count =0
        for num in mountains[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{tc_num}: {count}")

if __name__ == "__main__":
    main()