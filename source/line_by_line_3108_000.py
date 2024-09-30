import math
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    for test_case in range(1, T+1):
        N = int(data[index])
        P = int(data[index+1])
        index +=2
        if P ==0:
            print(f"Case #{test_case}: -{P:.15f}")
            continue
        # Compute P' = 100^(1/N) * P^((N-1)/N)
        p_float = float(P)
        one_over_N = 1.0 / N
        exponent_P = (N -1) / N
        try:
            pow_100 = math.pow(100.0, one_over_N)
            pow_P = math.pow(p_float, exponent_P)
            P_prime = pow_100 * pow_P
            diff = P_prime - p_float
            print(f"Case #{test_case}: {diff:.15f}")
        except:
            # Handle cases where P=0 or other edge cases
            print(f"Case #{test_case}: 0.000000000000000")

if __name__ == "__main__":
    main()