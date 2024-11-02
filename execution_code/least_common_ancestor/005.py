import sys
import threading

def main():
    import sys
    import math
    import bisect
    import threading
    sys.setrecursionlimit(1 << 25)

    T = int(sys.stdin.readline())
    for case_num in range(1, T+1):
        N = int(sys.stdin.readline())
        P = []
        S = []
        name_list = []
        name_set = set()
        for _ in range(N):
            parts = sys.stdin.readline().strip().split()
            pi = int(parts[0])
            si = parts[1]
            P.append(pi -1) # Adjust index to 0-based
            S.append(si)
            name_set.add(si)
        U = sorted(name_set)
        name_to_idx = {name: idx for idx, name in enumerate(U)}
        K = len(U)
        # Build tree
        tree = [[] for _ in range(N)]
        root = -1
        for i in range(N):
            pi = P[i]
            if pi == -2:  # Root node
                root = i
            else:
                tree[pi].append(i)

        # Compute total frequencies of names
        total_freq = {}
        for name in S:
            total_freq[name] = total_freq.get(name, 0) + 1

        # Build parent pointers and depths
        depth = [0]*N
        parent = [-1]*N

        from collections import defaultdict

        # Build depth and parent arrays
        def dfs_build(node, dep):
            for child in tree[node]:
                depth[child] = dep+1
                parent[child] = node
                dfs_build(child, dep+1)

        dfs_build(root, 0)

        # For each node, try to collect names along ancestor path (limited to max_depth)
        max_depth = 1000  # Limit to prevent TLE or MemoryError

        A = [0]*N
        D = [0]*N

        # Compute A_i for each node
        def compute_A():
            for i in range(N):
                ancestor_names = set()
                node = i
                steps = 0
                while node != -1 and steps < max_depth:
                    ancestor_names.add(S[node])
                    node = parent[node]
                    steps +=1
                if len(ancestor_names) ==0:
                    A[i]=0
                else:
                    # Among ancestor names, pick the one with minimal total frequency
                    min_freq = float('inf')
                    min_name = None
                    for name in ancestor_names:
                        freq = total_freq[name]
                        if freq < min_freq or (freq == min_freq and name_to_idx[name] < name_to_idx[min_name]):
                            min_freq = freq
                            min_name = name
                    A[i] = name_to_idx[min_name]+1  # 1-based index
        # Compute D_i for each node
        minfreq = [float('inf')]*N
        minnames = ['']*N
        def dfs_D(node):
            if not tree[node]:
                # Leaf node
                minfreq[node] = 1
                minnames[node] = S[node]
            else:
                freqs = defaultdict(int)
                freqs[S[node]] +=1
                minf = total_freq[S[node]]
                minname = S[node]
                for child in tree[node]:
                    dfs_D(child)
                    cname = minnames[child]
                    cfreq = minfreq[child]
                    if cfreq < minf or (cfreq == minf and name_to_idx[cname]< name_to_idx[minname]):
                        minf = cfreq
                        minname = cname
                minfreq[node] = minf
                minnames[node] = minname
        compute_A()
        dfs_D(root)

        for i in range(N):
            if minnames[i]:
                D[i] = name_to_idx[minnames[i]]+1
            else:
                D[i]=0
            if A[i]==0:
                pass
            else:
                pass

        # Compute hash
        MOD = 998244353
        hash_val = 0
        for i in range(N):
            hash_val = (hash_val * (K+1) + A[i]) % MOD
            hash_val = (hash_val * (K+1) + D[i]) % MOD

        print('Case #{}: {}'.format(case_num, hash_val))

threading.Thread(target=main).start()