import sys
import threading
sys.setrecursionlimit(1 << 25)

MOD = 998244353

def main():
    import sys
    import math

    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N, M = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        A = [0] + A  # 1-indexed

        tree = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            u, v = map(int, sys.stdin.readline().split())
            tree[u].append(v)

        # Initialize data structures
        minA = [0] * (N + 1)
        minChild = [0] * (N + 1)
        pathID = [0] * (N + 1)
        posInPath = [0] * (N + 1)
        paths = []
        pathSum = []
        
        def dfs(node):
            minA[node] = A[node]
            min_child = 0
            for child in tree[node]:
                dfs(child)
                if minA[child] < minA[node]:
                    minA[node] = minA[child]
                    min_child = child
            minChild[node] = min_child

        dfs(1)

        path_counter = 0
        def decompose(node):
            nonlocal path_counter
            path = []
            curr_node = node
            while True:
                pathID[curr_node] = path_counter
                posInPath[curr_node] = len(path)
                path.append(curr_node)
                if minChild[curr_node]:
                    curr_node = minChild[curr_node]
                else:
                    break
            # compute cumulative sums along the path
            cumsum = [0]
            for idx in range(len(path)):
                cumsum.append(cumsum[-1] + A[path[idx]])
            paths.append(path)
            pathSum.append(cumsum)
            path_counter += 1
            for child in tree[node]:
                if child != minChild[node]:
                    decompose(child)

        decompose(1)

        total_sum = 0
        for S in range(1, N + 1):
            pid = pathID[S]
            pos = posInPath[S]
            cumsum = pathSum[pid]
            max_len = len(cumsum) - 1
            maxK = min(M, max_len - pos)
            # Since we need to sum over K = 1 to M
            # For K from 1 to maxK
            # total_sum += sum of cumsum[pos + K] - cumsum[pos]
            # But we can precompute this as:
            # F_S = sum_{k=1}^{maxK} (cumsum[pos + k] - cumsum[pos])
            #     = cumsum[pos + 1] - cumsum[pos] + cumsum[pos + 2] - cumsum[pos] + ... + cumsum[pos + maxK] - cumsum[pos]
            #     = (cumsum[pos + 1] + ... + cumsum[pos + maxK]) - maxK * cumsum[pos]
            # But cumsum[pos + 1] + ... + cumsum[pos + maxK] = cumsum[pos + maxK] - cumsum[pos]
            # So total_sum += (cumsum[pos + maxK] - cumsum[pos]) - maxK * cumsum[pos]
            # Wait, this doesn't help. We need to compute sum_{k=1}^{maxK} (cumsum[pos + k] - cumsum[pos])
            # Which is equal to (sum_{k=1}^{maxK} cumsum[pos + k]) - maxK * cumsum[pos]

            # Alternatively, we can precompute the sum of treasures for K from 1 to maxK

            for K in range(1, M + 1):
                if pos + K <= max_len:
                    total_sum += cumsum[pos + K] - cumsum[pos]
                else:
                    total_sum += cumsum[-1] - cumsum[pos]
                if total_sum >= MOD:
                    total_sum -= MOD

        print(f'Case #{case_num}: {total_sum % MOD}')

threading.Thread(target=main).start()