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
        max_S = 0.0
        min_S = float('inf')
        has_A_positive = False
        for i in range(1, N+1):
            A_i = int(input[idx])
            B_i = int(input[idx+1])
            idx +=2
            # Compute i / B_i
            current_max_S = i / B_i
            if current_max_S > max_S:
                max_S = current_max_S
            # If A_i >0, compute i / A_i
            if A_i >0:
                has_A_positive = True
                current_min_S = i / A_i
                if current_min_S < min_S:
                    min_S = current_min_S
        # After all stations
        if has_A_positive:
            if min_S >= max_S - 1e-12:  # Allow a tiny epsilon for floating point
                answer = max_S
            else:
                answer = -1
        else:
            answer = max_S
        if answer <0:
            print(f"Case #{tc}: -1")
        else:
            # To fix floating point representation issues, format with enough decimal places
            print(f"Case #{tc}: {answer:.10f}".rstrip('0').rstrip('.') if '.' in f"{answer:.10f}" else f"{answer:.10f}")
            

if __name__ == "__main__":
    main()