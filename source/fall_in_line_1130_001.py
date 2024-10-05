import sys
import random
from math import gcd
from collections import defaultdict

def readints():
    return list(map(int, sys.stdin.readline().split()))

def max_colinear(points, sample_size=500):
    n = len(points)
    if n == 0:
        return 0
    max_count = 1
    if n <= 1000:
        # Exact computation
        for i in range(n):
            slopes = defaultdict(int)
            xi, yi = points[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi
                if dx == 0:
                    slope = ('inf', 0)
                elif dy == 0:
                    slope = (0, 0)
                else:
                    sign = 1
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    if dy < 0:
                        sign = -1
                        dy = -dy
                    g = gcd(dx, dy)
                    slope = (sign * dy // g, dx // g)
                slopes[slope] += 1
            current_max = max(slopes.values(), default=0) + 1
            if current_max > max_count:
                max_count = current_max
        return max_count
    else:
        # Approximate with random sampling
        sample_size = min(sample_size, n)
        sampled_indices = random.sample(range(n), sample_size)
        for i in sampled_indices:
            slopes = defaultdict(int)
            xi, yi = points[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi
                if dx == 0:
                    slope = ('inf', 0)
                elif dy == 0:
                    slope = (0, 0)
                else:
                    sign = 1
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    if dy < 0:
                        sign = -1
                        dy = -dy
                    g = gcd(dx, dy)
                    slope = (sign * dy // g, dx // g)
                slopes[slope] += 1
            current_max = max(slopes.values(), default=0) + 1
            if current_max > max_count:
                max_count = current_max
        return max_count

def main():
    import sys
    import threading

    def run():
        T = int(sys.stdin.readline())
        for test_case in range(1, T + 1):
            N = int(sys.stdin.readline())
            points = []
            for _ in range(N):
                x, y = map(int, sys.stdin.readline().split())
                points.append((x, y))
            max_colinear_points = max_colinear(points)
            min_moves = N - max_colinear_points
            print(f"Case #{test_case}: {min_moves}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()