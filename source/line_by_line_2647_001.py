import math
import sys

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        line = sys.stdin.readline().strip()
        while line == '':
            line = sys.stdin.readline().strip()
        N, P = map(int, line.split())
        if P == 0:
            delta = -P  # Impossible to improve
        else:
            original_prob_log = math.log(P / 100)
            exponent = (N - 1) / N
            new_prob_log = exponent * original_prob_log
            new_P = 100 * math.exp(new_prob_log)
            delta = new_P - P
        print(f"Case #{case}: {delta}")

if __name__ == "__main__":
    main()