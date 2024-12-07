import sys
import sys
import sys
def main():
    import sys
    import sys
    from collections import defaultdict

    sys.setrecursionlimit(10000)

    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(R):
            grid.append(sys.stdin.readline().strip())
        robots = []
        for r in range(R):
            for c in range(C):
                if grid[r][c].isupper():
                    robots.append({'r': r, 'c': c, 's': grid[r][c].lower()})
        T_str = ''
        active_robots = list(robots)
        while True:
            # Find required_moves: robots with S_i == T_str
            required_moves = []
            for robot in active_robots:
                if robot['s'] == T_str:
                    required_moves.append(robot)
            if not required_moves:
                # No robots are exactly matching T_str, can stop
                break
            # Try to append c from 'z' to 'a'
            found = False
            for ci in range(ord('z'), ord('a')-1, -1):
                c = chr(ci)
                # For each required robot, find possible target cells with char >=c
                robot_to_targets = []
                target_set = set()
                for robot in required_moves:
                    moves = []
                    r, c_pos = robot['r'], robot['c']
                    # Move right
                    if c_pos + 1 < C:
                        char = grid[r][c_pos + 1].lower()
                        if char >= c:
                            moves.append( (r, c_pos + 1) )
                    # Move down
                    if r + 1 < R:
                        char = grid[r + 1][c_pos].lower()
                        if char >= c:
                            moves.append( (r + 1, c) )
                    if not moves:
                        break  # This c cannot be used
                    robot_to_targets.append(moves)
                else:
                    # All required robots have at least one move with char >=c
                    # Now, build bipartite graph
                    # Left nodes: required_moves indices
                    # Right nodes: possible target cells
                    # Need to assign unique cells to robots
                    # Assign unique IDs to target cells
                    target_cells = {}
                    cell_list = []
                    for moves in robot_to_targets:
                        for cell in moves:
                            if cell not in target_cells:
                                target_cells[cell] = len(cell_list)
                                cell_list.append(cell)
                    # Build graph
                    graph = [[] for _ in range(len(robot_to_targets))]
                    for i, moves in enumerate(robot_to_targets):
                        for cell in moves:
                            j = target_cells[cell]
                            graph[i].append(j)
                    # Now, find maximum matching
                    match_to = [-1] * len(cell_list)
                    def bpm(u, seen):
                        for v in graph[u]:
                            if not seen[v]:
                                seen[v] = True
                                if match_to[v] == -1 or bpm(match_to[v], seen):
                                    match_to[v] = u
                                    return True
                        return False
                    result = 0
                    for u in range(len(robot_to_targets)):
                        seen = [False] * len(cell_list)
                        if bpm(u, seen):
                            result += 1
                    if result == len(robot_to_targets):
                        # Matching exists, assign c to T_str
                        T_str += c
                        # Now, assign moves to required robots
                        # Reconstruct the matching
                        match_to_final = [-1] * len(cell_list)
                        for u in range(len(robot_to_targets)):
                            seen = [False] * len(cell_list)
                            bpm(u, seen)
                        # Assign moves
                        assigned_cells = {}
                        for v in range(len(cell_list)):
                            u = match_to[v]
                            if u != -1:
                                assigned_cells[u] = cell_list[v]
                        for i, robot in enumerate(required_moves):
                            target = assigned_cells[i]
                            robot['r'], robot['c'] = target
                            robot['s'] += grid[target[0]][target[1]].lower()
                        found = True
                        break
            if not found:
                break
        print(f"Case #{test_case}: {T_str}")

if __name__ == "__main__":
    main()