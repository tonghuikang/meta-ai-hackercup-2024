import sys
import random
import math
import numpy as np

def readints():
    return list(map(int, sys.stdin.read().split()))

def main():
    data = readints()
    idx = 0
    T = data[idx]
    idx +=1
    for test_case in range(1, T+1):
        N = data[idx]
        idx +=1
        xs = []
        ys = []
        for _ in range(N):
            x = data[idx]
            y = data[idx+1]
            xs.append(x)
            ys.append(y)
            idx +=2
        if N <= 3000:
            # Exact computation
            max_colinear = 1
            for i in range(N):
                slopes = {}
                same = 0
                xi, yi = xs[i], ys[i]
                for j in range(N):
                    if j == i:
                        continue
                    xj, yj = xs[j], ys[j]
                    dy = yj - yi
                    dx = xj - xi
                    if dx ==0:
                        slope = ('inf', 0)
                    else:
                        gcd = math.gcd(dy, dx)
                        dy_reduced = dy // gcd
                        dx_reduced = dx // gcd
                        if dx_reduced <0:
                            dy_reduced = -dy_reduced
                            dx_reduced = -dx_reduced
                        slope = (dy_reduced, dx_reduced)
                    slopes[slope] = slopes.get(slope, 0) +1
                current_max = max(slopes.values(), default=0) +1
                if current_max > max_colinear:
                    max_colinear = current_max
            M = N - max_colinear
        else:
            # Approximate for large N
            xs_np = np.array(xs)
            ys_np = np.array(ys)
            max_colinear = 0
            K = 500
            for _ in range(K):
                i, j = random.sample(range(N),2)
                xi, yi = xs[i], ys[i]
                xj, yj = xs[j], ys[j]
                dy = yj - yi
                dx = xj - xi
                if dx ==0:
                    # Vertical line: x = xi
                    count = np.sum(xs_np == xi)
                else:
                    # Compute A*x + B*y + C =0
                    A = dy
                    B = -dx
                    C = dx*yi - dy*xi
                    # To avoid floating point, compute A*x + B*y + C
                    vals = A*xs_np + B*ys_np + C
                    count = np.sum(vals ==0)
                if count > max_colinear:
                    max_colinear = count
                # Early stopping if all points are on a line
                if max_colinear == N:
                    break
            M = N - max_colinear
        print(f"Case #{test_case}: {M}")

if __name__ == "__main__":
    main()