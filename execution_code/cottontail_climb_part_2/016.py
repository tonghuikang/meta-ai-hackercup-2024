import sys
import bisect

def generate_mountain_numbers():
    # List to store mountain numbers
    mountains = []

    # Function to generate non-decreasing sequences
    def generate_non_decreasing(length, start, current, sequences):
        if len(current) == length:
            sequences.append(current.copy())
            return
        for digit in range(start, 10):
            current.append(digit)
            generate_non_decreasing(length, digit, current, sequences)
            current.pop()

    # Function to generate non-increasing sequences
    def generate_non_increasing(length, max_digit, current, sequences):
        if len(current) == length:
            sequences.append(current.copy())
            return
        for digit in range(1, max_digit + 1):
            current.append(digit)
            generate_non_increasing(length, digit, current, sequences)
            current.pop()

    # Generate mountain numbers for each odd digit length
    for total_digits in range(1, 19, 2):  # 1,3,5,...,17
        k = total_digits // 2
        first_half_length = k + 1
        second_half_length = k

        # Generate all non-decreasing first_half_length digits starting from 1 to 9
        sequences = []
        generate_non_decreasing(first_half_length, 1, [], sequences)

        for first_half in sequences:
            peak = first_half[-1]
            if k == 0:
                # Single digit mountain
                number = peak
                mountains.append(number)
                continue

            # The peak must be greater than the previous digit
            # and we need to generate second_half_length digits <= peak -1
            # because the middle digit must be > the next digit
            # But from the problem examples, it seems the middle digit should be > next digit
            # So the digit after peak should be <= peak -1
            # Thus, the possible second half sequences are non-increasing sequences
            # of length second_half_length with digits <= peak -1 and >=1
            if peak == 1:
                # No possible second half, since digits must be >=1 and <=0
                continue
            max_second = peak -1
            second_sequences = []
            generate_non_increasing(second_half_length, max_second, [], second_sequences)
            for second_half in second_sequences:
                # Combine first_half and second_half
                number_digits = first_half + second_half
                # Convert to integer
                number = 0
                for d in number_digits:
                    number = number * 10 + d
                mountains.append(number)

    mountains = sorted(mountains)
    return mountains

def main():
    import sys
    import threading

    def run():
        mountains = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for case in range(1, T +1):
            A, B, M = map(int, sys.stdin.readline().strip().split())
            # Find the left and right indices
            left = bisect.bisect_left(mountains, A)
            right = bisect.bisect_right(mountains, B)
            count = 0
            for num in mountains[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{case}: {count}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()