import math
import sys

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        parts = sys.stdin.readline().strip().split()
        if len(parts) < 2:
            # In case of empty lines or insufficient parts
            while len(parts) < 2:
                parts += sys.stdin.readline().strip().split()
        N, P = map(int, parts)
        original_prob = P / 100.0
        if original_prob == 0.0:
            # If original P is 0%, any increase is needed to get a positive probability
            # But since P starts from 1%, per constraints, this should not happen
            new_P = 100.0
        else:
            exponent = (N - 1) / N
            new_prob = original_prob ** exponent
            new_P = new_prob * 100.0
        increase = new_P - P
        # Ensure that small negative values due to floating point are treated as zero
        if increase < 0:
            increase = 0.0
        print(f"Case #{case}: {increase}")

if __name__ == "__main__":
    main()