import sys
import threading
import bisect

def main():
    import sys

    import sys

    from collections import defaultdict

    T = int(sys.stdin.readline())
    for test_case in range(1, T +1):
        R, C, K = map(int, sys.stdin.readline().split())
        grid = []
        owner_to_cells = defaultdict(list)
        for i in range(1, R +1):
            row = list(map(int, sys.stdin.readline().split()))
            for j in range(1, C +1):
                owner = row[j-1]
                owner_to_cells[owner].append( (i, j) )

        def count_same_owner_pairs(d):
            total = 0
            for cells in owner_to_cells.values():
                m = len(cells)
                if m <2:
                    continue
                # Sort cells by row, then by column
                cells_sorted = sorted(cells)
                left =0
                cols = []
                # Use a sorted list for columns
                sorted_cols = []
                n_ordered =0
                for right in range(m):
                    i_r, j_r = cells_sorted[right]
                    while i_r - cells_sorted[left][0] > d:
                        # Remove cells_sorted[left][1] from sorted_cols
                        remove_j = cells_sorted[left][1]
                        idx = bisect.bisect_left(sorted_cols, remove_j)
                        if idx < len(sorted_cols) and sorted_cols[idx] == remove_j:
                            sorted_cols.pop(idx)
                        left +=1
                    # Now, rows are within [i_r -d, i_r +d]
                    # Find number of j in sorted_cols within [j_r -d, j_r +d]
                    low = j_r - d
                    high = j_r + d
                    cnt = bisect.bisect_right(sorted_cols, high) - bisect.bisect_left(sorted_cols, low)
                    # Exclude the current cell itself
                    n_ordered += cnt
                    # Add current j to sorted_cols
                    bisect.insort(sorted_cols, j_r)
                # Each unordered pair is counted twice, so total ordered pairs is n_ordered
                total += n_ordered
            return total

        # Binary search over d
        left_d =0
        right_d = max(R, C)
        answer = right_d
        while left_d <= right_d:
            mid_d = (left_d + right_d)//2
            # Compute total_pairs_with_score_le_d
            term_R = R * (2 * mid_d +1) - mid_d * (mid_d +1)
            term_C = C * (2 * mid_d +1) - mid_d * (mid_d +1)
            total_pairs = term_R * term_C
            # Compute total_same_owner_pairs_le_d
            total_same = count_same_owner_pairs(mid_d)
            # Compute total_valid_pairs_le_d
            total_valid = total_pairs - total_same
            if total_valid >= K:
                answer = mid_d
                right_d = mid_d -1
            else:
                left_d = mid_d +1
        print(f"Case #{test_case}: {answer}")

threading.Thread(target=main).start()

# The code is embedded above within the triple backticks.