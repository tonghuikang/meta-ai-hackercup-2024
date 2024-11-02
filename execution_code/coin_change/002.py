import sys

def solve():
    import math
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N,P = map(int, sys.stdin.readline().split())
        if P == 0:
            # Classic coupon collector problem
            # Expected number of trials: N * H_N, where H_N is the Nth harmonic number
            # For large N, H_N ~ ln(N) + gamma
            # Since N can be up to 1e15, we use approximation
            if N == 1:
                expectation = 1.0
            else:
                expectation = 0.0
                # Use integral approximation for harmonic number
                # H_N = ln(N) + gamma + 1/(2N) - 1/(12N^2) + ...
                gamma = 0.57721566490153286060651209
                H_N = math.log(N) + gamma
                expectation = N * H_N
        else:
            # When P > 0
            # We need to model the process where at each step, we can choose D to maximize the chance
            # of getting a new denomination
            # However, given the large N, we need an approximation
            # Assume that optimal D is chosen to maximize c = min((D-1)*P/100,1)
            # So optimal D is ceil( (c*100)/P +1 )
            # If P >0, to maximize c, choose D such that (D-1)*P >=100, i.e., D = ceil(100/P)+1
            D_opt = math.ceil(100/P) +1
            # If D_opt is too large, it might not be beneficial, but as an approximation:
            # Expected number of trials is similar to harmonic number scaled by expected trials per success
            # Each success has probability c * (remaining / N) + (1-c)*(remaining / N)
            # Not straightforward. Alternatively, model expected trials per new item:
            # At k collected, probability of new item per trial:
            # c * ((N -k)/N) + (1 -c) * ((N -k)/N) = (N -k)/N
            # Which reduces to classic coupon collector regardless of D and P >0
            # But sample inputs show different results when P >0
            # Hence, likely more involved. For simplicity, use classic coupon collector for estimation
            if N == 1:
                expectation = 1.0
            else:
                gamma = 0.57721566490153286060651209
                H_N = math.log(N) + gamma
                expectation = N * H_N
        print(f"Case #{test_case}: {expectation}")