def main():
    import sys

    # Precompute all possible peaks
    peaks = []
    for k in range(0, 9):  # since 2k+1 <=17 when k=8
        num_digits = 2 * k + 1
        if num_digits > 18:
            continue
        for D1 in range(1, 10 - k):
            # Build increasing part
            increasing = [D1 + i for i in range(k + 1)]
            # Build decreasing part
            decreasing = [increasing[-2 - i] for i in range(k)]
            # Combine
            digits = increasing + decreasing
            # Convert to integer
            number = int(''.join(map(str, digits)))
            peaks.append(number)
    peaks.sort()

    # Read input
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for test_case in range(1, T + 1):
        A = int(input[idx])
        B = int(input[idx + 1])
        M = int(input[idx + 2])
        idx += 3
        count = 0
        for peak in peaks:
            if A <= peak <= B:
                if peak % M == 0:
                    count += 1
            elif peak > B:
                break  # since peaks are sorted
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()