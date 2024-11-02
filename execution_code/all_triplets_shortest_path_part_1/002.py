import sys
import threading

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            u, v = map(int, sys.stdin.readline().split())
            adj[u].append(v)
            adj[v].append(u)
        # Choose root as N
        root = N
        subtree_min = [N + 1] * (N + 1)
        parent = [0] * (N + 1)
        has_wrong = False
        def dfs(u, p):
            nonlocal has_wrong
            subtree_min[u] = u
            count = 0
            for v in adj[u]:
                if v != p:
                    parent[v] = u
                    dfs(v, u)
                    if subtree_min[v] < u:
                        count +=1
                    subtree_min[u] = min(subtree_min[u], subtree_min[v])
            if count >=2:
                has_wrong = True
        dfs(root, -1)
        print(f"Case #{test_case}: {'Wrong' if has_wrong else 'Lucky'}")
        

threading.Thread(target=main).start()