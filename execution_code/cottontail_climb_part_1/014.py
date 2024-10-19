def main():
    import sys

    # Precompute all possible peaks
    peaks = []
    for k in range(0, 9):  # k from 0 to 8
        for D1 in range(1, 10 - k):
            # Generate first k+1 digits increasing by 1
            increasing = [D1 + i for i in range(0, k + 1)]
            # Generate last k digits decreasing by 1
            decreasing = [D1 + k - i -1 for i in range(0, k)]
            digits = increasing + decreasing
            # Convert digits to integer
            p = int(''.join(str(d) for d in digits))
            peaks.append(p)
    # Sort the peaks
    peaks = sorted(peaks)
    
    # Read input
    input = sys.stdin.read().split()
    T = int(input[0])
    ptr =1
    for test_case in range(1, T +1):
        A = int(input[ptr])
        B = int(input[ptr +1])
        M = int(input[ptr +2])
        ptr +=3
        count =0
        for p in peaks:
            if A <= p <=B:
                if p % M ==0:
                    count +=1
            elif p > B:
                break  # since peaks are sorted, no need to check further
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()