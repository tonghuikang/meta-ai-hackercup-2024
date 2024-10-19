import sys

def solve():
    import sys
    import math

    import sys

    def readints():
        import sys
        return list(map(int, sys.stdin.read().split()))

    data = readints()
    idx = 0
    T = data[idx]
    idx +=1
    for test_case in range(1, T+1):
        N = data[idx]
        idx +=1
        max_lower = 0.0
        min_upper = float('inf')
        for i in range(1, N+1):
            A_i = data[idx]
            B_i = data[idx+1]
            idx +=2
            # Compute i / B_i
            if B_i ==0:
                # If B_i is 0, Sonic must reach exactly at t=0, which is impossible unless i=0
                # But i >=1, so no solution
                max_lower = float('inf')
                # No need to proceed further
                break
            t_lower = i / B_i
            max_lower = max(max_lower, t_lower)
            if A_i >0:
                t_upper = i / A_i
                min_upper = min(min_upper, t_upper)
            # If A_i ==0, no upper bound from this station
        # After all stations
        if max_lower <= min_upper:
            if math.isinf(max_lower):
                # No solution
                result = -1
            else:
                # Output max_lower with up to 7 decimal places to ensure required precision
                result = max_lower
        else:
            result = -1
        if result == -1:
            print(f"Case #{test_case}: -1")
        else:
            # To ensure floating point precision up to 1e-6, format with 10 decimal places
            print(f"Case #{test_case}: {result:.10f}".rstrip('0').rstrip('.'))