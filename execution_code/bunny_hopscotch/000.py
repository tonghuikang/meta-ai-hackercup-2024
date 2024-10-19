import sys
import numpy as np
from scipy.signal import fftconvolve

def readints():
    import sys
    return list(map(int, sys.stdin.read().split()))

def main():
    data = readints()
    idx = 0
    T = data[idx]; idx += 1
    for test_case in range(1, T+1):
        R, C, K = data[idx], data[idx+1], data[idx+2]; idx +=3
        B = []
        owner_positions = {}
        for i in range(R):
            row = data[idx: idx + C]; idx += C
            B.append(row)
            for j in range(C):
                b = row[j]
                if b not in owner_positions:
                    owner_positions[b] = []
                owner_positions[b].append( (i, j) )
        # Binary search over possible scores
        left = 1
        right = max(R, C)
        result = right
        while left <= right:
            mid = (left + right) // 2
            # Compute F_total(s)
            Fs_total = ((2*mid +1)*R - mid*(mid +1)) * ((2*mid +1)*C - mid*(mid +1))
            # Compute sum_b A_b(s)
            sum_A_b = 0
            for b, positions in owner_positions.items():
                n_b = len(positions)
                if n_b <=1:
                    continue
                # Create binary grid
                grid = np.zeros((R, C), dtype=np.int32)
                for (i,j) in positions:
                    grid[i,j] = 1
                # Perform convolution with window size (2s+1, 2s+1)
                # Using FFT-based convolution for efficiency
                window_size = 2*mid +1
                window = np.ones((window_size, window_size), dtype=np.int32)
                convolved = fftconvolve(grid, window, mode='same').astype(np.int32)
                # Subtract self-count
                convolved -= grid
                # Total A_b(s) is sum of convolved
                sum_A_b += convolved.sum()
            # Now, F_different(s) = Fs_total - sum_A_b
            F_different = Fs_total - sum_A_b
            if F_different >= K:
                result = mid
                right = mid -1
            else:
                left = mid +1
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()