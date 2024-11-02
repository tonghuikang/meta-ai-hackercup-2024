import sys
import bisect

def generate_mountain_numbers():
    mountains = []

    # Function to generate non-decreasing sequences without zero
    def generate_first_half(length, current, last_digit):
        if len(current) == length:
            return [current]
        sequences = []
        for digit in range(last_digit, 10):
            if digit == 0:
                continue
            sequences.extend(generate_first_half(length, current + [digit], digit))
        return sequences

    # Function to generate non-increasing sequences without zero
    def generate_second_half(length, current, last_digit):
        if len(current) == length:
            return [current]
        sequences = []
        for digit in range(last_digit, 0, -1):
            sequences.extend(generate_second_half(length, current + [digit], digit))
        return sequences

    # Generate mountain numbers for all possible odd lengths
    for total_length in range(1, 19+1, 2):  # up to 19 digits
        k = total_length // 2
        first_half_length = k + 1
        # Generate all non-decreasing sequences for the first half
        first_halves = generate_first_half(first_half_length, [], 1)
        for first_half in first_halves:
            peak = first_half[-1]
            # The peak must be greater than its previous digit if k > 0
            if k > 0 and first_half[-2] >= peak:
                continue  # Peak is not unique
            # Generate the second half which is non-increasing and starts with peak
            second_half_length = k
            second_halves = generate_second_half(second_half_length, [], peak)
            for second_half in second_halves:
                number_digits = first_half + second_half[::-1]
                number = int(''.join(map(str, number_digits)))
                mountains.append(number)
    mountains = sorted(set(mountains))
    return mountains

def main():
    import sys
    import threading

    def run():
        mountains = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for case in range(1, T + 1):
            A_str, B_str, M_str = sys.stdin.readline().strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find the range in mountains
            left = bisect.bisect_left(mountains, A)
            right = bisect.bisect_right(mountains, B)
            count = 0
            for num in mountains[left:right]:
                if num % M == 0:
                    count += 1
            print(f"Case #{case}: {count}")

    threading.Thread(target=run,).start()

if __name__ == "__main__":
    main()