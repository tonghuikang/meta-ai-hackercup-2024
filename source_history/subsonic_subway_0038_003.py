import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    import sys
    import math
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        s_min = 0.0
        s_max = math.inf
        has_A_positive = False
        for i in range(1, N+1):
            A_i = int(data[idx]); idx +=1
            B_i = int(data[idx]); idx +=1
            s_candidate_min = i / B_i
            if s_candidate_min > s_min:
                s_min = s_candidate_min
            if A_i > 0:
                s_candidate_max = i / A_i
                if s_candidate_max < s_max:
                    s_max = s_candidate_max
                has_A_positive = True
        possible = True
        if has_A_positive:
            if s_min > s_max + 1e-12:
                possible = False
        # If no A_i >0, then no upper limit
        if possible:
            # To handle precision, format with enough decimal places
            print(f"Case #{test_case}: {s_min if has_A_positive else s_min}")
        else:
            print(f"Case #{test_case}: -1")
            
if __name__ == "__main__":
    main()