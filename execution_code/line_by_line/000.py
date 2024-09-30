import math

def main():
    T = int(input())
    for case in range(1, T+1):
        N, P = map(int, input().split())
        if P == 100:
            delta = 0.0
        else:
            exponent = (N - 1) / N
            p_fraction = P / 100.0
            new_p = 100.0 * math.pow(p_fraction, exponent)
            delta = new_p - P
        print(f"Case #{case}: {delta:.15f}")

if __name__ == "__main__":
    main()