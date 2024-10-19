import sys
import threading
import numpy as np

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        R, C, K = map(int, sys.stdin.readline().split())
        owners = []
        for _ in range(R):
            owners.append(list(map(int, sys.stdin.readline().split())))
        G_owner = np.array(owners, dtype=np.int32)
        N_rows, N_cols = G_owner.shape

        max_distance = max(N_rows, N_cols) - 1

        N_diff_owner = np.zeros(max_distance + 1, dtype=np.int64)
        N_same_owner = np.zeros(max_distance + 1, dtype=np.int64)

        # Precompute shifts for each D
        shifts_by_D = [[] for _ in range(max_distance + 1)]
        for dx in range(-max_distance, max_distance + 1):
            for dy in range(-max_distance, max_distance + 1):
                D = max(abs(dx), abs(dy))
                if D >= 1 and D <= max_distance:
                    shifts_by_D[D].append((dx, dy))

        for D in range(1, max_distance + 1):
            shifts = shifts_by_D[D]
            total_diff = 0
            total_same = 0
            for dx, dy in shifts:
                # Determine slices
                if dx >= 0:
                    base_x_start = 0
                    base_x_end = N_rows - dx
                    shift_x_start = dx
                    shift_x_end = N_rows
                else:
                    base_x_start = -dx
                    base_x_end = N_rows
                    shift_x_start = 0
                    shift_x_end = N_rows + dx

                if dy >= 0:
                    base_y_start = 0
                    base_y_end = N_cols - dy
                    shift_y_start = dy
                    shift_y_end = N_cols
                else:
                    base_y_start = -dy
                    base_y_end = N_cols
                    shift_y_start = 0
                    shift_y_end = N_cols + dy

                base_grid = G_owner[base_x_start:base_x_end, base_y_start:base_y_end]
                shifted_grid = G_owner[shift_x_start:shift_x_end, shift_y_start:shift_y_end]

                # Compare owners
                same_owner = (base_grid == shifted_grid)
                diff_owner = (base_grid != shifted_grid)

                total_same += np.sum(same_owner)
                total_diff += np.sum(diff_owner)

            N_same_owner[D] = total_same
            N_diff_owner[D] = total_diff

        # Compute cumulative counts
        cum_N_diff_owner = np.cumsum(N_diff_owner[1:])
        # cum_N_diff_owner is of length max_distance
        # Find minimal D where cum_N_diff_owner >= K
        answer_D = -1
        for idx, cumulative_count in enumerate(cum_N_diff_owner):
            if cumulative_count >= K:
                answer_D = idx + 1  # idx starts from 0, distances start from 1
                break
        if answer_D == -1:
            answer_D = max_distance  # Should not happen per problem statement

        print(f"Case #{case_num}: {answer_D}")

threading.Thread(target=main).start()