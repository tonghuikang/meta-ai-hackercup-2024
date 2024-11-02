import sys
import threading
from collections import deque

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u = int(data[idx]); v = int(data[idx+1]); idx +=2
            adj[u].append(v)
            adj[v].append(u)
        # BFS from node1
        visited = [False]*(N+1)
        queue = deque()
        queue.append(1)
        visited[1] = True
        is_correct = True
        while queue and is_correct:
            current = queue.popleft()
            for neighbor in adj[current]:
                if not visited[neighbor]:
                    if neighbor < current:
                        is_correct = False
                        break
                    visited[neighbor] = True
                    queue.append(neighbor)
        result = "Lucky" if is_correct else "Wrong"
        print(f"Case #{test_case}: {result}")

threading.Thread(target=main,).start()