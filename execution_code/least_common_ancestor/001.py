import sys
import threading
def main():
    import sys
    import threading

    sys.setrecursionlimit(1 << 25)

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        P = []
        S = []
        name_set = set()
        for _ in range(N):
            parts = sys.stdin.readline().strip().split()
            p = int(parts[0])
            s = parts[1]
            P.append(p)  # store parent index
            S.append(s)  # store name
            name_set.add(s)

        # Map names to indices
        U = sorted(list(name_set))
        name_to_id = {name: idx + 1 for idx, name in enumerate(U)}  # names mapped to 1..|U|
        M = len(U)

        name_ids = [name_to_id[s] for s in S]  # list of name IDs

        # Build tree
        tree = [[] for _ in range(N)]
        root = -1
        for i in range(N):
            if P[i] == -1:
                root = i
            else:
                tree[P[i] - 1].append(i)

        # Initialize A and D
        A = [0] * N
        D = [0] * N

        # Function to compute descendant counts (D_i)
        def dfs_desc(u):
            counts = {}
            minfreq = None
            minname = None

            for v in tree[u]:
                child_counts, child_minfreq, child_minname = dfs_desc(v)
                # Merge counts
                if len(counts) < len(child_counts):
                    counts, child_counts = child_counts, counts
                    minfreq, minname = child_minfreq, child_minname
                for name, cnt in child_counts.items():
                    counts[name] = counts.get(name, 0) + cnt
                # Update minfreq and minname
                if child_minfreq is not None:
                    if minfreq is None or child_minfreq < minfreq or (child_minfreq == minfreq and child_minname < minname):
                        minfreq = child_minfreq
                        minname = child_minname

            # Compute D[u]
            if counts:
                # Find minfreq and minname among counts
                for name, cnt in counts.items():
                    if minfreq is None or cnt < minfreq or (cnt == minfreq and name < minname):
                        minfreq = cnt
                        minname = name
                D[u] = minname
            else:
                D[u] = 0

            # Update counts (exclude self)
            name_id = name_ids[u]
            counts[name_id] = counts.get(name_id, 0)  # exclude self

            return counts, minfreq, minname

        # Function to compute ancestor counts (A_i)
        def dfs_anc(u, counts):
            # Compute A[u]
            if counts:
                minfreq = None
                minname = None
                for name, cnt in counts.items():
                    if minfreq is None or cnt < minfreq or (cnt == minfreq and name < minname):
                        minfreq = cnt
                        minname = name
                A[u] = minname
            else:
                A[u] = 0

            # Update counts with current node's name
            name_id = name_ids[u]
            counts[name_id] = counts.get(name_id, 0) + 1

            for v in tree[u]:
                dfs_anc(v, counts)

            # Decrement counts after returning from recursion
            counts[name_id] -= 1
            if counts[name_id] == 0:
                del counts[name_id]

        # Compute D
        dfs_desc(root)

        # Compute A
        counts_dict = {}
        dfs_anc(root, counts_dict)

        # Now compute the hash
        hash_val = 0
        U_size = len(U)
        modulo = 998244353
        for i in range(N):
            hash_val = (hash_val * (U_size + 1) + A[i]) % modulo
            hash_val = (hash_val * (U_size + 1) + D[i]) % modulo

        print(f'Case #{test_case}: {hash_val}')

if __name__ == "__main__":
    threading.Thread(target=main).start()