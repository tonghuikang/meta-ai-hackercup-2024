import sys
import itertools
import bisect

def generate_mountain_numbers():
    all_mountains = []
    # n = 2k +1, k from0 up to9 (n<=19)
    for k in range(0, 10):
        n = 2 * k +1
        if n >19:
            break
        if k ==0:
            # single-digit mountains
            for d in range(1,10):
                all_mountains.append(d)
        else:
            # for k>=1
            for d in range(2,10):
                # Generate all non-decreasing sequences of length k with digits from 1 to d-1
                left_sequences = itertools.combinations_with_replacement(range(1, d), k)
                # Generate all non-decreasing sequences of length k with digits from 1 to d-1
                right_sequences = itertools.combinations_with_replacement(range(1, d), k)
                # Convert right_sequences to list since we need to iterate multiple times
                right_sequences = list(right_sequences)
                for left in left_sequences:
                    left_digits = list(left)
                    for right in right_sequences:
                        right_digits = list(right[::-1])  # non-increasing
                        # Combine left + [d] + right
                        digits = left_digits + [d] + right_digits
                        # Convert to integer
                        num = 0
                        for digit in digits:
                            num = num *10 + digit
                        all_mountains.append(num)
    # Sort all_mountains
    all_mountains.sort()
    return all_mountains

def main():
    all_mountains = generate_mountain_numbers()
    input = sys.stdin.read().split()
    T = int(input[0])
    idx=1
    for test_case in range(1, T+1):
        A = int(input[idx])
        B = int(input[idx+1])
        M = int(input[idx+2])
        idx +=3
        # Find the range of mountain numbers within [A,B]
        left = bisect.bisect_left(all_mountains, A)
        right_idx = bisect.bisect_right(all_mountains, B)
        count =0
        for num in all_mountains[left:right_idx]:
            if num % M ==0:
                count +=1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()