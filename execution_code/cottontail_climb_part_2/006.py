import sys
import bisect

def generate_mountain_numbers():
    mountain_numbers = []

    # Recursive function to generate non-decreasing sequences
    def generate_first_half(current, length, last_digit, numbers):
        if len(current) == length:
            numbers.append(current)
            return
        for digit in range(last_digit, 10):
            numbers.append(generate_first_half(current + [digit], length, digit, numbers))
            generate_first_half(current + [digit], length, digit, numbers)

    # Alternatively, use itertools to generate non-decreasing sequences
    from itertools import combinations_with_replacement

    for total_digits in range(1, 20, 2):  # Only odd lengths
        k = (total_digits - 1) // 2

        # Generate all possible first k+1 digits (non-decreasing)
        # Since digits are from 1 to 9, and first digit cannot be zero
        for first_half in combinations_with_replacement(range(1, 10), k + 1):
            # Ensure it is strictly non-decreasing
            # Since combinations_with_replacement already gives non-decreasing sequences
            # Now, ensure the middle digit is unique in the entire number
            middle_digit = first_half[-1]

            # To ensure uniqueness, we need to make sure that middle_digit does not appear in first k digits
            if middle_digit in first_half[:-1]:
                continue

            # Now, generate the second half (last k digits), which must be non-increasing and less than or equal to middle_digit
            # Also, middle_digit should be greater than the next digit to ensure uniqueness
            # So, next digit must be less than middle_digit
            def generate_second_half(current, remaining):
                if remaining == 0:
                    mountain = int(''.join(map(str, current)))
                    mountain_numbers.append(mountain)
                    return
                last = current[-1]
                for d in range(1, last + 1):
                    generate_second_half(current + [d], remaining - 1)

            # Initialize the second half with the middle digit
            generate_second_half(list(first_half), k)

    mountain_numbers.sort()
    return mountain_numbers

def generate_mountain_numbers_efficient():
    mountain_numbers = []

    from itertools import combinations_with_replacement, product

    for total_digits in range(1, 20, 2):
        k = (total_digits - 1) // 2

        # Generate all possible first k+1 digits (non-decreasing)
        # Use combinations_with_replacement to get non-decreasing sequences
        # Each sequence is a tuple
        first_half_sequences = list(combinations_with_replacement(range(1, 10), k + 1))

        for first_half in first_half_sequences:
            # Ensure the middle digit is unique in the entire number
            middle_digit = first_half[-1]
            if middle_digit in first_half[:-1]:
                continue  # Middle digit is not unique

            # Now, generate the second half: non-increasing, starting with middle_digit -1 down to 1
            # Because the next digit must be less than middle_digit to ensure uniqueness
            # And strictly less to ensure it's unique in entire number

            # The last k digits need to be non-increasing and <= middle_digit -1
            max_next_digit = middle_digit - 1
            if max_next_digit < 1:
                continue  # No valid second half

            # Generate all non-increasing sequences of length k with digits from 1 to max_next_digit
            # Using product with reversed digits to ensure non-increasing
            def generate_second_half(current, remaining, last_digit):
                if remaining == 0:
                    number = ''.join(map(str, first_half)) + ''.join(map(str, current))
                    mountain_numbers.append(int(number))
                    return
                for d in range(last_digit, 0, -1):
                    generate_second_half(current + [d], remaining - 1, d)

            generate_second_half([], k, max_next_digit)

    mountain_numbers.sort()
    return mountain_numbers

def main():
    import sys
    import bisect

    # Precompute all mountain numbers
    mountain_numbers = generate_mountain_numbers_efficient()
    # print(len(mountain_numbers))  # For debugging

    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        A_str, B_str, M_str = sys.stdin.readline().strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)

        # Find left and right indices using bisect
        left = bisect.bisect_left(mountain_numbers, A)
        right = bisect.bisect_right(mountain_numbers, B)

        # Count how many in mountain_numbers[left:right] are divisible by M
        count = 0
        for num in mountain_numbers[left:right]:
            if num % M == 0:
                count += 1

        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()