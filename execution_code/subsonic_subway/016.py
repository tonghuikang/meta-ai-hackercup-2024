import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    for test_case in range(1, T+1):
        N = int(input[ptr])
        ptr +=1
        lower_bound = 0.0
        upper_bound = float('inf')
        for i in range(1, N+1):
            Ai = int(input[ptr])
            Bi = int(input[ptr+1])
            ptr +=2
            s_lb_i = i / Bi
            lower_bound = max(lower_bound, s_lb_i)
            if Ai >0:
                s_ub_i = i / Ai
                upper_bound = min(upper_bound, s_ub_i)
        if lower_bound <= upper_bound:
            # To handle floating precision, format with enough decimals
            # Remove trailing zeros and possible decimal point
            s = lower_bound
            # To ensure minimal representation but enough precision
            s_str = "{0:.10f}".format(s).rstrip('0').rstrip('.')
            print(f"Case #{test_case}: {s_str}")
        else:
            print(f"Case #{test_case}: -1")

if __name__ == "__main__":
    main()