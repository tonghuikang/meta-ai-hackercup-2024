import sys
import threading
import math
from itertools import permutations, combinations

def main():
    import sys
    import bisect
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 10 ** 9 + 7
    for case_num in range(1, T + 1):
        N, M, L = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))
        A.sort()
        nigiri_unevenness = sum(abs(A[i] - A[i+1]) for i in range(N -1))
        nigiri_nigiri_diffs = [abs(A[i] - A[i+1]) for i in range(N -1)]
        nigiri_sashimi_diffs = []
        # Precompute differences between all nigiri and sashimi
        nigiri_sashimi_diff = [[abs(a - b) for b in B] for a in A]
        total_count = 0
        factorial = [1] * (M+1)
        for i in range(1, M+1):
            factorial[i] = factorial[i-1] * i
        sashimi_perms = list(permutations(B))
        M_factorial = factorial[M]
        # Precompute the number of ways to choose positions
        from math import comb
        positions_count = comb(N + M, M)
        # Since M is small, we can process per permutation
        # Now we need to process all permutations of the sashimi pieces
        total_count = 0
        for sashimi in sashimi_perms:
            sashimi_unevenness = sum(abs(sashimi[i] - sashimi[i+1]) for i in range(M -1))
            # Precompute differences between sashimi pieces
            sashimi_sashimi_diffs = [abs(sashimi[i] - sashimi[i+1]) for i in range(M -1)]
            # Generate all combinations of positions to insert the sashimi pieces
            # There are comb(N + M, M) ways
            # positions is a list of indices where the sashimi pieces will be inserted
            positions_list = combinations(range(N + M), M)
            # We need to process positions_list in chunks to avoid memory issues
            chunk_size = 100000
            positions_list_iter = combinations(range(N + M), M)
            # positions_list is an iterator, so we process it in chunks
            count = 0
            processed = 0
            while True:
                positions_chunk = list()
                try:
                    for _ in range(chunk_size):
                        positions_chunk.append(next(positions_list_iter))
                except StopIteration:
                    pass
                if not positions_chunk:
                    break
                for positions in positions_chunk:
                    total_unevenness = nigiri_unevenness + sashimi_unevenness
                    idx_nigiri = 0
                    idx_sashimi = 0
                    last_piece = None
                    last_piece_val = None
                    current_piece = None
                    current_piece_val = None
                    over_limit = False
                    for idx in range(N+M):
                        if idx in positions:
                            # Place a sashimi piece
                            current_piece_val = sashimi[idx_sashimi]
                            idx_sashimi +=1
                        else:
                            # Place a nigiri piece
                            current_piece_val = A[idx_nigiri]
                            idx_nigiri +=1
                        if last_piece_val is not None:
                            diff = abs(current_piece_val - last_piece_val)
                            total_unevenness += diff
                            if total_unevenness > L:
                                over_limit = True
                                break
                        last_piece_val = current_piece_val
                    if not over_limit:
                        count +=1
                processed += len(positions_chunk)
            total_count += count
        print(f'Case #{case_num}: {total_count % MOD}')
threading.Thread(target=main).start()