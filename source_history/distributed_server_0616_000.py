import sys
import sys
from collections import deque
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def solve_case(R, C, grid):
    robots = []
    for r in range(R):
        for c in range(C):
            if grid[r][c].isupper():
                robots.append((r, c))
    # Precompute lower case grid
    lower_grid = [[cell.lower() for cell in row] for row in grid]
    
    # Function to check if a robot can follow a path starting with s + c
    def can_robot_follow(r, c, s, next_c):
        # BFS where we need to follow s and then have next_c
        queue = deque()
        queue.append((r, c, 0))  # position and index in s
        visited = set()
        while queue:
            cr, cc, idx = queue.popleft()
            if (cr, cc, idx) in visited:
                continue
            visited.add((cr, cc, idx))
            if idx < len(s):
                # Need to match the current character in s
                if lower_grid[cr][cc] != s[idx]:
                    continue
                next_idx = idx + 1
                if next_idx == len(s):
                    # Next step needs to be >= next_c
                    for dr, dc in [(0,1),(1,0)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < R and 0 <= nc < C:
                            if lower_grid[nr][nc] >= next_c:
                                return True
                queue.append((cr, cc, next_idx))
            elif idx == len(s):
                # Now we need to have next_c
                if lower_grid[cr][cc] < next_c:
                    continue
                return True
            else:
                # Already beyond s + c
                return True
        return False
    
    # Initialize s
    s = ""
    while True:
        found = False
        for c_ord in range(ord('z'), ord('a')-1, -1):
            c = chr(c_ord)
            # Check for all robots
            flag = True
            for r, c_start in robots:
                # Each robot's path needs to have s + c as a prefix
                # Implement BFS to see if s + c can be a prefix
                need = s + c
                queue = deque()
                queue.append((r, c_start, 1))  # position and index in need
                visited = set()
                # Check first character
                if lower_grid[r][c_start] != s[:1] if s else True:
                    if not s:
                        if lower_grid[r][c_start] < c:
                            flag = False
                            break
                    # else, s is not empty
                # Now, perform BFS to check if need can be a prefix
                # To simplify, we check if the robot can collect need as a prefix
                # Implement DFS/BFS
                queue = deque()
                queue.append((r, c_start, 0))
                success = False
                visited = set()
                while queue:
                    cr, cc, idx = queue.popleft()
                    if (cr, cc, idx) in visited:
                        continue
                    visited.add((cr, cc, idx))
                    if idx < len(s):
                        if lower_grid[cr][cc] != s[idx]:
                            continue
                        next_idx = idx + 1
                        for dr, dc in [(0,1),(1,0)]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < R and 0 <= nc < C:
                                queue.append((nr, nc, next_idx))
                    elif idx == len(s):
                        # Need to have next character >=c
                        for dr, dc in [(0,1),(1,0)]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < R and 0 <= nc < C:
                                if lower_grid[nr][nc] >= c:
                                    success = True
                                    break
                                queue.append((nr, nc, idx))
                        if success:
                            break
                if not success:
                    flag = False
                    break
            if flag:
                s += c
                found = True
                break
        if not found:
            break
    return s

def main():
    import sys
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(R):
            row = sys.stdin.readline().strip()
            grid.append(row)
        result = solve_case(R, C, grid)
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()