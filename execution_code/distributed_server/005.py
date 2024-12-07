# Read the number of test cases
T = int(input())

for case_num in range(1, T + 1):
    R, C = map(int, input().split())
    grid = [input() for _ in range(R)]
    
    # Initialize dp table
    dp = [['' for _ in range(C + 1)] for _ in range(R + 1)]
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            ch = grid[r][c].lower()
            right = dp[r][c + 1]
            down = dp[r + 1][c]
            dp[r][c] = ch + max(right, down)
    
    robots = []
    for r in range(R):
        for c in range(C):
            if grid[r][c].isupper():
                robots.append((dp[r][c], r, c))
    
    # Sort robots by their dp[r][c] in decreasing order
    robots.sort(reverse=True)
    
    used_cells = [[False] * C for _ in range(R)]
    assigned = []
    
    for si, r, c in robots:
        path = []
        cr, cc = r, c
        can_assign = True
        while True:
            if used_cells[cr][cc]:
                can_assign = False
                break
            path.append((cr, cc))
            used_cells[cr][cc] = True
            if cr == R - 1 and cc == C - 1:
                break
            ch = grid[cr][cc].lower()
            right_s = dp[cr][cc + 1] if cc + 1 < C else ''
            down_s = dp[cr + 1][cc] if cr + 1 < R else ''
            if right_s >= down_s:
                # Move right
                if cc + 1 >= C:
                    can_assign = False
                    break
                cc += 1
            else:
                # Move down
                if cr + 1 >= R:
                    can_assign = False
                    break
                cr += 1
        if can_assign:
            assigned.append(si)
        # If we cannot assign, mark the path cells as unused
        else:
            for cr, cc in path:
                used_cells[cr][cc] = False
    
    # The minimal S_i among assigned robots is the last one in the list
    if assigned:
        answer = assigned[-1]
    else:
        answer = ''  # No robots can be assigned (unlikely in given constraints)
    print(f"Case #{case_num}: {answer}")