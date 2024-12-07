import sys
import math
from math import gcd

def readints():
    return list(map(int, sys.stdin.read().split()))

def count_lattice_points_triangle_fully_inside(x1, y1, x2, y2, x3, y3):
    # Compute 2A
    twice_A = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    # Compute B: boundary points
    def edge_gcd(xa, ya, xb, yb):
        return gcd(abs(xb - xa), abs(yb - ya))
    B1 = edge_gcd(x1, y1, x2, y2)
    B2 = edge_gcd(x2, y2, x3, y3)
    B3 = edge_gcd(x3, y3, x1, y1)
    B = B1 + B2 + B3
    # Total lattice points: (2A + B) // 2 + 1
    total = (twice_A + B) // 2 + 1
    return total

def count_lattice_points_partial(x1, y1, x2, y2, x3, y3, R):
    # Sort the vertices by y
    vertices = sorted([(x1, y1), (x2, y2), (x3, y3)], key=lambda p: p[1])
    (x1, y1), (x2, y2), (x3, y3) = vertices
    # Edges
    edges = [((x1, y1), (x2, y2)),
             ((x2, y2), (x3, y3)),
             ((x3, y3), (x1, y1))]
    # Find y range
    y_min = math.ceil(min(y1, y2, y3))
    y_max = math.floor(max(y1, y2, y3))
    # Initialize count
    count = 0
    for y in range(y_min, y_max + 1):
        # Find intersections with the triangle
        x_intersections = []
        for edge in edges:
            (xa, ya), (xb, yb) = edge
            if ya == yb:
                continue
            if y < min(ya, yb) or y >= max(ya, yb):
                continue
            # Compute intersection
            t = (y - ya) / (yb - ya)
            x = xa + t * (xb - xa)
            x_intersections.append(x)
        if len(x_intersections) < 2:
            continue
        x_left = min(x_intersections)
        x_right = max(x_intersections)
        # Compute x bounds from circle
        if y* y > R * R:
            continue
        try:
            delta = math.isqrt(R * R - y * y)
        except:
            delta = 0
            while (delta +1) * (delta +1) <= R * R - y * y:
                delta +=1
        x_min_circle = -delta
        x_max_circle = delta
        # Compute x_low and x_high
        x_start = math.ceil(x_left)
        x_end = math.floor(x_right)
        x_low = max(x_start, x_min_circle)
        x_high = min(x_end, x_max_circle)
        if x_low > x_high:
            continue
        count += x_high - x_low + 1
    return count

def main():
    data = readints()
    idx = 0
    T = data[idx]
    idx +=1
    MOD = 10**9 +7
    for test_case in range(1, T +1):
        N = data[idx]
        R = data[idx +1]
        idx +=2
        sum_heats = 0
        for _ in range(N):
            XA = data[idx]
            YA = data[idx +1]
            XB = data[idx +2]
            YB = data[idx +3]
            XC = data[idx +4]
            YC = data[idx +5]
            idx +=6
            # Check if fully inside
            in1 = XA * XA + YA * YA <= R * R
            in2 = XB * XB + YB * YB <= R * R
            in3 = XC * XC + YC * YC <= R * R
            if in1 and in2 and in3:
                count = count_lattice_points_triangle_fully_inside(XA, YA, XB, YB, XC, YC)
            else:
                count = count_lattice_points_partial(XA, YA, XB, YB, XC, YC, R)
            sum_heats = (sum_heats + count) % MOD
        print(f"Case #{test_case}: {sum_heats}")

if __name__ == "__main__":
    main()