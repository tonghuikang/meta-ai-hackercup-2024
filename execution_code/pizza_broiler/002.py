import sys
import math
import threading
from math import gcd

MOD = 10**9 + 7

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    import sys

    def input():
        return sys.stdin.read()

    def readints():
        return list(map(int, sys.stdin.read().split()))

    data = readints()
    idx = 0
    T = data[idx]
    idx += 1

    for test_case in range(1, T + 1):
        N, R = data[idx], data[idx + 1]
        idx += 2
        slices = []
        for _ in range(N):
            X_A = data[idx]
            Y_A = data[idx + 1]
            X_B = data[idx + 2]
            Y_B = data[idx + 3]
            X_C = data[idx + 4]
            Y_C = data[idx + 5]
            slices.append(((X_A, Y_A), (X_B, Y_B), (X_C, Y_C)))
            idx += 6

        total = 0
        R_sq = R * R

        for triangle in slices:
            (x0, y0), (x1, y1), (x2, y2) = triangle
            # Check if all vertices are inside or on the circle
            inside_all = True
            for x, y in triangle:
                if x * x + y * y > R_sq:
                    inside_all = False
                    break
            if inside_all:
                # Compute the number of lattice points inside the triangle using Pick's Theorem
                # First, compute area using the shoelace formula
                area = abs((x0*(y1 - y2) + x1*(y2 - y0) + x2*(y0 - y1))) / 2
                # Compute the number of lattice points on the boundary
                def boundary_points(x0, y0, x1, y1):
                    dx = abs(x1 - x0)
                    dy = abs(y1 - y0)
                    return gcd(dx, dy) + 1
                B = boundary_points(x0, y0, x1, y1) + boundary_points(x1, y1, x2, y2) + boundary_points(x2, y2, x0, y0) - 3
                # I = A - B/2 + 1
                I = area - B / 2 + 1
                # Number of lattice points is I + B
                count = int(I + B)
                total = (total + count) % MOD
            else:
                # Partially intersecting the circle
                # We need to find the number of lattice points inside both the triangle and the circle
                # Iterate over the bounding box of the triangle and count valid points
                # First, find bounding box
                min_x = math.floor(min(x0, x1, x2))
                max_x = math.ceil(max(x0, x1, x2))
                min_y = math.floor(min(y0, y1, y2))
                max_y = math.ceil(max(y0, y1, y2))
                # To speed up, iterate over integer y and find x ranges
                # Define function to check if point is inside the triangle
                def point_in_triangle(px, py):
                    # Barycentric coordinates
                    denominator = ((y1 - y2)*(x0 - x2) + (x2 - x1)*(y0 - y2))
                    if denominator == 0:
                        return False
                    a = ((y1 - y2)*(px - x2) + (x2 - x1)*(py - y2)) / denominator
                    b = ((y2 - y0)*(px - x2) + (x0 - x2)*(py - y2)) / denominator
                    c = 1 - a - b
                    return (0 <= a <= 1) and (0 <= b <= 1) and (0 <= c <= 1)

                count = 0
                for y in range(int(math.floor(min_y)), int(math.ceil(max_y)) + 1):
                    y_sq = y * y
                    if y_sq > R_sq:
                        continue
                    # Find intersection of the triangle with horizontal line y
                    intersections = []
                    for (x_a, y_a), (x_b, y_b) in [((x0, y0), (x1, y1)), ((x1, y1), (x2, y2)), ((x2, y2), (x0, y0))]:
                        if y_a == y_b:
                            continue
                        if y < min(y_a, y_b) or y > max(y_a, y_b):
                            continue
                        # Compute x where the edge intersects the line y
                        x = x_a + (y - y_a) * (x_b - x_a) / (y_b - y_a)
                        intersections.append(x)
                    if len(intersections) < 2:
                        continue
                    x1_int, x2_int = sorted(intersections)[:2]
                    # Now, iterate over integer x in [ceil(x1_int), floor(x2_int)]
                    start_x = math.ceil(x1_int)
                    end_x = math.floor(x2_int)
                    for x in range(start_x, end_x + 1):
                        if x * x + y * y <= R_sq:
                            if point_in_triangle(x, y):
                                count += 1
                total = (total + count) % MOD

        print(f"Case #{test_case}: {total}")

threading.Thread(target=main).start()