import math
import sys

def main():
    T_and_cases = sys.stdin.read().split()
    T = int(T_and_cases[0])
    index = 1
    for case in range(1, T+1):
        N = int(T_and_cases[index])
        P = int(T_and_cases[index+1])
        index +=2
        if P ==0:
            # If P is 0, even increasing it won't help since 0^x =0, but based on constraints P >=1
            increase = 0.0
        else:
            original_prob = (P / 100.0) ** (N -1)
            # We need new_P such that (new_P /100)^N = original_prob
            # So new_P = 100 * (original_prob)^(1/N)
            new_P = 100.0 * (original_prob) ** (1.0 / N)
            increase = new_P - P
        print(f"Case #{case}: {increase:.15f}")

if __name__ == "__main__":
    main()