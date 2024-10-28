import sys
import threading
import bisect

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    from bisect import bisect_left, bisect_right

    # Generate all mountain numbers
    mountain_numbers = []

    # Handle k = 0 separately (single-digit numbers)
    for d in range(1, 10):
        mountain_numbers.append(d)

    # For k from 1 to 9 (maximum k for 19-digit numbers)
    max_k = 9
    for k in range(1, max_k + 1):
        def generate(pos, D):
            if pos == k:
                # For middle digit, ensure it's unique by choosing D[pos] > D[pos-1]
                for d in range(D[pos - 1] + 1, 10):
                    D.append(d)
                    # Build the full number by mirroring D[0..k-1]
                    full_digits = D + D[k - 1::-1]
                    N = int(''.join(map(str, full_digits)))
                    mountain_numbers.append(N)
                    D.pop()
            else:
                # For next digit, maintain non-decreasing order
                for d in range(D[pos - 1], 10):
                    D.append(d)
                    generate(pos + 1, D)
                    D.pop()

        # Start generating sequences starting with digits 1 to 9
        for first_digit in range(1, 10):
            D = [first_digit]
            generate(1, D)

    # Sort the mountain numbers
    mountain_numbers.sort()

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        A_str, B_str, M_str = sys.stdin.readline().strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)

        # Find indices where mountain_numbers >= A and <= B
        l = bisect_left(mountain_numbers, A)
        r = bisect_right(mountain_numbers, B)

        count = 0
        for N in mountain_numbers[l:r]:
            if N % M == 0:
                count += 1

        print(f"Case #{test_case}: {count}")

threading.Thread(target=main).start()