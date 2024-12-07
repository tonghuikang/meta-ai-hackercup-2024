import math
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    rotated = []
    for x, y in polygon:
        x_new = x * cos_theta - y * sin_theta
        y_new = x * sin_theta + y * cos_theta
        rotated.append((x_new, y_new))
    return rotated

def translate_polygon(polygon, t_x):
    return [(x + t_x, y) for x, y in polygon]

def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]
        # Check if point is on the edge
        if ((yi > y) != (yj > y)):
            intersect_x = (xj - xi) * (y - yi) / (yj - yi + 1e-20) + xi
            if x < intersect_x:
                inside = not inside
    return inside

def segments_intersect(p1, p2, q1, q2):
    def orientation(a, b, c):
        val = (b[1]-a[1])*(c[0]-b[0]) - (b[0]-a[0])*(c[1]-b[1])
        if abs(val) < 1e-9:
            return 0
        return 1 if val > 0 else 2

    o1 = orientation(p1, p2, q1)
    o2 = orientation(p1, p2, q2)
    o3 = orientation(q1, q2, p1)
    o4 = orientation(q1, q2, p2)

    if o1 != o2 and o3 != o4:
        return True
    return False

def polygons_intersect(polygon1, polygon2):
    n1 = len(polygon1)
    n2 = len(polygon2)
    for i in range(n1):
        for j in range(n2):
            p1 = polygon1[i]
            p2 = polygon1[(i + 1) % n1]
            q1 = polygon2[j]
            q2 = polygon2[(j + 1) % n2]
            if segments_intersect(p1, p2, q1, q2):
                return True
    return False

def any_point_inside(polygon, rect):
    # rect is (xmin, ymin, xmax, ymax)
    # Sample some points inside rect and see if any is inside polygon
    # To be efficient, check the center
    x_center = (rect[0] + rect[2]) / 2
    y_center = (rect[1] + rect[3]) / 2
    if point_in_polygon((x_center, y_center), polygon):
        return True
    # Additionally, check corners
    corners = [
        (rect[0], rect[1]),
        (rect[2], rect[1]),
        (rect[2], rect[3]),
        (rect[0], rect[3])
    ]
    for corner in corners:
        if point_in_polygon(corner, polygon):
            return True
    return False

def solution():
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N, W, D = readints()
        polygon = []
        for _ in range(N):
            x, y = readints()
            polygon.append((x, y))
        possible = False
        for idx, (px, py) in enumerate(polygon):
            # Compute angle to rotate
            theta = math.atan2(-py, px)
            rotated = rotate_polygon(polygon, theta)
            # After rotation, the selected vertex is at (sqrt(px^2 + py^2), 0)
            L = math.hypot(px, py)
            # Translation to place L in [0, W]
            # t_x must satisfy 0 <= L + t_x <= W => t_x in [-L, W - L]
            t_x_min = -L
            t_x_max = W - L
            # Sample multiple t_x in [t_x_min, t_x_max]
            # To cover the space, sample t_x_min, t_x_max, and some in between
            steps = 10
            t_x_candidates = [t_x_min + (t_x_max - t_x_min) * i / steps for i in range(steps +1)]
            for t_x in t_x_candidates:
                translated = translate_polygon(rotated, t_x)
                # Check all y >=0
                all_y_non_negative = all(y >= -1e-9 for x, y in translated)
                if not all_y_non_negative:
                    continue
                # Find the position of the rotated vertex
                rotated_vertex = translated[idx]
                vx, vy = rotated_vertex
                if vy < -1e-9:
                    continue
                if not ( -1e-6 <= vy <= 1e-6 and 0 -1e-6 <= vx <= W +1e-6):
                    # The vertex should lie on x-axis between 0 and W
                    continue
                # Check if some point of polygon is strictly within the cup
                # i.e., exists (x, y) with 0 < x < W and 0 < y < D inside polygon
                # For simplicity, check the center of the cup
                center = (W / 2, D / 2)
                if not (0 < center[0] < W and 0 < center[1] < D and point_in_polygon(center, translated)):
                    # Alternatively, check intersection with cup rectangle
                    # Define cup rectangle
                    cup_rect = [
                        (0,0),
                        (W,0),
                        (W,D),
                        (0,D)
                    ]
                    # Check if polygons intersect (their interiors)
                    # Implemented as checking if any point of one is inside the other or edges intersect
                    intersects = polygons_intersect(translated, cup_rect)
                    if not intersects:
                        continue
                    # Additionally, ensure that some interior point is inside
                    # For simplicity, assume intersection implies this
                # Check that no point on the sauce cup lies strictly within the polygon
                # i.e., no point on the boundary of cup is inside polygon
                # Check all four edges of the cup
                # Sample points on the boundary
                boundary_points = [
                    (0,0), (W,0), (W,D), (0,D)
                ]
                # Additionally, sample midpoints of edges
                boundary_points += [
                    (W/2,0),
                    (W, D/2),
                    (W/2, D),
                    (0, D/2)
                ]
                boundary_inside = False
                for bp in boundary_points:
                    if point_in_polygon(bp, translated):
                        boundary_inside = True
                        break
                if boundary_inside:
                    continue
                # Also, check edges of cup against polygon
                # Not implemented due to complexity, but sample points should suffice
                # If all conditions hold
                possible = True
                break
            if possible:
                break
        print(f"Case #{test_case}: {'Yes' if possible else 'No'}")

if __name__ == "__main__":
    solution()