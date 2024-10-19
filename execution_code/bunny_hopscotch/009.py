import sys
import threading
from bisect import bisect_left, bisect_right
from collections import defaultdict

def main():
    import sys

    import sys

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        R, C, K = map(int, sys.stdin.readline().split())
        N = R * C
        grid = []
        owner_cells = defaultdict(list)
        for i in range(1, R + 1):
            row = list(map(int, sys.stdin.readline().split()))
            for j in range(1, C + 1):
                b = row[j -1]
                owner_cells[b].append( (i,j) )
        # Number of cells
        total_cells = R * C
        # Binary search over S
        low = 0
        high = max(R, C)
        # Precompute owner info: for owners with Nb >=2, sort their rows and columns
        owner_sorted = {}
        for b, cells in owner_cells.items():
            if len(cells) >=2:
                rows = defaultdict(list)
                for (i,j) in cells:
                    rows[i].append(j)
                for r in rows:
                    rows[r].sort()
                owner_sorted[b] = (sorted(rows.keys()), rows)
        while low < high:
            mid = (low + high) //2
            S = mid
            # Compute f_total(S)
            common = S * R - S * (S +1) //2
            common_c = S * C - S * (S +1) //2
            # To prevent negative counts when S is large
            if common <0:
                common =0
            if common_c <0:
                common_c =0
            f_total = 2 * R * common_c + 2 * C * common - (R*C)
            f_total += 4 * common * common_c
            # Now f_total is sum of all ordered pairs with distance <= S, excluding self pairs
            # Now compute f_same(S)
            f_same =0
            for b, (sorted_rows, rows) in owner_sorted.items():
                cells = owner_cells[b]
                count =0
                for (i,j) in cells:
                    r_min = max(1, i - S)
                    r_max = min(R, i + S)
                    # Find the range of rows
                    li = bisect_left(sorted_rows, r_min)
                    ri = bisect_right(sorted_rows, r_max)
                    relevant_rows = sorted_rows[li:ri]
                    for r in relevant_rows:
                        cols = rows[r]
                        c_min = j - S
                        c_max = j + S
                        left = bisect_left(cols, c_min)
                        right = bisect_right(cols, c_max)
                        count += right - left
                f_same += count
            # f_same includes A=B for each cell, so subtract total_cells
            f_same -= (R * C)
            # Now f(S) = f_total - f_same
            f_S = f_total - f_same
            if f_S >= K:
                high = mid
            else:
                low = mid +1
        # After binary search, low is the minimal S where f(S)>=K
        print(f"Case #{test_case}: {low}")

threading.Thread(target=main,).start()