import sys
import bisect

def generate_mountain_numbers():
    mountains = []
    from itertools import combinations_with_replacement, product

    def generate_non_decreasing(k_plus1):
        # Generate all non-decreasing sequences of length k_plus1 with digits 1-9
        if k_plus1 == 0:
            return []
        result = []
        def backtrack(start, path, length):
            if length == k_plus1:
                result.append(path[:])
                return
            for d in range(start, 10):
                if d == 0:
                    continue
                path.append(d)
                backtrack(d, path, length + 1)
                path.pop()
        backtrack(1, [], 0)
        return result

    def generate_non_increasing(k, max_digit, exclude_digit):
        # Generate all non-increasing sequences of length k with digits <= max_digit and != exclude_digit
        result = []
        def backtrack(start, path, length):
            if length == k:
                result.append(path[:])
                return
            for d in range(start, 0, -1):
                if d == exclude_digit:
                    continue
                path.append(d)
                backtrack(d, path, length + 1)
                path.pop()
        backtrack(max_digit, [], 0)
        return result

    for length in range(1, 20, 2):
        k = (length - 1) // 2
        k_plus1 = k + 1
        first_half_sequences = generate_non_decreasing(k_plus1)
        for first_half in first_half_sequences:
            middle_digit = first_half[-1]
            # Check that the middle digit is unique in the first half
            if first_half[:-1].count(middle_digit) > 0:
                continue
            # Generate the second half
            second_half_sequences = generate_non_increasing(k, middle_digit, middle_digit)
            for second_half in second_half_sequences:
                # Combine to form the full number
                full_number_digits = first_half + second_half
                # Convert digits to integer
                number = 0
                for d in full_number_digits:
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
        for case in range(1, T+1):
            line = sys.stdin.readline()
            while line.strip() == '':
                line = sys.stdin.readline()
            A_str, B_str, M_str = line.strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find the indices in the sorted mountain list
            left = bisect.bisect_left(mountains, A)
            right = bisect.bisect_right(mountains, B)
            count = 0
            # Iterate through the relevant mountains and count divisible by M
            for num in mountains[left:right]:
                if num % M == 0:
                    count +=1
            print(f"Case #{case}: {count}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()