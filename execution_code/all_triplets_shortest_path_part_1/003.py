import sys
import sys
import sys
def main():
    import sys
    import sys
    from collections import deque
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test in range(1, T+1):
        N = int(data[idx]); idx +=1
        adj = [[] for _ in range(N+1)]
        degree = [0]*(N+1)
        for _ in range(N-1):
            u = int(data[idx]); v = int(data[idx+1]); idx +=2
            adj[u].append(v)
            adj[v].append(u)
            degree[u] +=1
            degree[v] +=1
        if N ==1:
            centers = [1]
        else:
            # Initialize leaves
            q = deque()
            for i in range(1,N+1):
                if degree[i] <=1:
                    q.append(i)
            remaining = N
            while remaining >2:
                leaves_count = len(q)
                remaining -= leaves_count
                for _ in range(leaves_count):
                    leaf = q.popleft()
                    for neighbor in adj[leaf]:
                        degree[neighbor] -=1
                        if degree[neighbor] ==1:
                            q.append(neighbor)
            centers = list(q)
        if len(centers)==1:
            result = "Lucky"
        else:
            result = "Wrong"
        print(f"Case #{test}: {result}")
                

if __name__ == "__main__":
    main()

import sys
import sys
import sys
def main():
    import sys
    import sys
    from collections import deque
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test in range(1, T+1):
        N = int(data[idx]); idx +=1
        adj = [[] for _ in range(N+1)]
        degree = [0]*(N+1)
        for _ in range(N-1):
            u = int(data[idx]); v = int(data[idx+1]); idx +=2
            adj[u].append(v)
            adj[v].append(u)
            degree[u] +=1
            degree[v] +=1
        if N ==1:
            centers = [1]
        else:
            # Initialize leaves
            q = deque()
            for i in range(1,N+1):
                if degree[i] <=1:
                    q.append(i)
            remaining = N
            while remaining >2:
                leaves_count = len(q)
                remaining -= leaves_count
                for _ in range(leaves_count):
                    leaf = q.popleft()
                    for neighbor in adj[leaf]:
                        degree[neighbor] -=1
                        if degree[neighbor] ==1:
                            q.append(neighbor)
            centers = list(q)
        if len(centers)==1:
            result = "Lucky"
        else:
            result = "Wrong"
        print(f"Case #{test}: {result}")
                

if __name__ == "__main__":
    main()