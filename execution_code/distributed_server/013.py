import sys
import string
from collections import deque

def readints():
    return list(map(int, sys.stdin.readline().split()))

def to_lower(c):
    return c.lower()

def max_min_tray(R, C, grid, robot_positions):
    # Each robot can move right or down until it deactivates
    # We need to assign a path to each robot such that their tray strings are built accordingly
    # and the min(S_i) is maximized lex
    
    # Initialize tray strings with starting positions
    trays = []
    for r, c in robot_positions:
        trays.append(to_lower(grid[r][c]))
    
    # The problem reduces to finding, for each robot, a path that maximizes its own tray,
    # and then find the min of these trays.
    # To maximize the min, we need to make sure that all trays are as large as possible
    # So we want to make the min tray as large as possible
    
    # A heuristic approach: For each robot, choose the lex largest possible tray
    # Then the min among these is the answer
    
    def get_max_tray(r, c):
        # BFS to get the maximum possible tray starting from (r, c)
        # At each step, prefer higher letters
        # Since moving right or down, the path is determined by choices
        # We choose the path that gives the lex largest string
        tray = to_lower(grid[r][c])
        current_positions = [(r, c, tray)]
        max_tray = ""
        visited = {}
        while current_positions:
            new_positions = []
            temp = {}
            for pos in current_positions:
                r_curr, c_curr, tray_curr = pos
                # Try moving right
                if c_curr + 1 < C:
                    new_tray = tray_curr + to_lower(grid[r_curr][c_curr+1])
                    key = (r_curr, c_curr+1)
                    if key not in temp or new_tray > temp[key]:
                        temp[key] = new_tray
                # Try moving down
                if r_curr + 1 < R:
                    new_tray = tray_curr + to_lower(grid[r_curr+1][c_curr])
                    key = (r_curr+1, c_curr)
                    if key not in temp or new_tray > temp[key]:
                        temp[key] = new_tray
            for key, value in temp.items():
                new_positions.append((key[0], key[1], value))
                if value > max_tray:
                    max_tray = value
            current_positions = new_positions
        return max_tray
    
    # For each robot, get its maximum possible tray
    max_trays = []
    for r, c in robot_positions:
        max_trays.append(get_max_tray(r, c))
    
    # The min of these maximum trays is the lex min we can achieve
    # But we need to find the largest possible min, so it's the min(max_trays)
    return min(max_trays)

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R, C = readints()
        grid = []
        robot_positions = []
        for r in range(R):
            line = sys.stdin.readline().strip()
            grid.append(line)
            for c in range(C):
                if line[c].isupper():
                    robot_positions.append((r, c))
        answer = max_min_tray(R, C, grid, robot_positions)
        print(f"Case #{test_case}: {answer}")

if __name__ == "__main__":
    main()