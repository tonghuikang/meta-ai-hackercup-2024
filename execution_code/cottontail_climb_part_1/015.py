def main():
    import sys
    import bisect

    # Precompute all peaks
    peaks = []
    for k in range(0, 9):  # since k <=8 (d>=1, d+k <=9)
        for d in range(1, 10):
            if d + k > 9:
                continue
            # Build first k+1 digits
            ascending = [d + i for i in range(k +1)]
            # Build descending k digits (excluding the peak digit)
            descending = [d + k - i for i in range(1, k +1)]
            digits = ascending + descending
            # Convert to integer
            num = 0
            for digit in digits:
                num = num *10 + digit
            peaks.append(num)
    # Remove duplicates if any and sort
    peaks = sorted(peaks)
    # Read input
    input = sys.stdin.read().split()
    T = int(input[0])
    ptr =1
    for test_case in range(1, T+1):
        A = int(input[ptr])
        B = int(input[ptr+1])
        M = int(input[ptr+2])
        ptr +=3
        # Find peaks in [A,B]
        left = bisect.bisect_left(peaks, A)
        right = bisect.bisect_right(peaks, B)
        count =0
        for num in peaks[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()