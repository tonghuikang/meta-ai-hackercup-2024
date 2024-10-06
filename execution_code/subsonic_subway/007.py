import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr]); ptr +=1
    for test_case in range(1, T+1):
        N = int(input[ptr]); ptr +=1
        max_lower = 0.0
        min_upper = float('inf')
        for i in range(1, N+1):
            A = int(input[ptr]); ptr +=1
            B = int(input[ptr]); ptr +=1
            if B ==0:
                # Impossible to deliver
                max_lower = float('inf')
                break
            lower = i / B
            max_lower = max(max_lower, lower)
            if A >0:
                upper = i / A
                min_upper = min(min_upper, upper)
            # If A ==0, no upper bound
        # Continue to read remaining input if broken early
        if max_lower != float('inf'):
            # Check all B_i were read
            pass
        feasible = False
        if max_lower <= min_upper:
            feasible = True
        if feasible:
            # To handle floating point precision as required
            # We'll format with enough decimal places
            print(f"Case #{test_case}: {max_lower:.10f}".rstrip('0').rstrip('.') if '.' in f"{max_lower:.10f}" else f"{max_lower:.10f}")
        else:
            print(f"Case #{test_case}: -1")
        
if __name__ == "__main__":
    main()