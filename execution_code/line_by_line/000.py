import math
import sys

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        N_str, P_str = line.strip().split()
        N = int(N_str)
        P = int(P_str)
        p = P / 100.0
        exponent = (N - 1) / N
        P_prime = math.pow(p, exponent)
        P_prime_percent = P_prime * 100.0
        difference = P_prime_percent - P
        print(f"Case #{case}: {difference}")

if __name__ == "__main__":
    main()