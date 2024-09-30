import math
import sys

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        line = sys.stdin.readline()
        while line.strip() == '':
            line = sys.stdin.readline()
        N,P = map(float, line.strip().split())
        if P == 0:
            # If P is 0, no increase can make it possible
            answer = float('inf')
        else:
            # Compute P' = (P^(N-1) * 100)^(1/N)
            base = (P**(N-1)) * 100
            P_prime = base ** (1.0 / N)
            answer = P_prime - P
        print(f"Case #{tc}: {answer}")

if __name__ == "__main__":
    main()