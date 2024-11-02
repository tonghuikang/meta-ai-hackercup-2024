import sys
import sys
import sys
from collections import deque

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr]); ptr +=1
    for test_case in range(1, T+1):
        N = int(input[ptr]); ptr +=1
        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            U = int(input[ptr]); ptr +=1
            V = int(input[ptr]); ptr +=1
            adj[U].append(V)
            adj[V].append(U)
        # BFS from node1
        levels = [ -1 ] * (N+1)
        q = deque()
        q.append(1)
        levels[1] =0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if levels[v]==-1:
                    levels[v] = levels[u] +1
                    q.append(v)
        # Check if levels are non-decreasing in label order
        is_lucky = True
        prev_level = -1
        for node in range(1, N+1):
            current_level = levels[node]
            if current_level < prev_level:
                is_lucky = False
                break
            prev_level = current_level
        result = "Lucky" if is_lucky else "Wrong"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()

import sys
import sys
from collections import deque

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr]); ptr +=1
    for test_case in range(1, T+1):
        N = int(input[ptr]); ptr +=1
        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            U = int(input[ptr]); ptr +=1
            V = int(input[ptr]); ptr +=1
            adj[U].append(V)
            adj[V].append(U)
        # BFS from node1
        levels = [ -1 ] * (N+1)
        q = deque()
        q.append(1)
        levels[1] =0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if levels[v]==-1:
                    levels[v] = levels[u] +1
                    q.append(v)
        # Check if levels are non-decreasing in label order
        is_lucky = True
        prev_level = -1
        for node in range(1, N+1):
            current_level = levels[node]
            if current_level < prev_level:
                is_lucky = False
                break
            prev_level = current_level
        result = "Lucky" if is_lucky else "Wrong"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()