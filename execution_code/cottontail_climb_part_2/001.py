import sys
import threading
import bisect

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    test_cases = []
    for _ in range(T):
        A_str, B_str, M_str = sys.stdin.readline().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        test_cases.append((A, B, M))

    # Precompute all possible mountain numbers
    mountains = []

    def generate_mountains(length):
        def dfs(pos, num_str, used_digits, prev_digit, middle_digit):
            if pos == length:
                mountain_num = int(num_str)
                mountains.append(mountain_num)
                return
            middle = length // 2
            if pos < middle:
                # Non-decreasing part
                start_digit = prev_digit if prev_digit is not None else 1
                for digit in range(start_digit, 10):
                    if digit == 0:
                        continue
                    dfs(pos + 1, num_str + str(digit), used_digits | {digit}, digit, middle_digit)
            elif pos == middle:
                # Middle digit, must be unique
                for digit in range(1, 10):
                    if digit not in used_digits:
                        dfs(pos + 1, num_str + str(digit), used_digits | {digit}, digit, digit)
            else:
                # Non-increasing part, digits cannot be the middle digit
                start_digit = prev_digit
                for digit in range(1, start_digit + 1):
                    if digit == middle_digit:
                        continue
                    dfs(pos + 1, num_str + str(digit), used_digits | {digit}, digit, middle_digit)

        dfs(0, '', set(), None, None)

    # Generate mountains for all odd lengths from 1 to 19
    for length in range(1, 20, 2):
        generate_mountains(length)

    # Remove duplicates (if any) and sort
    mountains = sorted(set(mountains))

    # Process each test case
    for case_num, (A, B, M) in enumerate(test_cases, 1):
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M == 0:
                count += 1
        print(f'Case #{case_num}: {count}')

if __name__ == '__main__':
    threading.Thread(target=main).start()