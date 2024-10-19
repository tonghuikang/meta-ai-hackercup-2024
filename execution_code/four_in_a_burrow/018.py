import sys

def read_grid():
    grid = []
    for _ in range(6):
        row = sys.stdin.readline().strip()
        grid.append(row)
    return grid

def find_four_in_a_row(grid, player):
    four_in_a_rows = []
    # Check horizontal
    for r in range(6):
        for c in range(4):
            if all(grid[r][c+i] == player for i in range(4)):
                four_in_a_rows.append([(r, c+i) for i in range(4)])
    # Check vertical
    for c in range(7):
        for r in range(3):
            if all(grid[r+i][c] == player for i in range(4)):
                four_in_a_rows.append([(r+i, c) for i in range(4)])
    # Check diagonal down-right
    for r in range(3):
        for c in range(4):
            if all(grid[r+i][c+i] == player for i in range(4)):
                four_in_a_rows.append([(r+i, c+i) for i in range(4)])
    # Check diagonal up-right
    for r in range(3,6):
        for c in range(4):
            if all(grid[r-i][c+i] == player for i in range(4)):
                four_in_a_rows.append([(r-i, c+i) for i in range(4)])
    return four_in_a_rows

def minimal_move(grid, four_in_a_row):
    # For each cell in four_in_a_row, the number of cells below it in its column
    max_cells_below = 0
    for (r, c) in four_in_a_row:
        cells_below = 0
        for rr in range(r):
            if grid[rr][c] != '.':
                cells_below +=1
        max_cells_below = max(max_cells_below, cells_below)
    # Minimal move number is max_cells_below +1
    return max_cells_below +1

def process_test_case(grid):
    # Replace empty cells with '.' for consistency, though according to problem all cells are filled
    grid = [row.replace('C', 'C').replace('F', 'F') for row in grid]
    # Find all four-in-a-row for C and F
    c_fours = find_four_in_a_row(grid, 'C')
    f_fours = find_four_in_a_row(grid, 'F')
    # Find c_min
    c_min = float('inf')
    for four in c_fours:
        m = minimal_move(grid, four)
        c_min = min(c_min, m)
    # Find f_min
    f_min = float('inf')
    for four in f_fours:
        m = minimal_move(grid, four)
        f_min = min(f_min, m)
    # Determine the outcome
    if c_min < float('inf') and f_min < float('inf'):
        if c_min < f_min:
            return 'C'
        elif f_min < c_min:
            return 'F'
        else:
            return '?'
    elif c_min < float('inf'):
        return 'C'
    elif f_min < float('inf'):
        return 'F'
    else:
        return '0'

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        # Read possible empty lines
        while True:
            line = sys.stdin.readline()
            if line.strip() == '':
                continue
            else:
                grid = [line.strip()]
                break
        for _ in range(5):
            grid.append(sys.stdin.readline().strip())
        result = process_test_case(grid)
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()