import sys
import threading

def main():
    import sys
    import bisect

    import sys

    sys.setrecursionlimit(1 << 25)

    T = int(sys.stdin.readline())
    for test_case in range(1, T +1):
        R, C, K = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(R):
            grid.append(list(map(int, sys.stdin.readline().split())))
        # Collect cells per bunny
        from collections import defaultdict
        bunnies = defaultdict(list)
        for i in range(R):
            for j in range(C):
                b = grid[i][j]
                bunnies[b].append( (i, j) )
        # Precompute total_pairs_S for S from0 to max_S
        max_S = max(R, C)
        total_pairs_S = [0] * (max_S +1)
        for S in range(0, max_S +1):
            if S ==0:
                total_pairs_S[S] =0
                continue
            count =0
            for dx in range(-S, S+1):
                dy_min = -S
                dy_max = S
                if abs(dx) > S:
                    continue
                # Only count when max(|dx|, |dy|) == S
                for dy in range(-S, S+1):
                    if max(abs(dx), abs(dy)) != S:
                        continue
                    cnt = (R - abs(dx)) * (C - abs(dy))
                    count += cnt
            total_pairs_S[S] = total_pairs_S[S-1] + count
        # Binary search over S
        left =0
        right = max_S
        answer = max_S
        while left <= right:
            mid = (left + right) //2
            # Compute total_pairs_S
            total_S = total_pairs_S[mid]
            # Compute same_b_pairs_S
            same_S =0
            for b, cells in bunnies.items():
                n = len(cells)
                if n <2:
                    continue
                # Sort cells by row, then column
                cells_sorted = sorted(cells)
                rows = [cell[0] for cell in cells_sorted]
                cols = [cell[1] for cell in cells_sorted]
                # Two pointers over rows
                l =0
                active_cols = []
                total =0
                for r in range(n):
                    while l <= r and rows[r] - rows[l] > mid:
                        l +=1
                    # Now, cells from l to r are within row distance <=mid
                    # Need to count number of cells within column distance <=mid
                    # Extract the relevant columns
                    # Use binary search on the sorted cols[l to r]
                    # Since cols are sorted within cells_sorted
                    # So slice and sort is already sorted
                    # Count number of columns within mid of cols[r]
                    # The window is from cols[r] - mid to cols[r] + mid
                    # Find leftmost index in l to r where col >= cols[r] - mid
                    left_col = bisect.bisect_left(cols, cols[r] - mid, l, r+1)
                    right_col = bisect.bisect_right(cols, cols[r] + mid, l, r+1)
                    count = right_col - left_col
                    # Exclude self
                    count -=1
                    total += count
                same_S += total
            # Compute frequency_S
            frequency_S = total_S - same_S
            if frequency_S >= K:
                answer = mid
                right = mid -1
            else:
                left = mid +1
        print(f"Case #{test_case}: {answer}")

threading.Thread(target=main,).start()