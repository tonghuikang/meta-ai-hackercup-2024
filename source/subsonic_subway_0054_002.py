import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(input[idx]); idx +=1
        s_min_candidate = 0.0
        s_max_candidate = math.inf
        for i in range(1, N+1):
            A_i = float(input[idx]); idx +=1
            B_i = float(input[idx]); idx +=1
            s_i_min = i / B_i
            s_min_candidate = max(s_min_candidate, s_i_min)
            if A_i > 0:
                s_i_max = i / A_i
                if s_i_max < s_max_candidate:
                    s_max_candidate = s_i_max
        if s_min_candidate <= s_max_candidate:
            # To ensure precision, format with enough decimal places
            print(f"Case #{test_case}: {s_min_candidate:.10f}".rstrip('0').rstrip('.'))
        else:
            print(f"Case #{test_case}: -1")

if __name__ == "__main__":
    main()