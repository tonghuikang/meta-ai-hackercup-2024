import sys
import threading

def main():
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        sys.stdin.readline()  # Read the empty line
        grid = []
        for _ in range(6):
            row = sys.stdin.readline().strip()
            grid.append(list(row))
        # Reverse the grid to make row 0 the bottom (southernmost)
        grid = grid[::-1]
        result = solve_case(grid)
        print(f"Case #{case_num}: {result}")

def solve_case(grid):
    # Initialize the earliest move numbers for each cell
    earliest_moves = {}
    # Players
    players = ['C', 'F']
    # Map players to their move numbers
    player_move_nums = {'C': [i for i in range(1, 43, 2)], 'F': [i for i in range(2, 43, 2)]}

    # For memoization
    memo_earliest = {}

    # Function to compute earliest move number for a cell
    def get_earliest_move(r, c, player):
        if (r, c, player) in memo_earliest:
            return memo_earliest[(r, c, player)]

        cell_player = grid[r][c]
        if cell_player != player:
            return None  # This cell doesn't belong to the player

        # If we're at the bottom row
        if r == 0:
            earliest = player_move_nums[player][0]
        else:
            below_player = grid[r - 1][c]
            if below_player == player:
                earliest_below = get_earliest_move(r - 1, c, player)
                if earliest_below is None:
                    return None
                # Must wait two moves (opponent's turn)
                earliest = earliest_below + 2
            elif below_player == opponent(player):
                earliest_below = get_earliest_move(r - 1, c, opponent(player))
                if earliest_below is None:
                    return None
                # Can move immediately after opponent
                earliest = earliest_below + 1
            else:
                # Empty below, cannot place here yet
                return None

        # Adjust earliest to the player's own move numbers
        player_moves = player_move_nums[player]
        earliest_player_move = next((m for m in player_moves if m >= earliest), None)
        if earliest_player_move is None:
            return None
        memo_earliest[(r, c, player)] = earliest_player_move
        return earliest_player_move

    # Function to get opponent
    def opponent(player):
        return 'C' if player == 'F' else 'F'

    # Collect winning lines for each player
    winning_lines = {'C': [], 'F': []}
    for player in players:
        # Horizontal lines
        for r in range(6):
            for c in range(4):
                if all(grid[r][c + i] == player for i in range(4)):
                    winning_lines[player].append([(r, c + i) for i in range(4)])
        # Vertical lines
        for c in range(7):
            for r in range(3):
                if all(grid[r + i][c] == player for i in range(4)):
                    winning_lines[player].append([(r + i, c) for i in range(4)])
        # Diagonal (positive slope)
        for r in range(3):
            for c in range(4):
                if all(grid[r + i][c + i] == player for i in range(4)):
                    winning_lines[player].append([(r + i, c + i) for i in range(4)])
        # Diagonal (negative slope)
        for r in range(3):
            for c in range(3, 7):
                if all(grid[r + i][c - i] == player for i in range(4)):
                    winning_lines[player].append([(r + i, c - i) for i in range(4)])

    # For each player, compute earliest winning move
    earliest_wins = {}
    for player in players:
        min_earliest_win = None
        for line in winning_lines[player]:
            memo_earliest.clear()
            earliest_moves_in_line = []
            valid_line = True
            for r, c in line:
                earliest_move = get_earliest_move(r, c, player)
                if earliest_move is None:
                    valid_line = False
                    break
                earliest_moves_in_line.append(earliest_move)
            if valid_line:
                earliest_win_move = max(earliest_moves_in_line)
                if min_earliest_win is None or earliest_win_move < min_earliest_win:
                    min_earliest_win = earliest_win_move
        if min_earliest_win is not None:
            earliest_wins[player] = min_earliest_win

    # Determine who won first
    if not earliest_wins:
        return '0'  # Nobody has won
    elif 'C' in earliest_wins and 'F' not in earliest_wins:
        return 'C'  # Only Connie has a winning line
    elif 'F' in earliest_wins and 'C' not in earliest_wins:
        return 'F'  # Only Forrest has a winning line
    else:
        # Both have winning lines
        if earliest_wins['C'] < earliest_wins['F']:
            return 'C'  # Connie must have won first
        elif earliest_wins['F'] < earliest_wins['C']:
            return 'F'  # Forrest must have won first
        else:
            # Earliest winning move numbers are equal
            return '?'  # Can't determine who won first

# Run the main function in a separate thread to avoid recursion limit issues
threading.Thread(target=main).start()