import sys
import math

def compute_expected_bills(N, P):
    if P == 0:
        # Expected bills when always using D=1
        gamma = 0.5772156649015328606  # Euler-Mascheroni constant
        return N * (math.log(N) + gamma)
    elif P == 100:
        # Optimal to use D=2 after the first coin
        if N == 1:
            return 1.0
        else:
            # Expected bills for the first coin
            E_first = 1.0
            # Expected bills to get second coin (with D=1)
            E_second = N / (N - 1)
            # Expected bills for remaining coins
            E_remaining = (N - 2) * 2
            return E_first + E_second + E_remaining
    else:
        s_crossover = P / (100.0 + P)
        k_crossover = N * (1 - s_crossover)
        D_star = math.ceil(100.0 / P + 1)
        # Expected bills in phase 1
        if s_crossover <= 0:
            E_phase1 = 0.0
        else:
            E_phase1 = -math.log(P / (100.0 + P))
        # Expected bills in phase 2
        E_phase2 = N * s_crossover * D_star
        E_total = E_phase1 + E_phase2
        return E_total

def main():
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N_str, P_str = sys.stdin.readline().split()
        N = int(N_str)
        P = int(P_str)
        expected_bills = compute_expected_bills(N, P)
        print(f"Case #{case_num}: {expected_bills}")

if __name__ == "__main__":
    main()