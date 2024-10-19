import sys
import bisect

def generate_mountain_numbers():
    mountains = []

    # Maximum number of digits is 19 (since B <= 10^18)
    for k in range(0, 10):  # since 2k+1 <=19 when k<=9
        length = 2 * k + 1
        if length > 19:
            continue

        # Generate all possible non-decreasing sequences for the first k+1 digits
        def backtrack_first(pos, current, last_digit):
            if pos == k +1:
                # Now generate the last k+1 digits, which should be non-increasing and starts with current[-1]
                middle_digit = current[-1]
                backtrack_last(0, current, [middle_digit], middle_digit)
                return
            for d in range(last_digit, 10):
                if d ==0:
                    continue
                current.append(d)
                backtrack_first(pos +1, current, d)
                current.pop()

        # Generate all possible non-increasing sequences for the last k+1 digits
        def backtrack_last(pos, first_part, current_last, last_digit):
            if pos == k +1:
                # Combine first_part and current_last, ensuring uniqueness of middle digit
                # First part has k+1 digits, current_last has k+1 digits with first being the middle digit
                full_digits = first_part + current_last[1:]
                # Check uniqueness of middle digit
                # Ensure that the middle digit is unique, meaning it's greater than its neighbors
                # However, according to the problem, "the middle digit is unique" likely means it's distinct.
                # So we ensure that the middle digit is greater than the digits before and after
                mid = k
                if full_digits[mid] > full_digits[mid -1] and full_digits[mid] > full_digits[mid +1]:
                    # Convert to number
                    number = 0
                    for d in full_digits:
                        number = number *10 + d
                    mountains.append(number)
                return
            for d in range(1, last_digit+1):
                current_last.append(d)
                backtrack_last(pos +1, first_part, current_last, d)
                current_last.pop()

        backtrack_first(0, [], 1)

    mountains = sorted(set(mountains))
    return mountains

def main():
    import sys
    import threading

    def run():
        mountains = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for case in range(1, T+1):
            A_str, B_str, M_str = sys.stdin.readline().strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find the indices of mountains >=A and <=B
            left = bisect.bisect_left(mountains, A)
            right = bisect.bisect_right(mountains, B)
            count = 0
            for num in mountains[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{case}: {count}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()