import sys
import math
import random
from collections import defaultdict

def readints():
    return list(map(int, sys.stdin.read().split()))

def max_colinear_exact(points):
    n = len(points)
    max_k = 1
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
                gcd = math.gcd(dy, dx)
                slope = (dy // gcd, dx // gcd)
            slopes[slope] += 1
        current_max = max(slopes.values(), default=0) + 1
        if current_max > max_k:
            max_k = current_max
    return max_k

def max_colinear_sampled(points, sample_size=500):
    n = len(points)
    if n == 0:
        return 0
    max_k = 1
    sampled_indices = random.sample(range(n), min(sample_size, n))
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
                gcd = math.gcd(dy, dx)
                slope = (dy // gcd, dx // gcd)
            slopes[slope] += 1
        current_max = max(slopes.values(), default=0) + 1
        if current_max > max_k:
            max_k = current_max
    return max_k

def main():
    data = readints()
    idx = 0
    T = data[idx]
    idx += 1
    for tc in range(1, T+1):
        N = data[idx]
        idx +=1
        points = []
        for _ in range(N):
            x = data[idx]
            y = data[idx+1]
            points.append((x, y))
            idx +=2
        if N <= 5000:
            K = max_colinear_exact(points)
        else:
            K = max_colinear_sampled(points, sample_size=500)
        M = N - K
        print(f"Case #{tc}: {M}")

if __name__ == "__main__":
    main()