import math
import sys

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        parts = sys.stdin.readline().strip().split()
        if len(parts) <2:
            # In case of extra empty lines
            while len(parts)<2:
                parts += sys.stdin.readline().strip().split()
        N, P = map(int, parts)
        p = P / 100.0
        exponent = (N -1)/N
        p_prime = math.pow(p, exponent)
        P_prime = 100.0 * p_prime
        delta = P_prime - P
        # To ensure enough precision, format with 15 decimal places
        print(f"Case #{case}: {delta:.15f}")

if __name__ == "__main__":
    main()