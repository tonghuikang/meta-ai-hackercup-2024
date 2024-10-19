def generate_peaks():
    peaks = []
    # k from 0 to 9 (since 2*9+1=19 digits, which is the max for 10^18)
    for k in range(0, 10):
        # Starting digit D1 from 1 to 9 - k
        for D1 in range(1, 10 - k):
            # Build the increasing part
            increasing = [D1 + i for i in range(k +1)]
            # Build the decreasing part
            decreasing = [D1 + k - i for i in range(1, k +1)]
            # Combine to form the peak digits
            peak_digits = increasing + decreasing
            # Convert digits to integer
            peak = int(''.join(map(str, peak_digits)))
            peaks.append(peak)
    return sorted(peaks)

def count_peaks_in_range(peaks, A, B, M):
    count = 0
    for p in peaks:
        if A <= p <= B:
            if p % M == 0:
                count +=1
    return count

def main():
    import sys
    import sys
    peaks = generate_peaks()
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        line = sys.stdin.readline()
        if not line.strip():
            # skip empty lines
            line = sys.stdin.readline()
        A, B, M = map(int, line.strip().split())
        # Handle A=0: since peaks have no zeros, minimum peak is 1
        A = max(A,1)
        result = count_peaks_in_range(peaks, A, B, M)
        print(f"Case #{case}: {result}")

if __name__ == "__main__":
    main()