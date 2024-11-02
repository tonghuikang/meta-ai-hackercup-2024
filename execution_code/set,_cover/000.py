import sys
import threading

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N_K = sys.stdin.readline()
        while N_K.strip() == '':
            N_K = sys.stdin.readline()
        N, K = map(int, N_K.strip().split())
        grid = []
        for _ in range(N):
            row = sys.stdin.readline().strip()
            while len(row) < N:
                row += sys.stdin.readline().strip()
            grid.append(row)
        # Find existing 1s
        existing_ones = []
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '1':
                    existing_ones.append((i, j))
        if existing_ones:
            min_row = min(x for x, y in existing_ones)
            max_row = max(x for x, y in existing_ones)
            min_col = min(y for x, y in existing_ones)
            max_col = max(y for x, y in existing_ones)
        else:
            min_row = max_row = min_col = max_col = None

        # Precompute for each direction the possible expansion steps
        # Rows are 0-indexed
        rows_with_question = [False] * N
        cols_with_question = [False] * N
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '?':
                    rows_with_question[i] = True
                    cols_with_question[j] = True
        # If there are existing 1s
        if existing_ones:
            # Compute up_steps_max
            up_steps_max = 0
            for d in range(1, min_row + 1):
                if rows_with_question[min_row - d]:
                    up_steps_max += 1
                else:
                    break
            # Compute down_steps_max
            down_steps_max = 0
            for d in range(1, N - max_row):
                if rows_with_question[max_row + d]:
                    down_steps_max += 1
                else:
                    break
            # Compute left_steps_max
            left_steps_max = 0
            for d in range(1, min_col + 1):
                if cols_with_question[min_col - d]:
                    left_steps_max += 1
                else:
                    break
            # Compute right_steps_max
            right_steps_max = 0
            for d in range(1, N - max_col):
                if cols_with_question[max_col + d]:
                    right_steps_max += 1
                else:
                    break
            max_area = (max_row - min_row + 1) * (max_col - min_col + 1)
            # Iterate over possible expansions
            for up in range(0, up_steps_max +1):
                new_min_row = min_row - up
                if new_min_row <0:
                    continue
                cost_up = up
                for down in range(0, down_steps_max + 1):
                    new_max_row = max_row + down
                    if new_max_row >= N:
                        continue
                    cost_down = down
                    remaining_K = K - cost_up - cost_down
                    if remaining_K <0:
                        continue
                    # Now handle horizontal expansions
                    # We need to set left and/or right steps such that left + right <= remaining_K
                    # and each step has at least one ? in the corresponding column
                    # We can precompute the possible left_steps and right_steps
                    # For this, find the maximum left_steps we can take with remaining_K
                    max_left_possible = min(left_steps_max, remaining_K)
                    for left in range(0, max_left_possible +1):
                        new_min_col = min_col - left
                        if new_min_col <0:
                            continue
                        cost_left = left
                        rem_K = remaining_K - cost_left
                        max_right_possible = min(right_steps_max, rem_K)
                        for right in range(0, max_right_possible +1):
                            new_max_col = max_col + right
                            if new_max_col >= N:
                                continue
                            cost_right = right
                            total_cost = up + down + left + right
                            if total_cost > K:
                                continue
                            area = (new_max_row - new_min_row +1) * (new_max_col - new_min_col +1)
                            if area > max_area:
                                max_area = area
            # Additionally, consider not expanding vertically or horizontally
            # (Already considered in the above loop with up=0, down=0, left=0, right=0)
        else:
            # No existing 1s, need to place exactly K 1s
            # To maximize the area, place K 1s as far apart as possible
            # Potentially, place them at four corners
            # Since K can be up to N*N, the maximum area is N*N
            # But need to place K points such that the bounding rectangle is as large as possible
            # The maximum area would be min(N*N, N*N) = N*N
            # However, with K=1, area=1
            # With K>=2, place two 1s as far apart as possible
            # So, area = (|x1 - x2| +1) * (|y1 - y2| +1)
            # Similarly for K>2, but it's complex
            # A heuristic is to place 1s on the perimeter to maximize the rectangle
            # The optimal is to set the top-left and bottom-right K points on the grid
            # which would cover the maximum area
            # So, the maximum area is at least:

            # If K >=2, place one at (0,0) and another at (N-1, N-1)
            # Area = N * N
            # If K <2, area =1
            # For K >=2, it's always N*N
            if K ==0:
                # No 1s to set, but the constraints say K + existing 1s >0
                # So this case shouldn't occur
                max_area = 0
            elif K ==1:
                max_area =1
            else:
                max_area = N * N
        print(f"Case #{test_case}: {max_area}")

threading.Thread(target=main,).start()