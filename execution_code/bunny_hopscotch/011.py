import sys
import threading
from collections import defaultdict
import bisect

def main():
    import sys

    import sys

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx +=1
    for test_case in range(1, T+1):
        R = int(data[idx])
        C = int(data[idx+1])
        K = int(data[idx+2])
        idx +=3
        B = []
        for _ in range(R):
            row = list(map(int, data[idx:idx+C]))
            B.append(row)
            idx +=C
        # Build owner to list of cells
        owner_cells = defaultdict(list)
        for i in range(R):
            for j in range(C):
                owner = B[i][j]
                owner_cells[owner].append( (i, j) )
        # Binary search over S
        left = 0
        right = max(R, C)
        answer = right
        while left <= right:
            mid = (left + right) //2
            # Compute total ordered pairs within S=mid
            # sum_row = R + 2*(R*mid - mid*(mid+1)//2)
            if mid >= R:
                sum_row = R + 2*(R*mid - (mid*(mid+1))//2)
            else:
                sum_row = R + 2*(R*mid - (mid*(mid+1))//2)
            if mid >= C:
                sum_col = C + 2*(C*mid - (mid*(mid+1))//2)
            else:
                sum_col = C + 2*(C*mid - (mid*(mid+1))//2)
            # To avoid negative counts when mid > min(R,C)
            sum_row = 0
            for di in range(-mid, mid+1):
                ni = R - abs(di)
                if ni >0:
                    sum_row += ni
            sum_col =0
            for dj in range(-mid, mid+1):
                nj = C - abs(dj)
                if nj >0:
                    sum_col += nj
            total_pairs = sum_row * sum_col
            # Now compute same_owner_pairs
            same_owner_pairs =0
            for owner, cells in owner_cells.items():
                m = len(cells)
                if m <=1:
                    continue
                # Sort cells by row, then by column
                cells_sorted = sorted(cells)
                # Use sliding window on rows
                count =0
                l =0
                cols_window = []
                for r in range(m):
                    while l <=r and cells_sorted[r][0] - cells_sorted[l][0] > mid:
                        l +=1
                    # Now cells_sorted[l..r] have rows within mid of cells_sorted[r]
                    # We need to count number of cells in cells_sorted[l..r] with column within mid of cells_sorted[r][1]
                    # Extract columns in the window
                    # Since cells_sorted is sorted by row, but columns are arbitrary, we need to have sorted columns
                    # To optimize, sort the columns in the window
                    if l >0:
                        # Remove the column of cells_sorted[l-1]
                        pass
                    # Extract columns in window
                    cols = [cells_sorted[k][1] for k in range(l, r+1)]
                    cols_sorted = sorted(cols)
                    # Number of columns within mid of cells_sorted[r][1]
                    j = cells_sorted[r][1]
                    left_j = j - mid
                    right_j = j + mid
                    low = bisect.bisect_left(cols_sorted, left_j)
                    high = bisect.bisect_right(cols_sorted, right_j)
                    cnt = high - low
                    count += cnt
                # Subtract self-pairs
                same_owner_pairs += count
            # Each ordered pair is counted once in same_owner_pairs
            # Now, number of ordered pairs with different owners:
            different_owner_pairs = total_pairs - same_owner_pairs
            if different_owner_pairs >= K:
                answer = mid
                right = mid -1
            else:
                left = mid +1
        print(f"Case #{test_case}: {answer}")

threading.Thread(target=main).start()