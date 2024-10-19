import sys

def read_grid():
    grid = []
    for _ in range(6):
        line = sys.stdin.readline().strip()
        grid.append(list(line))
    return grid

def get_four_in_a_row(grid, player):
    sequences = []
    # Horizontal
    for r in range(6):
        for c in range(4):
            if all(grid[r][c+i] == player for i in range(4)):
                sequences.append([(r, c+i) for i in range(4)])
    # Vertical
    for c in range(7):
        for r in range(3):
            if all(grid[r+i][c] == player for i in range(4)):
                sequences.append([(r+i, c) for i in range(4)])
    # Diagonal /
    for r in range(3):
        for c in range(4):
            if all(grid[r+i][c+i] == player for i in range(4)):
                sequences.append([(r+i, c+i) for i in range(4)])
    # Diagonal \
    for r in range(3):
        for c in range(3,7):
            if all(grid[r+i][c-i] == player for i in range(4)):
                sequences.append([(r+i, c-i) for i in range(4)])
    return sequences

def find_min_move(grid, sequences):
    min_move = float('inf')
    for seq in sequences:
        # The highest cell in the sequence
        highest = max(seq, key=lambda x: x[0])
        r, c = highest
        # Move number is at least the number of cells below +1
        move_num = r + 1  # since rows are 0-indexed
        if move_num < min_move:
            min_move = move_num
    return min_move

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        # Read empty line
        while True:
            line = sys.stdin.readline()
            if line.strip() == '':
                continue
            else:
                break
        # Read grid
        grid = [list(line.strip()) for line in [line] + [sys.stdin.readline().strip() for _ in range(5)]]
        # Find four in a row for C and F
        c_seqs = get_four_in_a_row(grid, 'C')
        f_seqs = get_four_in_a_row(grid, 'F')
        if not c_seqs and not f_seqs:
            result = '0'
        elif c_seqs and not f_seqs:
            result = 'C'
        elif f_seqs and not c_seqs:
            result = 'F'
        else:
            # Both have sequences, determine who could have achieved first
            # Find the minimal move number for C and F
            c_min = find_min_move(grid, c_seqs)
            f_min = find_min_move(grid, f_seqs)
            if c_min < f_min:
                result = 'C'
            elif f_min < c_min:
                result = 'F'
            else:
                result = '?'
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()