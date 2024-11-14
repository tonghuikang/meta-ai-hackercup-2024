T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    max_L = 0.0
    min_R = float('inf')
    for i in range(1, N + 1):
        A_i_str, B_i_str = input().strip().split()
        A_i, B_i = int(A_i_str), int(B_i_str)
        L_i = i / B_i  # Lower bound for speed at station i
        max_L = max(max_L, L_i)
        if A_i > 0:
            R_i = i / A_i  # Upper bound for speed at station i
            min_R = min(min_R, R_i)
        # If A_i == 0, R_i is infinite (no upper limit)

    if max_L <= min_R:
        print(f"Case #{case_num}: {max_L}")
    else:
        print(f"Case #{case_num}: -1")