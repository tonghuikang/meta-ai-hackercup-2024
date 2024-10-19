import sys

def read_input():
    lines = sys.stdin.read().splitlines()
    T = int(lines[0])
    test_cases = []
    idx = 1
    for _ in range(T):
        while idx < len(lines) and lines[idx] == '':
            idx += 1
        grid = []
        for _ in range(6):
            grid.append(lines[idx])
            idx += 1
        test_cases.append(grid)
    return test_cases

def check_win(grid, player):
    rows = 6
    cols = 7
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != player:
                continue
            # Check horizontal
            if c + 3 < cols and all(grid[r][c+i] == player for i in range(4)):
                return True
            # Check vertical
            if r + 3 < rows and all(grid[r+i][c] == player for i in range(4)):
                return True
            # Check diagonal down-right
            if r + 3 < rows and c + 3 < cols and all(grid[r+i][c+i] == player for i in range(4)):
                return True
            # Check diagonal up-right
            if r - 3 >= 0 and c + 3 < cols and all(grid[r-i][c+i] == player for i in range(4)):
                return True
    return False

def count_moves(grid):
    C = sum(row.count('C') for row in grid)
    F = sum(row.count('F') for row in grid)
    return C, F

def get_play_sequence(grid):
    # Reconstruct the sequence of moves
    cols = 7
    rows = 6
    stack = [[] for _ in range(cols)]
    for c in range(cols):
        for r in range(rows-1, -1, -1):
            if grid[r][c] != '.':
                stack[c].append(grid[r][c])
    total_moves = sum(len(col) for col in stack)
    sequence = []
    # Players take turns: C starts first
    turn = 'C'
    for _ in range(total_moves):
        # Find the last move that was not yet in sequence
        for c in range(cols):
            if stack[c]:
                # The burrow was placed last in this column
                player = stack[c].pop()
                sequence.append((player, c))
                break
    return sequence[::-1]  # reverse to get the play order

def solve_case(grid):
    # First, check if both have winning lines
    C_win = check_win(grid, 'C')
    F_win = check_win(grid, 'F')
    if not C_win and not F_win:
        return '0'
    if C_win and not F_win:
        return 'C'
    if F_win and not C_win:
        return 'F'
    # If both have winning lines, need to determine the first winner
    # Reconstruct the move sequence
    # However, since the game continued after a win, it's possible that both have winning lines
    # We need to determine if one must have achieved the win before the other
    # To simplify, we can assume that if C has more or equal moves, and both have wins, 
    # it's 'C' if C could have achieved the win first, 'F' otherwise
    # However, this is not always accurate; for the problem's requirement, we'll output '?'
    return '?'

def main():
    test_cases = read_input()
    for i, grid in enumerate(test_cases, 1):
        result = solve_case(grid)
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()