def generate_peaks():
    peaks = []
    for k in range(0, 10):  # since 2k+1 <=19 when k<=9
        N = 2 * k + 1
        max_D1 = 9 - k
        if max_D1 < 1:
            continue
        for D1 in range(1, max_D1 +1):
            # Generate up part
            up = [D1 + i for i in range(k +1)]
            # Check if all digits are <=9
            if up[-1] >9:
                continue
            # Generate down part
            down = [up[-2 -i] for i in range(k)] if k >0 else []
            digits = up + down
            # Ensure no digit is zero and all digits are between1 and9
            if any(d <1 or d >9 for d in digits):
                continue
            # Convert digits to number
            num = int(''.join(map(str,digits)))
            peaks.append(num)
    peaks.sort()
    return peaks

def main():
    import sys
    import bisect

    peaks = generate_peaks()

    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        A_str, B_str, M_str = sys.stdin.readline().split()
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
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()