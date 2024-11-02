import sys
import threading
from collections import deque

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T +1):
        N = int(sys.stdin.readline())
        adj = [[] for _ in range(N +1)]
        for _ in range(N -1):
            u, v = map(int, sys.stdin.readline().split())
            adj[u].append(v)
            adj[v].append(u)
        # BFS from node1
        queue = deque()
        queue.append(1)
        visited = [False] * (N +1)
        visited[1] = True
        is_lucky = True
        while queue and is_lucky:
            current = queue.popleft()
            for neighbor in adj[current]:
                if not visited[neighbor]:
                    if neighbor <= current:
                        is_lucky = False
                        break
                    visited[neighbor] = True
                    queue.append(neighbor)
        if is_lucky:
            print(f"Case #{test_case}: Lucky")
        else:
            print(f"Case #{test_case}: Wrong")

threading.Thread(target=main).start()