import sys
import math

def main():
    import sys

    import sys

    def readints():
        return list(map(int, sys.stdin.read().split()))
    
    data = readints()
    it = iter(data)
    T = next(it)
    for tc in range(1, T+1):
        try:
            N = next(it)
        except StopIteration:
            N = 0
        lower_bound = 0.0
        upper_bound = float('inf')
        for i in range(1, N+1):
            try:
                A_i = next(it)
                B_i = next(it)
            except StopIteration:
                A_i = 0
                B_i = 1
            if B_i ==0:
                # Impossible, since B_i > A_i >=0
                # But according to constraints, B_i > A_i >=0
                # So B_i >=1
                pass
            station_lower = i / B_i
            lower_bound = max(lower_bound, station_lower)
            if A_i >0:
                station_upper = i / A_i
                upper_bound = min(upper_bound, station_upper)
        # Compare lower_bound and upper_bound with allowed precision
        if lower_bound <= upper_bound + 1e-12:
            # Format the lower_bound with up to 10 decimal digits, remove trailing zeros
            s = lower_bound
            s_str = "{0:.10f}".format(s).rstrip('0').rstrip('.')
            print(f"Case #{tc}: {s_str}")
        else:
            print(f"Case #{tc}: -1")

if __name__ == "__main__":
    main()