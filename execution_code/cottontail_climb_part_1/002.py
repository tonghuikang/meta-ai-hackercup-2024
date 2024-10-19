def generate_peaks():
    peaks = []
    # k from 0 to 9 (since 2*9+1=19 digits)
    for k in range(0, 10):
        max_start = 9 - k
        for start in range(1, max_start +1):
            digits = []
            # Increasing part
            for i in range(k+1):
                digit = start + i
                if digit >9:
                    break
                digits.append(str(digit))
            else:
                # Decreasing part
                for i in range(1, k+1):
                    digit = start +k -i
                    if digit <1:
                        break
                    digits.append(str(digit))
                else:
                    # Successfully constructed all digits
                    number = int(''.join(digits))
                    peaks.append(number)
    return sorted(peaks)

def count_peaks(peaks, A, B, M):
    count =0
    for peak in peaks:
        if A <= peak <=B and peak % M ==0:
            count +=1
    return count

def main():
    import sys
    import sys
    peaks = generate_peaks()
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        line=""
        while line.strip()=='':
            line = sys.stdin.readline()
        A_str, B_str, M_str = line.strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        cnt = count_peaks(peaks, A, B, M)
        print(f"Case #{case}: {cnt}")

if __name__ == "__main__":
    main()