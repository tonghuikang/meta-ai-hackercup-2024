import sys
import math
from math import gcd

MOD = 10**9 + 7

def readints():
    return list(map(int, sys.stdin.readline().split()))

def lattice_points_in_triangle(vertices):
    (x1, y1), (x2, y2), (x3, y3) = vertices
    # Shoelace formula for area * 2
    shoelace = abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)
    # Boundary points
    B = gcd(abs(x2 - x1), abs(y2 - y1)) + gcd(abs(x3 - x2), abs(y3 - y2)) + gcd(abs(x1 - x3), abs(y1 - y3))
    A = shoelace / 2
    # From Pick's theorem: I = A - B/2 + 1
    I = A - B / 2 + 1
    # Total lattice points: I + B
    total = I + B
    return int(total)

def point_in_circle(x, y, R):
    return x*x + y*y <= R*R

def point_in_triangle(px, py, vertices):
    (x1, y1), (x2, y2), (x3, y3) = vertices
    # Barycentric coordinates
    det = (y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3)
    if det == 0:
        return False
    a = ((y2 - y3)*(px - x3) + (x3 - x2)*(py - y3)) / det
    b = ((y3 - y1)*(px - x3) + (x1 - x3)*(py - y3)) / det
    c = 1 - a - b
    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1

def count_lattice_points_in_triangle_and_circle(vertices, R):
    # Find bounding box of the intersection
    x_coords = [v[0] for v in vertices]
    y_coords = [v[1] for v in vertices]
    min_x = max(math.floor(min(x_coords)), -R)
    max_x = min(math.ceil(max(x_coords)), R)
    min_y = max(math.floor(min(y_coords)), -R)
    max_y = min(math.ceil(max(y_coords)), R)
    count = 0
    for x in range(int(min_x), int(max_x)+1):
        for y in range(int(min_y), int(max_y)+1):
            if point_in_circle(x, y, R) and point_in_triangle(x, y, vertices):
                count += 1
    return count

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N, R = readints()
        total = 0
        for _ in range(N):
            X_A, Y_A, X_B, Y_B, X_C, Y_C = readints()
            vertices = [(X_A, Y_A), (X_B, Y_B), (X_C, Y_C)]
            # Check if all vertices are inside the circle
            all_inside = all(point_in_circle(x, y, R) for x, y in vertices)
            if all_inside:
                cnt = lattice_points_in_triangle(vertices)
                total = (total + cnt) % MOD
            else:
                # Partially overlapping, need to count points inside both
                cnt = count_lattice_points_in_triangle_and_circle(vertices, R)
                total = (total + cnt) % MOD
        print(f"Case #{tc}: {total}")

if __name__ == "__main__":
    main()