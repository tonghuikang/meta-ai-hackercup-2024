import sys

def find_four_in_a_row(grid, player):
    four_in_a_rows = []
    rows = 6
    cols = 7
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != player:
                continue
            # Check horizontally to the right
            if c + 3 < cols:
                if all(grid[r][c + i] == player for i in range(4)):
                    four_in_a_rows.append([(r, c + i) for i in range(4)])
            # Check vertically upwards
            if r + 3 < rows:
                if all(grid[r + i][c] == player for i in range(4)):
                    four_in_a_rows.append([(r + i, c) for i in range(4)])
            # Check diagonally up-right
            if r + 3 < rows and c + 3 < cols:
                if all(grid[r + i][c + i] == player for i in range(4)):
                    four_in_a_rows.append([(r + i, c + i) for i in range(4)])
            # Check diagonally up-left
            if r + 3 < rows and c - 3 >= 0:
                if all(grid[r + i][c - i] == player for i in range(4)):
                    four_in_a_rows.append([(r + i, c - i) for i in range(4)])
    return four_in_a_rows

def compute_min_step(grid, player, steps):
    four_in_a_rows = find_four_in_a_row(grid, player)
    if not four_in_a_rows:
        return float('inf')
    min_step = float('inf')
    for four in four_in_a_rows:
        max_step = max(steps[r][c] for (r, c) in four)
        if max_step < min_step:
            min_step = max_step
    return min_step

def main():
    input = sys.stdin.read().split('\n')
    T = int(input[0])
    idx = 1
    for tc in range(1, T+1):
        # Skip empty lines
        while idx < len(input) and input[idx].strip() == '':
            idx +=1
        grid = []
        for _ in range(6):
            if idx < len(input):
                grid.append(input[idx].strip())
                idx +=1
            else:
                grid.append('.......')
        # Assign steps for C and F
        steps_c = [[float('inf') for _ in range(7)] for _ in range(6)]
        steps_f = [[float('inf') for _ in range(7)] for _ in range(6)]
        for c in range(7):
            count_c =0
            count_f =0
            for r in range(6):
                cell = grid[r][c]
                if cell == 'C':
                    steps_c[r][c] = 2 * count_c +1
                    count_c +=1
                elif cell == 'F':
                    steps_f[r][c] = 2 * count_f +2
                    count_f +=1
        min_step_c = compute_min_step(grid, 'C', steps_c)
        min_step_f = compute_min_step(grid, 'F', steps_f)
        # Determine the result
        if min_step_c < float('inf') and min_step_f < float('inf'):
            if min_step_c < min_step_f:
                result = 'C'
            elif min_step_f < min_step_c:
                result = 'F'
            else:
                result = '?'
        elif min_step_c < float('inf'):
            result = 'C'
        elif min_step_f < float('inf'):
            result = 'F'
        else:
            result = '0'
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()