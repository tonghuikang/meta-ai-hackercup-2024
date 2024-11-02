import sys
import itertools
import bisect

def generate_mountain_numbers():
    list_mountain = []
    for L in range(1, 20, 2):  # L=1,3,5,...,19
        k = (L -1)//2
        if k ==0:
            # Single digit mountains: 1-9
            for d in range(1,10):
                list_mountain.append(d)
            continue
        # For L >=3
        for D in range(1,10):
            if D ==1 and k >=1:
                # No possible last digits since D-1=0
                continue
            # Generate all non-decreasing sequences of length k with digits from 1 to D
            first_combinations = itertools.combinations_with_replacement(range(1, D+1), k)
            for first_k in first_combinations:
                # The first k+1 digits: first_k + [D]
                first_k_plus1 = list(first_k) + [D]
                # Generate all non-increasing sequences of length k with digits from 1 to D-1
                if D ==1:
                    continue  # No last digits possible
                last_combinations = itertools.combinations_with_replacement(range(1, D), k)
                for last_k in last_combinations:
                    last_k_rev = list(last_k)[::-1]
                    # Ensure non-increasing
                    # Since combinations_with_replacement gives non-decreasing, reversing makes it non-increasing
                    full_digits = first_k_plus1 + last_k_rev
                    # Convert digits to number
                    number = 0
                    for digit in full_digits:
                        number = number *10 + digit
                    list_mountain.append(number)
    list_mountain.sort()
    return list_mountain

def main():
    list_mountain = generate_mountain_numbers()
    input = sys.stdin.read().split()
    T = int(input[0])
    ptr =1
    for tc in range(1, T+1):
        A = int(input[ptr])
        B = int(input[ptr+1])
        M = int(input[ptr+2])
        ptr +=3
        # Find left and right indices
        left = bisect.bisect_left(list_mountain, A)
        right = bisect.bisect_right(list_mountain, B)
        count =0
        for num in list_mountain[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{tc}: {count}")

if __name__ == "__main__":
    main()