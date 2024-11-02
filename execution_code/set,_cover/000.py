import sys
import threading

def main():
    import sys

    import sys

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N, K = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(N):
            row = sys.stdin.readline().strip()
            grid.append(row)
        
        # Find initial bounds
        R_min, R_max = N, -1
        C_min, C_max = N, -1
        question_rows = [[] for _ in range(N)]
        question_cols = [[] for _ in range(N)]
        all_questions = []
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '1':
                    if i < R_min:
                        R_min = i
                    if i > R_max:
                        R_max = i
                    if j < C_min:
                        C_min = j
                    if j > C_max:
                        C_max = j
                elif grid[i][j] == '?':
                    question_rows[i].append(j)
                    question_cols[j].append(i)
                    all_questions.append((i,j))
        # If there are no initial '1's, any placement of K '1's needs to have at least one '1'
        if R_max == -1:
            # No initial '1's, need to set K '1's
            # To maximize cover, place '1's as far apart as possible
            # If K >=2, place one '1' at (0,0) and one at (N-1,N-1)
            # If K ==1, area is 1
            if K ==0:
                # Not possible as per constraints
                area = 0
            elif K ==1:
                area =1
            else:
                area = (N) * (N)
        else:
            # Collect possible extensions
            up_candidates = []
            for r in range(R_min-1, -1, -1):
                if question_rows[r]:
                    up_candidates.append(r)
            down_candidates = []
            for r in range(R_max+1, N):
                if question_rows[r]:
                    down_candidates.append(r)
            left_candidates = []
            for c in range(C_min-1, -1, -1):
                if question_cols[c]:
                    left_candidates.append(c)
            right_candidates = []
            for c in range(C_max+1, N):
                if question_cols[c]:
                    right_candidates.append(c)
            # Precompute prefix sums for extensions
            up_pre = []
            for r in up_candidates:
                up_pre.append(r)
            down_pre = []
            for r in down_candidates:
                down_pre.append(r)
            left_pre = []
            for c in left_candidates:
                left_pre.append(c)
            right_pre = []
            for c in right_candidates:
                right_pre.append(c)
            # Now, try all possible combinations of extensions
            # To optimize, iterate possible number of up, down, left, right extensions
            max_area = (R_max - R_min +1) * (C_max - C_min +1)
            # To make it faster, iterate over possible number of directions
            # Use four nested loops but limit their ranges
            # Given K up to N^2, but in practice, max extensions per direction is len(up_candidates), etc.
            up_len = len(up_pre)
            down_len = len(down_pre)
            left_len = len(left_pre)
            right_len = len(right_pre)
            # To iterate efficiently, precompute the costs for up, down, left, right
            # Each extension in a direction costs 1 (set at least one '?')
            # So it's similar to assigning how many to extend each direction with total <= K
            # Iterate over possible up extensions
            for u in range(0, min(up_len, K) +1):
                remaining_after_u = K - u
                for d in range(0, min(down_len, remaining_after_u)+1):
                    remaining_after_ud = remaining_after_u - d
                    for l in range(0, min(left_len, remaining_after_ud)+1):
                        r_lim = min(right_len, remaining_after_ud - l)
                        for r_ext in range(0, r_lim +1):
                            total = u + d + l + r_ext
                            if total > K:
                                continue
                            # Compute new bounds
                            new_R_min = R_min
                            if u >0:
                                new_R_min = up_pre[u-1]
                            new_R_max = R_max
                            if d >0:
                                new_R_max = down_pre[d-1]
                            new_C_min = C_min
                            if l >0:
                                new_C_min = left_pre[l-1]
                            new_C_max = C_max
                            if r_ext >0:
                                new_C_max = right_pre[r_ext-1]
                            area = (new_R_max - new_R_min +1) * (new_C_max - new_C_min +1)
                            if area > max_area:
                                max_area = area
            # Also consider the case where all extensions are to one or two directions only
            # The above loop already considers all combinations
        print(f"Case #{test_case}: {max_area}")

threading.Thread(target=main,).start()