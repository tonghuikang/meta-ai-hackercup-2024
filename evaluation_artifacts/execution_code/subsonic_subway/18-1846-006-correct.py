import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    pointer = 0
    T = int(input[pointer]); pointer +=1
    results = []
    for tc in range(1, T+1):
        N = int(input[pointer]); pointer +=1
        max_s_low = 0.0
        min_s_high = float('inf')
        for i in range(1, N+1):
            A_i = int(input[pointer]); pointer +=1
            B_i = int(input[pointer]); pointer +=1
            # Compute s_low = i / B_i
            s_low = i / B_i
            if s_low > max_s_low:
                max_s_low = s_low
            # Compute s_high = i / A_i if A_i >0
            if A_i >0:
                s_high = i / A_i
                if s_high < min_s_high:
                    min_s_high = s_high
        # After all stations
        if max_s_low <= min_s_high:
            # Format the output with up to 10 decimal places to ensure precision
            ans = "{0:.10f}".format(max_s_low).rstrip('0').rstrip('.')
            results.append(f"Case #{tc}: {ans}")
        else:
            results.append(f"Case #{tc}: -1")
    # Print all results
    print('\n'.join(results))

if __name__ == "__main__":
    main()