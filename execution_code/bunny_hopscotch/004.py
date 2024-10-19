import sys
import threading
from bisect import bisect_left, bisect_right

def main():
    import sys

    import sys

    def readints():
        return list(map(int, sys.stdin.read().split()))

    data = readints()
    ptr = 0
    T = data[ptr]
    ptr +=1
    for test_case in range(1, T+1):
        R = data[ptr]
        C = data[ptr+1]
        K = data[ptr+2]
        ptr +=3
        grid = []
        for _ in range(R):
            row = data[ptr:ptr+C]
            grid.append(row)
            ptr += C
        # Build bunny to cells mapping
        bunny_map = {}
        for i in range(R):
            for j in range(C):
                b = grid[i][j]
                if b not in bunny_map:
                    bunny_map[b] = []
                bunny_map[b].append( (i+1, j+1) )  # 1-indexed
        # Binary search on s
        low = 0
        high = max(R, C)
        answer = high
        while low <= high:
            mid = (low + high) //2
            # Compute N_total
            term1 = R*(2*mid +1) - mid*(mid +1)
            term2 = C*(2*mid +1) - mid*(mid +1)
            N_total = term1 * term2 - R*C
            # Compute N_same
            N_same =0
            for cells in bunny_map.values():
                m = len(cells)
                if m <2:
                    continue
                sorted_cells = sorted(cells, key=lambda x: (x[0], x[1]))
                n = m
                count =0
                j_sorted = [cell[1] for cell in sorted_cells]
                left =0
                for right in range(n):
                    i_right, j_right = sorted_cells[right]
                    while left <= right and i_right - sorted_cells[left][0] > mid:
                        left +=1
                    # Now, cells[left..right] have i within s
                    # Find j within [j_right -s, j_right +s]
                    low_j = j_right - mid
                    high_j_val = j_right + mid
                    l_idx = bisect_left(j_sorted, low_j, left, right+1)
                    r_idx = bisect_right(j_sorted, high_j_val, left, right+1)
                    count += (r_idx - l_idx) -1  # exclude self
                N_same += count *2  # ordered pairs
            # Compute N_valid
            N_valid = N_total - N_same
            if N_valid >= K:
                answer = mid
                high = mid -1
            else:
                low = mid +1
        print(f"Case #{test_case}: {answer}")

threading.Thread(target=main).start()