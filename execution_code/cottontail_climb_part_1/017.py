def generate_peaks():
    peaks = set()
    # k = 0: single-digit peaks
    for d in range(1, 10):
        peaks.add(d)
    # k >=1
    for k in range(1, 10):
        num_digits = 2 * k + 1
        for d1 in range(1, 10 - k):
            # Build the first k+1 digits increasing by 1
            digits = [d1 + i for i in range(k + 1)]
            # Build the last k digits decreasing by 1
            digits += [digits[-1] - i for i in range(1, k +1)]
            # Check all digits are between 1 and 9
            if all(1 <= d <=9 for d in digits):
                # Convert digits to number
                num = 0
                for d in digits:
                    num = num *10 + d
                peaks.add(num)
    return sorted(peaks)

def main():
    import sys
    import math

    peaks = generate_peaks()
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        A_str, B_str, M_str = sys.stdin.readline().strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        count = 0
        for peak in peaks:
            if A <= peak <= B:
                if peak % M ==0:
                    count +=1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()