import sys
import bisect

def generate_peaks():
    peaks = []
    for k in range(0, 10):  # since 2k+1 <=19 when k<=9
        num_digits = 2 * k +1
        if num_digits > 19:
            continue
        for start in range(1, 10 - k):
            digits = []
            # Ascending part
            for i in range(0, k+1):
                digits.append(str(start + i))
            # Descending part
            for i in range(k-1, -1, -1):
                digits.append(str(start + i))
            peak_num = int(''.join(digits))
            peaks.append(peak_num)
    peaks = sorted(peaks)
    return peaks

def count_peaks(peaks, A, B, M):
    left = bisect.bisect_left(peaks, A)
    right = bisect.bisect_right(peaks, B)
    count = 0
    for i in range(left, right):
        if peaks[i] % M ==0:
            count +=1
    return count

def main():
    peaks = generate_peaks()
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        A_str,B_str,M_str = line.strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        cnt = count_peaks(peaks, A, B, M)
        print(f"Case #{case}: {cnt}")

if __name__ == "__main__":
    main()