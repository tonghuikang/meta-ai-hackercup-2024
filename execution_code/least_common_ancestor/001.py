import sys
import threading
import sys
def main():
    import sys
    import threading
    import math
    import bisect
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T+1):
        N = int(sys.stdin.readline())
        P = []
        S = []
        name_set = set()
        for _ in range(N):
            tokens = sys.stdin.readline().strip().split()
            pi = int(tokens[0])
            si = tokens[1]
            P.append(pi)
            S.append(si)
            name_set.add(si)
        name_list = sorted(list(name_set))
        name_to_index = {name:i for i,name in enumerate(name_list)}
        U_size = len(name_list)
        tree = [[] for _ in range(N)]
        root = -1
        for i in range(N):
            if P[i]==-1:
                root = i
            else:
                parent_idx = P[i]-1
                tree[parent_idx].append(i)

        # For D_i (descendants)
        D = [0]*N
        from collections import Counter

        # Post-order traversal
        def dfs_descendants(u):
            counts = Counter()
            counts[S[u]] +=1
            min_count = counts[S[u]]
            min_name = S[u]
            for v in tree[u]:
                child_counts = dfs_descendants(v)
                # Merge counts using small-to-large
                if len(counts)<len(child_counts):
                    counts, child_counts = child_counts, counts
                counts.update(child_counts)
            # Find the name with the minimum count
            min_count = None
            min_name = None
            for name, cnt in counts.items():
                if min_count is None or cnt<min_count or (cnt==min_count and name_to_index[name]<name_to_index[min_name]):
                    min_count = cnt
                    min_name = name
            D[u] = name_to_index[min_name]+1
            return counts
        dfs_descendants(root)

        # For A_i (ancestors)
        A = [0]*N

        # Pre-order traversal
        from collections import defaultdict

        counts = Counter()
        def dfs_ancestors(u):
            # Before visiting u, counts contain counts of ancestors' names (excluding current node's name)
            # Find the name with minimum count
            min_count = None
            min_name = None
            if counts:
                for name, cnt in counts.items():
                    if min_count is None or cnt<min_count or (cnt==min_count and name_to_index[name]<name_to_index[min_name]):
                        min_count = cnt
                        min_name = name
                A[u] = name_to_index[min_name]+1
            else:
                A[u]=0
            # Include current node's name for child nodes
            counts[S[u]] +=1
            for v in tree[u]:
                dfs_ancestors(v)
            counts[S[u]] -=1
            if counts[S[u]]==0:
                del counts[S[u]]
        dfs_ancestors(root)

        # Compute the hash
        hash_value = 0
        mod = 998244353
        for i in range(N):
            hash_value = (hash_value * (U_size + 1) + A[i]) % mod
            hash_value = (hash_value * (U_size + 1) + D[i]) % mod

        print(f"Case #{case_num}: {hash_value}")

if __name__ == "__main__":
    threading.Thread(target=main).start()