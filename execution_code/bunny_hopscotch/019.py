import sys
import threading

def main():
    import sys
    import math
    from collections import defaultdict

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        R, C, K = map(int, sys.stdin.readline().split())
        grid = []
        owner_cells = defaultdict(list)
        for i in range(R):
            row = list(map(int, sys.stdin.readline().split()))
            grid.append(row)
            for j in range(C):
                owner = row[j]
                owner_cells[owner].append((i, j))
        # Precompute total number of unordered pairs
        # Use binary search to find the smallest D where the number of different-owner ordered pairs >= K
        low = 0
        high = max(R, C)
        while low < high:
            mid = (low + high) // 2
            # Compute total unordered pairs with distance <= mid
            total_pairs = 0
            # Sum over dx=0..mid and dy=0..mid of (R - dx) * (C - dy)
            # Then subtract R*C to exclude same cell
            # Formula: total_pairs = ((mid +1)*R - mid*(mid +1)//2) * ((mid +1)*C - mid*(mid +1)//2) - R*C
            # However, this formula is incorrect. Instead, compute directly:
            total_pairs = 0
            for dx in range(0, mid +1):
                row_pairs = R - dx
                for dy in range(0, mid +1):
                    if dx ==0 and dy ==0:
                        continue
                    col_pairs = C - dy
                    total_pairs += row_pairs * col_pairs
            # Now, total_pairs is the number of unordered pairs with distance <= mid
            # Now, compute the number of unordered same-owner pairs with distance <= mid
            same_owner_pairs = 0
            for owner, cells in owner_cells.items():
                n = len(cells)
                if n <=1:
                    continue
                # To count the number of unordered pairs within distance <= mid
                # Implement a grid to mark owner's cells
                # Then use a sliding window approach
                # Alternatively, brute-force if n is small
                if n <= 1000:
                    cnt = 0
                    cells_sorted = sorted(cells)
                    for i1 in range(n):
                        x1, y1 = cells_sorted[i1]
                        for i2 in range(i1 +1, n):
                            x2, y2 = cells_sorted[i2]
                            if max(abs(x2 - x1), abs(y2 - y1)) <= mid:
                                cnt +=1
                    same_owner_pairs += cnt
                else:
                    # For large n, use grid-based counting
                    # Create a grid marking the owner's cells
                    owner_grid = [[0]*C for _ in range(R)]
                    for x, y in cells:
                        owner_grid[x][y] =1
                    # Compute prefix sums
                    prefix = [[0]*(C+1) for _ in range(R+1)]
                    for i in range(R):
                        row_sum =0
                        for j in range(C):
                            row_sum += owner_grid[i][j]
                            prefix[i+1][j+1] = prefix[i][j+1] + row_sum
                    # Now, for each cell, count number of cells in its D square
                    cnt =0
                    for x, y in cells:
                        x1 = max(0, x - mid)
                        y1 = max(0, y - mid)
                        x2 = min(R -1, x + mid)
                        y2 = min(C -1, y + mid)
                        # Number of cells in rectangle [x1, x2] x [y1, y2]
                        total = prefix[x2 +1][y2 +1] - prefix[x1][y2 +1] - prefix[x2 +1][y1] + prefix[x1][y1]
                        cnt += total
                    # Each pair counted twice
                    same_owner_pairs += cnt //2
            different_owner_pairs = total_pairs - same_owner_pairs
            different_owner_ordered = different_owner_pairs *2
            if different_owner_ordered >= K:
                high = mid
            else:
                low = mid +1
        # After binary search, low is the answer
        print(f"Case #{test_case}: {low}")

threading.Thread(target=main,).start()