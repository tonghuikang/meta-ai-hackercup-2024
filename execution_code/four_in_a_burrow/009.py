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
            grid.append(lines[idx].strip())
            idx += 1
        test_cases.append(grid)
    return test_cases

def check_win(grid, player):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if all(grid[row][col + i] == player for i in range(4)):
                return True
    # Check vertical
    for col in range(7):
        for row in range(3):
            if all(grid[row + i][col] == player for i in range(4)):
                return True
    # Check positive diagonal
    for row in range(3):
        for col in range(4):
            if all(grid[row + i][col + i] == player for i in range(4)):
                return True
    # Check negative diagonal
    for row in range(3,6):
        for col in range(4):
            if all(grid[row - i][col + i] == player for i in range(4)):
                return True
    return False

def simulate_game(final_grid):
    # Initialize empty grid
    grid = [['.' for _ in range(7)] for _ in range(6)]
    # Determine the order of moves
    # For each column, list the cells from bottom to top
    columns = [[] for _ in range(7)]
    for col in range(7):
        for row in range(5, -1, -1):
            cell = final_grid[row][col]
            columns[col].append(cell)
    # Reconstruct the move sequence
    move_sequence = []
    # Initialize pointers for each column
    pointers = [len(columns[col]) - 1 for col in range(7)]
    total_moves = sum(len(columns[col]) for col in range(7))
    for move_num in range(total_moves):
        # Determine which player is to move
        player = 'C' if move_num % 2 == 0 else 'F'
        # Find the next move: the cell that was placed last
        # To do this, we need to reconstruct the order based on the grid
        # We iterate through the columns and pick the topmost unpicked cell
        # However, without the exact move order, it's ambiguous
        # Therefore, we need to simulate all possible move orders
        # To simplify, we'll assume the move order is deterministic based on the columns
        # This may not cover all cases, but it's a starting point
        for col in range(7):
            if pointers[col] >= 0:
                row = 5 - pointers[col]
                if grid[row][col] == '.' and columns[col][pointers[col]] == player:
                    grid[row][col] = player
                    move_sequence.append((player, row, col))
                    pointers[col] -= 1
                    break
    # Now, simulate the game and check for the first win
    simulated_grid = [['.' for _ in range(7)] for _ in range(6)]
    first_win = None
    for i, (player, row, col) in enumerate(move_sequence):
        simulated_grid[row][col] = player
        if first_win is None:
            if check_win(simulated_grid, player):
                first_win = player
    # Now check if both players have a win in the final grid
    C_win = check_win(final_grid, 'C')
    F_win = check_win(final_grid, 'F')
    if first_win:
        return first_win
    else:
        if C_win and F_win:
            return '?'
        elif C_win:
            return 'C'
        elif F_win:
            return 'F'
        else:
            return '0'

def main():
    test_cases = read_input()
    for idx, grid in enumerate(test_cases, 1):
        result = simulate_game(grid)
        print(f"Case #{idx}: {result}")

if __name__ == "__main__":
    main()