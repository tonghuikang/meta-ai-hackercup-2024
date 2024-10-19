import sys
import threading

def main():
    import sys
    import math
    from collections import defaultdict

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        R,C,K = map(int, sys.stdin.readline().split())
        grid = []
        owners = defaultdict(list)
        for i in range(R):
            row = list(map(int, sys.stdin.readline().split()))
            grid.append(row)
            for j in range(C):
                owners[row[j]].append((i,j))
        # Binary search over possible scores
        left = 0
        right = max(R,C)
        def count_less_equal(S):
            total = 0
            # For each cell, count number of cells within S in max distance
            # and different owner
            # To optimize, we can use prefix sums per owner
            # But since owners can be many, we use overall counts minus same owner
            # First, total ordered pairs with distance <= S
            # Each cell can reach cells in square of side 2S+1
            # Total possible ordered pairs with distance <=S: sum over all cells, number of cells within distance S
            # which is R*C + 2 * sum for d=1 to S of (R -d)*(C -d)*4
            # But to be precise:
            total_pairs = 0
            for i in range(R):
                min_i = max(0, i - S)
                max_i = min(R-1, i + S)
                for j in range(C):
                    min_j = max(0, j - S)
                    max_j = min(C-1, j + S)
                    cnt = (max_i - min_i +1) * (max_j - min_j +1) -1
                    total_pairs += cnt
            total_pairs = total_pairs
            # Now, need to subtract pairs where owners are same
            same_owner = 0
            for owner, cells in owners.items():
                n = len(cells)
                if n <=1:
                    continue
                # For each cell, count number of cells within distance S
                # using brute force since n is small
                cells_sorted = sorted(cells)
                for idx, (x,y) in enumerate(cells):
                    for x2,y2 in cells[idx+1:]:
                        if max(abs(x2 - x), abs(y2 - y)) <= S:
                            same_owner +=2
            return total_pairs - same_owner
        while left < right:
            mid = (left + right) //2
            cnt = count_less_equal(mid)
            if cnt >= K:
                right = mid
            else:
                left = mid +1
        print(f"Case #{tc}: {left}")

threading.Thread(target=main,).start()