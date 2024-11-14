import sys

def solve():
    import sys
    import math

    from sys import stdin
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        s_lower_max = 0.0
        s_upper_min = math.inf
        for i in range(1, N+1):
            A_i = float(data[idx]); idx +=1
            B_i = float(data[idx]); idx +=1
            if B_i == 0:
                # According to constraints, A_i < B_i, so B_i >0
                pass
            s_lower_i = i / B_i
            if s_lower_i > s_lower_max:
                s_lower_max = s_lower_i
            if A_i > 0:
                s_upper_i = i / A_i
                if s_upper_i < s_upper_min:
                    s_upper_min = s_upper_i
            else:
                # A_i =0: no upper limit from this station
                pass
        # After all stations
        if s_lower_max <= s_upper_min:
            # Valid speed exists
            # To handle precision up to 1e-6, format accordingly
            answer = s_lower_max
            print(f"Case #{test_case}: {answer:.10f}".rstrip('0').rstrip('.'))
        else:
            print(f"Case #{test_case}: -1")

import sys

def solve():
    import sys
    import math

    from sys import stdin
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        s_lower_max = 0.0
        s_upper_min = math.inf
        for i in range(1, N+1):
            A_i = float(data[idx]); idx +=1
            B_i = float(data[idx]); idx +=1
            if B_i == 0:
                # According to constraints, A_i < B_i, so B_i >0
                pass
            s_lower_i = i / B_i
            if s_lower_i > s_lower_max:
                s_lower_max = s_lower_i
            if A_i > 0:
                s_upper_i = i / A_i
                if s_upper_i < s_upper_min:
                    s_upper_min = s_upper_i
            else:
                # A_i =0: no upper limit from this station
                pass
        # After all stations
        if s_lower_max <= s_upper_min:
            # Valid speed exists
            # To handle precision up to 1e-6, format accordingly
            answer = s_lower_max
            print(f"Case #{test_case}: {answer:.10f}".rstrip('0').rstrip('.'))
        else:
            print(f"Case #{test_case}: -1")