import sys
import bisect
from itertools import combinations_with_replacement

def generate_mountain_numbers():
    mountain_numbers = set()
    for k in range(0, 10):  # L=2k+1=1,...,19
        L = 2 * k + 1
        if L > 19:
            break
        for m_digit in range(1, 10):
            if k == 0:
                mountain_numbers.add(m_digit)
                continue
            if m_digit == 1 and k > 0:
                # No digits less than 1, skip
                continue
            # Generate all non-decreasing sequences of first k digits, digits 1 to m_digit-1
            first_digits = list(combinations_with_replacement(range(1, m_digit), k))
            if not first_digits:
                continue
            # Similarly for last k digits:
            last_digits = list(combinations_with_replacement(range(1, m_digit), k))
            if not last_digits:
                continue
            for fd in first_digits:
                for ld in last_digits:
                    # Ensure that last digits are non-increasing by reversing
                    ld_rev = ld[::-1]
                    # Combine
                    num_digits = list(fd) + [m_digit] + list(ld_rev)
                    # Convert to integer
                    num = 0
                    for d in num_digits:
                        num = num * 10 + d
                    mountain_numbers.add(num)
    return sorted(mountain_numbers)

def main():
    import sys
    import threading

    def run():
        mountain_numbers = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for case in range(1, T + 1):
            A_str, B_str, M_str = sys.stdin.readline().strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find the left and right indices
            left = bisect.bisect_left(mountain_numbers, A)
            right = bisect.bisect_right(mountain_numbers, B)
            count = 0
            for num in mountain_numbers[left:right]:
                if num % M == 0:
                    count += 1
            print(f"Case #{case}: {count}")

    threading.Thread(target=run,).start()

if __name__ == "__main__":
    main()