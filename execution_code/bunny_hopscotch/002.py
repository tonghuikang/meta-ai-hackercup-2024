import sys
import numpy as np

def readints():
    import sys
    return list(map(int, sys.stdin.read().split()))

def main():
    data = readints()
    ptr = 0
    T = data[ptr]; ptr +=1
    for tc in range(1, T+1):
        R = data[ptr]; C = data[ptr+1]; K = data[ptr+2]; ptr +=3
        B = []
        for _ in range(R):
            row = data[ptr:ptr+C]
            B.append(row)
            ptr +=C
        # Group cells by owner
        owner_dict = {}
        for i in range(R):
            for j in range(C):
                owner = B[i][j]
                if owner not in owner_dict:
                    owner_dict[owner] = []
                owner_dict[owner].append( (i,j) )
        # Binary search
        low = 0
        high = max(R, C)
        while low < high:
            mid = (low + high) //2
            # Compute total_ordered_pairs <=mid
            rows_count = R*(2*mid +1) - mid*(mid +1)
            cols_count = C*(2*mid +1) - mid*(mid +1)
            total_ordered_pairs = rows_count * cols_count - R * C
            # Compute total_ordered_pairs_same_owner
            total_same = 0
            for owner, points in owner_dict.items():
                n = len(points)
                if n <2:
                    continue
                # Create grid
                G = np.zeros( (R, C), dtype=np.int32)
                rows, cols = zip(*points)
                G[rows, cols] =1
                # Compute summed area table
                S = G.cumsum(axis=0).cumsum(axis=1)
                # Convert points to numpy arrays
                points_np = np.array(points)
                i = points_np[:,0]
                j = points_np[:,1]
                i1 = np.maximum(i - mid, 0)
                j1 = np.maximum(j - mid, 0)
                i2 = np.minimum(i + mid, R -1)
                j2 = np.minimum(j + mid, C -1)
                # Get counts using summed area table
                counts = S[i2, j2].astype(np.int64)
                mask_i1 = (i1 >0)
                counts[mask_i1] -= S[i1[mask_i1]-1, j2[mask_i1]]
                mask_j1 = (j1 >0)
                counts[mask_j1] -= S[i2[mask_j1], j1[mask_j1]-1]
                mask_both = (i1 >0) & (j1 >0)
                counts[mask_both] += S[i1[mask_both]-1, j1[mask_both]-1]
                # Subtract self
                sum_counts_x = counts.sum() - n
                total_same += sum_counts_x
            # Compute different owner pairs
            total_diff = total_ordered_pairs - total_same
            if total_diff >= K:
                high = mid
            else:
                low = mid +1
        print(f"Case #{tc}: {low}")

if __name__ == "__main__":
    main()