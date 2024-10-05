import sys
import threading
import random
from math import gcd
from collections import defaultdict

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        points = []
        for _ in range(N):
            x = int(data[idx]); y = int(data[idx+1]); idx +=2
            points.append( (x, y) )
        if N <= 2:
            M = 0
            print(f"Case #{test_case}: {M}")
            continue
        # Determine number of samples
        S = 30
        if N < S:
            sample_points = points
        else:
            sample_points = random.sample(points, S)
        max_collinear = 0
        for p in sample_points:
            slopes = defaultdict(int)
            x1, y1 = p
            for p2 in points:
                if p2 == p:
                    continue
                x2, y2 = p2
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0:
                    key = ('inf', 0)
                elif dy == 0:
                    key = (0, 'inf')
                else:
                    sign = 1
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    if dy < 0:
                        sign = -1
                        dy = -dy
                    g = gcd(abs(dy), abs(dx))
                    reduced_dy = dy // g
                    reduced_dx = dx // g
                    key = (reduced_dy * sign, reduced_dx)
                slopes[key] +=1
            current_max = 1
            if slopes:
                current_max += max(slopes.values())
            if current_max > max_collinear:
                max_collinear = current_max
            if max_collinear == N:
                break
        M = N - max_collinear
        # To ensure within [M, 2*M], we can cap it
        # But problem allows any value between M and 2*M
        print(f"Case #{test_case}: {M}")
        
threading.Thread(target=main).start()