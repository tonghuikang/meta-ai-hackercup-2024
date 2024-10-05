import math
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    for test_case in range(1, T+1):
        N = int(data[index])
        P = int(data[index+1])
        index +=2
        if P == 0:
            # If P is 0, it's impossible to type correctly, so any increase doesn't help
            difference = 0.0
        else:
            probability = P / 100.0
            exponent = (N - 1) / N
            P_prime = 100.0 * math.pow(probability, exponent)
            difference = P_prime - P
        # To ensure enough precision, format with 15 decimal places
        print(f"Case #{test_case}: {difference:.15f}")

if __name__ == "__main__":
    main()