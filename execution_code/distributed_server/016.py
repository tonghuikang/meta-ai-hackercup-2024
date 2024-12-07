def solve():
    import sys
    import sys
    sys.setrecursionlimit(1000000)
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        G = []
        for _ in range(R):
            row = sys.stdin.readline().strip()
            G.append(row)
        # Initialize DP table
        S_max = [['' for _ in range(C)] for _ in range(R)]
        # Fill DP table from bottom-right to top-left
        for r in reversed(range(R)):
            for c in reversed(range(C)):
                current_char = G[r][c].lower()
                right = S_max[r][c+1] if c+1 < C else None
                down = S_max[r+1][c] if r+1 < R else None
                # Choose the lex larger between right and down
                if right and down:
                    if right > down:
                        next_part = right
                    else:
                        next_part = down
                elif right:
                    next_part = right
                elif down:
                    next_part = down
                else:
                    next_part = ''
                S_max[r][c] = current_char + next_part
        # Find all robot starting positions (uppercase letters)
        robots = []
        for r in range(R):
            for c in range(C):
                if 'A' <= G[r][c] <= 'Z':
                    robots.append( (r, c) )
        # For each robot, get its S_i_max
        S_i_max_list = []
        for r, c in robots:
            s_max = S_max[r][c]
            S_i_max_list.append(s_max)
        if not S_i_max_list:
            answer = ''
        else:
            # Find the minimal string among S_i_max_list
            answer = min(S_i_max_list)
        print(f"Case #{test_case}: {answer}")

def solve():
    import sys
    import sys
    sys.setrecursionlimit(1000000)
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        G = []
        for _ in range(R):
            row = sys.stdin.readline().strip()
            G.append(row)
        # Initialize DP table
        S_max = [['' for _ in range(C)] for _ in range(R)]
        # Fill DP table from bottom-right to top-left
        for r in reversed(range(R)):
            for c in reversed(range(C)):
                current_char = G[r][c].lower()
                right = S_max[r][c+1] if c+1 < C else None
                down = S_max[r+1][c] if r+1 < R else None
                # Choose the lex larger between right and down
                if right and down:
                    if right > down:
                        next_part = right
                    else:
                        next_part = down
                elif right:
                    next_part = right
                elif down:
                    next_part = down
                else:
                    next_part = ''
                S_max[r][c] = current_char + next_part
        # Find all robot starting positions (uppercase letters)
        robots = []
        for r in range(R):
            for c in range(C):
                if 'A' <= G[r][c] <= 'Z':
                    robots.append( (r, c) )
        # For each robot, get its S_i_max
        S_i_max_list = []
        for r, c in robots:
            s_max = S_max[r][c]
            S_i_max_list.append(s_max)
        if not S_i_max_list:
            answer = ''
        else:
            # Find the minimal string among S_i_max_list
            answer = min(S_i_max_list)
        print(f"Case #{test_case}: {answer}")