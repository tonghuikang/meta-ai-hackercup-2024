import math

def main():
    import sys
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        line = sys.stdin.readline().strip()
        if not line:
            # In case of blank lines
            line = sys.stdin.readline().strip()
        N_str, P_str = line.split()
        N = int(N_str)
        P = int(P_str)
        
        P_decimal = P / 100.0
        exponent = (N - 1) / N
        P_new_decimal = math.pow(P_decimal, exponent)
        P_new = P_new_decimal * 100.0
        increase = P_new - P
        # To handle very small negative values due to floating point inaccuracies, ensure non-negative
        if increase < 0 and abs(increase) < 1e-12:
            increase = 0.0
        print(f"Case #{case}: {increase}")

if __name__ == "__main__":
    main()