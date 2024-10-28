import sys
import itertools
import bisect

def generate_mountain_numbers():
    mountains = []
    for k in range(0, 10):
        l = 2 * k + 1
        if k == 0:
            # Single-digit mountain numbers
            for D in range(1, 10):
                mountains.append(D)
        else:
            # For each possible middle digit D
            for D in range(1, 10):
                # Generate all non-decreasing prefixes of length k with digits < D
                # Using combinations with replacement from 1 to D-1
                if D == 1:
                    # If D is 1, all prefix digits must be <1, which is invalid
                    continue
                # Generate non-decreasing sequences of length k from 1 to D-1
                for prefix in itertools.combinations_with_replacement(range(1, D), k):
                    prefix = list(prefix)
                    # Append the middle digit D
                    full_prefix = prefix + [D]
                    # Now generate non-increasing suffix of length k with digits <= D-1
                    # This is equivalent to non-decreasing sequences from 1 to D-1, reversed
                    suffix_sequences = itertools.combinations_with_replacement(range(1, D), k)
                    for suffix in suffix_sequences:
                        suffix = list(suffix)
                        # To make it non-increasing, reverse the non-decreasing sequence
                        suffix = suffix[::-1]
                        # Combine prefix and suffix
                        number_digits = full_prefix + suffix
                        # Convert digits to integer
                        number = 0
                        for digit in number_digits:
                            number = number * 10 + digit
                        mountains.append(number)
    mountains = sorted(mountains)
    return mountains

def main():
    mountains = generate_mountain_numbers()
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                break
        if not line:
            break
        A_str, B_str, M_str = line.strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        # Find left and right indices using bisect
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M == 0:
                count +=1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()