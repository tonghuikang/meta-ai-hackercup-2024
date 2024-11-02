import sys
import sys
import sys
import sys
import sys
import sys
import sys
from collections import defaultdict
import sys
import sys
import sys

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    from collections import defaultdict

    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr]); ptr +=1
    MOD = 998244353

    for test in range(1, T+1):
        N = int(input[ptr]); ptr +=1
        P = [0]*(N+1)
        S = ['']*(N+1)
        for i in range(1, N+1):
            P_i = input[ptr]; ptr +=1
            S_i = input[ptr]; ptr +=1
            P[i] = int(P_i)
            S[i] = S_i
        # Create U
        unique_names = sorted(set(S[1:]))
        U = unique_names
        name_to_idx = {name: idx+1 for idx, name in enumerate(U)}
        u_size = len(U)

        # Build tree
        tree = [[] for _ in range(N+1)]
        for i in range(2, N+1):
            parent = P[i]
            tree[parent].append(i)

        # Precompute in and out times
        in_order = [0]*(N+1)
        out_order = [0]*(N+1)
        time = 0
        def dfs_time(u):
            nonlocal time
            time +=1
            in_order[u] = time
            for v in tree[u]:
                dfs_time(v)
            out_order[u] = time
        dfs_time(1)

        # For D_i, prepare name occurrences
        name_occurrences = defaultdict(list)
        for i in range(1, N+1):
            name = S[i]
            idx = name_to_idx[name]
            name_occurrences[idx].append(in_order[i])
        # Sort the occurrences
        for idx in name_occurrences:
            name_occurrences[idx].sort()

        # Function to count occurrences in a range
        def count_in_range(lst, l, r):
            # Binary search for left and right
            import bisect
            left = bisect.bisect_left(lst, l)
            right = bisect.bisect_right(lst, r)
            return right - left

        # Compute D_i
        D = [0]*(N+1)
        for i in range(1, N+1):
            l = in_order[i]
            r = out_order[i]
            min_count = float('inf')
            min_idx = 0
            for idx in range(1, u_size+1):
                cnt = count_in_range(name_occurrences[idx], l, r) -1  # exclude itself if needed
                # But D_i is about descendants, so exclude self
                if S[i] == U[idx-1]:
                    cnt -=1
                if cnt < min_count and cnt >0:
                    min_count = cnt
                    min_idx = idx
                elif cnt == min_count and cnt >0 and idx < min_idx:
                    min_idx = idx
            # If i has no descendants, D_i=0
            if l == r or (all(count_in_range(name_occurrences[idx], l, r) - (1 if S[i]==U[idx-1] else 0) ==0 for idx in range(1, u_size+1))):
                D[i] =0
            else:
                D[i] = min_idx

        # Compute A_i
        A = [0]*(N+1)
        freq = [0]*(u_size+1)
        freq_to_names = defaultdict(set)
        min_freq = float('inf')
        min_name = 0

        def dfs_A(u):
            nonlocal min_freq, min_name
            # Add parent name
            if P[u] != -1:
                parent = P[u]
                name_idx = name_to_idx[S[parent]]
                freq[name_idx] +=1
                cnt = freq[name_idx]
                freq_to_names[cnt].add(name_idx)
                if cnt >1:
                    freq_to_names[cnt-1].discard(name_idx)
                    if not freq_to_names[cnt-1]:
                        del freq_to_names[cnt-1]
                if cnt < min_freq or (cnt == min_freq and name_idx < min_name):
                    min_freq = cnt
                    min_name = name_idx
                elif min_freq not in freq_to_names or not freq_to_names[min_freq]:
                    min_freq = min(freq_to_names.keys())
                    min_name = min(freq_to_names[min_freq])
            # Set A[u]
            if P[u] == -1:
                A[u] =0
            else:
                if min_freq == float('inf'):
                    A[u]=0
                else:
                    A[u]= min_name
            # Recurse to children
            for v in tree[u]:
                dfs_A(v)
            # Remove parent name
            if P[u] != -1:
                parent = P[u]
                name_idx = name_to_idx[S[parent]]
                cnt = freq[name_idx]
                freq_to_names[cnt].discard(name_idx)
                if not freq_to_names[cnt]:
                    del freq_to_names[cnt]
                freq[name_idx] -=1
                if freq[name_idx] >0:
                    freq_to_names[freq[name_idx]].add(name_idx)
                    if freq[name_idx] < min_freq or (freq[name_idx] == min_freq and name_idx < min_name):
                        min_freq = freq[name_idx]
                        min_name = name_idx
                else:
                    if min_freq == cnt:
                        if freq_to_names:
                            min_freq = min(freq_to_names.keys())
                            min_name = min(freq_to_names[min_freq])
                        else:
                            min_freq = float('inf')
                            min_name =0

        dfs_A(1)

        # Compute hash
        hash_val =0
        for i in range(1, N+1):
            hash_val = (hash_val * (u_size +1) + A[i]) % MOD
            hash_val = (hash_val * (u_size +1) + D[i]) % MOD
        print(f"Case #{test}: {hash_val}")

if __name__ == "__main__":
    main()