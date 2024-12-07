def solve():
    import sys
    import sys
    from sys import stdin
    import sys
    def input():
        return sys.stdin.read()
    
    data = input().splitlines()
    T = int(data[0])
    idx = 1
    for test_case in range(1, T+1):
        R_C = data[idx].strip().split()
        R = int(R_C[0])
        C = int(R_C[1])
        idx +=1
        grid = []
        for _ in range(R):
            grid.append(data[idx].strip())
            idx +=1
        # Find robot positions
        robots = []
        for r in range(R):
            for c in range(C):
                if 'A' <= grid[r][c] <= 'Z':
                    robots.append( (r, c) )
        # Build grid in lowercase
        lower_grid = [ list(row.lower()) for row in grid ]
        # Initialize dp table
        dp = [ [''] * C for _ in range(R) ]
        for r in reversed(range(R)):
            for c in reversed(range(C)):
                current_char = lower_grid[r][c]
                if r == R-1 and c == C-1:
                    dp[r][c] = current_char
                else:
                    s_down = s_right = ''
                    if r < R-1:
                        s_down = current_char + dp[r+1][c]
                    if c < C-1:
                        s_right = current_char + dp[r][c+1]
                    if s_down and s_right:
                        dp[r][c] = max(s_down, s_right)
                    elif s_down:
                        dp[r][c] = s_down
                    elif s_right:
                        dp[r][c] = s_right
                    else:
                        dp[r][c] = current_char
        # Get S_i for each robot
        s_i_list = []
        for r, c in robots:
            s_i_list.append( dp[r][c] )
        if s_i_list:
            min_S_i = min(s_i_list)
        else:
            min_S_i = ""
        print(f"Case #{test_case}: {min_S_i}")

def solve():
    import sys
    import sys
    from sys import stdin
    import sys
    def input():
        return sys.stdin.read()
    
    data = input().splitlines()
    T = int(data[0])
    idx = 1
    for test_case in range(1, T+1):
        R_C = data[idx].strip().split()
        R = int(R_C[0])
        C = int(R_C[1])
        idx +=1
        grid = []
        for _ in range(R):
            grid.append(data[idx].strip())
            idx +=1
        # Find robot positions
        robots = []
        for r in range(R):
            for c in range(C):
                if 'A' <= grid[r][c] <= 'Z':
                    robots.append( (r, c) )
        # Build grid in lowercase
        lower_grid = [ list(row.lower()) for row in grid ]
        # Initialize dp table
        dp = [ [''] * C for _ in range(R) ]
        for r in reversed(range(R)):
            for c in reversed(range(C)):
                current_char = lower_grid[r][c]
                if r == R-1 and c == C-1:
                    dp[r][c] = current_char
                else:
                    s_down = s_right = ''
                    if r < R-1:
                        s_down = current_char + dp[r+1][c]
                    if c < C-1:
                        s_right = current_char + dp[r][c+1]
                    if s_down and s_right:
                        dp[r][c] = max(s_down, s_right)
                    elif s_down:
                        dp[r][c] = s_down
                    elif s_right:
                        dp[r][c] = s_right
                    else:
                        dp[r][c] = current_char
        # Get S_i for each robot
        s_i_list = []
        for r, c in robots:
            s_i_list.append( dp[r][c] )
        if s_i_list:
            min_S_i = min(s_i_list)
        else:
            min_S_i = ""
        print(f"Case #{test_case}: {min_S_i}")