import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr]); ptr +=1
    for test_case in range(1, T+1):
        N = int(input[ptr]); ptr +=1
        lower_bound = 0.0
        upper_bound = float('inf')
        for i in range(1, N+1):
            A_i = int(input[ptr]); ptr +=1
            B_i = int(input[ptr]); ptr +=1
            ratio_lower = i / B_i
            lower_bound = max(lower_bound, ratio_lower)
            if A_i >0:
                ratio_upper = i / A_i
                upper_bound = min(upper_bound, ratio_upper)
        if lower_bound <= upper_bound + 1e-12:
            # To ensure precision, format with 10 decimal places and strip trailing zeros
            answer = "{0:.10f}".format(lower_bound).rstrip('0').rstrip('.')
            print(f"Case #{test_case}: {answer}")
        else:
            print(f"Case #{test_case}: -1")

if __name__ == "__main__":
    main()