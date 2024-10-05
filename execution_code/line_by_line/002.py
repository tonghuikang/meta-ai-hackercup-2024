import math
import sys

def calculate_delta_p(N, P):
    # Convert P to decimal
    P_decimal = P / 100.0
    # Calculate P' as (P / 100)^( (N-1)/N ) * 100
    exponent = (N - 1) / N
    P_new = (P_decimal ** exponent) * 100.0
    # Calculate delta P
    delta_P = P_new - P
    return delta_P

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        line = sys.stdin.readline().strip()
        if not line:
            # If the line is empty, read next line
            line = sys.stdin.readline().strip()
        N_P = line.split()
        N = int(N_P[0])
        P = float(N_P[1])
        delta_P = calculate_delta_p(N, P)
        # Ensure the output has enough decimal places
        print(f"Case #{case}: {delta_P}")

if __name__ == "__main__":
    main()