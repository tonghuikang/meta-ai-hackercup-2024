import sys
import math
import sys
import sys
from math import gcd

MOD = 10**9 + 7

def count_boundary_points(x1, y1, x2, y2):
    return gcd(abs(x2 - x1), abs(y2 - y1)) + 1

def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)

def count_lattice_points_in_triangle(x1, y1, x2, y2, x3, y3):
    area = triangle_area(x1, y1, x2, y2, x3, y3)
    # Count boundary points
    B = (count_boundary_points(x1, y1, x2, y2) +
         count_boundary_points(x2, y2, x3, y3) +
         count_boundary_points(x3, y3, x1, y1) - 3)
    # Pick's theorem
    I = int(area - B / 2 + 1)
    return I + B  # Total points inside and on boundary

def is_inside_circle(x, y, R_sq):
    return x*x + y*y <= R_sq

def main():
    import sys
    import threading
    def run():
        T = int(sys.stdin.readline())
        for tc in range(1, T + 1):
            N, R = map(int, sys.stdin.readline().split())
            R_sq = R * R
            total = 0
            for _ in range(N):
                X1, Y1, X2, Y2, X3, Y3 = map(int, sys.stdin.readline().split())
                # Check if all vertices are inside or on the circle
                in1 = is_inside_circle(X1, Y1, R_sq)
                in2 = is_inside_circle(X2, Y2, R_sq)
                in3 = is_inside_circle(X3, Y3, R_sq)
                if in1 and in2 and in3:
                    # Fully inside, use Pick's theorem
                    count = count_lattice_points_in_triangle(X1, Y1, X2, Y2, X3, Y3)
                    total = (total + count) % MOD
                else:
                    # Partially intersecting, iterate over bounding box
                    min_x = min(X1, X2, X3)
                    max_x = max(X1, X2, X3)
                    min_y = min(Y1, Y2, Y3)
                    max_y = max(Y1, Y2, Y3)
                    count = 0
                    for x in range(min_x, max_x + 1):
                        if x*x > R_sq:
                            continue
                        y_limit_sq = R_sq - x*x
                        y_min_circle = -int(math.isqrt(y_limit_sq))
                        y_max_circle = int(math.isqrt(y_limit_sq))
                        ymin = max(min_y, y_min_circle)
                        ymax = min(max_y, y_max_circle)
                        for y in range(ymin, ymax + 1):
                            # Point inside circle already
                            # Check if inside triangle using barycentric coordinates
                            det = (Y2 - Y3)*(X1 - X3) + (X3 - X2)*(Y1 - Y3)
                            if det == 0:
                                continue
                            a = ((Y2 - Y3)*(x - X3) + (X3 - X2)*(y - Y3)) / det
                            b = ((Y3 - Y1)*(x - X3) + (X1 - X3)*(y - Y3)) / det
                            c = 1 - a - b
                            if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
                                count += 1
                    total = (total + count) % MOD
            print(f"Case #{tc}: {total}")
    threading.Thread(target=run).start()