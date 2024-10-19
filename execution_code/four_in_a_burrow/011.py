import sys

def read_input():
    lines = sys.stdin.read().splitlines()
    T = int(lines[0])
    test_cases = []
    idx = 1
    for _ in range(T):
        while idx < len(lines) and lines[idx].strip() == '':
            idx += 1
        grid = []
        for _ in range(6):
            grid.append(list(lines[idx].strip()))
            idx += 1
        test_cases.append(grid)
    return test_cases

def check_winner(grid, player):
    rows = 6
    cols = 7
    # Directions: horizontal, vertical, diag1, diag2
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != player:
                continue
            # Horizontal
            if c + 3 < cols and all(grid[r][c+i] == player for i in range(4)):
                return True
            # Vertical
            if r + 3 < rows and all(grid[r+i][c] == player for i in range(4)):
                return True
            # Diagonal /
            if r + 3 < rows and c + 3 < cols and all(grid[r+i][c+i] == player for i in range(4)):
                return True
            # Diagonal \
            if r - 3 >= 0 and c + 3 < cols and all(grid[r-i][c+i] == player for i in range(4)):
                return True
    return False

def simulate_game(final_grid):
    # Reconstruct move order
    # For each column, from bottom to top, list the cells
    columns = [[] for _ in range(7)]
    for c in range(7):
        for r in range(5, -1, -1):
            if final_grid[r][c] != '.':
                columns[c].append((r, c, final_grid[r][c]))
    # Now, reconstruct the move sequence
    # Each move is a tuple: (r, c, player)
    move_sequence = []
    # The total number of burrows should be 42
    # Assign moves based on the filling order
    # Each move is assigned a turn number based on the order they were placed
    # To assign the correct move order, we need to interleave the columns
    # Since each column is filled from bottom to top, the first burrow in a column was earlier than the second, etc.
    # We'll use a list of iterators for each column
    # And simulate the sequence by selecting the earliest move based on row number
    movement = [[] for _ in range(7)]
    for c in range(7):
        movement[c] = final_grid[::-1][c]
        # To clarify, fill columns from bottom to top
    # Instead of trying to sort, we'll iterate move by move
    # Assign move numbers based on the sequence: first burrow is move 1, etc.
    # Since the order of filling across columns is not defined, we need to sort moves based on when they could have been placed
    # To simplify, we'll assign moves in the order they were filled (from bottom to top, left to right)
    moves = []
    for c in range(7):
        for r in range(6):
            if final_grid[5 - r][c] != '.':
                moves.append((r, c, final_grid[5 - r][c]))
    # Now sort moves based on the order they could have been placed
    # The earliest move is the one with the lowest level (r) and earliest column
    # To better reconstruct, we can assign move numbers based on the height in each column
    column_heights = [len([final_grid[r][c] for r in range(6) if final_grid[r][c] != '.']) for c in range(7)]
    # Assign move numbers
    # The first burrow in each column was placed first, etc.
    # So the overall move order can be determined by interleaving the moves from each column based on when they were placed
    # To accurately reconstruct, we need to assign a global move order
    # We'll iterate move by move, selecting the next possible move (the lowest unassigned in any column)
    # Since players alternate, the order is 'C', 'F', 'C', 'F', etc.
    # So we can sort the moves by the order they must have been placed
    # Basically, moves are ordered first by the row (from bottom to top), then by column (left to right)
    # So earlier moves have lower row numbers, then lower column numbers
    moves_sorted = sorted(moves, key=lambda x: (x[0], x[1]))
    # Now simulate the game
    grid = [['.' for _ in range(7)] for _ in range(6)]
    winner = None
    for i, move in enumerate(moves_sorted):
        r, c, player = move
        grid[r][c] = player
        # After this move, check if this player has a connect four
        if check_winner(grid, player):
            if winner is None:
                winner = player
            elif winner != player:
                # If different player also forms connect four at the same move
                winner = '?'
                break
    if winner is None:
        return '0'
    else:
        return winner

def determine_winner(final_grid):
    # Check if 'C' or 'F' have connect fours in the final grid
    c_win = check_winner(final_grid, 'C')
    f_win = check_winner(final_grid, 'F')
    if not c_win and not f_win:
        return '0'
    if c_win and not f_win:
        return 'C'
    if f_win and not c_win:
        return 'F'
    # Both have connect fours, need to determine who formed first
    # Simulate the game step by step
    # Reconstruct move order based on the final grid
    # Here, to handle this properly, we need to assign move numbers and simulate
    # However, the initial simulation above may not handle all cases correctly
    # Instead, we need a more accurate simulation
    # Here's an improved simulation
    # Reconstruct move sequence based on column filling
    columns = [[] for _ in range(7)]
    for c in range(7):
        for r in range(5, -1, -1):
            if final_grid[r][c] != '.':
                columns[c].append(final_grid[r][c])
    # Assign moves in the order they were placed
    # The earliest move is move 0, then move 1, etc.
    # To simulate correctly, we need to assign a global order
    # We'll use the order in which the cells were filled
    # It's impossible to know the exact global order, but we can assign based on the row index
    # Lower row index means earlier move in the column
    # We'll sort by row first, then column
    move_order = []
    for c in range(7):
        for r in range(len(columns[c])):
            move_order.append((r, c, columns[c][r]))
    # Now sort by the order in which they were placed across all columns
    # Assuming that within the same row, columns are filled left to right
    move_order_sorted = sorted(move_order, key=lambda x: (x[0], x[1]))
    # Now simulate the game and find the first winner
    grid_sim = [['.' for _ in range(7)] for _ in range(6)]
    first_winner = None
    for i, move in enumerate(move_order_sorted):
        r, c, player = move
        grid_sim[r][c] = player
        if check_winner(grid_sim, player):
            first_winner = player
            break
    # After simulation, determine the output
    if first_winner is not None:
        return first_winner
    else:
        return '0'

def process_test_cases(test_cases):
    results = []
    for idx, grid in enumerate(test_cases):
        # Determine the winner
        # Using the improved simulation
        c_win = check_winner(grid, 'C')
        f_win = check_winner(grid, 'F')
        if not c_win and not f_win:
            result = '0'
        elif c_win and not f_win:
            result = 'C'
        elif f_win and not c_win:
            result = 'F'
        else:
            # Both have connect fours, need to determine who won first
            # Simulate the game to find the earliest winner
            # Reconstruct move order
            move_order = []
            for c in range(7):
                for r in range(5, -1, -1):
                    if grid[r][c] != '.':
                        move_order.append((r, c, grid[r][c]))
            # Sort moves by row then column
            move_order_sorted = sorted(move_order, key=lambda x: (x[0], x[1]))
            grid_sim = [['.' for _ in range(7)] for _ in range(6)]
            first_winner = None
            for move in move_order_sorted:
                r, c, player = move
                grid_sim[r][c] = player
                if check_winner(grid_sim, player):
                    if first_winner is None:
                        first_winner = player
                    elif first_winner != player:
                        first_winner = '?'
                        break
            if first_winner is None:
                result = '0'
            elif first_winner in ['C', 'F']:
                # Now check if both have connect fours in final grid
                # but the first_winner determined by simulation
                result = first_winner
            else:
                result = '?'
        results.append(f"Case #{idx+1}: {result}")
    return results

def main():
    test_cases = read_input()
    results = process_test_cases(test_cases)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()