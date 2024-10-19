import sys

def solve():
    import sys
    import math
    from sys import stdin
    def input():
        return sys.stdin.read()
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for tc in range(1, T+1):
        N = int(data[idx]); idx +=1
        v_min = 0.0
        v_max = float('inf')
        impossible = False
        for i in range(1, N+1):
            A_i = int(data[idx]); idx +=1
            B_i = int(data[idx]); idx +=1
            if B_i ==0:
                # Cannot reach in zero time unless i==0, which isn't possible
                impossible = True
                # Skip remaining inputs
                idx += 2*(N -i)
                break
            v_min_candidate = i / B_i
            if v_min < v_min_candidate:
                v_min = v_min_candidate
            if A_i >0:
                v_max_candidate = i / A_i
                if v_max > v_max_candidate:
                    v_max = v_max_candidate
            # If A_i ==0, no upper bound imposed
        if not impossible and v_min <= v_max + 1e-12:
            # Adding a small epsilon to handle floating point precision
            # Format to at least 6 decimal places
            print(f"Case #{tc}: {v_min:.10f}".rstrip('0').rstrip('.'))
        else:
            print(f"Case #{tc}: -1")