import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for tc in range(1, T+1):
        N = int(input[idx])
        idx +=1
        max_lower = 0.0
        min_upper = math.inf
        for i in range(1, N+1):
            A = int(input[idx])
            B = int(input[idx+1])
            idx +=2
            lower = i / B
            if lower > max_lower:
                max_lower = lower
            if A >0:
                upper = i / A
                if upper < min_upper:
                    min_upper = upper
        if max_lower <= min_upper:
            # Round to 10 decimal places to avoid floating point issues
            s = max_lower
            print(f"Case #{tc}: {s}")
        else:
            print(f"Case #{tc}: -1")

if __name__ == "__main__":
    main()