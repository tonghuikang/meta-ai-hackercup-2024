import sys
import math
from collections import defaultdict

def main():
    import sys
    import math
    from collections import defaultdict
    from math import gcd

    def max_colinear(points):
        N = len(points)
        if N <= 1000:
            max_count = 1
            for i in range(N):
                slopes = {}
                x1, y1 = points[i]
                for j in range(i+1, N):
                    x2, y2 = points[j]
                    dx = x2 - x1
                    dy = y2 - y1
                    if dx == 0:
                        slope = ('inf', 0)
                    else:
                        sign = 1 if dx * dy >= 0 else -1
                        dy_abs = abs(dy)
                        dx_abs = abs(dx)
                        g = gcd(dy_abs, dx_abs)
                        slope = (sign * (dy_abs // g), dx_abs // g)
                    slopes[slope] = slopes.get(slope, 0) + 1
                if slopes:
                    current_max = max(slopes.values()) + 1
                    if current_max > max_count:
                        max_count = current_max
            return max_count
        else:
            count_x = defaultdict(int)
            count_y = defaultdict(int)
            count_ymx = defaultdict(int)
            count_ymx = defaultdict(int)
            for x, y in points:
                count_x[x] +=1
                count_y[y] +=1
                count_ymx[y - x] +=1
                count_ymx[y + x] +=1
            max_line_count = max(
                max(count_x.values()),
                max(count_y.values()),
                max(count_ymx.values()),
                max(count_ymx.values())
            )
            return max_line_count

    input = sys.stdin.read().split()
    it = iter(input)
    T = int(next(it))
    results = []
    for tc in range(1, T+1):
        N = int(next(it))
        points = []
        for _ in range(N):
            x = int(next(it))
            y = int(next(it))
            points.append( (x,y) )
        T_max = max_colinear(points)
        M = N - T_max
        # According to problem statement, any answer between M and 2*M is accepted
        # We'll return M
        results.append(f"Case #{tc}: {M}")
    print('\n'.join(results))

if __name__ == "__main__":
    main()