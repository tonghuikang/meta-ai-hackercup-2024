import sys
import math
from collections import defaultdict

MOD = 10**9 + 7

def readints():
    return list(map(int, sys.stdin.readline().split()))

def lattice_points_in_circle(R):
    points = []
    for x in range(-R, R+1):
        y_limit = int(math.isqrt(R*R - x*x))
        for y in range(-y_limit, y_limit+1):
            points.append((x, y))
    return points

def point_in_triangle(px, py, tri):
    (x1, y1), (x2, y2), (x3, y3) = tri
    # Barycentric coordinates
    denominator = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    if denominator == 0:
        return False
    a = ((y2 - y3)*(px - x3) + (x3 - x2)*(py - y3)) / denominator
    b = ((y3 - y1)*(px - x3) + (x1 - x3)*(py - y3)) / denominator
    c = 1 - a - b
    return (0 <= a <= 1) and (0 <= b <= 1) and (0 <= c <= 1)

def main():
    import sys
    import math

    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N, R = map(int, sys.stdin.readline().split())
        triangles = []
        for _ in range(N):
            coords = list(map(int, sys.stdin.readline().split()))
            tri = [(coords[0], coords[1]), (coords[2], coords[3]), (coords[4], coords[5])]
            triangles.append(tri)
        
        points = lattice_points_in_circle(R)
        heat = 0
        for tri in triangles:
            # Bounding box for the triangle
            min_x = min(p[0] for p in tri)
            max_x = max(p[0] for p in tri)
            min_y = min(p[1] for p in tri)
            max_y = max(p[1] for p in tri)
            count = 0
            for (x, y) in points:
                if min_x <= x <= max_x and min_y <= y <= max_y:
                    if point_in_triangle(x, y, tri):
                        count += 1
            heat = (heat + count) % MOD
        print(f"Case #{tc}: {heat}")

if __name__ == "__main__":
    main()