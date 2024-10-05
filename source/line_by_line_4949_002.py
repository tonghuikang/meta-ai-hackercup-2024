import math

def calculate_delta_P(N, P):
    if P == 0:
        return 100.0  # If P is 0%, you need to increase it to 100%
    P_frac = P / 100.0
    exponent = (N - 1) / N
    P_new_frac = math.pow(P_frac, exponent)
    P_new = P_new_frac * 100.0
    delta_P = P_new - P
    return delta_P

def main():
    import sys
    T_and_cases = sys.stdin.read().strip().split()
    T = int(T_and_cases[0])
    idx = 1
    for test_case in range(1, T +1):
        N = int(T_and_cases[idx])
        P = int(T_and_cases[idx +1])
        idx +=2
        delta_P = calculate_delta_P(N, P)
        # Ensure enough decimal places
        print(f"Case #{test_case}: {delta_P}")
        
if __name__ == "__main__":
    main()