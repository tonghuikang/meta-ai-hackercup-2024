import math

def solve():
    import sys
    T_and_cases = sys.stdin.read().split()
    T = int(T_and_cases[0])
    idx =1
    for tc in range(1, T+1):
        N = int(T_and_cases[idx])
        P = int(T_and_cases[idx+1])
        idx +=2
        if P ==0:
            # If P is 0, no increase can make it possible
            increase =0.0
        else:
            P_fraction = P /100.0
            exponent = (N-1)/N
            P_new_fraction = math.pow(P_fraction, exponent)
            P_new = P_new_fraction *100.0
            increase = P_new - P
        print(f"Case #{tc}: {increase}")