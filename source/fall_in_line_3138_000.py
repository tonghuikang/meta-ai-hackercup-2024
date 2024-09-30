import sys
import random
from math import gcd

def main():
    import sys
    import sys
    from math import gcd
    import sys
    def readints():
        import sys
        return list(map(int, sys.stdin.readline().split()))
    
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr]); ptr +=1
    for test_case in range(1, T +1):
        N = int(input[ptr]); ptr +=1
        points = []
        for _ in range(N):
            x = int(input[ptr]); ptr +=1
            y = int(input[ptr]); ptr +=1
            points.append( (x, y) )
        if N <= 500:
            max_on_line = 0
            for i in range(N):
                slopes = {}
                p = points[i]
                for j in range(N):
                    if i == j:
                        continue
                    q = points[j]
                    dx = q[0] - p[0]
                    dy = q[1] - p[1]
                    if dx ==0 and dy ==0:
                        continue
                    elif dx ==0:
                        slope = ('inf', 0)
                    elif dy ==0:
                        slope = (0, 0)
                    else:
                        sign = 1
                        if dx * dy <0:
                            sign = -1
                        dx_abs = abs(dx)
                        dy_abs = abs(dy)
                        g = gcd(dy_abs, dx_abs)
                        slope = (sign * (dy_abs // g), dx_abs // g)
                    if slope in slopes:
                        slopes[slope] +=1
                    else:
                        slopes[slope] =1
                current_max = max(slopes.values(), default=0) +1
                if current_max > max_on_line:
                    max_on_line = current_max
        else:
            k = 30
            max_on_line = 0
            for _ in range(k):
                idx = random.randint(0, N-1)
                p = points[idx]
                slopes = {}
                current_max =0
                for q in points:
                    if p == q:
                        continue
                    dx = q[0] - p[0]
                    dy = q[1] - p[1]
                    if dx ==0 and dy ==0:
                        continue
                    elif dx ==0:
                        slope = ('inf', 0)
                    elif dy ==0:
                        slope = (0, 0)
                    else:
                        sign = 1
                        if dx * dy <0:
                            sign = -1
                        dx_abs = abs(dx)
                        dy_abs = abs(dy)
                        g = gcd(dy_abs, dx_abs)
                        slope = (sign * (dy_abs // g), dx_abs // g)
                    if slope in slopes:
                        slopes[slope] +=1
                        if slopes[slope] > current_max:
                            current_max = slopes[slope]
                    else:
                        slopes[slope] =1
                        if slopes[slope] > current_max:
                            current_max = slopes[slope]
                current_max +=1
                if current_max > max_on_line:
                    max_on_line = current_max
            # Edge case: if all points are unique and no line has more than 2 points
            if max_on_line ==0:
                max_on_line =1
        M = N - max_on_line
        print(f"Case #{test_case}: {M}")

if __name__ == "__main__":
    main()