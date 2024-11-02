import sys
import threading

MOD = 998244353

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, M = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        tree = [[] for _ in range(N)]
        parent = [ -1]*N
        for _ in range(N-1):
            U, V = map(int, sys.stdin.readline().split())
            U -=1
            V -=1
            tree[U].append(V)
            parent[V] = U
        # Find root
        root = 0
        # DP array: for each node, store F[k] from 0 to M
        # To save memory, use only one array and overwrite
        # Initialize F for all nodes as empty
        F = [ [0]*(M+1) for _ in range(N)]
        # Post-order traversal
        order = []
        stack = [root]
        visited = [False]*N
        while stack:
            node = stack[-1]
            if not visited[node]:
                visited[node] = True
                for child in tree[node]:
                    stack.append(child)
            else:
                stack.pop()
                order.append(node)
        # Now process in post-order
        for node in order:
            if not tree[node]:  # Leaf
                F[node][0] = 0
                for k in range(1, M+1):
                    F[node][k] = A[node]
            else:
                # Compute min_child F(child,k) for all k
                minF = [float('inf')] * (M+1)
                for child in tree[node]:
                    for k in range(M+1):
                        if F[child][k] < minF[k]:
                            minF[k] = F[child][k]
                # Now compute F[node][k]
                F[node][0] = minF[0]
                for k in range(1, M+1):
                    collect = A[node] + (minF[k-1] if k-1 >=0 else 0)
                    not_collect = minF[k]
                    F[node][k] = max(collect, not_collect)
        # Now compute the sum over F(S,K) for S=1..N and K=1..M
        total = 0
        for node in range(N):
            total += sum(F[node][1:M+1])
            if total >= MOD:
                total %= MOD
        print(f"Case #{test_case}: {total % MOD}")

threading.Thread(target=main).start()