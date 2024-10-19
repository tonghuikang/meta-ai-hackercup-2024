#!/usr/bin/env python3

T = int(input())
for case_num in range(1, T+1):
    input_line = input()  # Read the empty line
    grid = []
    for _ in range(6):
        grid.append(list(input().strip()))
    # Since the bottom row is the southernmost (index 5)
    # We'll process the grid and assign earliest possible move numbers
    
    E = [[None]*7 for _ in range(6)]  # Earliest possible move numbers
    for c in range(7):
        E_prev = 0
        player_prev = None
        for r in range(5, -1, -1):  # from bottom to top
            cell = grid[r][c]
            if cell == 'C' or cell == 'F':
                player = cell
                if E_prev == 0:
                    # First cell in this column
                    E_candidate = 1 if player == 'C' else 2
                else:
                    if player == player_prev:
                        # Same player as cell below
                        E_candidate = E_prev + 2
                    else:
                        # Different player from cell below
                        E_candidate = E_prev + 1
                # Adjust E_candidate to correct parity
                if player == 'C':
                    if E_candidate %2 == 0:
                        # Move number must be odd
                        E_candidate +=1
                else:
                    if E_candidate %2 ==1:
                        # Move number must be even
                        E_candidate +=1
                E[r][c] = E_candidate
                E_prev = E_candidate
                player_prev = player
            else:
                # Empty cell
                E_prev = 0
                player_prev = None

    # Now, find all winning lines
    earliest_win_C = None  # Minimal earliest move number when 'C' could have won
    earliest_win_F = None  # Same for 'F'
    # Directions to check: horizontal, vertical, diagonal /
    directions = [ (0,1), (1,0), (1,1), (1,-1) ]  # right, down, down-right, down-left
    for r in range(6):
        for c in range(7):
            player = grid[r][c]
            if player != 'C' and player != 'F':
                continue
            for dr, dc in directions:
                cells = []
                for k in range(4):
                    rr = r + dr*k
                    cc = c + dc*k
                    if 0 <= rr <6 and 0<=cc<7 and grid[rr][cc]==player:
                        cells.append( (rr, cc) )
                    else:
                        break
                if len(cells)==4:
                    # Winning line found
                    move_numbers = [ E[rr][cc] for rr,cc in cells ]
                    win_move = max(move_numbers)
                    if player == 'C':
                        if earliest_win_C is None or win_move < earliest_win_C:
                            earliest_win_C = win_move
                    else:
                        if earliest_win_F is None or win_move < earliest_win_F:
                            earliest_win_F = win_move
    # Decide who won first
    output = ''
    if earliest_win_C is None and earliest_win_F is None:
        output = '0'  # Nobody won
    elif earliest_win_C is not None and (earliest_win_F is None or earliest_win_C < earliest_win_F):
        output = 'C'  # Connie must have won first
    elif earliest_win_F is not None and (earliest_win_C is None or earliest_win_F < earliest_win_C):
        output = 'F'  # Forrest must have won first
    elif earliest_win_C == earliest_win_F:
        output = '?'  # Can't determine who won first
    print(f"Case #{case_num}: {output}")