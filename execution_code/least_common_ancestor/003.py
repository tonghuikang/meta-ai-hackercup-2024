import sys
import threading
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        P = []
        S = []
        name_set = set()
        for _ in range(N):
            parts = sys.stdin.readline().strip().split()
            p = int(parts[0])
            s = parts[1]
            P.append(p)
            S.append(s)
            name_set.add(s)
        U = sorted(list(name_set))
        name_to_idx = {name: idx + 1 for idx, name in enumerate(U)}
        # Build tree
        children = [[] for _ in range(N + 1)]
        for i in range(2, N + 1):
            parent = P[i -1]
            children[parent].append(i)
        # Ancestor processing
        A = [0] * (N +1)
        freq = defaultdict(int)
        min_freq = None
        min_name_idx = None
        def dfs_ancestor(u, freq_map, current_min_freq, current_min_idx):
            s_idx = name_to_idx[S[u -1]]
            freq_map[s_idx] +=1
            # Update min
            if current_min_freq is None or freq_map[s_idx] < current_min_freq or (freq_map[s_idx] == current_min_freq and s_idx < current_min_idx):
                current_min_freq = freq_map[s_idx]
                current_min_idx = s_idx
            A[u] = current_min_idx
            for v in children[u]:
                dfs_ancestor(v, freq_map, current_min_freq, current_min_idx)
            freq_map[s_idx] -=1
            if freq_map[s_idx] ==0:
                del freq_map[s_idx]
        freq_map = defaultdict(int)
        dfs_ancestor(1, freq_map, None, None)
        # For root, if no ancestors, set A[1]=0
        A[1] =0
        # Descendant processing
        D = [0] * (N +1)
        def dfs_descendant(u):
            freq_map = defaultdict(int)
            freq_map[name_to_idx[S[u -1]]] +=1
            min_freq = freq_map[name_to_idx[S[u -1]]]
            min_idx = name_to_idx[S[u -1]]
            for v in children[u]:
                child_map, child_min_freq, child_min_idx = dfs_descendant(v)
                # Merge child_map into freq_map
                for k, v_cnt in child_map.items():
                    freq_map[k] += v_cnt
                    # Update min
                    if freq_map[k] < min_freq or (freq_map[k] == min_freq and k < min_idx):
                        min_freq = freq_map[k]
                        min_idx = k
            # Determine D[u]
            # If u has no descendants, D[u]=0
            if len(children[u]) ==0:
                D[u] =0
            else:
                D[u] = min_idx
            return freq_map, min_freq, min_idx
        dfs_descendant(1)
        # For nodes with no descendants set D=0
        for u in range(1, N+1):
            if len(children[u]) ==0:
                D[u] =0
        # Compute hash
        U_len = len(U)
        hash_val =0
        for i in range(1, N+1):
            hash_val = (hash_val * (U_len +1) + A[i]) % MOD
            hash_val = (hash_val * (U_len +1) + D[i]) % MOD
        print(f"Case #{test_case}: {hash_val}")

threading.Thread(target=main).start()