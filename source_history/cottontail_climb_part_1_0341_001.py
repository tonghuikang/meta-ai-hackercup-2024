#!/usr/bin/env python3
import sys

def generate_peaks():
    peaks = []
    for k in range(0, 9):  # k from 0 to 8
        for D1 in range(1, 10 - k):
            # Generate the increasing part
            digits_up = [D1 + i for i in range(k + 1)]
            # Generate the decreasing part (exclude the peak digit to avoid duplication)
            digits_down = digits_up[:-1][::-1]
            digits = digits_up + digits_down
            # Convert digits to number
            number = int(''.join(map(str, digits)))
            peaks.append(number)
    peaks.sort()
    return peaks

def main():
    import sys
    import threading

    def run():
        peaks = generate_peaks()
        T = int(sys.stdin.readline())
        for case_num in range(1, T + 1):
            line = sys.stdin.readline()
            while line.strip() == '':
                line = sys.stdin.readline()
            A_str, B_str, M_str = line.strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            count = 0
            for peak in peaks:
                if peak < A:
                    continue
                if peak > B:
                    break
                if peak % M == 0:
                    count += 1
            print(f"Case #{case_num}: {count}")

    threading.Thread(target=run).start()

if __name__ == '__main__':
    main()