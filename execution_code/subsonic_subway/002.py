import sys

def main():
    import sys
    import math

    import sys

    import sys

    def input():
        return sys.stdin.read()

    data = input().split()
    idx = 0
    T = int(data[idx])
    idx +=1
    for case in range(1, T+1):
        N = int(data[idx])
        idx +=1
        max_lower = 0.0
        min_upper = float('inf')
        for i in range(1, N+1):
            A_i = int(data[idx])
            B_i = int(data[idx+1])
            idx +=2
            # Compute lower bound
            lower = i / B_i
            if lower > max_lower:
                max_lower = lower
            # Compute upper bound if A_i >0
            if A_i >0:
                upper = i / A_i
                if upper < min_upper:
                    min_upper = upper
        # After all stations
        if min_upper < float('inf'):
            if max_lower <= min_upper +1e-12:
                result = max_lower
            else:
                result = -1
        else:
            result = max_lower
        if result < -0.5:
            print(f"Case #{case}: -1")
        else:
            print(f"Case #{case}: {result:.10f}".rstrip('0').rstrip('.') if '.' in f"{result:.10f}" else f"{result:.10f}")

if __name__ == "__main__":
    main()