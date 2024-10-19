import sys
import bisect
from itertools import combinations_with_replacement, product

def generate_mountain_numbers():
    mountain_numbers = set()
    for length in range(1, 20, 2):  # odd lengths from 1 to 19
        k = (length - 1) // 2
        for m in range(1, 10):  # middle digit
            # Generate left sequences: length k, non-decreasing, digits 1-9, <=m, not containing m
            left_sequences = []

            def generate_left(pos, last_digit, current):
                if pos == k:
                    left_sequences.append(''.join(map(str, current)))
                    return
                for d in range(last_digit, m+1):
                    if d == m:
                        continue
                    current.append(d)
                    generate_left(pos+1, d, current)
                    current.pop()

            if k == 0:
                left_sequences = ['']
            else:
                generate_left(0, 1, [])

            # Generate right sequences: length k, non-increasing, digits 1-9, <=m, not containing m
            right_sequences = []

            def generate_right(pos, last_digit, current):
                if pos == k:
                    right_sequences.append(''.join(map(str, current)))
                    return
                for d in range(last_digit, 0, -1):
                    if d == m:
                        continue
                    current.append(d)
                    generate_right(pos+1, d, current)
                    current.pop()

            if k == 0:
                right_sequences = ['']
            else:
                generate_right(0, m, [])

            # Combine left, middle, and right
            for left in left_sequences:
                for right in right_sequences:
                    number_str = left + str(m) + right
                    number = int(number_str)
                    mountain_numbers.add(number)
    return sorted(mountain_numbers)

def main():
    mountain_numbers = generate_mountain_numbers()
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        A_str, B_str, M_str = sys.stdin.readline().strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        # Find the range in mountain_numbers
        left = bisect.bisect_left(mountain_numbers, A)
        right = bisect.bisect_right(mountain_numbers, B)
        count = 0
        for num in mountain_numbers[left:right]:
            if num % M == 0:
                count +=1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()