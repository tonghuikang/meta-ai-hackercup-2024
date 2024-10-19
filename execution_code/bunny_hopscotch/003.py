import sys
import bisect

import threading
def main():
    import sys

    import sys

    sys.setrecursionlimit(1 << 25)
    T=int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R,C,K=map(int, sys.stdin.readline().split())
        owner_to_cells={}
        for i in range(1,R+1):
            row = list(map(int, sys.stdin.readline().split()))
            for j in range(1,C+1):
                owner = row[j-1]
                if owner not in owner_to_cells:
                    owner_to_cells[owner]=[]
                owner_to_cells[owner].append( (i,j) )
        owners_with_multiple = [cells for cells in owner_to_cells.values() if len(cells)>=2]
        def count_same_non_identity(S):
            total=0
            for cells in owners_with_multiple:
                # Sort cells by row, then column
                cells_sorted = sorted(cells)
                sorted_j = []
                start =0
                n = len(cells_sorted)
                j_list = []
                for idx in range(n):
                    i,j = cells_sorted[idx]
                    # Remove cells with row < i -S
                    while start < n and cells_sorted[start][0] < i - S:
                        old_j = cells_sorted[start][1]
                        pos = bisect.bisect_left(sorted_j, old_j)
                        if pos < len(sorted_j) and sorted_j[pos]==old_j:
                            sorted_j.pop(pos)
                        start +=1
                    # Count number of j in [j -S, j +S]
                    left = j - S
                    right = j + S
                    l = bisect.bisect_left(sorted_j, left)
                    r = bisect.bisect_right(sorted_j, right)
                    total += r - l
                    # Insert current j
                    bisect.insort(sorted_j, j)
            return total
        def count_total_pairs(S):
            term1 = (2*S +1)*R - S*(S+1)
            term2 = (2*S +1)*C - S*(S+1)
            total = term1 * term2 - R * C
            return total
        # Binary search over S
        low=0
        high = max(R,C)
        answer = high
        while low <= high:
            mid = (low + high) //2
            total_pairs = count_total_pairs(mid)
            same_pairs = count_same_non_identity(mid)
            diff_pairs = total_pairs - same_pairs
            if diff_pairs >= K:
                answer=mid
                high=mid -1
            else:
                low=mid +1
        print(f"Case #{test_case}: {answer}")

threading.Thread(target=main,).start()