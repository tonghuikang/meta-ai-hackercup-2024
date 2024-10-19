def generate_peaks():
    peaks = []
    for k in range(0, 9):  # k from 0 to 8 since 2*8+1=17 digits
        max_start = 9 - k
        for s in range(1, max_start + 1):
            # Build the first k+1 digits increasing by 1
            inc_part = [s + i for i in range(k + 1)]
            # Ensure all digits are <=9
            if inc_part[-1] > 9:
                continue
            # Build the decreasing part
            dec_part = inc_part[-2::-1]  # Exclude the peak digit
            full_number_digits = inc_part + dec_part
            # Check for any zero digits
            if 0 in full_number_digits:
                continue
            # Convert to integer
            num = int(''.join(map(str, full_number_digits)))
            peaks.append(num)
    # Also include single-digit peaks (k=0)
    single_digit_peaks = list(range(1, 10))
    peaks = list(set(peaks + single_digit_peaks))
    peaks.sort()
    return peaks

def main():
    import sys
    import bisect

    peaks = generate_peaks()
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        A, B, M = map(int, sys.stdin.readline().split())
        # Find the peaks within [A, B]
        left = bisect.bisect_left(peaks, A)
        right = bisect.bisect_right(peaks, B)
        count = 0
        for num in peaks[left:right]:
            if num % M == 0:
                count +=1
        print(f"Case #{tc}: {count}")

if __name__ == "__main__":
    main()