import sys, math, random
from collections import defaultdict

def main():
    import sys
    import math
    import random
    from collections import defaultdict

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx += 1

    for test_case in range(1, T + 1):
        N = int(input[idx]); idx += 1
        points = []
        for _ in range(N):
            x = int(input[idx]); y = int(input[idx+1]); idx += 2
            points.append((x, y))
        
        if N <= 3000:
            max_count = 0
            for i in range(N):
                slopes = defaultdict(int)
                xi, yi = points[i]
                for j in range(N):
                    if j == i:
                        continue
                    xj, yj = points[j]
                    dy = yj - yi
                    dx = xj - xi
                    if dx == 0:
                        key = ('inf', 0)
                    elif dy == 0:
                        key = (0, 0)
                    else:
                        if dx < 0:
                            dy = -dy
                            dx = -dx
                        gcd = math.gcd(abs(dy), abs(dx))
                        dy_reduced = dy // gcd
                        dx_reduced = dx // gcd
                        key = (dy_reduced, dx_reduced)
                    slopes[key] += 1
                current_max = max(slopes.values(), default=0) + 1
                if current_max > max_count:
                    max_count = current_max
                if max_count == N:
                    break
            M = N - max_count
        else:
            K = 30
            sample_size = min(K, N)
            sample_indices = random.sample(range(N), sample_size)
            max_count = 0
            for i in sample_indices:
                slopes = defaultdict(int)
                xi, yi = points[i]
                for j in range(N):
                    if j == i:
                        continue
                    xj, yj = points[j]
                    dy = yj - yi
                    dx = xj - xi
                    if dx == 0:
                        key = ('inf', 0)
                    elif dy == 0:
                        key = (0, 0)
                    else:
                        if dx < 0:
                            dy = -dy
                            dx = -dx
                        gcd = math.gcd(abs(dy), abs(dx))
                        dy_reduced = dy // gcd
                        dx_reduced = dx // gcd
                        key = (dy_reduced, dx_reduced)
                    slopes[key] += 1
                current_max = max(slopes.values(), default=0) + 1
                if current_max > max_count:
                    max_count = current_max
                if max_count >= N // 2:
                    break
            M = N - max_count
        
        print(f"Case #{test_case}: {M}")

if __name__ == "__main__":
    main()