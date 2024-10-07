import sys

def solve():
    import sys
    import math

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx +=1
    for tc in range(1, T+1):
        N = int(input[idx]); idx +=1
        max_lower = 0.0
        min_upper = float('inf')
        for i in range(1, N+1):
            A_i = int(input[idx]); idx +=1
            B_i = int(input[idx]); idx +=1
            lower = i / B_i
            max_lower = max(max_lower, lower)
            if A_i ==0:
                upper = float('inf')
            else:
                upper = i / A_i
            min_upper = min(min_upper, upper)
        if max_lower <= min_upper + 1e-12:
            # To handle floating point precision, add a small epsilon
            result = max_lower
            # Clamp to min_upper in case floating points slightly exceed
            if result > min_upper:
                result = min_upper
            print(f"Case #{tc}: {result}")
        else:
            print(f"Case #{tc}: -1")

if __name__ == "__main__":
    solve()