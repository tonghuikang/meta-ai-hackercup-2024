import sys
import math
import random
from collections import defaultdict

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
        points = []
        for _ in range(N):
            x = data[idx]
            y = data[idx+1]
            points.append( (x,y) )
            idx +=2
        if N <= 1000:
            max_count = 1
            for i in range(N):
                slopes = defaultdict(int)
                x1, y1 = points[i]
                for j in range(N):
                    if i ==j:
                        continue
                    x2, y2 = points[j]
                    dy = y2 - y1
                    dx = x2 - x1
                    if dx ==0:
                        slope = ('inf', 0)
                    elif dy ==0:
                        slope = (0, 0)
                    else:
                        if dx <0:
                            dx = -dx
                            dy = -dy
                        g = math.gcd(abs(dy), abs(dx))
                        slope = (dy // g, dx //g)
                    slopes[slope] +=1
                current_max = 1 + (max(slopes.values()) if slopes else 0)
                if current_max > max_count:
                    max_count = current_max
        else:
            max_count =1
            K = 30
            if N < K:
                sample_points = points
            else:
                sample_points = random.sample(points, K)
            for p in sample_points:
                slopes = defaultdict(int)
                x1, y1 = p
                for q in points:
                    if q == p:
                        continue
                    x2, y2 = q
                    dy = y2 - y1
                    dx = x2 - x1
                    if dx ==0:
                        slope = ('inf', 0)
                    elif dy ==0:
                        slope = (0, 0)
                    else:
                        if dx <0:
                            dx = -dx
                            dy = -dy
                        g = math.gcd(abs(dy), abs(dx))
                        slope = (dy // g, dx //g)
                    slopes[slope] +=1
                current_max = 1 + (max(slopes.values()) if slopes else 0)
                if current_max > max_count:
                    max_count = current_max
        M = N - max_count
        print(f"Case #{test_case}: {M}")

if __name__ == "__main__":
    main()