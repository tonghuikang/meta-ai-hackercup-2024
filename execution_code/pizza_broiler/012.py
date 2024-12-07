import sys
import math
from math import gcd

MOD = 10**9 + 7

def readints():
    return list(map(int, sys.stdin.readline().split()))

def point_in_circle(x, y, R_sq):
    return x*x + y*y <= R_sq

def orientation(p, q, r):
    # Returns the orientation of triplet (p, q, r)
    # 0 -> colinear, 1 -> clockwise, 2 -> counterclockwise
    val = (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def on_segment(p, q, r):
    # Check if point q lies on segment pr
    if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
        return True
    return False

def segments_intersect(p1, q1, p2, q2):
    # Check if segments p1q1 and p2q2 intersect
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True
    return False

def count_lattice_points_in_triangle(vertices):
    # Use Pick's theorem: Area = I + B/2 - 1
    # So I = Area - B/2 + 1
    # Area can be computed using shoelace formula
    (x1,y1), (x2,y2), (x3,y3) = vertices
    area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))/2
    # Compute boundary points using gcd
    def boundary_points(p1, p2):
        return gcd(abs(p2[0]-p1[0]), abs(p2[1]-p1[1])) + 1
    B = boundary_points(vertices[0], vertices[1]) + boundary_points(vertices[1], vertices[2]) + boundary_points(vertices[2], vertices[0]) - 3
    I = int(area - B / 2 + 1)
    return I + B  # Total lattice points: I inside + B on boundary

def main():
    import sys
    import threading

    def solve():
        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            N, R = map(int, sys.stdin.readline().split())
            R_sq = R * R
            total = 0
            for _ in range(N):
                Xa, Ya, Xb, Yb, Xc, Yc = map(int, sys.stdin.readline().split())
                vertices = [(Xa, Ya), (Xb, Yb), (Xc, Yc)]
                # Check if all vertices inside the circle
                all_inside = all(point_in_circle(x, y, R_sq) for x,y in vertices)
                if all_inside:
                    # Count all lattice points in the triangle
                    count = count_lattice_points_in_triangle(vertices)
                    total = (total + count) % MOD
                else:
                    # Partially intersecting, need to count lattice points inside both triangle and circle
                    # Implement a scanline approach or use inclusion techniques
                    # Given time constraints, we'll use a bounding box and iterate, optimize for possible small triangles
                    xs = [v[0] for v in vertices]
                    ys = [v[1] for v in vertices]
                    min_x = max(math.ceil(min(xs)), -R)
                    max_x = min(math.floor(max(xs)), R)
                    count = 0
                    for x in range(int(min_x), int(max_x)+1):
                        # For each x, find y range inside the triangle
                        # Using barycentric coordinates or edge functions
                        # This is a placeholder for actual scanline intersection
                        # For simplicity, iterate over y within circle for this x
                        max_y_sq = R_sq - x*x
                        if max_y_sq < 0:
                            continue
                        min_y = max(math.ceil(min(ys)), -int(math.sqrt(max_y_sq)))
                        max_y_val = int(math.sqrt(max_y_sq))
                        max_y = min(math.floor(max(ys)), max_y_val)
                        for y in range(int(min_y), int(max_y)+1):
                            # Check if (x,y) is inside the triangle
                            # Using barycentric coordinates
                            denominator = ((Yb - Yc)*(Xa - Xc) + (Xc - Xb)*(Ya - Yc))
                            if denominator == 0:
                                continue  # Degenerate triangle, but problem states positive area
                            a = ((Yb - Yc)*(x - Xc) + (Xc - Xb)*(y - Yc)) / denominator
                            b = ((Yc - Ya)*(x - Xc) + (Xa - Xc)*(y - Yc)) / denominator
                            c = 1 - a - b
                            if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
                                count +=1
                    total = (total + count) % MOD
            print(f"Case #{test_case}: {total}")

    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()