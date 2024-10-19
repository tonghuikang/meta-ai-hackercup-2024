import sys
import threading

def main():
    import sys
    import bisect
    from collections import defaultdict

    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R, C, K = map(int, sys.stdin.readline().split())
        grid = []
        owner_cells = defaultdict(list)
        for i in range(1, R+1):
            row = list(map(int, sys.stdin.readline().split()))
            grid.append(row)
            for j in range(1, C+1):
                owner = row[j-1]
                owner_cells[owner].append( (i, j) )

        # Function to compute total ordered pairs with score <=s
        def total_pairs(s):
            sum_rows = 0
            for i in range(1, R+1):
                top = max(1, i - s)
                bottom = min(R, i + s)
                rows_in_window = bottom - top +1
                sum_rows += rows_in_window

            sum_cols = 0
            for j in range(1, C+1):
                left = max(1, j - s)
                right = min(C, j + s)
                cols_in_window = right - left +1
                sum_cols += cols_in_window

            total = sum_rows * sum_cols - R*C
            return total

        # Function to compute total same-owner ordered pairs with score <=s
        def same_owner_pairs(s):
            total = 0
            for owner, cells in owner_cells.items():
                m = len(cells)
                if m <=1:
                    continue
                # Sort cells by row, then column
                cells_sorted = sorted(cells)
                # For each cell, count number of cells within s distance
                # Using two pointers
                # Since max distance is max row difference and max column difference,
                # use nested loops approach
                # To optimize, we can sort by row and then for each row window, use column window
                # But for simplicity, use brute force for small m
                # Given constraints, m can be up to 640k, but likely much smaller per owner
                # Thus, use grid-based counting
                # Create a grid for this owner's cells
                # and use prefix sums to count within s
                # But R and C up to 800, which is manageable
                grid_owner = [[0]*(C+2) for _ in range(R+2)]
                for (i,j) in cells:
                    grid_owner[i][j] +=1
                # Compute prefix sums
                prefix = [[0]*(C+2) for _ in range(R+2)]
                for i in range(1, R+1):
                    row_sum = 0
                    for j in range(1, C+1):
                        row_sum += grid_owner[i][j]
                        prefix[i][j] = prefix[i-1][j] + row_sum
                # For each cell, count number of cells in (i-s, j-s) to (i+s,j+s)
                for (i,j) in cells:
                    top = max(1, i - s)
                    bottom = min(R, i + s)
                    left = max(1, j - s)
                    right = min(C, j + s)
                    count = prefix[bottom][right] - prefix[top-1][right] - prefix[bottom][left-1] + prefix[top-1][left-1]
                    total += (count -1)  # exclude the cell itself
            return total

        # Binary search over possible scores
        left = 0
        right = max(R, C)
        answer = right
        while left <= right:
            mid = (left + right) //2
            tp = total_pairs(mid)
            sop = same_owner_pairs(mid)
            valid = tp - sop
            if valid >= K:
                answer = mid
                right = mid -1
            else:
                left = mid +1

        print(f"Case #{test_case}: {answer}")

threading.Thread(target=main,).start()