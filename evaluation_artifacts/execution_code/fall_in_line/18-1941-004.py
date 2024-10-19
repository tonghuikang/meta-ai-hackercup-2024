import sys
import random
from math import gcd
import threading

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx += 1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        points = []
        for _ in range(N):
            x = int(data[idx]); idx +=1
            y = int(data[idx]); idx +=1
            points.append( (x, y) )
        if N <= 2:
            M = 0
            print(f"Case #{test_case}: {M}")
            continue
        # If N is small, do exact
        if N <= 3000:
            max_count = 0
            for i in range(N):
                slopes = {}
                xi, yi = points[i]
                for j in range(N):
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
                        if dx * dy < 0:
                            sign = -1
                        dx = abs(dx)
                        dy = abs(dy)
                        g = gcd(dy, dx)
                        reduced_dy = dy // g
                        reduced_dx = dx // g
                        slope = (sign * reduced_dy, reduced_dx)
                    slopes[slope] = slopes.get(slope, 0) +1
                current_max = max(slopes.values()) +1
                if current_max > max_count:
                    max_count = current_max
                if max_count == N:
                    break
            M = N - max_count
            print(f"Case #{test_case}: {M}")
            continue
        # For large N, use random sampling
        # Number of samples depends on the number of points
        # To keep it fast, limit the number of samples
        sample_size = 30
        sampled_points = random.sample(points, min(sample_size, N))
        max_count = 0
        for i in range(len(sampled_points)):
            xi, yi = sampled_points[i]
            slopes = {}
            for j in range(N):
                if points[j] == (xi, yi):
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
                    if dx * dy < 0:
                        sign = -1
                    dx = abs(dx)
                    dy = abs(dy)
                    g = gcd(dy, dx)
                    reduced_dy = dy // g
                    reduced_dx = dx // g
                    slope = (sign * reduced_dy, reduced_dx)
                slopes[slope] = slopes.get(slope, 0) +1
            if slopes:
                current_max = max(slopes.values()) +1
                if current_max > max_count:
                    max_count = current_max
            else:
                current_max =1
                if current_max > max_count:
                    max_count = current_max
        M = N - max_count
        print(f"Case #{test_case}: {M}")

threading.Thread(target=main,).start()