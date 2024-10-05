import sys
import math

def main():
    import sys
    import threading

    def run():
        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            N_line = ''
            # Read until a non-empty line
            while N_line.strip() == '':
                N_line = sys.stdin.readline()
            N = int(N_line)
            max_lower = 0.0
            min_upper = float('inf')
            for i in range(1, N+1):
                line = ''
                while line.strip() == '':
                    line = sys.stdin.readline()
                A_i_str, B_i_str = line.strip().split()
                A_i = int(A_i_str)
                B_i = int(B_i_str)
                # Compute i / B_i
                lower = i / B_i
                if lower > max_lower:
                    max_lower = lower
                # Compute i / A_i if A_i >0
                if A_i > 0:
                    upper = i / A_i
                    if upper < min_upper:
                        min_upper = upper
            if max_lower <= min_upper:
                # Output max_lower with sufficient precision
                # To ensure the required precision, format with 10 decimal places
                # and remove trailing zeros
                S = max_lower
                print(f"Case #{test_case}: {S:.10f}".rstrip('0').rstrip('.'))
            else:
                print(f"Case #{test_case}: -1")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()