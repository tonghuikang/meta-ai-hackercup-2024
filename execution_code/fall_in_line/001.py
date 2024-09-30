from collections import defaultdict
from math import gcd
import sys
from sys import stdin

def read_input():
    input = stdin.read().splitlines()
    idx = 0
    T = int(input[idx])
    idx += 1
    test_cases = []
    
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        points = []
        for _ in range(N):
            x, y = map(int, input[idx].split())
            points.append((x, y))
            idx += 1
        test_cases.append(points)
    
    return test_cases

def max_on_same_line(points):
    n = len(points)
    if n <= 2:
        return n
    
    max_count = 1
    
    for i in range(n):
        slopes = defaultdict(int)
        for j in range(n):
            if i == j:
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0:  # Vertical line
                slope = ('inf', points[i][0])  # Vertical lines can be uniquely identified
            elif dy == 0:  # Horizontal line
                slope = (0, points[i][1])  # Horizontal lines
            else:
                sign = 1 if (dx * dy) > 0 else -1
                dx = abs(dx)
                dy = abs(dy)
                common_gcd = gcd(dx, dy)
                reduced_dx = (dx // common_gcd) * sign
                reduced_dy = dy // common_gcd
                slope = (reduced_dx, reduced_dy)

            slopes[slope] += 1
        
        if slopes:
            max_count = max(max_count, max(slopes.values()) + 1)  # +1 for the original point
    
    return max_count

def solve():
    test_cases = read_input()
    results = []
    
    for i, points in enumerate(test_cases):
        n = len(points)
        max_aligned = max_on_same_line(points)
        moves_needed = n - max_aligned
        results.append(f"Case #{i + 1}: {moves_needed}")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()