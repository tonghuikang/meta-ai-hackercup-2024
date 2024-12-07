import sys
import sys
import sys
def readints():
    return list(map(int, sys.stdin.readline().split()))

from collections import deque
import sys

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        G = [sys.stdin.readline().strip() for _ in range(R)]
        # Identify robots
        robots = []
        for r in range(R):
            for c in range(C):
                if G[r][c].isupper():
                    robots.append( (r, c) )
        # Function to get all possible paths for a robot
        # Due to constraints, we cannot enumerate all paths. So instead, for each robot, find the lex smallest path
        # But we need to maximize the min(S_i), which implies we need to find the lex smallest S_i as large as possible
        # A heuristic approach: find for each robot the lex smallest S_i, then take the min
        # Then, the max over possible S_i min is the answer
        # Alternatively, find for each robot the lex smallest S_i, and take the min
        # But sample suggests more complex behavior
        # Let's instead for each robot, find the lex smallest S_i
        # And then take the min of those
        # To maximize the min(S_i), we need to maximize the min over robots' S_i
        # So alternatively, choose for each robot the lex largest S_i, and the min of those
        # Let us try to choose for each robot the lex largest possible S_i
        # Then, the min(S_i) will be the smallest of these lex largest
        # To find lex largest S_i for a robot, choose to move in the direction with higher letters first
        # Implement for each robot, find the lex largest S_i
        def get_lex_largest(r, c):
            visited = {}
            memo = {}
            def dfs(r, c):
                if (r, c) in memo:
                    return memo[(r,c)]
                s = G[r][c].lower()
                paths = []
                if r+1 < R:
                    paths.append( s + dfs(r+1, c) )
                if c+1 < C:
                    paths.append( s + dfs(r, c+1) )
                if not paths:
                    result = s
                else:
                    result = max(paths)
                memo[(r,c)] = result
                return result
            return G[r][c] + dfs(r,c)
        # Now get all robots' lex largest S_i
        S_list = [get_lex_largest(r,c) for r,c in robots]
        # The min(S_i) is the minimal string in lex order
        min_S = min(S_list)
        print(f"Case #{test_case}: {min_S.lower()}")
        
if __name__ == "__main__":
    main()