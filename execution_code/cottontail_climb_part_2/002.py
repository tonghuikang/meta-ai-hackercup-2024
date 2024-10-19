import sys
import bisect

def generate_mountains():
    mountains = set()

    # Single-digit mountains
    for d in range(1, 10):
        mountains.add(d)

    # Function to generate mountain numbers of length n=2k+1
    def generate(n):
        k = (n - 1) // 2

        def backtrack(position, number, last_digit, digits_used):
            if position == n:
                mountains.add(int(''.join(map(str, number))))
                return
            if position < k + 1:
                # Non-decreasing part
                start = last_digit if last_digit != -1 else 1
                for d in range(start, 10):
                    if d == 0:
                        continue
                    number.append(d)
                    backtrack(position + 1, number, d, digits_used | (1 << d) if position == k else digits_used)
                    number.pop()
            else:
                # Non-increasing part
                start = number[k]  # The middle digit
                for d in range(start, -1, -1):
                    if d == 0:
                        continue
                    # Ensure that the digit does not violate non-increasing
                    if d > number[position - 1]:
                        continue
                    # Ensure the middle digit is unique
                    if position == k + 1 and d == number[k]:
                        continue
                    # To ensure uniqueness of the middle digit, we check if it appears elsewhere
                    if d == number[k]:
                        continue
                    number.append(d)
                    backtrack(position + 1, number, d, digits_used)
                    number.pop()

        backtrack(0, [], -1, 0)

    # Generate mountains for all odd lengths up to 17 digits
    for n in range(1, 18, 2):
        generate(n)

    return sorted(mountains)

def main():
    mountains = generate_mountains()
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        A_str, B_str, M_str = sys.stdin.readline().strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        # Find the range of mountains within [A, B]
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M == 0:
                count += 1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()