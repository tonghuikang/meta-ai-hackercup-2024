import sys

def main():
    import sys
    import math
    import threading

    def run():
        import sys

        input = sys.stdin.read().split()
        idx = 0
        T = int(input[idx])
        idx +=1
        for test_case in range(1, T+1):
            N = int(input[idx])
            idx +=1
            S_min = 0.0
            S_max = float('inf')
            for i in range(1, N+1):
                A_i = int(input[idx])
                B_i = int(input[idx+1])
                idx +=2
                # Calculate S_min
                if B_i ==0:
                    # To reach station i in 0 time, speed needs to be infinity, which is impossible
                    S_min_candidate = float('inf')
                else:
                    S_min_candidate = i / B_i
                S_min = max(S_min, S_min_candidate)
                # Calculate S_max
                if A_i >0:
                    S_max_candidate = i / A_i
                    S_max = min(S_max, S_max_candidate)
                # If A_i ==0, no upper limit from this station
            if S_min <= S_max and S_min != float('inf'):
                # To ensure precision up to 1e-6, format accordingly
                # Remove trailing zeros and unnecessary decimal points
                # Use format with 10 decimal places and strip
                result = "{0:.10f}".format(S_min).rstrip('0').rstrip('.')
                print(f"Case #{test_case}: {result}")
            else:
                print(f"Case #{test_case}: -1")

    threading.Thread(target=run,).start()

if __name__ == "__main__":
    main()