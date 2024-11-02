import sys
import bisect

def generate_mountain_numbers():
    mountains = []

    def backtrack(n_digits, current_digits, pos, is_increasing, peak_pos, last_digit):
        if pos == n_digits:
            # Check if it's a valid mountain
            mountains.append(int(''.join(map(str, current_digits))))
            return
        if pos < peak_pos:
            # Left side: non-decreasing
            start = last_digit
            for d in range(start, 10):
                if d == 0:
                    continue
                current_digits[pos] = d
                backtrack(n_digits, current_digits, pos + 1, True, peak_pos, d)
        elif pos == peak_pos:
            # Peak: must be greater than previous digit
            for d in range(last_digit + 1, 10):
                if d == 0:
                    continue
                current_digits[pos] = d
                backtrack(n_digits, current_digits, pos + 1, False, peak_pos, d)
        else:
            # Right side: non-increasing
            start = current_digits[pos - 1]
            for d in range(1, current_digits[pos -1]+1):
                if d == 0:
                    continue
                current_digits[pos] = d
                backtrack(n_digits, current_digits, pos + 1, False, peak_pos, d)

    for total_digits in range(1, 20, 2):
        peak = total_digits // 2
        current = [0] * total_digits
        backtrack(total_digits, current, 0, True, peak, 0)

    mountains = sorted(mountains)
    return mountains

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    index = 1
    mountains = generate_mountain_numbers()
    for test_case in range(1, T + 1):
        A = int(input[index])
        B = int(input[index + 1])
        M = int(input[index + 2])
        index += 3
        # Find the left and right indices using bisect
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M == 0:
                count += 1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()