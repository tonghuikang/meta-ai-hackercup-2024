import sys
import bisect

def generate_peaks():
    peaks = []
    # Single-digit peaks
    for d in range(1, 10):
        peaks.append(d)
    # Multi-digit peaks
    for k in range(1, 10):  # k from 1 to 9, since 2*9 +1 =19 digits
        num_digits = 2 * k + 1
        for start in range(1, 10 - k):
            # Build first k+1 digits
            first_part = [start + i for i in range(k + 1)]
            # Verify no digit exceeds 9
            if first_part[-1] > 9:
                continue
            # Build the full peak by appending the decreasing part
            full_digits = first_part + [first_part[-2 - i] for i in range(k)]
            # Convert digits to number
            peak = 0
            for d in full_digits:
                if d == 0:
                    break  # Skip if any digit is zero
                peak = peak * 10 + d
            else:
                peaks.append(peak)
    peaks.sort()
    return peaks

def main():
    peaks = generate_peaks()
    input = sys.stdin.read().split()
    T = int(input[0])
    ptr = 1
    for test_case in range(1, T + 1):
        A = int(input[ptr])
        B = int(input[ptr + 1])
        M = int(input[ptr + 2])
        ptr += 3
        # Find indices of peaks within [A, B]
        left = bisect.bisect_left(peaks, A)
        right = bisect.bisect_right(peaks, B)
        count = 0
        for peak in peaks[left:right]:
            if peak % M == 0:
                count += 1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()