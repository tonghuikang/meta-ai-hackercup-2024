import sys

def read_input():
    lines = sys.stdin.read().splitlines()
    T = int(lines[0])
    test_cases = []
    idx = 1
    for _ in range(T):
        while idx < len(lines) and lines[idx].strip() == '':
            idx +=1
        grid = []
        for _ in range(6):
            grid.append(lines[idx].strip())
            idx +=1
        test_cases.append(grid)
    return test_cases

def get_four_in_a_rows(grid, player):
    four_in_a_rows = []
    # Horizontal
    for r in range(6):
        for c in range(4):
            if all(grid[r][c+i]==player for i in range(4)):
                four_in_a_rows.append([(r, c+i) for i in range(4)])
    # Vertical
    for c in range(7):
        for r in range(3):
            if all(grid[r+i][c]==player for i in range(4)):
                four_in_a_rows.append([(r+i, c) for i in range(4)])
    # Diagonal down-right
    for r in range(3):
        for c in range(4):
            if all(grid[r+i][c+i]==player for i in range(4)):
                four_in_a_rows.append([(r+i, c+i) for i in range(4)])
    # Diagonal up-right
    for r in range(3,6):
        for c in range(4):
            if all(grid[r-i][c+i]==player for i in range(4)):
                four_in_a_rows.append([(r-i, c+i) for i in range(4)])
    return four_in_a_rows

def compute_min_win_step(grid, player):
    four_in_a_rows = get_four_in_a_rows(grid, player)
    if not four_in_a_rows:
        return None
    min_step = float('inf')
    for seq in four_in_a_rows:
        max_step = 0
        for (r,c) in seq:
            # Minimal step when this cell could have been placed
            step = r +1
            if step > max_step:
                max_step = step
        if max_step < min_step:
            min_step = max_step
    return min_step

def solve(test_cases):
    results = []
    case_num =1
    for grid in test_cases:
        cnt_C = sum(row.count('C') for row in grid)
        cnt_F = sum(row.count('F') for row in grid)
        # Validate counts if necessary
        four_C = compute_min_win_step(grid, 'C')
        four_F = compute_min_win_step(grid, 'F')
        if four_C is None and four_F is None:
            res = '0'
        elif four_C is not None and four_F is None:
            res = 'C'
        elif four_F is not None and four_C is None:
            res = 'F'
        else:
            if four_C < four_F:
                res = 'C'
            elif four_F < four_C:
                res = 'F'
            else:
                res = '?'
        results.append(f"Case #{case_num}: {res}")
        case_num +=1
    return results

if __name__ == "__main__":
    test_cases = read_input()
    results = solve(test_cases)
    for res in results:
        print(res)