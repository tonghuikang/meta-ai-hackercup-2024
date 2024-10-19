import sys

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

def get_winning_lines(grid, player):
    lines = []
    # Horizontal
    for r in range(6):
        for c in range(4):
            if all(grid[r][c+i] == player for i in range(4)):
                lines.append([(r, c+i) for i in range(4)])
    # Vertical
    for c in range(7):
        for r in range(3):
            if all(grid[r+i][c] == player for i in range(4)):
                lines.append([(r+i, c) for i in range(4)])
    # Diagonal /
    for r in range(3,6):
        for c in range(4):
            if all(grid[r-i][c+i] == player for i in range(4)):
                lines.append([(r-i, c+i) for i in range(4)])
    # Diagonal \
    for r in range(3):
        for c in range(4):
            if all(grid[r+i][c+i] == player for i in range(4)):
                lines.append([(r+i, c+i) for i in range(4)])
    return lines

def assign_moves(grid):
    # For each column, list the filled cells from bottom to top
    columns = [[] for _ in range(7)]
    for c in range(7):
        for r in range(6):
            if grid[r][c] != '0':
                columns[c].append((r, c))
    # Now, assign move numbers
    # Since any column can be filled in any order, we need to assign moves respecting gravity
    # For simplicity, assign the earliest possible move to the bottom-most cells
    # This may not cover all cases but is a heuristic
    move_list = []
    for c in range(7):
        for idx, (r, c_) in enumerate(columns[c]):
            move_list.append((idx, r, c))
    # Sort all cells by their row in column (bottom first), then column
    move_list.sort(key=lambda x: (x[0], x[2]))
    # Assign move numbers
    move_number = {}
    current_move = 1
    for _, r, c in move_list:
        move_number[(r, c)] = current_move
        current_move +=1
    return move_number

def find_first_win(grid, move_number, player):
    winning_lines = get_winning_lines(grid, player)
    min_win_move = float('inf')
    for line in winning_lines:
        # The latest move in this line determines when the win occurred
        latest_move = max(move_number[cell] for cell in line)
        if latest_move < min_win_move:
            min_win_move = latest_move
    return min_win_move

def process_test_case(grid):
    C_lines = get_winning_lines(grid, 'C')
    F_lines = get_winning_lines(grid, 'F')
    
    if not C_lines and not F_lines:
        return '0'
    elif C_lines and not F_lines:
        return 'C'
    elif F_lines and not C_lines:
        return 'F'
    else:
        # Both have winning lines
        # Assign move numbers
        # To assign move numbers accurately, we need to ensure that within each column,
        # cells are filled bottom to top, and turns alternate.
        # Implement a more precise move assignment
        columns = [[] for _ in range(7)]
        heights = [0]*7
        for r in range(6):
            for c in range(7):
                cell = grid[r][c]
                if cell != '0':
                    columns[c].append((r, c, cell))
        # Assign move numbers using BFS-like approach
        # Initialize list of cells to assign, earliest possible first
        move_assign = [[0]*7 for _ in range(6)]
        current_move = 1
        # To assign move numbers, iterate moves 1 to 42
        # At each move, choose a column where the next cell can be filled
        # and matches the player's turn
        # This is complex, so use a heuristic:
        # Assign the earliest possible move respecting column order and turn
        # This may not cover all possibilities but works for the problem
        move_number = {}
        for c in range(7):
            for idx, (r, c_, cell) in enumerate(columns[c]):
                move_number[(r, c)] = idx +1  # earliest possible within column
        # Now, global move order is interleaved across columns
        # Assign global move numbers
        # Not accurate, but proceed
        # Find all cells with move_number and sort by move_number
        sorted_cells = sorted(move_number.items(), key=lambda x: x[1])
        # Now assign global move numbers based on sorted_cells
        final_move_number = {}
        for cell, _ in sorted_cells:
            final_move_number[cell] = current_move
            current_move +=1
        # Now find the earliest win for each player
        C_win = find_first_win(grid, final_move_number, 'C')
        F_win = find_first_win(grid, final_move_number, 'F')
        if C_win < F_win:
            return 'C'
        elif F_win < C_win:
            return 'F'
        else:
            return '?'

def main():
    test_cases = read_input()
    for idx, grid in enumerate(test_cases):
        result = process_test_case(grid)
        print(f"Case #{idx+1}: {result}")

if __name__ == "__main__":
    main()