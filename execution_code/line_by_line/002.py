import math
import sys

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for tc in range(1, T + 1):
        N = int(input[idx])
        P = int(input[idx + 1])
        idx += 2
        
        # Convert P to probability
        S1 = P / 100.0
        
        # Calculate the new probability
        exponent = (N - 1) / N
        P_new = 100.0 * (S1 ** exponent)
        
        # Calculate the required increase
        increase = P_new - P
        
        # Print the result with full precision
        print(f"Case #{tc}: {increase}")

if __name__ == "__main__":
    main()