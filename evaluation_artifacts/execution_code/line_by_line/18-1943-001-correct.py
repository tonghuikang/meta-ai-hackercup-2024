import sys
import math

T = int(sys.stdin.readline())
for case_num in range(1, T + 1):
    N_and_P = sys.stdin.readline().split()
    while len(N_and_P) < 2:
        N_and_P += sys.stdin.readline().split()
    N, P = map(int, N_and_P)
    N = int(N)
    P = float(P)
    ln_P = math.log(P / 100.0)
    exponent = (N - 1) / N
    ln_P_new = exponent * ln_P
    P_new_fraction = math.exp(ln_P_new)
    P_new = P_new_fraction * 100.0
    Increase = P_new - P
    print(f"Case #{case_num}: {Increase}")