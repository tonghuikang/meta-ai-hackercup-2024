def generate_peaks():
    peaks = []
    for k in range(0, 9):  # k from 0 to 8
        max_start = 9 - k
        for D1 in range(1, max_start +1):
            # First k+1 digits: D1 to D1+k
            increasing = [D1 + i for i in range(0, k+1)]
            # Last k digits: D1+k-1 down to D1
            decreasing = [D1 + k - i for i in range(1, k+1)]
            digits = increasing + decreasing
            number = int(''.join(map(str, digits)))
            peaks.append(number)
    peaks = sorted(peaks)
    return peaks

def main():
    import sys
    import bisect

    peaks = generate_peaks()

    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        A_str, B_str, M_str = line.strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        count = 0
        for peak in peaks:
            if A <= peak <= B:
                if peak % M ==0:
                    count +=1
            elif peak > B:
                break
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()