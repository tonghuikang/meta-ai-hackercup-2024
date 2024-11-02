import sys
import threading

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N, M = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        children = [[] for _ in range(N)]
        parents = [ -1 for _ in range(N)]
        for _ in range(N - 1):
            U, V = map(int, sys.stdin.readline().split())
            U -= 1
            V -= 1
            children[U].append(V)
            parents[V] = U

        # Initialize F for each node and each K
        # To handle large N and M, we cannot store F[S][K]
        # Instead, we can observe that F(S,K) is the minimum sum over any path from S with up to K stops
        # Since we need to take the min over all possible paths, and we can choose to collect up to K treasures
        # For each node, F(S,K) = A[S] + min over children F(child, K-1)
        # Or, if not collecting A[S], min over children F(child, K)
        # To maximize the minimum, we need to choose whether to collect or not

        # However, due to time constraints, we need a different approach.

        # Since we need to sum F(S,K) for all S and K, and F(S,K) >= F(S,K-1),
        # let's assume F(S,K) = min_{paths from S} sum of up to K A_i on the path

        # Since the minimum is over paths, for each S, F(S,K) is the minimum possible sum by choosing up to K nodes on any path from S to a leaf.

        # For a path, the minimal sum by choosing up to K nodes is to select the K smallest A_i on that path.

        # Therefore, F(S,K) = A_S if K >=1 and no children
        # Else, F(S,K) = min(A_S + min over children F(child, K-1), F(child, K))

        # Let's define dp[S] as a list of size up to M where dp[S][k] is min sum
        # Initialize dp from leaves up

        # Due to large N and M, we need to limit K up to the depth of the tree
        # Or find a way to compute the sum over all S and K without explicit DP

        # Here's an alternative idea:
        # Since F(S,K) is the minimum sum over any path from S where you collect up to K treasures,
        # To guarantee the minimum, we need to consider the minimum sum you can collect in the worst-case path

        # Let's realize that for each S, the worst path is the one that gives the minimal sum when you optimally collect up to K treasures.

        # Therefore, for each node, F(S,K) = A_S + min over children F(child,K-1)
        # If K >=1
        # For K=0, F(S,0)=0
        # Similarly, if not collecting A_S:
        # F(S,K)=min over children F(child,K)

        # Therefore, F(S,K)= min(A_S + min F(child,K-1), min F(child,K))
        # Which can be rewritten as:
        # F(S,K)= min over children (A_S + F(child,K-1), F(child,K))

        # So, for each node, for each K from 1 to M:
        # F(S,K)=min(A_S + F(child,K-1) for all children) and min(F(child,K) for all children)
        # So F(S,K)=min(A_S + min_child F(child,K-1), min_child F(child,K))

        # To compute this efficiently, we can precompute for each node the min_child F(child,K) and min_child F(child,K-1)

        # Let's proceed with this approach.

        # Initialize F for all nodes as a dict
        # To optimize, we can keep for each node the min F(child,K) and min F(child,K-1)

        # To make it efficient, we can process nodes in post-order and for each node keep the min F(child,K) for each K

        # Initialize F as list of lists
        # Due to large M, we need to find a smarter way, but for now let's proceed

        from collections import deque

        # Find the root
        root = 0
        # Post-order traversal
        order = []
        stack = deque()
        stack.append(root)
        visited = [False] * N
        while stack:
            node = stack.pop()
            if node < 0:
                order.append(-node -1)
                continue
            stack.append(-node -1)
            for child in children[node]:
                stack.append(child)

        # Initialize DP table
        # To optimize space, we can keep only up to M per node
        dp = [ [0]*(M+1) for _ in range(N)]

        for node in order:
            if not children[node]:
                # Leaf node
                dp[node][0] = 0
                if M >=1:
                    dp[node][1] = A[node]
                for k in range(2, M+1):
                    dp[node][k] = dp[node][k-1]
            else:
                dp[node][0] = 0
                min_children_k = [float('inf')] * (M+1)
                min_children_km1 = [float('inf')] * (M+1)
                for child in children[node]:
                    for k in range(0, M+1):
                        if dp[child][k] < min_children_k[k]:
                            min_children_k[k] = dp[child][k]
                        if k >=1 and dp[child][k-1] < min_children_km1[k]:
                            min_children_km1[k] = dp[child][k-1]
                if M >=1:
                    dp[node][1] = min(A[node] + (min_children_km1[1] if 1 <=M else float('inf')), min_children_k[1])
                for k in range(2, M+1):
                    dp[node][k] = min(A[node] + (min_children_km1[k] if k <= M else float('inf')), min_children_k[k])
        
        # Now sum over all F(S,K) for S=1..N and K=1..M
        total = 0
        for s in range(N):
            for k in range(1, M+1):
                total = (total + dp[s][k]) % MOD
        print(f"Case #{test_case}: {total}")

threading.Thread(target=main,).start()