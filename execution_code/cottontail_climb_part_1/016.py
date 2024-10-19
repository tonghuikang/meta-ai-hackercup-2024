import bisect

def generate_peaks():
    peaks = []
    for k in range(0, 9):  # k from 0 to8, since for k=9, 10-9=1, but s +k=10 which exceeds digits
        n_digits = 2 * k + 1
        for s in range(1, 10 - k):
            first_half = [s + i for i in range(k + 1)]
            second_half = [s + k - i for i in range(1, k + 1)]
            digits = first_half + second_half
            num = 0
            for d in digits:
                num = num * 10 + d
            peaks.append(num)
    peaks.sort()
    return peaks

def main():
    import sys
    import sys
    peaks = generate_peaks()
    T_and_rest = sys.stdin.read().split()
    T = int(T_and_rest[0])
    idx =1
    for test_case in range(1, T+1):
        A = int(T_and_rest[idx])
        B = int(T_and_rest[idx+1])
        M = int(T_and_rest[idx+2])
        idx +=3
        left = bisect.bisect_left(peaks, A)
        right = bisect.bisect_right(peaks, B)
        count =0
        for p in peaks[left:right]:
            if p % M ==0:
                count +=1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()