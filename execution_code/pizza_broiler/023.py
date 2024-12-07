import sys
import math
from math import gcd
from collections import defaultdict

MOD = 10**9 + 7

def readints():
    return list(map(int, sys.stdin.readline().split()))

def count_boundary_points(x1, y1, x2, y2, x3, y3):
    # Function to count boundary points of a triangle using gcd
    def edge_points(xa, ya, xb, yb):
        return gcd(abs(xb - xa), abs(yb - ya)) + 1
    B = edge_points(x1, y1, x2, y2) + edge_points(x2, y2, x3, y3) + edge_points(x3, y3, x1, y1) - 3
    return B

def triangle_area(x1, y1, x2, y2, x3, y3):
    # Calculate the area of the triangle using determinant
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2)

def point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    # Barycentric coordinate method to check if point is in triangle
    denom = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    if denom == 0:
        return False
    a = ((y2 - y3)*(px - x3) + (x3 - x2)*(py - y3)) / denom
    b = ((y3 - y1)*(px - x3) + (x1 - x3)*(py - y3)) / denom
    c = 1 - a - b
    return 0 <= a <=1 and 0 <= b <=1 and 0 <= c <=1

def count_lattice_points_in_triangle_and_circle(x1, y1, x2, y2, x3, y3, R):
    # Find bounding box of the triangle
    min_x = max(min(x1, x2, x3), -R)
    max_x = min(max(x1, x2, x3), R)
    min_y = max(min(y1, y2, y3), -R)
    max_y = min(max(y1, y2, y3), R)
    count = 0
    R_sq = R * R
    for y in range(min_y, max_y + 1):
        # For given y, find intersection with circle
        try:
            x_limit = int(math.floor(math.sqrt(R_sq - y*y)))
        except:
            x_limit = -1
        if x_limit == -1:
            continue
        # Find intersection of triangle with this y
        # Find segments of triangle that intersect this y
        intersections = []
        vertices = [(x1, y1), (x2, y2), (x3, y3)]
        for i in range(3):
            (x_start, y_start) = vertices[i]
            (x_end, y_end) = vertices[(i+1)%3]
            if y_start == y_end:
                continue
            if y < min(y_start, y_end) or y > max(y_start, y_end):
                continue
            # Compute intersection x
            x = x_start + (x_end - x_start) * (y - y_start) / (y_end - y_start)
            intersections.append(x)
        if len(intersections) < 2:
            continue
        intersections.sort()
        x_min = math.ceil(min(intersections))
        x_max = math.floor(max(intersections))
        # Now intersect with circle's x range
        x_min = max(x_min, -x_limit)
        x_max = min(x_max, x_limit)
        if x_min > x_max:
            continue
        count += max(0, x_max - x_min + 1)
    return count

def main():
    import sys
    import threading
    def run():
        T = int(sys.stdin.readline())
        for tc in range(1, T+1):
            N, R = map(int, sys.stdin.readline().split())
            total = 0
            for _ in range(N):
                x1, y1, x2, y2, x3, y3 = map(int, sys.stdin.readline().split())
                # Check if all vertices inside the circle
                inside = True
                for x, y in [(x1,y1), (x2,y2), (x3,y3)]:
                    if x*x + y*y > R*R:
                        inside = False
                        break
                if inside:
                    # Use Pick's theorem
                    area = triangle_area(x1, y1, x2, y2, x3, y3)
                    B = count_boundary_points(x1, y1, x2, y2, x3, y3)
                    I = area - B/2 +1
                    total += int(I + B)
                else:
                    # Need to count lattice points in intersection
                    cnt = count_lattice_points_in_triangle_and_circle(x1, y1, x2, y2, x3, y3, R)
                    total += cnt
            print(f"Case #{tc}: {total % MOD}")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()