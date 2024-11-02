import sys
import threading
import sys
import sys
import sys

sys.setrecursionlimit(1 << 25)

def main():
    import sys
    import math
    input = sys.stdin.read
    from collections import defaultdict, deque
    T = int(sys.stdin.readline())
    MOD = 998244353
    for test_case in range(1, T+1):
        N, M = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        tree = [[] for _ in range(N)]
        parent = [ -1 for _ in range(N)]
        for _ in range(N-1):
            U, V = map(int, sys.stdin.readline().split())
            U -=1
            V -=1
            tree[U].append(V)
            parent[V]=U
        # Find root (node with parent -1)
        root = 0
        # Find child_min for each node
        child_min = [ -1 for _ in range(N)]
        # Post-order traversal
        order = []
        stack = [root]
        visited = [False]*N
        while stack:
            node = stack.pop()
            if node < 0:
                order.append(~node)
                continue
            stack.append(~node)
            for child in tree[node]:
                stack.append(child)
        # Initialize F as list of lists
        # To save memory, use list of lists with M+1
        # But it's too big, use separate arrays
        F = [ [0]*(M+1) for _ in range(N)]
        # Precompute child_min as child with minimal A
        for node in order:
            if not tree[node]:
                child_min[node] = -1
            else:
                min_a = math.inf
                min_c = -1
                for child in tree[node]:
                    if A[child] < min_a:
                        min_a = A[child]
                        min_c = child
                child_min[node] = min_c
        # Now compute F in post order
        for node in order:
            if child_min[node]==-1:
                # Leaf node
                for k in range(1, M+1):
                    F[node][k] = max(F[node][k-1], A[node])
            else:
                c = child_min[node]
                for k in range(1, M+1):
                    option1 = A[node] + (F[c][k-1] if k-1>=0 else 0)
                    option2 = min(F[child][k] for child in tree[node])
                    F[node][k] = max(option1, option2)
        # Now sum over all F[S][K] for S=1..N and K=1..M
        total = 0
        for s in range(N):
            total += sum(F[s][1:M+1])
            total %= MOD
        print(f"Case #{test_case}: {total}")

threading.Thread(target=main).start()

# Note: The answer already contains the Python code above.