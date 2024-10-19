import math
import sys

def main():
    import sys

    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        line = sys.stdin.readline()
        while line.strip() == '':
            line = sys.stdin.readline()
        N_str, P_str = line.strip().split()
        N = int(N_str)
        P = float(P_str)

        if P == 0:
            # If P is 0, no increase can help
            delta = 0.0
        else:
            # Calculate Q
            # Q = (P / 100) ** ((N-1)/N) * 100
            # To prevent math domain error when P=0, already handled
            Q = (P / 100) ** ((N - 1) / N) * 100
            delta = Q - P

        print(f"Case #{case}: {delta}")

if __name__ == "__main__":
    main()