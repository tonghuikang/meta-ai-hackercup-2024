import sys
import threading
from bisect import bisect_left, bisect_right

def main():
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline().strip())
    test_cases = []
    max_M = 0
    for _ in range(T):
        A, B, M = map(int, sys.stdin.readline().strip().split())
        test_cases.append((A, B, M))
        max_M = max(max_M, M)
    mountain_numbers = []

    def generate_mountains(length, pos, is_increasing, last_digit, number_so_far, used_digits, middle_digit):
        if pos == length:
            mountain_numbers.append(number_so_far)
            return
        if pos < (length + 1) // 2:
            # Increasing part
            start_digit = last_digit
            for d in range(start_digit, 10):
                if d == 0:
                    continue
                new_number = number_so_far * 10 + d
                new_used_digits = used_digits.copy()
                new_used_digits.add(d)
                generate_mountains(length, pos + 1, True, d, new_number, new_used_digits, middle_digit)
        elif pos == (length + 1) // 2 - 1:
            # Middle digit position
            for d in range(last_digit, 10):
                if d == 0 or d in used_digits:
                    continue
                new_number = number_so_far * 10 + d
                new_used_digits = used_digits.copy()
                new_used_digits.add(d)
                generate_mountains(length, pos + 1, False, d, new_number, new_used_digits, d)
        else:
            # Decreasing part
            for d in range(min(last_digit, 9), 0, -1):
                if d == middle_digit:
                    continue
                new_number = number_so_far * 10 + d
                new_used_digits = used_digits.copy()
                new_used_digits.add(d)
                generate_mountains(length, pos + 1, False, d, new_number, new_used_digits, middle_digit)

    # Generate mountain numbers of lengths 1 to 19 (odd numbers)
    for length in range(1, 20, 2):
        def generate(length):
            def helper(pos, is_increasing, last_digit, number_so_far, used_digits, middle_digit):
                if pos == length:
                    if number_so_far <= 1e18:
                        mountain_numbers.append(number_so_far)
                    return
                if pos < (length + 1) // 2:
                    # Increasing part
                    start_digit = last_digit
                    for d in range(start_digit, 10):
                        if d == 0:
                            continue
                        new_number = number_so_far * 10 + d
                        new_used_digits = used_digits.copy()
                        new_used_digits.add(d)
                        helper(pos + 1, True, d, new_number, new_used_digits, middle_digit)
                elif pos == (length + 1) // 2:
                    # Middle digit position
                    for d in range(last_digit, 10):
                        if d == 0 or d in used_digits:
                            continue
                        new_number = number_so_far * 10 + d
                        new_used_digits = used_digits.copy()
                        new_used_digits.add(d)
                        helper(pos + 1, False, d, new_number, new_used_digits, d)
                else:
                    # Decreasing part
                    for d in range(min(last_digit,9), 0, -1):
                        if d == middle_digit:
                            continue
                        new_number = number_so_far * 10 + d
                        new_used_digits = used_digits.copy()
                        new_used_digits.add(d)
                        helper(pos + 1, False, d, new_number, new_used_digits, middle_digit)
            helper(0, True, 1, 0, set(), -1)

        generate(length)

    mountain_numbers = sorted(mountain_numbers)

    for idx, (A, B, M) in enumerate(test_cases, 1):
        left = bisect_left(mountain_numbers, A)
        right = bisect_right(mountain_numbers, B)
        count = 0
        for num in mountain_numbers[left:right]:
            if num % M == 0:
                count += 1
        print(f"Case #{idx}: {count}")

threading.Thread(target=main).start()