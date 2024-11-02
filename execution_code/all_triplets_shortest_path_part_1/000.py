import sys
import sys
import sys
import sys
import sys
import sys
from collections import deque

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    T = int(data[ptr]); ptr +=1
    for test_case in range(1, T+1):
        N = int(data[ptr]); ptr +=1
        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u = int(data[ptr]); ptr +=1
            v = int(data[ptr]); ptr +=1
            adj[u].append(v)
            adj[v].append(u)
        # Find the node with the minimal label
        min_label = 1
        # Perform BFS from min_label
        visited = [False] * (N+1)
        parent = [0] * (N+1)
        queue = deque()
        queue.append(min_label)
        visited[min_label] = True
        is_correct = True
        while queue and is_correct:
            current = queue.popleft()
            for neighbor in adj[current]:
                if not visited[neighbor]:
                    if neighbor <= current:
                        is_correct = False
                        break
                    parent[neighbor] = current
                    visited[neighbor] = True
                    queue.append(neighbor)
                else:
                    if neighbor != parent[current]:
                        if neighbor < current:
                            is_correct = False
                            break
        if is_correct:
            # Additionally, ensure all nodes were visited
            if all(visited[1:]):
                print(f"Case #{test_case}: Lucky")
            else:
                print(f"Case #{test_case}: Wrong")
        else:
            print(f"Case #{test_case}: Wrong")

if __name__ == "__main__":
    main()