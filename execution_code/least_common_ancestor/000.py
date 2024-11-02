import sys
import threading
from collections import defaultdict, deque

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353

    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        parents = []
        names = []
        for _ in range(N):
            parts = sys.stdin.readline().strip().split()
            p = int(parts[0])
            s = parts[1]
            parents.append(p)
            names.append(s)

        # Create list of unique names sorted lex
        unique_names = sorted(list(set(names)))
        name_to_idx = {name: idx + 1 for idx, name in enumerate(unique_names)}
        U = unique_names
        U_size = len(U)

        # Build tree
        children = [[] for _ in range(N + 1)]
        for i in range(2, N + 1):
            p = parents[i - 1]
            children[p].append(i)

        # Precompute descendant counts
        # For descendants, we need frequency counts in subtree
        # Since we need least common name, which is min count, and lowest index
        # We can do a post-order traversal and count frequencies

        # Initialize D array
        D = [0] * (N + 1)

        # To store frequency for each subtree
        def dfs_desc(u):
            freq = defaultdict(int)
            freq[name_to_idx[names[u - 1]]] += 1
            for v in children[u]:
                child_freq = dfs_desc(v)
                for k, v_count in child_freq.items():
                    freq[k] += v_count
            # Find least common name
            min_count = float('inf')
            min_idx = 0
            for name_idx, count in freq.items():
                if count < min_count or (count == min_count and name_idx < min_idx):
                    min_count = count
                    min_idx = name_idx
            if len(children[u]) == 0:
                # No descendants
                D[u] = 0
            else:
                D[u] = min_idx
            return freq

        dfs_desc(1)

        # For ancestors, we need to track frequencies along the path from root to current node
        # We can do a pre-order traversal and maintain a global frequency dict
        A = [0] * (N + 1)
        freq = defaultdict(int)

        def dfs_anc(u):
            # Update frequency with current node
            freq[name_to_idx[names[u - 1]]] += 1
            # Find least common name among ancestors (excluding self)
            if parents[u - 1] == -1:
                A[u] = 0
            else:
                # Exclude current node's name
                current_name_idx = name_to_idx[names[u - 1]]
                min_count = float('inf')
                min_idx = 0
                for name_idx, count in freq.items():
                    if name_idx == current_name_idx:
                        continue
                    if count < min_count or (count == min_count and name_idx < min_idx):
                        min_count = count
                        min_idx = name_idx
                if min_count == float('inf'):
                    A[u] = 0
                else:
                    A[u] = min_idx
            for v in children[u]:
                dfs_anc(v)
            freq[name_to_idx[names[u - 1]]] -= 1

        dfs_anc(1)

        # Compute hash
        hash_val = 0
        for i in range(1, N + 1):
            hash_val = (hash_val * (U_size + 1) + A[i]) % MOD
            hash_val = (hash_val * (U_size + 1) + D[i]) % MOD

        print(f"Case #{test_case}: {hash_val}")

threading.Thread(target=main).start()