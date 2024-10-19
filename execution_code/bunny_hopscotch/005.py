import sys
import threading

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        R, C, K = map(int, sys.stdin.readline().split())
        N = R * C
        grid = []
        owner_positions = dict()

        for i in range(R):
            row = list(map(int, sys.stdin.readline().split()))
            grid.append(row)
            for j in range(C):
                owner = row[j]
                if owner not in owner_positions:
                    owner_positions[owner] = []
                owner_positions[owner].append((i, j))

        # Prepare function to compute TotalOrderedPairsAtDistanceD
        max_possible_S = R + C - 2

        def compute_total_pairs_within_distance(S):
            total_pairs = N  # For D = 0 (self-pairs)
            for D in range(1, S + 1):
                R_D = R - D
                C_D = C - D
                if R_D <= 0 or C_D <= 0:
                    break
                total_pairs += 8 * D * R_D * C_D
            return total_pairs

        low = 0
        high = R + C  # Since max Chebyshev distance in grid is R + C -2
        answer = -1

        while low <= high:
            mid = (low + high) // 2
            # Compute total pairs within distance mid
            total_pairs = compute_total_pairs_within_distance(mid)
            # Compute total same-owner pairs within distance mid
            total_same_owner_pairs = 0
            # Build per owner summed-area tables
            for owner, positions in owner_positions.items():
                N_i = len(positions)
                if N_i == 0:
                    continue
                # Build grid mask for owner
                owner_grid = [[0] * C for _ in range(R)]
                for (x, y) in positions:
                    owner_grid[x][y] = 1
                # Build summed-area table for owner
                prefix_sum = [[0] * (C + 1) for _ in range(R + 1)]
                for i in range(1, R + 1):
                    for j in range(1, C + 1):
                        prefix_sum[i][j] = owner_grid[i - 1][j - 1] + \
                                           prefix_sum[i - 1][j] + \
                                           prefix_sum[i][j - 1] - \
                                           prefix_sum[i - 1][j - 1]
                # For each position, compute number of own burrows within distance mid
                for (i0, j0) in positions:
                    x1 = max(i0 - mid, 0)
                    x2 = min(i0 + mid, R - 1)
                    y1 = max(j0 - mid, 0)
                    y2 = min(j0 + mid, C - 1)
                    sum_i0_j0 = prefix_sum[x2 + 1][y2 + 1] - prefix_sum[x1][y2 + 1] - \
                                prefix_sum[x2 + 1][y1] + prefix_sum[x1][y1]
                    sum_i0_j0 -= 1  # Exclude self
                    total_same_owner_pairs += sum_i0_j0
            total_valid_hops = total_pairs - total_same_owner_pairs
            if total_valid_hops >= K:
                high = mid - 1
                answer = mid
            else:
                low = mid + 1

        print(f"Case #{test_case}: {answer}")

threading.Thread(target=main).start()