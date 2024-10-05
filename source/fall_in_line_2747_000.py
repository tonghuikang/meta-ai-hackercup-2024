import sys
import math
from collections import defaultdict

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for tc in range(1, T + 1):
        N = int(input[ptr])
        ptr += 1
        points = []
        for _ in range(N):
            x = int(input[ptr])
            y = int(input[ptr + 1])
            points.append((x, y))
            ptr += 2

        if N <= 1000:
            # Exact approach for small N
            max_collinear = 1
            for i in range(N):
                slopes = {}
                x1, y1 = points[i]
                for j in range(N):
                    if i == j:
                        continue
                    x2, y2 = points[j]
                    dx = x2 - x1
                    dy = y2 - y1
                    if dx == 0:
                        slope = ('inf', 0)
                    else:
                        g = math.gcd(dy, dx)
                        slope = (dy // g, dx // g)
                    if slope in slopes:
                        slopes[slope] += 1
                    else:
                        slopes[slope] = 1
                    current = slopes[slope] + 1
                    if current > max_collinear:
                        max_collinear = current
            M = N - max_collinear
        else:
            # Approximation approach for large N
            count_x = defaultdict(int)
            count_y = defaultdict(int)
            for x, y in points:
                count_x[x] += 1
                count_y[y] += 1
            max_freq = 0
            if count_x:
                max_freq = max(count_x.values())
            if count_y:
                max_freq = max(max_freq, max(count_y.values()))
            M = N - max_freq

        print(f"Case #{tc}: {M}")

if __name__ == "__main__":
    main()