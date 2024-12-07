def solve():
    import sys
    import sys
    from collections import defaultdict

    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R,C = map(int, sys.stdin.readline().split())
        grid = []
        robots = []
        for r in range(R):
            line = sys.stdin.readline().strip()
            grid.append(line)
            for c, ch in enumerate(line):
                if 'A' <= ch <= 'Z':
                    robots.append( (r, c) )
        # Initialize dp
        dp = [ ["" for _ in range(C+2)] for __ in range(R+2)]
        for r in range(R, 0, -1):
            for c in range(C, 0, -1):
                cell = grid[r-1][c-1].lower()
                if r == R and c == C:
                    dp[r][c] = cell
                else:
                    down = dp[r+1][c] if r < R else ""
                    right = dp[r][c+1] if c < C else ""
                    if down and right:
                        if down > right:
                            dp[r][c] = cell + down
                        else:
                            dp[r][c] = cell + right
                    elif down:
                        dp[r][c] = cell + down
                    elif right:
                        dp[r][c] = cell + right
                    else:
                        dp[r][c] = cell
        s_i_max = []
        for (r, c) in robots:
            s_i_max.append(dp[r+1][c+1])
        if not s_i_max:
            x = ""
        else:
            x = min(s_i_max)
        print(f"Case #{test_case}: {x}")

def solve():
    import sys
    import sys
    from collections import defaultdict

    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R,C = map(int, sys.stdin.readline().split())
        grid = []
        robots = []
        for r in range(R):
            line = sys.stdin.readline().strip()
            grid.append(line)
            for c, ch in enumerate(line):
                if 'A' <= ch <= 'Z':
                    robots.append( (r, c) )
        # Initialize dp
        dp = [ ["" for _ in range(C+2)] for __ in range(R+2)]
        for r in range(R, 0, -1):
            for c in range(C, 0, -1):
                cell = grid[r-1][c-1].lower()
                if r == R and c == C:
                    dp[r][c] = cell
                else:
                    down = dp[r+1][c] if r < R else ""
                    right = dp[r][c+1] if c < C else ""
                    if down and right:
                        if down > right:
                            dp[r][c] = cell + down
                        else:
                            dp[r][c] = cell + right
                    elif down:
                        dp[r][c] = cell + down
                    elif right:
                        dp[r][c] = cell + right
                    else:
                        dp[r][c] = cell
        s_i_max = []
        for (r, c) in robots:
            s_i_max.append(dp[r+1][c+1])
        if not s_i_max:
            x = ""
        else:
            x = min(s_i_max)
        print(f"Case #{test_case}: {x}")