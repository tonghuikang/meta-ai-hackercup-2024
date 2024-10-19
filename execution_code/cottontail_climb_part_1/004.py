import sys
import bisect

def generate_peaks():
    peaks = []
    # k=0: single-digit peaks
    for d in range(1, 10):
        peaks.append(d)
    # k >=1
    for k in range(1, 9):  # k from1 to8, since 2*8+1=17 digits
        for d in range(1, 10 - k):  # d from1 to9 -k
            # Build the increasing part
            increasing = [d + i for i in range(k +1)]
            # Build the decreasing part
            decreasing = [d + k - i for i in range(1, k +1)]
            number_digits = increasing + decreasing
            # Convert to integer
            number = 0
            for digit in number_digits:
                number = number *10 + digit
            peaks.append(number)
    peaks.sort()
    return peaks

def count_peaks_in_range(peaks, A, B):
    left = bisect.bisect_left(peaks, A)
    right = bisect.bisect_right(peaks, B)
    return peaks[left:right]

def main():
    peaks = generate_peaks()
    T = int(sys.stdin.readline())
    for case in range(1, T +1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                break
        if not line:
            break
        A_str, B_str, M_str = line.strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        # Get peaks in [A, B]
        selected_peaks = count_peaks_in_range(peaks, A, B)
        # Count peaks divisible by M
        if M ==1:
            count = len(selected_peaks)
        else:
            count = 0
            for p in selected_peaks:
                if p % M ==0:
                    count +=1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()