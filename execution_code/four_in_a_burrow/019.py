def read_grid():
    grid = []
    for _ in range(6):
        row = input().strip()
        grid.append(row)
    return grid

def has_won(grid, player):
    # Directions: horizontal, vertical, diagonal /
    directions = [(0,1),(1,0),(1,1),(1,-1)]
    for r in range(6):
        for c in range(7):
            if grid[r][c] != player:
                continue
            for dr, dc in directions:
                count = 1
                nr, nc = r + dr, c + dc
                while 0 <= nr <6 and 0 <= nc <7 and grid[nr][nc] == player:
                    count +=1
                    if count ==4:
                        return True
                    nr += dr
                    nc += dc
    return False

def main():
    T = int(input())
    for test_case in range(1, T+1):
        # Read empty line
        while True:
            line = input()
            if line.strip() == '':
                continue
            else:
                grid = [line]
                break
        # Read remaining 5 rows
        for _ in range(5):
            grid.append(input().strip())
        # Now grid has 6 rows, bottom to top
        # Check who has won
        C_win = has_won(grid, 'C')
        F_win = has_won(grid, 'F')
        if C_win and not F_win:
            result = 'C'
        elif F_win and not C_win:
            result = 'F'
        elif C_win and F_win:
            result = '?'
        else:
            result = '0'
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()