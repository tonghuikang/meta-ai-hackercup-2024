import sys
import math
from math import gcd
sys.setrecursionlimit(1 << 25)

MOD = 10**9 + 7

def input():
    return sys.stdin.read()

def triangle_area2(xa, ya, xb, yb, xc, yc):
    return abs((xa*(yb - yc) + xb*(yc - ya) + xc*(ya - yb)))

def boundary_points(xa, ya, xb, yb, xc, yc):
    # Number of lattice points on the boundary of the triangle
    def edge_gcd(x1, y1, x2, y2):
        return gcd(abs(x2 - x1), abs(y2 - y1))
    return edge_gcd(xa, ya, xb, yb) + edge_gcd(xb, yb, xc, yc) + edge_gcd(xc, yc, xa, ya)

def is_fully_inside(R_sq, points):
    # Check if all three points are inside or on the circle
    for (x, y) in points:
        if x*x + y*y > R_sq:
            return False
    return True

def count_lattice_points_in_circle_and_triangle(R, R_sq, triangle):
    # For partially intersecting triangles, perform a scanline approach
    # This is a simplified implementation and may not be optimized for large inputs
    # Given the problem constraints, a more optimized approach might be necessary
    # Here, we use bounding box intersection for simplicity
    xa, ya, xb, yb, xc, yc = triangle
    min_x = max(math.ceil(min(xa, xb, xc)), math.ceil(-R))
    max_x = min(math.floor(max(xa, xb, xc)), math.floor(R))
    count = 0
    for x in range(int(min_x), int(max_x)+1):
        # For each x, find the y range in the triangle
        # Using barycentric coordinates or edge functions would be more efficient
        # Here, we simplify by iterating over possible y
        min_y = max(math.ceil(min(ya, yb, yc)), math.ceil(-math.sqrt(R_sq - x*x)) if R_sq - x*x >=0 else 0)
        max_y = min(math.floor(max(ya, yb, yc)), math.floor(math.sqrt(R_sq - x*x)) if R_sq - x*x >=0 else -1)
        for y in range(int(min_y), int(max_y)+1):
            # Check if (x, y) is inside the triangle
            # Using barycentric coordinates
            # Compute vectors
            v0x, v0y = xc - xa, yc - ya
            v1x, v1y = xb - xa, yb - ya
            v2x, v2y = x - xa, y - ya
            # Compute dot products
            dot00 = v0x * v0x + v0y * v0y
            dot01 = v0x * v1x + v0y * v1y
            dot02 = v0x * v2x + v0y * v2y
            dot11 = v1x * v1x + v1y * v1y
            dot12 = v1x * v2x + v1y * v2y
            # Compute barycentric coordinates
            denom = dot00 * dot11 - dot01 * dot01
            if denom == 0:
                continue
            inv_denom = 1 / denom
            u = (dot11 * dot02 - dot01 * dot12) * inv_denom
            v = (dot00 * dot12 - dot01 * dot02) * inv_denom
            if u >= 0 and v >= 0 and (u + v) <= 1:
                # Now check if inside the circle
                if x*x + y*y <= R_sq:
                    count +=1
    return count

def main():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx])
        R = int(data[idx+1])
        idx +=2
        R_sq = R*R
        total = 0
        for _ in range(N):
            xa = int(data[idx])
            ya = int(data[idx+1])
            xb = int(data[idx+2])
            yb = int(data[idx+3])
            xc = int(data[idx+4])
            yc = int(data[idx+5])
            idx +=6
            points = [(xa, ya), (xb, yb), (xc, yc)]
            if is_fully_inside(R_sq, points):
                # Compute number of lattice points in the triangle using Pick's theorem
                area2 = triangle_area2(xa, ya, xb, yb, xc, yc)
                area = area2 // 2
                B = boundary_points(xa, ya, xb, yb, xc, yc)
                I = area - (B // 2) + 1
                total = (total + I + (B // 2)) % MOD  # I + B/2 gives total lattice points
            else:
                # Partially intersecting, compute exact number
                count = count_lattice_points_in_circle_and_triangle(R, R_sq, (xa, ya, xb, yb, xc, yc))
                total = (total + count) % MOD
        print(f"Case #{test_case}: {total}")

if __name__ == "__main__":
    main()