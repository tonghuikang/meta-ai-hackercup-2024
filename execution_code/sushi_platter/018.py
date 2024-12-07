import sys
import threading
from functools import lru_cache

def main():
    import sys

    sys.setrecursionlimit(1000000)
    MOD = 10**9+7

    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, M, L = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))
        all_pieces = A + B
        n = N + M
        types = ['A']*N + ['B']*M
        # Precompute absolute differences
        diffs = {}
        for i in range(n):
            for j in range(n):
                if i != j:
                    diffs[(i,j)] = abs(all_pieces[i] - all_pieces[j])
        # Assign indices to A and B
        A_indices = list(range(N))
        B_indices = list(range(N, n))
        from collections import defaultdict
        dp = defaultdict(int)
        # Initialize DP: for each starting piece
        for i in range(n):
            dp[(1 << i, i)] = 1
        for _ in range(n-1):
            new_dp = defaultdict(int)
            for (mask, last), count in dp.items():
                for next_p in range(n):
                    if not (mask & (1 << next_p)):
                        new_mask = mask | (1 << next_p)
                        s = diffs.get((last, next_p), 0)
                        # We need to track sum, but L is too large.
                        # Thus, we cannot track sum in state. Alternative approach needed.
                        # Not feasible.
                        # Hence, alternative approach: impossible with large L.
                        # Perhaps precompute total differences and check.
                        # Not feasible.
                        pass
            dp = new_dp
        # As the above approach is not feasible due to L being too large, we need a different approach.
        # Instead, since M is small (<=5), we can iterate over all permutations of B's and insert them into A's.
        from itertools import permutations, combinations
        # Precompute all possible orders of B's
        ans = 0
        A_sorted = sorted(A)
        A_sorted_rev = sorted(A, reverse=True)
        # Precompute sum differences for A sorted and reverse
        def calc_sum(arr):
            s = 0
            for i in range(len(arr)-1):
                s += abs(arr[i] - arr[i+1])
            return s
        A_sum_sorted = calc_sum(A_sorted)
        A_sum_rev = calc_sum(A_sorted_rev)
        # All permutations of B
        for b_order in permutations(B):
            # Now, we need to interleave B's into A's sorted and reverse
            # Since M <=5, and N <=50, try all possible insertion points
            # Number of insertion points: N+1
            # Choose M positions out of N+1, allowing multiple B's in same position
            # But M is small
            from itertools import product
            insertion_points = list(range(N+1))
            # Generate all possible ways to assign M B's to N+1 positions
            # This is combinations with replacement: C(N+1+M-1, M) = C(N+M, M)
            # But for N=50 and M=5, it's C(55,5)= 3,478,761 possible
            # Which is manageable
            valid = 0
            # To optimize, precompute A sorted and reversed
            A_variants = [A_sorted, A_sorted_rev]
            for a_variant in A_variants:
                # Precompute the sum within A's
                A_sum = calc_sum(a_variant)
                # Now, insert B's into a_variant
                # For M=0, just check A_sum <= L
                if M ==0:
                    if A_sum <= L:
                        valid +=1
                    continue
                # Assign B's to positions
                # Generate combinations with replacement: assign each B to a position
                # To reduce computation, group by how many B's in each position
                # But since M=5, proceed with product
                # To further optimize, use combinations with non-decreasing positions
                for positions in combinations(range(N+1), M):
                    # positions is a tuple of M positions in non-decreasing order
                    # Now, place the B's in these positions in the given order
                    # Build the full permutation
                    perm = []
                    a_idx =0
                    b_idx =0
                    total_sum =0
                    last = None
                    for pos in range(N+M):
                        # Check if current pos is a B position
                        # positions are sorted
                        if b_idx < M and pos == positions[b_idx]:
                            current = b_order[b_idx]
                            b_idx +=1
                        else:
                            current = a_variant[a_idx]
                            a_idx +=1
                        if last is not None:
                            total_sum += abs(current - last)
                            if total_sum > L:
                                break
                        last = current
                    if total_sum <= L:
                        valid = (valid +1)%MOD
            ans = valid % MOD
        print(f"Case #{test_case}: {ans}")

threading.Thread(target=main).start()

import sys
import threading
from functools import lru_cache

def main():
    import sys

    sys.setrecursionlimit(1000000)
    MOD = 10**9+7

    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, M, L = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))
        all_pieces = A + B
        n = N + M
        types = ['A']*N + ['B']*M
        # Precompute absolute differences
        diffs = {}
        for i in range(n):
            for j in range(n):
                if i != j:
                    diffs[(i,j)] = abs(all_pieces[i] - all_pieces[j])
        # Assign indices to A and B
        A_indices = list(range(N))
        B_indices = list(range(N, n))
        from collections import defaultdict
        dp = defaultdict(int)
        # Initialize DP: for each starting piece
        for i in range(n):
            dp[(1 << i, i)] = 1
        for _ in range(n-1):
            new_dp = defaultdict(int)
            for (mask, last), count in dp.items():
                for next_p in range(n):
                    if not (mask & (1 << next_p)):
                        new_mask = mask | (1 << next_p)
                        s = diffs.get((last, next_p), 0)
                        # We need to track sum, but L is too large.
                        # Thus, we cannot track sum in state. Alternative approach needed.
                        # Not feasible.
                        # Perhaps precompute total differences and check.
                        # Not feasible.
                        pass
            dp = new_dp
        # As the above approach is not feasible due to L being too large, we need a different approach.
        # Instead, since M is small (<=5), we can iterate over all permutations of B's and insert them into A's.
        from itertools import permutations, combinations
        # Precompute all possible orders of B's
        ans = 0
        A_sorted = sorted(A)
        A_sorted_rev = sorted(A, reverse=True)
        # Precompute sum differences for A sorted and reverse
        def calc_sum(arr):
            s = 0
            for i in range(len(arr)-1):
                s += abs(arr[i] - arr[i+1])
            return s
        A_sum_sorted = calc_sum(A_sorted)
        A_sum_rev = calc_sum(A_sorted_rev)
        # All permutations of B
        for b_order in permutations(B):
            # Now, we need to interleave B's into A's sorted and reverse
            # Since M <=5, and N <=50, try all possible insertion points
            # Since M is small
            from itertools import product
            insertion_points = list(range(N+1))
            # Generate all possible ways to assign M B's to N+1 positions
            # This is combinations with replacement: C(N+1+M-1, M) = C(N+M, M)
            # But for N=50 and M=5, it's C(55,5)= ~3.478e6 possible
            # Which is manageable
            valid = 0
            # To optimize, precompute A sorted and reversed
            A_variants = [A_sorted, A_sorted_rev]
            for a_variant in A_variants:
                # Precompute the sum within A's
                A_sum = calc_sum(a_variant)
                # Now, insert B's into a_variant
                # For M=0, just check A_sum <= L
                if M ==0:
                    if A_sum <= L:
                        valid +=1
                    continue
                # Assign B's to positions
                # Generate combinations with replacement: assign each B to a position
                # To reduce computation, group by how many B's in each position
                # But since M=5, proceed with product
                # To further optimize, use combinations with non-decreasing positions
                for positions in combinations(range(N+1), M):
                    # positions is a tuple of M positions in non-decreasing order
                    # Now, place the B's in these positions in the given order
                    # Build the full permutation
                    perm = []
                    a_idx =0
                    b_idx =0
                    total_sum =0
                    last = None
                    for pos in range(N+M):
                        # Check if current pos is a B position
                        # positions are sorted
                        if b_idx < M and pos == positions[b_idx]:
                            current = b_order[b_idx]
                            b_idx +=1
                        else:
                            current = a_variant[a_idx]
                            a_idx +=1
                        if last is not None:
                            total_sum += abs(current - last)
                            if total_sum > L:
                                break
                        last = current
                    if total_sum <= L:
                        valid = (valid +1)%MOD
            ans = valid % MOD
        print(f"Case #{test_case}: {ans}")

threading.Thread(target=main).start()