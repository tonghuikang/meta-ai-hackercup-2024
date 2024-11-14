import sys

def main():
    import math
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        max_s_min = 0.0
        min_s_max = float('inf')
        impossible = False
        for i in range(1, N+1):
            A_i = int(data[idx]); idx +=1
            B_i = int(data[idx]); idx +=1
            if B_i ==0:
                # Need s >= i /0 , impossible unless i==0
                impossible = True
                # Consume remaining input
                for _ in range(i, N+1):
                    A_skip = data[idx]; idx +=1
                    B_skip = data[idx]; idx +=1
                break
            s_min_candidate = i / B_i
            if A_i >0:
                s_max_candidate = i / A_i
                if s_max_candidate < min_s_max:
                    min_s_max = s_max_candidate
            # else s_max_candidate is +inf, do not change min_s_max
            if s_min_candidate > max_s_min:
                max_s_min = s_min_candidate
        if not impossible and max_s_min <= min_s_max:
            # Format to 10 decimal places to ensure precision
            print(f"Case #{test_case}: {max_s_min:.10f}".rstrip('0').rstrip('.'))
        else:
            print(f"Case #{test_case}: -1")
                

if __name__ == "__main__":
    main()