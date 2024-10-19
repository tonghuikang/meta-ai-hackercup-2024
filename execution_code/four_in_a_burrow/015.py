import sys

def read_input():
    T = int(sys.stdin.readline())
    test_cases = []
    for _ in range(T):
        while True:
            line = sys.stdin.readline()
            if line.strip() == '':
                continue
            else:
                grid = [line.strip()]
                break
        for _ in range(5):
            grid.append(sys.stdin.readline().strip())
        test_cases.append(grid)
    return test_cases

def check_win(board, player):
    # Check horizontal
    for r in range(6):
        for c in range(4):
            if all(board[r][c+i] == player for i in range(4)):
                return True
    # Check vertical
    for c in range(7):
        for r in range(3):
            if all(board[r+i][c] == player for i in range(4)):
                return True
    # Check diagonal /
    for r in range(3,6):
        for c in range(4):
            if all(board[r-i][c+i] == player for i in range(4)):
                return True
    # Check diagonal \
    for r in range(3):
        for c in range(4):
            if all(board[r+i][c+i] == player for i in range(4)):
                return True
    return False

def simulate(grid):
    # Initialize empty board
    board = [['.' for _ in range(7)] for _ in range(6)]
    # Extract the moves in the order they were played
    # We'll reconstruct the move sequence by filling the board from bottom up
    columns = [[] for _ in range(7)]
    for c in range(7):
        for r in range(5,-1,-1):
            if grid[r][c] != '.':
                columns[c].append(grid[r][c])
    # Now, simulate the game move by move
    move_sequence = []
    # The maximum number of moves is 42
    for i in range(6):
        for c in range(7):
            if i < len(columns[c]):
                move_sequence.append((c, columns[c][i]))
    # Now, play the moves in order
    current_board = [['.' for _ in range(7)] for _ in range(6)]
    first_win = None
    for idx, (c, player) in enumerate(move_sequence):
        # Place the piece
        for r in range(6):
            if current_board[r][c] == '.':
                current_board[r][c] = player
                break
        # After each move, check for a win
        if idx >= 6:  # Minimum 7 moves needed for a win
            if check_win(current_board, player):
                if first_win is None:
                    first_win = player
                else:
                    # Already have a winner, do not overwrite
                    pass
        # Alternate players is implicit by move_sequence
    # Now, check who won in the first_win
    # Now, check if both have a win in the final grid
    c_win = check_win(grid, 'C')
    f_win = check_win(grid, 'F')
    if c_win and f_win:
        if first_win == 'C' and first_win == 'F':
            return '?'
        elif first_win == 'C':
            return 'C'
        elif first_win == 'F':
            return 'F'
        else:
            return '?'
    elif c_win:
        return 'C' if first_win == 'C' else '?'
    elif f_win:
        return 'F' if first_win == 'F' else '?'
    else:
        return '0'

def main():
    test_cases = read_input()
    for idx, grid in enumerate(test_cases, 1):
        result = simulate(grid)
        print(f"Case #{idx}: {result}")

if __name__ == "__main__":
    main()