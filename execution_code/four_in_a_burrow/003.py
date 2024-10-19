import sys

def read_grid():
    grid = []
    for _ in range(6):
        line = sys.stdin.readline().strip()
        grid.append(list(line))
    return grid

def find_four_in_a_row(grid):
    lines = []
    rows = 6
    cols = 7
    # Horizontal
    for r in range(rows):
        for c in range(cols - 3):
            line = [(r, c + i) for i in range(4)]
            if all(grid[r][c + i] == grid[r][c] for i in range(4)):
                lines.append(line)
    # Vertical
    for c in range(cols):
        for r in range(rows - 3):
            line = [(r + i, c) for i in range(4)]
            if all(grid[r + i][c] == grid[r][c] for i in range(4)):
                lines.append(line)
    # Diagonal down-right
    for r in range(rows - 3):
        for c in range(cols - 3):
            line = [(r + i, c + i) for i in range(4)]
            if all(grid[r + i][c + i] == grid[r][c] for i in range(4)):
                lines.append(line)
    # Diagonal up-right
    for r in range(3, rows):
        for c in range(cols - 3):
            line = [(r - i, c + i) for i in range(4)]
            if all(grid[r - i][c + i] == grid[r][c] for i in range(4)):
                lines.append(line)
    return lines

def has_four_in_a_row(grid):
    return len(find_four_in_a_row(grid)) > 0

def get_top_burrows(grid):
    top_burrows = []
    for c in range(7):
        for r in range(5, -1, -1):
            if grid[r][c] != '.':
                top_burrows.append( (r, c) )
                break
    return top_burrows

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        _ = sys.stdin.readline()  # Read empty line
        grid = read_grid()
        lines = find_four_in_a_row(grid)
        if not lines:
            result = '0'
        else:
            # Collect all critical cells
            critical_cells = set()
            for line in lines:
                # Critical cell is the one with the highest row in the line
                critical = max(line, key=lambda x: x[0])
                critical_cells.add(critical)
            # Now check which critical cells are responsible
            responsible_players = set()
            for cell in critical_cells:
                r, c = cell
                # Remove this cell
                new_grid = [row[:] for row in grid]
                new_grid[r][c] = '.'
                if not has_four_in_a_row(new_grid):
                    responsible_players.add(grid[r][c])
            if not responsible_players:
                result = '0'
            elif len(responsible_players) == 1:
                result = responsible_players.pop()
            else:
                result = '?'
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()