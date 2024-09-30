import math
import sys

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        N_str, P_str = line.strip().split()
        N = int(N_str)
        P = float(P_str)

        if P == 0:
            # If P is 0%, no chance of success, increasing P is the only way
            # But as per constraints P >=1
            diff = 0.0
        else:
            p_original = P / 100.0
            exponent = (N - 1) / N
            p_new = 100.0 * math.pow(p_original, exponent)
            diff = p_new - P

        # Ensure the output has enough decimal places
        print(f"Case #{case}: {diff:.15f}")

if __name__ == "__main__":
    main()