def generate_peaks():
    peaks = []
    for k in range(0, 10):  # k from 0 to 9
        max_D1 = 9 - k
        for D1 in range(1, max_D1 +1):
            # Generate first k+1 digits
            ascending = [str(D1 + i) for i in range(0, k+1)]
            # Generate last k digits, descending
            descending = [str(D1 + k - i) for i in range(1, k+1)]
            # Combine to form the peak
            digits = ascending + descending
            peak = int(''.join(digits))
            peaks.append(peak)
    return sorted(peaks)

def main():
    import sys
    import bisect
    peaks = generate_peaks()
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
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
        count =0
        for peak in peaks:
            if A <= peak <= B:
                if peak % M ==0:
                    count +=1
            elif peak > B:
                break
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()