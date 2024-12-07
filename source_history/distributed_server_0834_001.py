import sys
import threading
from collections import deque

def main():
    import sys

    import sys

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T +1):
        R, C = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(R):
            line = sys.stdin.readline().strip()
            grid.append(line)
        capitals = []
        for r in range(R):
            for c in range(C):
                if grid[r][c].isupper():
                    capitals.append((r, c))
        # Precompute dp[r][c] which is lex max path from (r,c) to bottom-right
        dp = [[ '' for _ in range(C+1)] for _ in range(R+1)]
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                lower_char = grid[r][c].lower()
                option1 = dp[r+1][c] if r+1 < R+1 else ''
                option2 = dp[r][c+1] if c+1 < C+1 else ''
                if option1 > option2:
                    dp[r][c] = lower_char + option1
                else:
                    dp[r][c] = lower_char + option2
        # For each robot starting position, get their lex max S_i
        robots = []
        for idx, (r, c) in enumerate(capitals):
            start_Si = dp[r][c]
            robots.append({'idx': idx, 'start_r': r, 'start_c': c, 'max_Si': start_Si})
        # Sort robots by their lex max S_i decreasing
        robots.sort(key=lambda x: x['max_Si'], reverse=True)
        occupied_positions = {}
        global_max_Si = ""
        robot_Si_list = ['' for _ in robots]
        for robot in robots:
            r0, c0 = robot['start_r'], robot['start_c']
            idx = robot['idx']
            visited = {}
            from collections import deque
            queue = deque()
            initial_Si = grid[r0][c0].lower()
            queue.append((r0, c0, 0, initial_Si))
            visited[(r0,c0,0)] = initial_Si
            max_Si = ''
            path_found = False
            # We will keep the previous positions occupied by previous robots
            # We need to avoid positions in occupied_positions[time]
            # Our goal is to find the path with lex max S_i avoiding conflicts
            while queue:
                curr_r, curr_c, t, curr_Si = queue.popleft()
                # Check if this position is occupied at time t
                pos = (curr_r, curr_c)
                if occupied_positions.get(t, set()) & {pos}:
                    continue
                # If we have reached further S_i, update max_Si
                if curr_Si > max_Si:
                    max_Si = curr_Si
                elif curr_Si == max_Si:
                    path_found = True
                # Try to move down or right
                for dr, dc in [(1,0), (0,1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    nt = t +1
                    if 0 <= nr < R and 0 <= nc < C:
                        npos = (nr,nc)
                        if occupied_positions.get(nt, set()) & {npos}:
                            continue
                        lower_char = grid[nr][nc].lower()
                        n_Si = curr_Si + lower_char
                        state = (nr,nc, nt)
                        if state not in visited or visited[state] < n_Si:
                            visited[state] = n_Si
                            queue.append((nr, nc, nt, n_Si))
            # After BFS, get the lex max S_i found
            robot_Si_list[idx] = max_Si
            # Now, reconstruct path to update occupied_positions
            # For simplicity, we can perform BFS again, but now keep track of path
            queue = deque()
            visited = {}
            queue.append((r0, c0, 0, grid[r0][c0].lower(), []))
            visited[(r0,c0,0)] = grid[r0][c0].lower()
            found = False
            while queue and not found:
                curr_r, curr_c, t, curr_Si, path = queue.popleft()
                pos = (curr_r, curr_c)
                if occupied_positions.get(t, set()) & {pos}:
                    continue
                if curr_Si == max_Si:
                    # Found the path
                    path.append((curr_r, curr_c, t))
                    found = True
                    # Update occupied_positions
                    for r, c, time in path:
                        if time not in occupied_positions:
                            occupied_positions[time] = set()
                        occupied_positions[time].add((r,c))
                    break
                # Append current position to path
                path_next = path + [(curr_r, curr_c, t)]
                for dr, dc in [(1,0), (0,1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    nt = t +1
                    if 0 <= nr < R and 0 <= nc < C:
                        npos = (nr,nc)
                        if occupied_positions.get(nt, set()) & {npos}:
                            continue
                        lower_char = grid[nr][nc].lower()
                        n_Si = curr_Si + lower_char
                        state = (nr,nc, nt)
                        if state not in visited or visited[state] < n_Si:
                            visited[state] = n_Si
                            queue.append((nr, nc, nt, n_Si, path_next))
            if not found:
                # Could not find path to achieve max_Si avoiding collisions
                # This should not happen as per the constraints of the problem
                # But if it does, we might need to adjust, but the problem seems to allow achieving max_Si
                pass
        # The minimal S_i among robots is our answer
        answer = min(robot_Si_list)
        print(f"Case #{case_num}: {answer}")

if __name__ == '__main__':
    threading.Thread(target=main).start()