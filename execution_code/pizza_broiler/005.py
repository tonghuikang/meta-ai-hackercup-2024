import sys
import math
import threading

def main():
    import sys
    import math
    sys.setrecursionlimit(1 << 25)

    MOD = 10 ** 9 + 7

    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N, R = map(int, sys.stdin.readline().split())
        R_float = float(R)
        slices = []
        for _ in range(N):
            coords = list(map(float, sys.stdin.readline().split()))
            triangle = [(coords[0], coords[1]), (coords[2], coords[3]), (coords[4], coords[5])]
            slices.append(triangle)
        total_heat = 0
        for triangle in slices:
            # Compute total area of the triangle
            Ax, Ay = triangle[0]
            Bx, By = triangle[1]
            Cx, Cy = triangle[2]
            A_T = abs((Ax*(By - Cy) + Bx*(Cy - Ay) + Cx*(Ay - By)) / 2.0)
            
            # Compute number of integer lattice points in the triangle using Pick's Theorem
            # First, compute the number of lattice points on the boundary
            def gcd(a, b):
                while b != 0:
                    a, b = b, a % b
                return abs(a)
            B_count = 0
            for i in range(3):
                x0, y0 = triangle[i]
                x1, y1 = triangle[(i+1)%3]
                dx = x1 - x0
                dy = y1 - y0
                B_count += gcd(int(dx), int(dy))
            # The triangle's area should be integer or half-integer
            I_T = A_T + 1 - B_count / 2
            I_T = int(round(I_T))  # Number of integer points in the triangle

            # Now compute the area of intersection with the circle
            # This is complex and requires handling
            # Implement polygon-circle intersection area computation
            # For a triangle, we can write a specific function
            circle_center = (0.0, 0.0)
            intersection_area = compute_polygon_circle_intersection_area(triangle, circle_center, R_float)
            # Estimated number of integer points in the intersected area
            N_T = I_T * (intersection_area / A_T)
            N_T_int = int(round(N_T))
            total_heat = (total_heat + N_T_int) % MOD

        print(f"Case #{case_num}: {total_heat}")

def compute_polygon_circle_intersection_area(polygon, center, radius):
    # Compute the area of the intersection between a polygon and a circle
    # For this problem, polygon is triangle
    # Code adapted from standard algorithms

    def is_point_inside_circle(p, center, radius):
        x, y = p
        cx, cy = center
        return (x - cx) ** 2 + (y - cy) ** 2 <= radius ** 2 + 1e-8

    def segment_circle_intersection(p0, p1, center, radius):
        x0, y0 = p0
        x1, y1 = p1
        dx = x1 - x0
        dy = y1 - y0
        a = dx * dx + dy * dy
        b = 2 * (dx * (x0 - center[0]) + dy * (y0 - center[1]))
        c = (x0 - center[0]) ** 2 + (y0 - center[1]) ** 2 - radius ** 2
        discriminant = b * b - 4 * a * c
        if discriminant < -1e-8:
            return []
        elif discriminant < 1e-8:
            t = -b / (2 * a)
            if 0 <= t <= 1:
                return [(x0 + t * dx, y0 + t * dy)]
            else:
                return []
        else:
            sqrt_disc = math.sqrt(discriminant)
            t1 = (-b - sqrt_disc) / (2 * a)
            t2 = (-b + sqrt_disc) / (2 * a)
            points = []
            if 0 <= t1 <= 1:
                points.append((x0 + t1 * dx, y0 + t1 * dy))
            if 0 <= t2 <= 1:
                points.append((x0 + t2 * dx, y0 + t2 * dy))
            return points

    # Clip the polygon with the circle
    # This is a complex task; for the triangle, we can handle it manually
    # We need to construct the intersection polygon
    from shapely.geometry import Polygon, LineString, Point

    # Create polygon
    poly = Polygon(polygon)

    # Create circle
    circle = Point(center).buffer(radius, resolution=64)

    # Intersection
    intersection = poly.intersection(circle)

    # Compute area
    intersection_area = intersection.area

    return intersection_area

threading.Thread(target=main).start()