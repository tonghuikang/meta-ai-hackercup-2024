import sys
import sys
import sys
from collections import defaultdict, deque

def readints():
    return list(map(int, sys.stdin.readline().split()))

class HopcroftKarp:
    def __init__(self, graph, num_left, num_right):
        self.graph = graph
        self.num_left = num_left
        self.num_right = num_right
        self.pair_left = [-1] * num_left
        self.pair_right = [-1] * num_right
        self.dist = [0] * num_left

    def bfs(self):
        queue = deque()
        for u in range(self.num_left):
            if self.pair_left[u] == -1:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        dist_found = float('inf')
        while queue:
            u = queue.popleft()
            if self.dist[u] < dist_found:
                for v in self.graph[u]:
                    if self.pair_right[v] == -1:
                        dist_found = self.dist[u] + 1
                    elif self.dist[self.pair_right[v]] == float('inf'):
                        self.dist[self.pair_right[v]] = self.dist[u] + 1
                        queue.append(self.pair_right[v])
        return dist_found != float('inf')

    def dfs(self, u):
        for v in self.graph[u]:
            if self.pair_right[v] == -1 or (self.dist[self.pair_right[v]] == self.dist[u] + 1 and self.dfs(self.pair_right[v])):
                self.pair_left[u] = v
                self.pair_right[v] = u
                return True
        self.dist[u] = float('inf')
        return False

    def max_matching(self):
        matching = 0
        while self.bfs():
            for u in range(self.num_left):
                if self.pair_left[u] == -1:
                    if self.dfs(u):
                        matching += 1
        return matching

def main():
    import sys
    sys.setrecursionlimit(1000000)
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        G = []
        robots = []
        for r in range(R):
            line = sys.stdin.readline().strip()
            row = []
            for c, ch in enumerate(line):
                if 'A' <= ch <= 'Z':
                    robots.append( (r, c) )
                    row.append(ch.lower())
                else:
                    row.append(ch)
            G.append(row)
        num_robots = len(robots)
        robot_positions = robots.copy()
        T_str = ""
        while True:
            ch_found = False
            for ch_ord in range(ord('z'), ord('a')-1, -1):
                ch = chr(ch_ord)
                # For each robot, find possible next cells with char >= ch
                robot_options = []
                possible_cells = set()
                for idx, (r, c) in enumerate(robot_positions):
                    options = []
                    if r + 1 < R:
                        cell_char = G[r+1][c]
                        if cell_char >= ch:
                            options.append( (r+1, c) )
                    if c + 1 < C:
                        cell_char = G[r][c+1]
                        if cell_char >= ch:
                            options.append( (r, c+1) )
                    robot_options.append(options)
                # Check if all robots have at least one option
                feasible = True
                for opts in robot_options:
                    if not opts:
                        feasible = False
                        break
                if not feasible:
                    continue
                # Now, need to assign unique cells to robots
                # Assign indices to unique cells
                cell_mapping = {}
                cell_list = []
                cell_id = 0
                for opts in robot_options:
                    for cell in opts:
                        if cell not in cell_mapping:
                            cell_mapping[cell] = cell_id
                            cell_list.append(cell)
                            cell_id += 1
                num_cells = len(cell_list)
                # Build graph
                graph = [[] for _ in range(num_robots)]
                for u in range(num_robots):
                    for cell in robot_options[u]:
                        v = cell_mapping[cell]
                        graph[u].append(v)
                # Perform Hopcroft-Karp
                hk = HopcroftKarp(graph, num_robots, num_cells)
                matching = hk.max_matching()
                if matching == num_robots:
                    # Assign cells based on matching
                    new_positions = [ (-1, -1) ] * num_robots
                    for u in range(num_robots):
                        v = hk.pair_left[u]
                        cell = cell_list[v]
                        new_positions[u] = cell
                    # Update robot positions
                    robot_positions = new_positions
                    # Append ch to T_str
                    T_str += ch
                    ch_found = True
                    break
            if not ch_found:
                break
        print(f"Case #{test_case}: {T_str}")

if __name__ == "__main__":
    main()