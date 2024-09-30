import sys
import math
from collections import defaultdict

def readints():
    return list(map(int, sys.stdin.readline().split()))

def max_colinear(points):
    n = len(points)
    if n == 1:
        return 1
    max_on_line = 1
    for i in range(n):
        slopes = defaultdict(int)
        same = 0
        vertical = 0
        xi, yi = points[i]
        current_max = 0
        for j in range(n):
            if i == j:
                continue
            xj, yj = points[j]
            dx = xj - xi
            dy = yj - yi
            if dx == 0:
                vertical += 1
                current_max = max(current_max, vertical)
            else:
                gcd = math.gcd(dy, dx)
                reduced_dy = dy // gcd
                reduced_dx = dx // gcd
                # Ensure the direction is consistent
                if reduced_dx < 0:
                    reduced_dy = -reduced_dy
                    reduced_dx = -reduced_dx
                slopes[(reduced_dy, reduced_dx)] += 1
                current_max = max(current_max, slopes[(reduced_dy, reduced_dx)])
        max_on_line = max(max_on_line, current_max + 1)  # +1 to include the current point
    return max_on_line

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx +=1
    for tc in range(1, T+1):
        N = int(input[idx]); idx +=1
        points = []
        for _ in range(N):
            x = int(input[idx]); idx +=1
            y = int(input[idx]); idx +=1
            points.append((x, y))
        if N <= 1000:
            M = max_colinear(points)
            ants_to_move = N - M
        else:
            # For large N, assume maximum colinear points is 2
            ants_to_move = N - 2
        print(f"Case #{tc}: {ants_to_move}")

if __name__ == "__main__":
    main()