import sys

T = int(sys.stdin.readline())

INF = float('inf')

for case_num in range(1, T+1):
    N = int(sys.stdin.readline())

    v_min_overall = 0.0
    v_max_overall = INF

    for i in range(1, N+1):
        A_i_str, B_i_str = sys.stdin.readline().split()
        A_i = int(A_i_str)
        B_i = int(B_i_str)

        v_min_i = i / B_i

        if A_i > 0:
            v_max_i = i / A_i
        else:
            v_max_i = INF

        v_min_overall = max(v_min_overall, v_min_i)
        v_max_overall = min(v_max_overall, v_max_i)

    if v_min_overall <= v_max_overall + 1e-9:
        ans = v_min_overall
        print(f"Case #{case_num}: {ans}")
    else:
        print(f"Case #{case_num}: -1")