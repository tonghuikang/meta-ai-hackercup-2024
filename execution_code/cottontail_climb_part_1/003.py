def generate_peaks():
    peaks = []
    for k in range(0, 9):  # k from 0 to 8, since 2*8+1=17 digits
        num_digits = 2 * k + 1
        if num_digits > 18:
            continue  # since B can be up to 10^18
        max_start = 9 - k
        for D1 in range(1, max_start +1):
            digits = []
            # Ascending part
            for i in range(k +1):
                digit = D1 + i
                if digit >9:
                    break
                digits.append(str(digit))
            else:
                # Descending part
                for i in range(k):
                    digit = digits[-1] -1
                    if digit <1:
                        break
                    digits.append(str(digit))
                else:
                    peak_num = int("".join(digits))
                    peaks.append(peak_num)
    peaks_sorted = sorted(peaks)
    return peaks_sorted

def main():
    import sys
    import bisect
    peaks = generate_peaks()
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        A, B, M = map(int, sys.stdin.readline().split())
        count = 0
        # Iterate through peaks and count those in [A,B] divisible by M
        for p in peaks:
            if A <= p <= B:
                if p % M ==0:
                    count +=1
        print(f"Case #{tc}: {count}")

if __name__ == "__main__":
    main()