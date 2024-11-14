import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx +=1
    for tc in range(1, T+1):
        N = int(input[idx]); idx +=1
        max_s_lower = 0.0
        min_s_upper = math.inf
        for i in range(1, N+1):
            A = int(input[idx]); idx +=1
            B = int(input[idx]); idx +=1
            s_lower = i / B
            if s_lower > max_s_lower:
                max_s_lower = s_lower
            if A > 0:
                s_upper = i / A
                if s_upper < min_s_upper:
                    min_s_upper = s_upper
        if max_s_lower <= min_s_upper:
            # To avoid floating point issues, format with sufficient decimals
            # Remove trailing zeros
            s = max_s_lower
            s_str = "{0:.10f}".format(s).rstrip('0').rstrip('.')
            print(f"Case #{tc}: {s_str}")
        else:
            print(f"Case #{tc}: -1")

if __name__ == "__main__":
    main()