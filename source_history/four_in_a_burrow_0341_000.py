import sys

def main():
    import sys
    import sys
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        # Read empty lines
        while True:
            line = sys.stdin.readline()
            if line.strip() == '':
                continue
            else:
                grid_lines = [line.rstrip()]
                break
        while len(grid_lines) <6:
            grid_lines.append(sys.stdin.readline().rstrip())
        # Reverse the grid to have row0 at bottom
        grid = grid_lines[::-1]
        # Assign min_move[c][r] = r +1
        min_move = [[0 for _ in range(6)] for _ in range(7)]
        for c in range(7):
            for r in range(6):
                if grid[r][c] != '.':
                    min_move[c][r] = r +1
                else:
                    min_move[c][r] = float('inf')  # Empty, but per constraints, grid is full
        # Function to find all four-in-a-row for a player
        def find_fours(player):
            fours = []
            for r in range(6):
                for c in range(7):
                    if grid[r][c] != player:
                        continue
                    # Horizontal
                    if c <= 7-4:
                        if all(grid[r][c+i] == player for i in range(4)):
                            fours.append([(c+i, r) for i in range(4)])
                    # Vertical
                    if r <= 6-4:
                        if all(grid[r+i][c] == player for i in range(4)):
                            fours.append([(c, r+i) for i in range(4)])
                    # Diagonal up-right
                    if c <=7-4 and r <=6-4:
                        if all(grid[r+i][c+i] == player for i in range(4)):
                            fours.append([(c+i, r+i) for i in range(4)])
                    # Diagonal up-left
                    if c >=3 and r <=6-4:
                        if all(grid[r+i][c-i] == player for i in range(4)):
                            fours.append([(c-i, r+i) for i in range(4)])
            return fours
        # Find all fours for 'C' and 'F'
        fours_C = find_fours('C')
        fours_F = find_fours('F')
        # Function to compute next move
        def next_move(player, completion):
            if player == 'C':
                earliest = max(7, completion)
                if earliest %2 ==1:
                    return earliest
                else:
                    return earliest +1
            elif player == 'F':
                earliest = max(8, completion)
                if earliest %2 ==0:
                    return earliest
                else:
                    return earliest +1
        # Find minimal completion move for 'C'
        min_C = float('inf')
        for four in fours_C:
            max_move_four = max(min_move[c][r] for c,r in four)
            c_move = next_move('C', max_move_four)
            if c_move < min_C:
                min_C = c_move
        # Find minimal completion move for 'F'
        min_F = float('inf')
        for four in fours_F:
            max_move_four = max(min_move[c][r] for c,r in four)
            f_move = next_move('F', max_move_four)
            if f_move < min_F:
                min_F = f_move
        # Determine the result
        if min_C < float('inf') and min_F < float('inf'):
            if min_C < min_F:
                result = 'C'
            elif min_F < min_C:
                result = 'F'
            else:
                result = '?'
        elif min_C < float('inf'):
            result = 'C'
        elif min_F < float('inf'):
            result = 'F'
        else:
            result = '0'
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()