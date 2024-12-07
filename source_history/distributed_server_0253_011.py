import sys
import sys
import math
from collections import deque
from copy import deepcopy

def readints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        G = [sys.stdin.readline().strip() for _ in range(R)]
        # Find all robots
        robots = []
        for r in range(R):
            for c in range(C):
                if 'A' <= G[r][c] <= 'Z':
                    robots.append((r, c))
        # Now, for each robot, we need to find possible paths
        # To maximize the min(S_i), we need to find the lex min string across all robots to be as high as possible
        # We'll build the minimal string character by character
        # At each step, choose the highest possible next character that all robots can achieve
        # This is similar to finding the minimal among all S_i and maximize it
        # Initialize for each robot the possible positions and their current strings
        # To simplify, let's assume each robot takes the lex highest path possible
        # Then the min(S_i) will be the min among these
        # So for each robot, find the lex highest path
        # Then take the min of these paths
        # To find lex highest path, prefer 'z' over 'a', etc.
        # So, for each robot, perform a BFS choosing the highest possible letters first
        def get_lex_highest_path(r, c):
            path = [G[r][c].lower()]
            while r < R-1 or c < C-1:
                options = []
                if r < R-1:
                    options.append((G[r+1][c].lower(), r+1, c))
                if c < C-1:
                    options.append((G[r][c+1].lower(), r, c+1))
                if not options:
                    break
                # Choose the option with the highest character
                options.sort(reverse=True)
                chosen = options[0]
                path.append(chosen[0])
                r, c = chosen[1], chosen[2]
            return ''.join(path)
        paths = []
        for r, c in robots:
            paths.append(get_lex_highest_path(r, c))
        if paths:
            min_path = min(paths)
        else:
            min_path = ''
        print(f"Case #{tc}: {min_path}")

if __name__ == "__main__":
    main()