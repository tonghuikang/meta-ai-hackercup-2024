import sys
import math

MOD = 10**9 + 7

def readints():
    return list(map(int, sys.stdin.readline().split()))

def count_lattice_points_triangle_circle(xa, ya, xb, yb, xc, yc, R_sq):
    # Bounding box of the triangle
    xmin = min(xa, xb, xc)
    xmax = max(xa, xb, xc)
    ymin = min(ya, yb, yc)
    ymax = max(ya, yb, yc)
    
    count = 0
    for y in range(ymin, ymax + 1):
        # Find intersection of horizontal line y with the circle
        dy_sq = R_sq - y*y
        if dy_sq < 0:
            continue
        dx = int(math.isqrt(dy_sq))
        x_min_circle = -dx
        x_max_circle = dx
        
        # Within triangle, find x range for this y
        # Using barycentric coordinates or edge intersections
        # Find intersections with triangle edges
        intersections = []
        for (x1, y1, x2, y2) in [ (xa, ya, xb, yb), (xb, yb, xc, yc), (xc, yc, xa, ya) ]:
            if y1 == y2:
                continue
            if y < min(y1, y2) or y > max(y1, y2):
                continue
            # Compute intersection point
            t = (y - y1) / (y2 - y1)
            x = x1 + t * (x2 - x1)
            intersections.append(x)
        if len(intersections) < 2:
            continue
        x1, x2 = sorted(intersections)[:2]
        x_min_tri = math.ceil(x1)
        x_max_tri = math.floor(x2)
        # Intersection with circle
        final_min = max(x_min_tri, x_min_circle)
        final_max = min(x_max_tri, x_max_circle)
        if final_min > final_max:
            continue
        count += (final_max - final_min + 1)
    return count

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N, R = readints()
        R_sq = R * R
        total = 0
        for _ in range(N):
            xa, ya, xb, yb, xc, yc = readints()
            cnt = count_lattice_points_triangle_circle(xa, ya, xb, yb, xc, yc, R_sq)
            total = (total + cnt) % MOD
        print(f"Case #{test_case}: {total}")

if __name__ == "__main__":
    main()