import sys
import threading
import sys
import sys
import numpy as np

def main():
    import sys
    import sys

    sys.setrecursionlimit(1 << 25)
    from collections import defaultdict

    T = int(sys.stdin.readline())
    MOD = 998244353

    for test_case in range(1, T + 1):
        N_line = ''
        while N_line.strip() == '':
            N_line = sys.stdin.readline()
        N = int(N_line.strip())
        P = []
        S = []
        for _ in range(N):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            parts = line.strip().split()
            p = int(parts[0])
            s = parts[1]
            P.append(p)
            S.append(s)
        # Assign U
        unique_names = sorted(set(S))
        U = unique_names
        name_to_u = {name: idx+1 for idx, name in enumerate(U)}
        U_size = len(U)
        S_u = [name_to_u[name] for name in S]
        # Build tree
        children = [[] for _ in range(N +1)]
        for i in range(1, N):
            parent = P[i]
            children[parent].append(i+1)
        # Compute A_i
        A = [0]*(N+1)
        frequency = np.zeros(U_size +2, dtype=np.int32)
        freq_count = defaultdict(int)
        freq_count = np.zeros(U_size +2, dtype=np.int32)
        min_freq = 1
        # Precompute sorted U indices
        sorted_u = np.arange(1, U_size+1)
        def dfs_a(node):
            nonlocal min_freq
            name = S_u[node-1]
            freq_prev = frequency[name]
            frequency[name] +=1
            freq_new = frequency[name]
            freq_count[freq_prev] -=1
            freq_count[freq_new] +=1
            if freq_prev == min_freq and freq_count[freq_prev] ==0:
                min_freq +=1
            # Find A_i
            if node ==1:
                A[node] = 0
            else:
                # Find the min U index with frequency == min_freq
                # Since U is sorted, iterate and find first with freq == min_freq
                # Use NumPy for speed
                candidates = np.where(frequency[1:U_size+1] == min_freq)[0] +1
                if candidates.size >0:
                    A[node] = candidates.min()
                else:
                    A[node] =0
            for child in children[node]:
                dfs_a(child)
            # Backtrack
            frequency[name] -=1
            freq_count[freq_new] -=1
            freq_count[freq_prev] +=1
            if freq_prev < min_freq:
                min_freq = freq_prev
        dfs_a(1)
        # Compute D_i
        D = [0]*(N+1)
        # To handle D_i, perform post-order traversal and maintain frequency counts
        # Implemented using merging child frequency dictionaries
        # But with large N and U, use NumPy arrays for frequencies
        def dfs_d(node):
            name = S_u[node-1]
            freq = np.zeros(U_size +2, dtype=np.int32)
            # For each child, merge frequencies
            for child in children[node]:
                child_freq = dfs_d(child)
                freq += child_freq
            # Now, add the current node's name to frequency
            # But D_i requires frequencies of descendants, excluding the node itself
            # So D_i is based on freq before adding the current node's name
            if children[node]:
                # freq already has descendants
                min_f = freq[1:U_size+1].min()
                candidates = np.where(freq[1:U_size+1] == min_f)[0] +1
                if candidates.size >0:
                    D[node] = candidates.min()
                else:
                    D[node] =0
            else:
                D[node] =0
            # Now, include the current node's name for the parent's frequencies
            freq[name] +=1
            return freq
        dfs_d(1)
        # Compute hash
        hash_val = 0
        U_plus_1 = U_size +1
        for i in range(1, N+1):
            hash_val = (hash_val * U_plus_1 + A[i]) % MOD
            hash_val = (hash_val * U_plus_1 + D[i]) % MOD
        print(f"Case #{test_case}: {hash_val}")

threading.Thread(target=main).start()