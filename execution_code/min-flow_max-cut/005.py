import sys
import threading
import math
from collections import defaultdict

sys.setrecursionlimit(1 << 25)

MOD = 998244353

def main():
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N, M = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        adj = [[] for _ in range(N)]
        for _ in range(N - 1):
            U, V = map(int, sys.stdin.readline().split())
            U -= 1
            V -= 1
            adj[U].append(V)

        # Build minimal paths and compute prefix sums along them
        paths = []
        node_to_path = [None] * N
        path_positions = [None] * N

        def dfs(u):
            # If leaf node
            if not adj[u]:
                path = [u]
                node_to_path[u] = len(paths)
                path_positions[u] = 0
                paths.append([A[u]])
                return (A[u], u)
            min_total = float('inf')
            min_child = None
            for v in adj[u]:
                total, _ = dfs(v)
                if total < min_total:
                    min_total = total
                    min_child = v
            # Build the minimal path
            node_to_path[u] = node_to_path[min_child]
            path_positions[u] = path_positions[min_child] - 1
            paths[node_to_path[u]].insert(0, A[u])
            return (A[u] + min_total, u)

        for u in range(N):
            if node_to_path[u] is None:
                dfs(u)

        # For each path, compute prefix sums
        path_prefix_sums = []
        for path in paths:
            prefix_sum = [0]
            for val in path:
                prefix_sum.append(prefix_sum[-1] + val)
            path_prefix_sums.append(prefix_sum)

        total_sum = 0
        for S in range(N):
            path_idx = node_to_path[S]
            pos = path_positions[S]
            length = len(paths[path_idx]) - pos
            prefix_sum = path_prefix_sums[path_idx]
            for K in range(1, min(M, length) +1):
                sum_K = prefix_sum[pos + K] - prefix_sum[pos]
                total_sum = (total_sum + sum_K) % MOD

        print(f"Case #{case_num}: {total_sum}")

threading.Thread(target=main).start()