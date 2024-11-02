import sys

def process_test_case(N, K, grid):
    # Find initial '1's positions
    rows_with_ones = set()
    cols_with_ones = set()
    for r in range(N):
        for c in range(N):
            if grid[r][c] == '1':
                rows_with_ones.add(r)
                cols_with_ones.add(c)
    if not rows_with_ones:
        min_row = max_row = min_col = max_col = -1
    else:
        min_row = min(rows_with_ones)
        max_row = max(rows_with_ones)
        min_col = min(cols_with_ones)
        max_col = max(cols_with_ones)
    # Height and width
    if min_row == -1:
        H = 0
        W = 0
    else:
        H = max_row - min_row +1
        W = max_col - min_col +1
    # Find possible extensions
    # Upwards
    up_extensions = []
    if min_row != -1:
        r = min_row -1
    else:
        r = N-1
    while r >=0:
        if '?' in grid[r]:
            up_extensions.append(r)
        r -=1
    # Downwards
    down_extensions = []
    if min_row != -1:
        r = max_row +1
    else:
        r = 0
    while r < N:
        if '?' in grid[r]:
            down_extensions.append(r)
        r +=1
    # Leftwards
    left_extensions = []
    if min_col != -1:
        c = min_col -1
    else:
        c = N-1
    while c >=0:
        has_q = False
        for r in range(N):
            if grid[r][c] == '?':
                has_q = True
                break
        if has_q:
            left_extensions.append(c)
        c -=1
    # Rightwards
    right_extensions = []
    if min_col != -1:
        c = max_col +1
    else:
        c = 0
    while c < N:
        has_q = False
        for r in range(N):
            if grid[r][c] == '?':
                has_q = True
                break
        if has_q:
            right_extensions.append(c)
        c +=1
    # Maximum possible extensions
    up_max = len(up_extensions)
    down_max = len(down_extensions)
    left_max = len(left_extensions)
    right_max = len(right_extensions)
    total_vertical = up_max + down_max
    total_horizontal = left_max + right_max
    # Now, iterate over possible vertical extensions
    max_area = 0
    # Precompute possible vertical extensions
    possible_vertical = min(total_vertical, K)
    for e_h in range(0, min(total_vertical, K)+1):
        e_w = min(K - e_h, total_horizontal)
        current_H = H + e_h
        current_W = W + e_w
        current_area = current_H * current_W
        if current_area > max_area:
            max_area = current_area
    return max_area if max_area >0 else 1

def main():
    import sys
    import threading
    def run():
        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            N_K = line.strip().split()
            while len(N_K) <2:
                N_K += sys.stdin.readline().strip().split()
            N, K = map(int, N_K)
            grid = []
            for _ in range(N):
                row = sys.stdin.readline().strip()
                while len(row) < N:
                    row += sys.stdin.readline().strip()
                grid.append(row)
            max_cover_area = process_test_case(N, K, grid)
            print(f"Case #{test_case}: {max_cover_area}")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()