import sys
import bisect

def generate_peaks():
    peaks = set()
    # k from 0 to 8 (since 2*8+1=17 digits)
    for k in range(0, 9):
        max_start_digit = 9 - k  # Ensure D1 + k <=9
        for D1 in range(1, max_start_digit +1):
            # Build increasing part
            increasing = [D1 + i for i in range(0, k+1)]
            # Build decreasing part
            decreasing = [increasing[-2 -i] for i in range(0, k)] if k >0 else []
            full_number_digits = increasing + decreasing
            # Check all digits are non-zero (already ensured by D1 >=1 and D1 +k <=9)
            number = int(''.join(map(str, full_number_digits)))
            peaks.add(number)
    # Also include single-digit peaks (k=0, already included)
    return sorted(peaks)

def main():
    peaks = generate_peaks()
    input = sys.stdin.read().splitlines()
    T = int(input[0])
    for test_case in range(1, T+1):
        A_str, B_str, M_str = input[test_case].strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        # Find the indices where peaks >= A and peaks <= B
        left = bisect.bisect_left(peaks, A)
        right = bisect.bisect_right(peaks, B)
        count = 0
        for num in peaks[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()