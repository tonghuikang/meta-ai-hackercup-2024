import sys
import math
import itertools

def readints():
    return list(map(int, sys.stdin.readline().split()))

MOD = 10**9+7

T = int(sys.stdin.readline())
for test_case in range(1, T+1):
    N, M, L = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A_sorted = sorted(A)
    # Precompute prefix sums for internal sums
    prefix_internal_sum = [0] * (N+1)
    for i in range(1, N):
        prefix_internal_sum[i] = prefix_internal_sum[i-1] + (A_sorted[i] - A_sorted[i-1])
    prefix_internal_sum[N] = prefix_internal_sum[N-1]
    # Generate all permutations of B
    B_perms = list(itertools.permutations(B))
    count = 0
    # Precompute all possible splits
    # Splits are M+1 blocks, need to choose M split points among N
    # Using itertools.combinations
    split_combinations = list(itertools.combinations(range(N+1), M))
    for B_perm in B_perms:
        for splits in split_combinations:
            # splits is a tuple of M split points, in increasing order
            # Define block ranges
            blocks = []
            prev = 0
            for s in splits:
                blocks.append( (prev, s) )
                prev = s
            blocks.append( (prev, N) )
            # Now, for each block, decide sorted or reversed
            # 2^(M+1) options
            for arrange in range(1 << (M+1)):
                valid = True
                total_sum = 0
                block_first = []
                block_last = []
                for k in range(M+1):
                    l, r = blocks[k]
                    if l < r:
                        if (arrange >> k) &1:
                            first = A_sorted[r-1]
                            last = A_sorted[l]
                        else:
                            first = A_sorted[l]
                            last = A_sorted[r-1]
                        block_first.append(first)
                        block_last.append(last)
                        # Internal sum
                        internal = A_sorted[r-1] - A_sorted[l]
                        total_sum += internal
                    else:
                        block_first.append(None)
                        block_last.append(None)
                # Now compute transitions
                for k in range(M):
                    Bk = B_perm[k]
                    Bk_plus_1 = B_perm[k+1] if k+1 < M else None
                    # Transition between block k and Bk
                    if block_last[k] is not None:
                        total_sum += abs(block_last[k] - Bk)
                    # Transition between Bk and block k+1
                    if blocks[k] != (blocks[k][1], blocks[k][1]):
                        if block_first[k+1] is not None:
                            total_sum += abs(Bk - block_first[k+1])
                    else:
                        # If block k+1 is empty, transition between Bk and Bk+1
                        if k+1 < M:
                            total_sum += abs(Bk - B_perm[k+1])
                # Handle the first block connecting to nothing or B1
                # And the last block connecting to nothing
                # But already handled in the loop
                # Check the total_sum
                if total_sum <= L:
                    count = (count +1) % MOD
    print(f"Case #{test_case}: {count % MOD}")