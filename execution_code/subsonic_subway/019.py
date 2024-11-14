import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for test_case in range(1, T + 1):
        N = int(input[idx])
        idx += 1
        min_speed = 0.0
        max_speed = math.inf
        for i in range(1, N + 1):
            A_i = float(input[idx])
            B_i = float(input[idx + 1])
            idx += 2
            # Calculate speed lower bound: s >= i / B_i
            if B_i == 0:
                # Impossible to reach if B_i is 0
                min_speed = math.inf
            else:
                min_speed = max(min_speed, i / B_i)
            # Calculate speed upper bound: s <= i / A_i, only if A_i > 0
            if A_i > 0:
                max_speed = min(max_speed, i / A_i)
            # If at any point min_speed > max_speed, no solution
        if min_speed - max_speed > 1e-12:
            result = -1
        else:
            # If min_speed <= max_speed, it is achievable
            # If min_speed is infinite, no solution
            if min_speed == math.inf:
                result = -1
            else:
                result = min_speed
        if result == -1:
            print(f"Case #{test_case}: -1")
        else:
            # Print with up to 10 decimal places to ensure precision
            print(f"Case #{test_case}: {result:.10f}".rstrip('0').rstrip('.'))
            
if __name__ == "__main__":
    main()