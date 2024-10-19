import sys
import bisect

def count_ordered_pairs_within_S(cells, S):
    # Sort cells by row, then by column
    cells_sorted = sorted(cells, key=lambda x: (x[0], x[1]))
    n = len(cells_sorted)
    count = 0
    left = 0
    sorted_cols = []
    for right in range(n):
        row_r, col_r = cells_sorted[right]
        # Move left pointer to keep row difference <= S
        while row_r - cells_sorted[left][0] > S:
            # Remove cells_sorted[left][1] from sorted_cols
            idx = bisect.bisect_left(sorted_cols, cells_sorted[left][1])
            if idx < len(sorted_cols) and sorted_cols[idx] == cells_sorted[left][1]:
                sorted_cols.pop(idx)
            left +=1
        # Now, cells from left to right have row difference <= S
        # Count number of cells with col in [col_r - S, col_r + S]
        low = col_r - S
        high = col_r + S
        l = bisect.bisect_left(sorted_cols, low)
        r_idx = bisect.bisect_right(sorted_cols, high)
        count += r_idx - l
        # Insert current column into sorted_cols
        bisect.insort(sorted_cols, col_r)
    # Each pair is counted once (a,b) where a is the right cell and b is within S
    # Now, to get ordered pairs, it's the same as count
    # Subtract the self-pairs (a,b) where a == b, which are exactly len(cells)
    count -= len(cells)
    return count

def process_test_case(R, C, K, grid):
    from collections import defaultdict
    bunnies = defaultdict(list)
    for i in range(R):
        for j in range(C):
            bunny_id = grid[i][j]
            bunnies[bunny_id].append( (i+1, j+1) )
    # Extract bunnies with M >=2
    bunnies_multi = {k:v for k,v in bunnies.items() if len(v) >=2}
    # Binary search over S
    low =0
    high = max(R, C)
    answer = high
    while low <= high:
        mid = (low + high) //2
        # Compute total_pairs(mid)
        total_pairs = (2 * mid * R - mid * (mid +1) + R) * (2 * mid * C - mid * (mid +1) + C) - R*C
        # Compute same_owner_pairs(mid)
        same_owner_pairs =0
        for cells in bunnies_multi.values():
            same_owner_pairs += count_ordered_pairs_within_S(cells, mid)
        # Compute valid_hops
        valid_hops = total_pairs - same_owner_pairs
        if valid_hops >= K:
            answer = mid
            high = mid -1
        else:
            low = mid +1
    return answer

def main():
    import sys
    import threading
    def run():
        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            R, C, K = map(int, line.strip().split())
            grid = []
            count =0
            while count < R:
                row = []
                while len(row) < C:
                    parts = sys.stdin.readline().strip().split()
                    row += [int(x) for x in parts]
                grid.append(row[:C])
                count +=1
            answer = process_test_case(R, C, K, grid)
            print(f"Case #{test_case}: {answer}")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()