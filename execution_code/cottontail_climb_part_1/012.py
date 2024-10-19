def main():
    import sys

    # Precompute all peak numbers
    peaks = []

    for k in range(0, 10):  # k from 0 to 9 (for up to 19 digits)
        length = 2 * k + 1
        if length > 19:
            continue
        if k == 0:
            # Single-digit peaks
            for d in range(1, 10):
                peaks.append(d)
        else:
            # Multi-digit peaks
            max_start = 9 - k
            for d1 in range(1, max_start +1):
                digits_up = [d1 + i for i in range(k+1)]
                digits_down = [digits_up[-1] - i for i in range(1, k+1)]
                digits = digits_up + digits_down
                # Check all digits are between 1 and 9
                if all(1 <= digit <=9 for digit in digits):
                    # Convert to integer
                    number = 0
                    for digit in digits:
                        number = number *10 + digit
                    peaks.append(number)

    # Sort the list of peaks
    peaks.sort()

    # Read input
    input = sys.stdin.read().split()
    T = int(input[0])
    ptr =1
    for test_case in range(1,T+1):
        A = int(input[ptr])
        B = int(input[ptr+1])
        M = int(input[ptr+2])
        ptr +=3
        count =0
        for peak in peaks:
            if A <= peak <= B:
                if peak % M ==0:
                    count +=1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()