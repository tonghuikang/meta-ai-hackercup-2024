import sys
import sys
import sys
from collections import defaultdict, deque
import sys
import sys

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr]); ptr +=1
    for test_case in range(1, T+1):
        N = int(input[ptr]); ptr +=1
        P = []
        S = []
        for _ in range(N):
            p = input[ptr]; ptr +=1
            s = input[ptr]; ptr +=1
            P.append(int(p))
            S.append(s)
        # Process unique names
        unique_names = sorted(set(S))
        name_to_idx = {name: idx+1 for idx, name in enumerate(unique_names)}
        U = unique_names
        U_size = len(U)
        # Build tree
        children = [[] for _ in range(N+1)]
        for i in range(2, N+1):
            parent = P[i-1]
            children[parent].append(i)
        # Calculate A[i]
        A = [0]*(N+1)
        freq_anc = defaultdict(int)
        min_freq = {}
        min_name_idx = {}
        def dfs_anc(node):
            name = S[node-1]
            freq_anc[name] +=1
            # Update min_freq and min_name_idx
            # Find the current minimum frequency and corresponding name index
            current_min = None
            current_min_idx = None
            for n in freq_anc:
                f = freq_anc[n]
                idx = name_to_idx[n]
                if current_min is None or f < current_min or (f == current_min and idx < current_min_idx):
                    current_min = f
                    current_min_idx = idx
            if node !=1:
                if current_min is not None:
                    A[node] = current_min_idx
                else:
                    A[node] =0
            else:
                A[node] =0
            for child in children[node]:
                dfs_anc(child)
            freq_anc[name] -=1
            if freq_anc[name] ==0:
                del freq_anc[name]
        dfs_anc(1)
        # Calculate D[i]
        D = [0]*(N+1)
        freq_desc = defaultdict(int)
        def dfs_desc(node):
            name = S[node-1]
            freq_desc[name] +=1
            for child in children[node]:
                dfs_desc(child)
            # After processing children, determine D[node]
            # If node has no children, D[node] = 0
            if len(children[node]) ==0:
                D[node] =0
            else:
                # Find the least common name in the subtree
                current_min = None
                current_min_idx = None
                for n in freq_desc:
                    f = freq_desc[n]
                    idx = name_to_idx[n]
                    if current_min is None or f < current_min or (f == current_min and idx < current_min_idx):
                        current_min = f
                        current_min_idx = idx
                D[node] = current_min_idx if current_min is not None else 0
            freq_desc[name] -=1
            if freq_desc[name] ==0:
                del freq_desc[name]
        dfs_desc(1)
        # Compute hash
        hash_val =0
        for i in range(1, N+1):
            hash_val = (hash_val * (U_size +1) + A[i]) % MOD
            hash_val = (hash_val * (U_size +1) + D[i]) % MOD
        print(f"Case #{test_case}: {hash_val}")

if __name__ == "__main__":
    main()