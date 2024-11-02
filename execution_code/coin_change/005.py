import sys
import math

# Euler-Mascheroni constant for harmonic number approximation
gamma_const = 0.57721566490153286060651209

def expected_bills(N, P):
    if P == 0:
        # Use harmonic number approximation
        H_N = math.log(N) + gamma_const + 1 / (2*N)
        return N * H_N
    elif P >= 100:
        # Optimal strategy after first coin
        return N + (N - 1) * 1  # First coin costs 1, then D=2 bills per new coin
    else:
        P_ratio = P / 100.0
        D_min = int(math.ceil(1 / P_ratio)) + 1
        f_thresh = 1 / D_min
        
        # Integrate over f from f_thresh to 1 for D=1
        integral_D1 = math.log(1 / f_thresh)
        
        # Bills spent when using D_min bills
        bills_Dmin = D_min * f_thresh
        
        total_expected_bills = N * (integral_D1 + bills_Dmin)
        return total_expected_bills

T = int(sys.stdin.readline())
for case_num in range(1, T+1):
    line = sys.stdin.readline()
    if not line.strip():
        # Read until we get a non-empty line
        line = sys.stdin.readline()
    N_str, P_str = line.strip().split()
    N = int(N_str)
    P = int(P_str)
    expected = expected_bills(N, P)
    # Ensure the precision matches the sample output's format
    print(f"Case #{case_num}: {expected}")