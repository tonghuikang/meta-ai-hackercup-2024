import sys
import threading
import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    import math
    MOD = 998244353
    from collections import defaultdict

    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, M = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        tree = [[] for _ in range(N)]
        for _ in range(N-1):
            U, V = map(int, sys.stdin.readline().split())
            U -=1
            V -=1
            tree[U].append(V)

        # To handle large M, we need to cap K per node to the depth from node
        # So first, compute depth from each node
        depth = [0]*N
        def dfs_depth(u):
            for v in tree[u]:
                depth[v] = depth[u] +1
                dfs_depth(v)
        dfs_depth(0)

        # Initialize F arrays
        # Since F(S,K) depends on children, process in post-order
        order = []
        visited = [False]*N
        def dfs_order(u):
            visited[u] = True
            for v in tree[u]:
                if not visited[v]:
                    dfs_order(v)
            order.append(u)
        dfs_order(0)

        # Initialize F as list of [0]*(M+1) per node
        # To save space, use list of lists compressed
        # Initialize F as dict with key (u, K)
        # But with constraints, need a better way
        # Instead, for each node, store F as a list up to min(M, depth[u]+1)
        # But still large, proceed with try

        # Initialize F as a list of N lists, each with M+1 elements
        # To save memory, use only necessary K
        # Use a list of lists
        F = [ [0]*(M+1) for _ in range(N) ]

        # Process nodes in post-order
        for u in order:
            if not tree[u]:  # Leaf node
                for k in range(1, M+1):
                    F[u][k] = A[u]
            else:
                min_c_F_K = [math.inf]*(M+1)
                min_c_F_Km1 = [math.inf]*(M+1)
                for v in tree[u]:
                    for k in range(1, M+1):
                        if F[v][k] < min_c_F_K[k]:
                            min_c_F_K[k] = F[v][k]
                    for k in range(0, M):  # K-1 from 1 to M
                        if F[v][k] < min_c_F_Km1[k+1]:
                            min_c_F_Km1[k+1] = F[v][k]
                for k in range(1, M+1):
                    option1 = A[u] + (min_c_F_Km1[k] if min_c_F_Km1[k] != math.inf else 0)
                    option2 = min_c_F_K[k]
                    F[u][k] = max(option1, option2)
        
        # Now compute the sum over all F[u][k]
        total = 0
        for u in range(N):
            max_k = min(M, len(F[u])-1)
            total += sum(F[u][1:max_k+1])
            total %= MOD
        print(f"Case #{test_case}: {total}")

threading.Thread(target=main).start()