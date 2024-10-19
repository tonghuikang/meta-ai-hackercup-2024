import sys
import bisect

def generate_peaks():
    peaks = []
    # k ranges such that 2k+1 <= 19 (since B <= 1e18 has 18 digits)
    for k in range(0, 10):  # 2k+1 <= 19 when k=9
        length = 2 * k + 1
        if length > 19:
            continue
        # The starting digit ranges from 1 to 9 - k
        for start in range(1, 10):
            # Check if the increasing sequence is possible
            peak_digits = []
            current = start
            valid = True
            for _ in range(k +1):
                if current >9:
                    valid = False
                    break
                peak_digits.append(current)
                current +=1
            if not valid:
                continue
            # Now decreasing part
            for _ in range(k):
                current -=1
                if current <1:
                    valid = False
                    break
                peak_digits.append(current)
            if valid:
                peak_num = int(''.join(map(str, peak_digits)))
                peaks.append(peak_num)
    # Sort the peaks
    peaks.sort()
    return peaks

def main():
    peaks = generate_peaks()
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        A_str = sys.stdin.readline().strip()
        while A_str == '':
            A_str = sys.stdin.readline().strip()
        A,B,M = map(int, A_str.split())
        # Find peaks within [A,B]
        left = bisect.bisect_left(peaks, A)
        right = bisect.bisect_right(peaks, B)
        count = 0
        for num in peaks[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()