import sys
import threading
import random
import math

def main():
    import sys
    import random
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N = int(sys.stdin.readline())
        points = []
        for _ in range(N):
            x_str, y_str = sys.stdin.readline().split()
            x = int(x_str)
            y = int(y_str)
            points.append((x, y))
        max_colinear = 1
        if N <= 5000:
            for i in range(N):
                slopes = {}
                xi, yi = points[i]
                for j in range(i + 1, N):
                    xj, yj = points[j]
                    dy = yj - yi
                    dx = xj - xi
                    if dx == 0:
                        slope = ('inf', 0)
                    else:
                        g = math.gcd(dy, dx)
                        dy //= g
                        dx //= g
                        if dx < 0:
                            dx = -dx
                            dy = -dy
                        slope = (dy, dx)
                    slopes[slope] = slopes.get(slope, 1) + 1
                    if slopes[slope] > max_colinear:
                        max_colinear = slopes[slope]
        else:
            K = min(20, N)
            sampled_indices = random.sample(range(N), K)
            for idx in sampled_indices:
                slopes = {}
                xi, yi = points[idx]
                for j in range(N):
                    if j == idx:
                        continue
                    xj, yj = points[j]
                    dy = yj - yi
                    dx = xj - xi
                    if dx == 0:
                        slope = ('inf', 0)
                    else:
                        g = math.gcd(dy, dx)
                        dy //= g
                        dx //= g
                        if dx < 0:
                            dx = -dx
                            dy = -dy
                        slope = (dy, dx)
                    slopes[slope] = slopes.get(slope, 1) + 1
                    if slopes[slope] > max_colinear:
                        max_colinear = slopes[slope]
        M = N - max_colinear
        # Ensure the output M is at least the minimal M
        print(f"Case #{case_num}: {M}")

threading.Thread(target=main).start()