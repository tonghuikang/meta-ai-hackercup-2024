import sys
import bisect

def generate_mountain_numbers():
    mountains = []

    # Function to recursively build the first part
    def build_first_part(length, current, start_digit):
        if length == 0:
            return [current]
        numbers = []
        for d in range(start_digit, 10):
            numbers += build_first_part(length - 1, current * 10 + d, d)
        return numbers

    # Function to build mountain numbers for a given total length
    def generate_for_length(total_length):
        k = (total_length -1)//2
        first_part_length = k +1
        last_part_length = k
        first_parts = build_first_part(first_part_length, 0, 1)
        for first in first_parts:
            first_digits = list(map(int, str(first)))
            peak = first_digits[-1]
            # Ensure the peak is unique
            if k >0 and first_digits[-2] == peak:
                continue
            # Build the last part: non-increasing starting from peak
            def build_last_part(length, current, max_digit):
                if length ==0:
                    return [current]
                numbers = []
                for d in range(1, max_digit +1):
                    numbers += build_last_part(length -1, current *10 + d, d)
                return numbers

            last_parts = build_last_part(last_part_length, 0, peak)
            for last in last_parts:
                number = first * (10**last_part_length) + last
                mountains.append(number)

    # Generate for all odd lengths from 1 to 19
    for total_length in range(1, 20, 2):
        generate_for_length(total_length)

    mountains = sorted(mountains)
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
            # Find the relevant mountain numbers
            left = bisect.bisect_left(mountains, A)
            right = bisect.bisect_right(mountains, B)
            count = 0
            # Iterate through the subset and count divisible by M
            for num in mountains[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{case}: {count}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()