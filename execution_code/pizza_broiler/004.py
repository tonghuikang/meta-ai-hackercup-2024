import sys
import math
from math import gcd

import sys
import sys
import sys

def input():
    return sys.stdin.read()

def is_inside_circle(x, y, R_sq):
    return x*x + y*y <= R_sq

def area2(x1, y1, x2, y2, x3, y3):
    # Returns double the area
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))

def boundary_points(x1, y1, x2, y2):
    # Number of lattice points on the line segment including endpoints
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if dx == 0 and dy == 0:
        return 1
    return gcd(dx, dy) + 1

def count_lattice_points_full(x1, y1, x2, y2, x3, y3):
    A2 = area2(x1, y1, x2, y2, x3, y3)
    B = boundary_points(x1, y1, x2, y2) + boundary_points(x2, y2, x3, y3) + boundary_points(x3, y3, x1, y1) - 3
    # A = A2 / 2
    # i = A - B / 2 + 1 = (A2 / 2) - (B / 2) +1 = (A2 - B)/2 +1
    i = (A2 - B) // 2 + 1
    return i

def point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    # Barycentric Technique
    # Compute vectors
    v0x, v0y = x3 - x1, y3 - y1
    v1x, v1y = x2 - x1, y2 - y1
    v2x, v2y = px - x1, py - y1

    # Compute dot products
    dot00 = v0x * v0x + v0y * v0y
    dot01 = v0x * v1x + v0y * v1y
    dot02 = v0x * v2x + v0y * v2y
    dot11 = v1x * v1x + v1y * v1y
    dot12 = v1x * v2x + v1y * v2y

    # Compute barycentric coordinates
    denom = dot00 * dot11 - dot01 * dot01
    if denom == 0:
        return False
    invDenom = 1 / denom
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom

    # Check if point is in triangle
    return (u >= 0) and (v >= 0) and (u + v <= 1)

def count_lattice_points_partial(x1, y1, x2, y2, x3, y3, R_sq):
    # Find bounding box
    min_x = min(x1, x2, x3)
    max_x = max(x1, x2, x3)
    min_y = min(y1, y2, y3)
    max_y = max(y1, y2, y3)
    count = 0
    for y in range(min_y, max_y + 1):
        # For each y, find intersection with triangle
        # Find intersections with triangle edges
        intersections = []
        for (xa, ya, xb, yb) in [(x1, y1, x2, y2), (x2, y2, x3, y3), (x3, y3, x1, y1)]:
            if ya == yb:
                continue
            if (y < min(ya, yb)) or (y > max(ya, yb)):
                continue
            # Compute x where the horizontal line y intersects the edge
            x = xa + (xb - xa) * (y - ya) / (yb - ya)
            intersections.append(x)
        if len(intersections) < 2:
            continue
        intersections.sort()
        x_start = math.ceil(min(intersections))
        x_end = math.floor(max(intersections))
        for x in range(int(x_start), int(x_end) + 1):
            if is_inside_circle(x, y, R_sq):
                if point_in_triangle(x, y, x1, y1, x2, y2, x3, y3):
                    count += 1
    return count

def main():
    MOD = 10**9 + 7
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); R = int(data[idx+1]); idx +=2
        R_sq = R * R
        total = 0
        for _ in range(N):
            x1 = int(data[idx]); y1 = int(data[idx+1])
            x2 = int(data[idx+2]); y2 = int(data[idx+3])
            x3 = int(data[idx+4]); y3 = int(data[idx+5]); idx +=6
            # Check if all three vertices are inside or on the circle
            inside1 = x1*x1 + y1*y1 <= R_sq
            inside2 = x2*x2 + y2*y2 <= R_sq
            inside3 = x3*x3 + y3*y3 <= R_sq
            if inside1 and inside2 and inside3:
                # Fully inside, use Pick's theorem
                count = count_lattice_points_full(x1, y1, x2, y2, x3, y3)
                total = (total + count) % MOD
            else:
                # Partially intersecting, compute exact count
                # Note: This is slow in Python for large inputs
                count = count_lattice_points_partial(x1, y1, x2, y2, x3, y3, R_sq)
                total = (total + count) % MOD
        print(f"Case #{test_case}: {total}")

if __name__ == "__main__":
    main()