import sys
import math
from math import gcd
from collections import defaultdict

MOD = 10**9 + 7

def readints():
    return list(map(int, sys.stdin.read().split()))

def area2(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))

def boundary_points(x1, y1, x2, y2, x3, y3):
    # Number of lattice points on the boundary using gcd
    def edge(xa, ya, xb, yb):
        return gcd(abs(xb - xa), abs(yb - ya)) + 1
    return edge(x1, y1, x2, y2) + edge(x2, y2, x3, y3) + edge(x3, y3, x1, y1) - 3

def pick_lattice_points(x1, y1, x2, y2, x3, y3):
    A2 = area2(x1, y1, x2, y2, x3, y3)
    B = boundary_points(x1, y1, x2, y2, x3, y3)
    # Pick's theorem: A = I + B/2 - 1 => I = A - B/2 + 1
    # Total lattice points: I + B = A + B/2 + 1
    return (A2 + B) // 2 + 1

def is_inside(x, y, R2):
    return x*x + y*y <= R2

def triangle_scanline_count(tri, R):
    # tri: [(x1,y1), (x2,y2), (x3,y3)]
    R2 = R * R
    vertices = sorted(tri, key=lambda p: p[1])
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]

    def y_edges():
        # Return edges sorted by y
        edges = []
        edges.append(((x1, y1), (x2, y2)))
        edges.append(((x2, y2), (x3, y3)))
        edges.append(((x3, y3), (x1, y1)))
        return edges

    edges = y_edges()

    # Find y_min and y_max overlap with circle
    y_min = max(math.ceil(min(y1, y2, y3)), -R)
    y_max = min(math.floor(max(y1, y2, y3)), R)
    y_min = int(math.ceil(y_min))
    y_max = int(math.floor(y_max))
    total = 0

    for y in range(y_min, y_max + 1):
        # Find intersection of triangle with y
        xs = []
        for edge in edges:
            (xa, ya), (xb, yb) = edge
            if ya == yb:
                continue  # horizontal edge, ignore to avoid double-counting
            if y < min(ya, yb) or y > max(ya, yb):
                continue
            # Compute intersection x
            # x = xa + (y - ya) * (xb - xa) / (yb - ya)
            # To avoid floating point, use fractions
            dy = yb - ya
            dx = xb - xa
            if dy == 0:
                continue
            # Compute x as float
            x = xa + (y - ya) * dx / dy
            xs.append(x)
        if len(xs) < 2:
            continue  # no intersection at this y
        xs.sort()
        x_left = math.ceil(math.ceil(xs[0]))
        x_right = math.floor(math.floor(xs[1]))
        if x_left > x_right:
            continue
        # Now, intersect with circle at y
        circle_x_limit = int(math.floor(math.sqrt(R2 - y*y)))
        x_c_left = -circle_x_limit
        x_c_right = circle_x_limit
        # Find overlap
        final_left = max(x_left, x_c_left)
        final_right = min(x_right, x_c_right)
        if final_left > final_right:
            continue
        count = final_right - final_left + 1
        total = (total + count) % MOD
    return total

def main():
    data = readints()
    idx = 0
    T = data[idx]
    idx += 1
    for test_case in range(1, T + 1):
        N, R = data[idx], data[idx + 1]
        idx += 2
        total = 0
        R2 = R * R
        for _ in range(N):
            xA, yA, xB, yB, xC, yC = data[idx:idx + 6]
            idx += 6
            # Check if all vertices are inside the circle
            inside = True
            for x, y in [(xA, yA), (xB, yB), (xC, yC)]:
                if x*x + y*y > R2:
                    inside = False
                    break
            if inside:
                # Use Pick's theorem
                count = pick_lattice_points(xA, yA, xB, yB, xC, yC)
                total = (total + count) % MOD
            else:
                # Need to compute intersection
                tri = [(xA, yA), (xB, yB), (xC, yC)]
                count = triangle_scanline_count(tri, R)
                total = (total + count) % MOD
        print(f"Case #{test_case}: {total}")

if __name__ == "__main__":
    main()