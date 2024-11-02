import sys
import threading
sys.setrecursionlimit(1 << 25)

def main():
    mod = 998244353
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N, M = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        tree = [[] for _ in range(N)]
        for _ in range(N - 1):
            U, V = map(int, sys.stdin.readline().split())
            U -= 1
            V -= 1
            tree[U].append(V)  # Since rivers are unidirectional from U to V
        total_sum_over_K = [0] * N
        len_path = [0] * N
        f = [0] * N
        visited = [False] * N

        def dfs(v):
            visited[v] = True
            A_v = A[v]
            if not tree[v]:  # Leaf node
                len_path[v] = 1
                total_sum_over_K[v] = A_v * M
                f[v] = A_v * (M - 1)
            else:
                u_worst = None
                min_f_u = None
                for u in tree[v]:
                    if not visited[u]:
                        dfs(u)
                    f_u = f[u]
                    if min_f_u is None or f_u < min_f_u:
                        min_f_u = f_u
                        u_worst = u
                len_path[v] = len_path[u_worst] + 1
                total_sum_over_K[v] = total_sum_over_K[u_worst] + A_v * (M - len_path[u_worst])
                f[v] = f[u_worst] - A_v
        # Since the rivers flow downstream from node 1, we need to ensure
        # that all nodes are visited (in case of multiple downstream nodes from the root)
        for i in range(N):
            if not visited[i]:
                dfs(i)
        result = sum(total_sum_over_K) % mod
        print(f'Case #{case_num}: {result}')

threading.Thread(target=main).start()