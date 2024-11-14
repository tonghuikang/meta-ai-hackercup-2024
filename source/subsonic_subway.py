import sys
import math

def main():
    import sys
    import threading

    def solve():
        import sys

        T = int(sys.stdin.readline())
        for case in range(1, T +1):
            N_line = ''
            while N_line.strip() == '':
                N_line = sys.stdin.readline()
            N = int(N_line)
            max_lower = 0.0
            min_upper = math.inf
            for i in range(1, N+1):
                line = ''
                while line.strip() == '':
                    line = sys.stdin.readline()
                A_i_str, B_i_str = line.strip().split()
                A_i = float(A_i_str)
                B_i = float(B_i_str)
                lower = i / B_i
                if lower > max_lower:
                    max_lower = lower
                if A_i > 0:
                    upper = i / A_i
                    if upper < min_upper:
                        min_upper = upper
            # If there are no A_i >0, min_upper remains inf
            # To handle this, min_upper should be inf, so check max_lower <= inf is always true
            # So S = max_lower
            if max_lower <= min_upper:
                # For output, need to handle precision up to 1e-6
                # But the problem allows any precision as long as within 1e-6
                print(f"Case #{case}: {max_lower}")
            else:
                print(f"Case #{case}: -1")
    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()