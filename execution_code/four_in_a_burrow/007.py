import sys
import itertools

def read_input():
    T = int(sys.stdin.readline())
    test_cases = []
    for _ in range(T):
        line = sys.stdin.readline()
        grid = []
        for _ in range(6):
            grid.append(sys.stdin.readline().strip())
        test_cases.append(grid)
    return test_cases

def find_connect_fours(grid, player):
    connects = []
    # Horizontal
    for r in range(6):
        for c in range(4):
            if all(grid[r][c+i] == player for i in range(4)):
                connects.append([(r, c+i) for i in range(4)])
    # Vertical
    for c in range(7):
        for r in range(3):
            if all(grid[r+i][c] == player for i in range(4)):
                connects.append([(r+i, c) for i in range(4)])
    # Diagonal /
    for r in range(3,6):
        for c in range(4):
            if all(grid[r-i][c+i] == player for i in range(4)):
                connects.append([(r-i, c+i) for i in range(4)])
    # Diagonal \
    for r in range(3):
        for c in range(4):
            if all(grid[r+i][c+i] == player for i in range(4)):
                connects.append([(r+i, c+i) for i in range(4)])
    return connects

def get_column_heights(grid):
    heights = [0]*7
    for c in range(7):
        for r in range(6):
            if grid[r][c] != '.':
                heights[c] +=1
    return heights

def assign_moves(grid):
    # For each column, list the filled cells from bottom to top
    cols = []
    for c in range(7):
        col = []
        for r in range(6):
            if grid[r][c] != '.':
                col.append((r, c))
        cols.append(col)
    # Now, we need to assign move numbers to each cell, respecting column order
    # The lower cells must have lower move numbers
    # Players alternate: C on odd, F on even
    # We need to assign move numbers from 1 to 42 to the cells
    # such that within each column, the order is preserved
    # and C-F alternation is respected
    # This is a partial order problem; we can model it as constraints
    # But for efficiency, we'll assign earliest possible moves for each player
    # and later possible moves for others
    # Not perfectly accurate, but should work for problem constraints
    # Build a list of all filled cells with their constraints
    cell_constraints = {}
    heights = get_column_heights(grid)
    for c in range(7):
        for idx, (r, _) in enumerate(cols[c]):
            cell_constraints[(r,c)] = idx+1  # at least this move in the column
    return cell_constraints

def earliest_win(grid, player):
    connects = find_connect_fours(grid, player)
    if not connects:
        return float('inf')
    min_step = float('inf')
    for connect in connects:
        # For the connect four, find the latest possible move number among the four cells
        # which would determine when the connect was completed
        latest = 0
        for (r,c) in connect:
            # The cell (r,c) is filled at move number >= the number of cells below +1
            # The earliest C can fill it is when it's Connie's turn and all below are filled
            # Similarly for F
            # To approximate, count how many cells are below it
            below = 0
            for rr in range(r):
                if grid[rr][c] == player:
                    below +=1
            # The earliest the player can have filled this cell is after filling 'below' cells in this column
            # Each player fills their own cells on their turns
            # So the earliest move number is (below)*2 + 1 if player is C, else (below)*2 + 2
            if player == 'C':
                earliest = 2*below +1
            else:
                earliest = 2*below +2
            latest = max(latest, earliest)
        min_step = min(min_step, latest)
    return min_step

def process_test_case(grid):
    # First, check if there are any connect fours
    c_connects = find_connect_fours(grid, 'C')
    f_connects = find_connect_fours(grid, 'F')
    if not c_connects and not f_connects:
        return '0'
    # Now, find the earliest step C and F could have achieved a connect four
    c_step = earliest_win(grid, 'C') if c_connects else float('inf')
    f_step = earliest_win(grid, 'F') if f_connects else float('inf')
    if c_step < f_step:
        return 'C'
    elif f_step < c_step:
        return 'F'
    elif c_step == f_step and c_step != float('inf'):
        return '?'
    else:
        return '0'

def main():
    test_cases = read_input()
    for idx, grid in enumerate(test_cases,1):
        result = process_test_case(grid)
        print(f"Case #{idx}: {result}")

if __name__ == "__main__":
    main()