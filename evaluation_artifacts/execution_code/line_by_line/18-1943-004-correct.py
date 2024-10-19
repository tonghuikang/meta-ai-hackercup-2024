import math
import sys

def calculate_increase(N, P):
    if P == 0:
        return 0.0  # If P is 0, no chance of success, but P >=1 per constraints
    # Calculate log((P/100)^(N-1)/N)
    # log(P_new/100) = (N-1)/N * log(P/100)
    log_P_over_100 = math.log(P / 100)
    exponent = (N -1)/N
    log_Pnew_over_100 = exponent * log_P_over_100
    P_new_over_100 = math.exp(log_Pnew_over_100)
    P_new = P_new_over_100 * 100
    increase = P_new - P
    return increase

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        N_str, P_str = line.strip().split()
        N = int(N_str)
        P = float(P_str)
        increase = calculate_increase(N, P)
        # Ensure floating point precision with 15 decimal places
        print(f"Case #{case}: {increase:.15f}")

if __name__ == "__main__":
    main()