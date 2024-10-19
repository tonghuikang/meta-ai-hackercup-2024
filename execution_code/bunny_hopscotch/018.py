import sys
import threading
import bisect

def main():
    import sys

    import sys

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T +1):
        R, C, K = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(R):
            row = list(map(int, sys.stdin.readline().split()))
            grid.append(row)
        n = R * C
        # Group cells by owner
        owner_dict = {}
        for i in range(R):
            for j in range(C):
                owner = grid[i][j]
                if owner not in owner_dict:
                    owner_dict[owner] = []
                owner_dict[owner].append( (i+1, j+1) )
        # Separate owners with multiple cells
        multi_owners = []
        for owner, cells in owner_dict.items():
            if len(cells) >=2:
                # Sort cells by row, then column
                cells_sorted = sorted(cells)
                multi_owners.append(cells_sorted)
        # Binary search over S
        low =0
        high = max(R, C)
        answer = high
        while low <= high:
            mid = (low + high)//2
            # Compute sum_row_counts
            sum_row =0
            for i in range(1, R+1):
                top = max(1, i - mid)
                bottom = min(R, i + mid)
                sum_row += (bottom - top +1)
            # Compute sum_col_counts
            sum_col =0
            for j in range(1, C+1):
                left = max(1, j - mid)
                right = min(C, j + mid)
                sum_col += (right - left +1)
            # f_total(S) = sum_row * sum_col - n
            f_total = sum_row * sum_col - R*C
            # Compute f_same(S)
            f_same =0
            for cells in multi_owners:
                m = len(cells)
                count =0
                active_cols = []
                start =0
                for idx, (r, c) in enumerate(cells):
                    # Remove cells with row < r - S
                    while start < len(cells) and cells[start][0] < r - mid:
                        # Remove cells[start][1] from active_cols
                        pos = bisect.bisect_left(active_cols, cells[start][1])
                        if pos < len(active_cols) and active_cols[pos] == cells[start][1]:
                            active_cols.pop(pos)
                        start +=1
                    # Count number of active_cols within [c - S, c + S]
                    left = c - mid
                    right = c + mid
                    l = bisect.bisect_left(active_cols, left)
                    r_ = bisect.bisect_right(active_cols, right)
                    count += (r_ - l)
                    # Insert current c into active_cols
                    bisect.insort(active_cols, c)
                f_same += 2 * count
            # Compute f_diff(S)
            f_diff = f_total - f_same
            if f_diff >= K:
                answer = mid
                high = mid -1
            else:
                low = mid +1
        print(f"Case #{test_case}: {answer}")

threading.Thread(target=main).start()

