import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    for tc in range(1, T+1):
        N = int(input[ptr])
        ptr +=1
        max_lower_v = 0.0
        min_upper_v = math.inf
        for i in range(1, N+1):
            A_i = int(input[ptr])
            B_i = int(input[ptr+1])
            ptr +=2
            lower_v_i = i / B_i
            if lower_v_i > max_lower_v:
                max_lower_v = lower_v_i
            if A_i >0:
                upper_v_i = i / A_i
                if upper_v_i < min_upper_v:
                    min_upper_v = upper_v_i
        if max_lower_v <= min_upper_v:
            # To ensure enough precision, format with 10 decimal places
            print(f"Case #{tc}: {max_lower_v:.10f}".rstrip('0').rstrip('.') if '.' in f"{max_lower_v:.10f}" else f"{max_lower_v:.10f}")
        else:
            print(f"Case #{tc}: -1")

if __name__ == "__main__":
    main()