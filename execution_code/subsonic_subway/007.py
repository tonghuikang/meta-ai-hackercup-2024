import sys

def main():
    import sys
    import math
    from sys import stdin
    import sys

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(input[idx]); idx +=1
        lower = 0.0
        upper = float('inf')
        for i in range(1, N+1):
            A_i = float(input[idx]); idx +=1
            B_i = float(input[idx]); idx +=1
            S_lower = i / B_i
            if A_i > 0:
                S_upper = i / A_i
                if S_upper < upper:
                    upper = S_upper
            # Update the lower bound
            if S_lower > lower:
                lower = S_lower
        # Check feasibility
        if lower <= upper:
            # Format the output with enough precision
            print(f"Case #{test_case}: {lower}")
        else:
            print(f"Case #{test_case}: -1")

if __name__ == "__main__":
    main()