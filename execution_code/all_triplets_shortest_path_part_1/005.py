import sys
import threading
import sys

def main():
    import sys
    import sys
    import threading

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N = int(sys.stdin.readline())
        adj = [[] for _ in range(N + 1)]
        for _ in range(N -1):
            u,v = map(int, sys.stdin.readline().split())
            adj[u].append(v)
            adj[v].append(u)

        from collections import deque
        parent = [0] * (N + 1)  # parent[u] = parent of u in BFS
        visited = [False] * (N +1)
        q = deque()
        q.append(1)
        visited[1] = True
        is_lucky = True

        while q and is_lucky:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    visited[v] = True
                    if v >= u:
                        q.append(v)
                    else:
                        # labels decreasing along the path
                        is_lucky = False
                        break
        result = "Lucky" if is_lucky else "Wrong"
        print(f"Case #{case_num}: {result}")

threading.Thread(target=main).start()