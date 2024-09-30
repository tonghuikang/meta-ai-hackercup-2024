import sys
import math
import random
from collections import defaultdict

def readints():
    return list(map(int, sys.stdin.readline().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_colinear(points):
    N = len(points)
    if N <= 1:
        return N
    max_count = 1
    for i in range(N):
        slopes = defaultdict(int)
        xi, yi = points[i]
        for j in range(N):
            if i == j:
                continue
            xj, yj = points[j]
            dx = xj - xi
            dy = yj - yi
            if dx == 0:
                key = ('inf', 0)
            else:
                sign = 1
                if dx < 0:
                    dx = -dx
                    dy = -dy
                g = gcd(abs(dy), abs(dx))
                dy_reduced = dy // g
                dx_reduced = dx // g
                key = (dy_reduced, dx_reduced)
            slopes[key] +=1
        current_max = max(slopes.values(), default=0) +1
        if current_max > max_count:
            max_count = current_max
    return max_count

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    for test_case in range(1, T+1):
        N = int(input[ptr])
        ptr +=1
        points = []
        freq_x = defaultdict(int)
        freq_y = defaultdict(int)
        for _ in range(N):
            x = int(input[ptr])
            y = int(input[ptr+1])
            ptr +=2
            points.append( (x, y) )
            freq_x[x] +=1
            freq_y[y] +=1
        if N <=2000:
            M = max_colinear(points)
        else:
            max_freq_x = max(freq_x.values()) if freq_x else 0
            max_freq_y = max(freq_y.values()) if freq_y else 0
            M = max(max_freq_x, max_freq_y)
        answer = N - M
        print(f"Case #{test_case}: {answer}")

if __name__ == "__main__":
    main()