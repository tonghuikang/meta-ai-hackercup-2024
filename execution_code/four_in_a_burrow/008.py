def check_winner(grid, player):
    rows, cols = 6, 7
    directions = [
        (0, 1),  # Horizontal
        (1, 0),  # Vertical
        (1, 1),  # Diagonal down-right
        (1, -1)  # Diagonal down-left
    ]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != player:
                continue
            for dr, dc in directions:
                count = 1
                for i in range(1, 4):
                    nr, nc = r + dr*i, c + dc*i
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == player:
                        count += 1
                    else:
                        break
                if count == 4:
                    return True
    return False

def solve_connect_four(test_cases):
    results = []
    for idx, grid in enumerate(test_cases, 1):
        c_win = check_winner(grid, 'C')
        f_win = check_winner(grid, 'F')

        if c_win and not f_win:
            result = 'C'
        elif f_win and not c_win:
            result = 'F'
        elif c_win and f_win:
            # Ambiguous who won first
            result = '?'
        else:
            result = '0'
        
        results.append(f"Case #{idx}: {result}")
    return results

if __name__ == "__main__":
    T = int(input())
    test_cases = []
    for _ in range(T):
        input()  # Read the empty line
        grid = []
        for _ in range(6):
            row = input().strip()
            grid.append(row)
        test_cases.append(grid)
    
    results = solve_connect_four(test_cases)
    for res in results:
        print(res)