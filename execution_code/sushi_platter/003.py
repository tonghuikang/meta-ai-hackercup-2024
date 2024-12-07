import sys
import threading
from math import comb
MOD = 10**9 + 7

def main():
    import sys
    import math
    from itertools import permutations, combinations
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, M, L = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))
        A_sorted = sorted(A)
        B_sorted = sorted(B)
        # Combine all elements
        all_elements = sorted(A_sorted + B_sorted)
        # To speed up, precompute differences
        diffs = {}
        for i in range(len(all_elements)):
            for j in range(len(all_elements)):
                if i != j:
                    diffs[(all_elements[i], all_elements[j])] = abs(all_elements[i] - all_elements[j])
        # Since N=50 and M=5, which is manageable
        # We can use DP where we keep track of used sashimi
        # Assign indices to sashimi
        sashimi = B_sorted
        nigiri = A_sorted
        total = N + M
        from functools import lru_cache
        @lru_cache(None)
        def dp(last, mask, count, total_diff):
            if count == total:
                return 1 if total_diff <= L else 0
            res = 0
            # Try to place a nigiri
            if count < N + M:
                # Place any unused nigiri
                # But to prevent overcounting, we need to have a unique state
                # Since all nigiri are distinct, but their order can be arranged
                # To simplify, assume nigiri are indistinct in the DP
                # This might not work due to distinct differences
                # Alternative: iterate through all nigiri not used
                # But N=50 is too big for bitmask
                pass  # This approach fails due to large N
            # Alternative approach: since M is small, fix the order of sashimi
            return 0
        # The above approach is not feasible. Alternative:
        # Since M is small, iterate over all possible orders of sashimi and their insertion positions
        # Precompute the sum of differences for nigiri in sorted order
        sum_nigiri = 0
        for i in range(N-1):
            sum_nigiri += abs(A_sorted[i] - A_sorted[i+1])
        # Now, insert M sashimi into N+1 positions
        from itertools import permutations, combinations
        result = 0
        # Precompute all possible permutations of sashimi
        permuts = list(permutations(B_sorted))
        # Select M positions out of N+1
        positions = list(combinations(range(N+1), M))
        for perm in permuts:
            for pos in positions:
                # Build the full sequence
                seq = []
                s_idx = 0
                a_idx = 0
                for i in range(N+M):
                    if i in pos:
                        seq.append(perm[s_idx])
                        s_idx +=1
                    else:
                        seq.append(A_sorted[a_idx])
                        a_idx +=1
                # Compute sum of differences
                s = 0
                for i in range(len(seq)-1):
                    s += abs(seq[i] - seq[i+1])
                    if s > L:
                        break
                if s <= L:
                    result = (result +1) % MOD
        print(f"Case #{test_case}: {result}")
                

threading.Thread(target=main).start()