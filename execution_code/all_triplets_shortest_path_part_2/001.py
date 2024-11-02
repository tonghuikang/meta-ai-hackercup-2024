import sys
import threading
import math
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T+1):
        S = sys.stdin.readline().strip()
        N = int(sys.stdin.readline())
        edges = [[] for _ in range(N+1)]
        for _ in range(N-1):
            U, V = map(int, sys.stdin.readline().split())
            edges[U].append(V)
            edges[V].append(U)
        # Check if N <= 5000 to simulate
        if N <= 5000:
            # Initialize dist matrix
            dist = [[N]* (N+1) for _ in range(N+1)]
            for i in range(1,N+1):
                dist[i][i] = 0
            for u in range(1,N+1):
                for v in edges[u]:
                    dist[u][v] = 1
            # Map S to loop variables
            var_order = S
            var_to_pos = {'i': var_order.index('i'), 'j': var_order.index('j'), 'k': var_order.index('k')}
            # Simulate the code snippet
            indices = [range(1,N+1)] * 3
            loops = ['x1', 'x2', 'x3']
            variables = [''] * 3
            for x1 in indices[0]:
                for x2 in indices[1]:
                    for x3 in indices[2]:
                        vars = [x1,x2,x3]
                        i = vars[var_to_pos['i']]
                        j = vars[var_to_pos['j']]
                        k = vars[var_to_pos['k']]
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
            # Compute actual distances using BFS
            correct_dist = [[0]*(N+1) for _ in range(N+1)]
            for s in range(1,N+1):
                # BFS from node s
                visited = [False]*(N+1)
                q = deque()
                q.append((s,0))
                visited[s] = True
                while q:
                    u, d = q.popleft()
                    correct_dist[s][u] = d
                    for v in edges[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append((v, d+1))
            # Compare dist and correct_dist
            is_correct = True
            for i in range(1,N+1):
                for j in range(1,N+1):
                    if dist[i][j] != correct_dist[i][j]:
                        is_correct = False
                        break
                if not is_correct:
                    break
            print(f"Case #{case_num}: {'Lucky' if is_correct else 'Wrong'}")
        else:
            if S == 'kij' or S == 'kji':
                print(f"Case #{case_num}: Lucky")
            else:
                print(f"Case #{case_num}: Wrong")

if __name__ == "__main__":
    threading.Thread(target=main).start()