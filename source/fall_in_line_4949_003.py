import sys
import random
from math import gcd
from collections import defaultdict

def readints():
    import sys
    return list(map(int, sys.stdin.readline().split()))

def main():
    import sys
    import sys
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N = int(sys.stdin.readline())
        points = []
        point_set = set()
        for _ in range(N):
            x, y = map(int, sys.stdin.readline().split())
            points.append( (x, y) )
            point_set.add( (x, y) )
        if N <= 2:
            print(f"Case #{tc}: 0")
            continue
        s_max = 0
        # Number of samples
        k = 500
        if N < k:
            sample_points = points
        else:
            sample_points = random.sample(points, k)
        # To store lines already checked
        checked_lines = {}
        for p in sample_points:
            slopes = defaultdict(int)
            same = 1
            x1, y1 = p
            for q in points:
                if q == p:
                    continue
                x2, y2 = q
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0 and dy == 0:
                    same +=1
                    continue
                elif dx == 0:
                    slope = ('inf', 0)
                elif dy == 0:
                    slope = (0, 0)
                else:
                    sign = 1
                    if dx * dy < 0:
                        sign = -1
                    dx_abs = abs(dx)
                    dy_abs = abs(dy)
                    g = gcd(dx_abs, dy_abs)
                    slope = (sign * dy_abs // g, dx_abs // g)
                slopes[slope] +=1
            current_max = same
            for cnt in slopes.values():
                if cnt + same > current_max:
                    current_max = cnt + same
            if current_max > s_max:
                s_max = current_max
            if s_max >= N:
                break
        M = N - s_max
        print(f"Case #{tc}: {M}")

if __name__ == "__main__":
    main()