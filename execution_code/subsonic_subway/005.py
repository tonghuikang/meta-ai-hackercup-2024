import sys

import threading

def main():
    import math
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N = int(sys.stdin.readline())
        v_min = 0.0
        v_max = float('inf')
        for i in range(1, N +1):
            A_i_str, B_i_str = sys.stdin.readline().split()
            A_i = int(A_i_str)
            B_i = int(B_i_str)
            v_min_candidate = i / B_i
            v_min = max(v_min, v_min_candidate)
            if A_i > 0:
                v_max_candidate = i / A_i
                v_max = min(v_max, v_max_candidate)
            # No update to v_max when A_i == 0
        if v_min <= v_max + 1e-9:  # Adding a small epsilon to account for floating point errors
            # Ensure output within acceptable precision
            print(f"Case #{case_num}: {v_min:.10f}")
        else:
            print(f"Case #{case_num}: -1")


threading.Thread(target=main).start()