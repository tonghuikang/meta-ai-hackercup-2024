import sys
import bisect

def generate_mountain_numbers():
    mountain_numbers = []

    # Function to generate non-decreasing sequences
    def generate_non_decreasing(length, start, current, sequences):
        if len(current) == length:
            sequences.append(current[:])
            return
        for digit in range(start, 10):
            current.append(digit)
            generate_non_decreasing(length, digit, current, sequences)
            current.pop()

    # Function to generate non-increasing sequences
    def generate_non_increasing(length, start, current, sequences):
        if len(current) == length:
            sequences.append(current[:])
            return
        for digit in range(start, 0, -1):
            current.append(digit)
            generate_non_increasing(length, digit, current, sequences)
            current.pop()

    for total_length in range(1, 20, 2):  # Odd lengths from 1 to 19
        k = total_length // 2
        first_half_length = k + 1
        second_half_length = k + 1

        first_sequences = []
        generate_non_decreasing(first_half_length, 1, [], first_sequences)

        for first_seq in first_sequences:
            middle_digit = first_seq[-1]
            # Ensure the middle digit is unique by having the second half start strictly less than middle_digit
            second_sequences = []
            generate_non_increasing(second_half_length, first_seq[-1], [], second_sequences)
            for second_seq in second_sequences:
                if second_seq and second_seq[0] == middle_digit:
                    # Ensure uniqueness of the middle digit
                    if len(second_seq) == 1 or second_seq[1] < second_digit := second_seq[0]:
                        pass
                    else:
                        continue
                # Combine first_seq and second_seq excluding the last digit of first_seq to avoid duplication
                full_number_digits = first_seq + second_seq[1:]
                # Convert to integer
                number = int(''.join(map(str, full_number_digits)))
                mountain_numbers.append(number)

    mountain_numbers = sorted(set(mountain_numbers))
    return mountain_numbers

def main():
    mountain_numbers = generate_mountain_numbers()
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        A_str, B_str, M_str = sys.stdin.readline().strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        # Find the indices where mountain_numbers >= A and <= B
        left = bisect.bisect_left(mountain_numbers, A)
        right = bisect.bisect_right(mountain_numbers, B)
        count = 0
        for num in mountain_numbers[left:right]:
            if num % M == 0:
                count += 1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()