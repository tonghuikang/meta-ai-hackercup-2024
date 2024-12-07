import sys
import math

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, angle):
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    rotated = []
    for (x, y) in polygon:
        xr = x * cos_theta - y * sin_theta
        yr = x * sin_theta + y * cos_theta
        rotated.append((xr, yr))
    return rotated

def translate_polygon(polygon, dx, dy):
    return [(x + dx, y + dy) for (x, y) in polygon]

def polygon_contains_point(polygon, point):
    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]
        if ((yi > y) != (yj > y)):
            x_intersect = (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi
            if x < x_intersect:
                inside = not inside
    return inside

def point_on_polygon(polygon, point):
    # Check if the point is on any edge of the polygon
    x, y = point
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]
        if on_segment((xi, yi), (xj, yj), (x, y)):
            return True
    return False

def on_segment(p, q, r):
    # Check if point r is on segment pq
    (px, py) = p
    (qx, qy) = q
    (rx, ry) = r
    if min(px, qx) - 1e-8 <= rx <= max(px, qx) + 1e-8 and min(py, qy) - 1e-8 <= ry <= max(py, qy) + 1e-8:
        # Compute cross product
        cross = (qx - px) * (ry - py) - (qy - py) * (rx - px)
        if abs(cross) < 1e-8:
            return True
    return False

def any_point_inside_cup(polygon, W, D):
    # Check if any point in polygon is strictly inside the cup
    for (x, y) in polygon:
        if 0 < x < W and 0 < y < D:
            return True
    return False

def no_cup_points_inside_polygon(polygon, W, D):
    # Check boundary points of cup are not strictly inside polygon
    # Since the polygon is convex, we can sample points on the boundary
    # Let's sample some points on the bottom and sides
    steps = max(W, D) * 10  # Number of points to sample
    for i in range(steps + 1):
        t = i / steps
        # Bottom edge (0,0) to (W,0)
        x = t * W
        y = 0
        if polygon_contains_point(polygon, (x, y)) and not point_on_polygon(polygon, (x, y)):
            return False
    for i in range(1, steps):
        t = i / steps
        # Left edge (0,0) to (0,D)
        x = 0
        y = t * D
        if polygon_contains_point(polygon, (x, y)) and not point_on_polygon(polygon, (x, y)):
            return False
        # Right edge (W,0) to (W,D)
        x = W
        y = t * D
        if polygon_contains_point(polygon, (x, y)) and not point_on_polygon(polygon, (x, y)):
            return False
    for i in range(steps + 1):
        t = i / steps
        # Top edge (0,D) to (W,D)
        x = t * W
        y = D
        if polygon_contains_point(polygon, (x, y)) and not point_on_polygon(polygon, (x, y)):
            return False
    return True

def can_fit(polygon, W, D):
    N = len(polygon)
    for i in range(N):
        # Edge from polygon[i] to polygon[j]
        j = (i + 1) % N
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        # Calculate angle to rotate this edge to x-axis
        dx = xj - xi
        dy = yj - yi
        angle = -math.atan2(dy, dx)
        rotated = rotate_polygon(polygon, angle)
        # After rotation, edge i-j should be horizontal
        # Let's set point i to be on x-axis
        rotated_i = rotated[i]
        # Compute translation needed to set rotated_i to (0,0)
        dx_trans = -rotated_i[0]
        dy_trans = -rotated_i[1]
        translated = translate_polygon(rotated, dx_trans, dy_trans)
        # Now, edge i-j is from (0,0) to (xj', yj') where yj' should be approximately 0
        # Find the other end of the edge after transformation
        translated_j = translated[j]
        # Adjust translation so that translated_j[0] is within [0, W]
        # Since edge is horizontal, yj' should be 0
        if abs(translated_j[1]) > 1e-6:
            continue  # Not horizontal enough
        # Now, translated_i is at (0,0) and translated_j is at (W',0)
        # We need to translate along x-axis so that some point between translated_i and translated_j lies within [0, W]
        # The entire edge spans from 0 to W', so to have some part within [0, W], shift x by t where t ranges
        # from -W' to W
        W_edge = translated_j[0] - translated_i[0]
        for t_shift in range(0, W + 1):
            # Shift the polygon by t_shift along x-axis
            shifted = translate_polygon(translated, t_shift, 0)
            # Now, check:
            # 1. All vertices y >= 0
            all_above = all(y >= -1e-6 for (x, y) in shifted)
            if not all_above:
                continue
            # 2. Some vertex on x-axis between 0 and W
            on_x_axis = any(0 <= x <= W and abs(y) < 1e-6 for (x, y) in shifted)
            if not on_x_axis:
                continue
            # 3. Some point strictly inside the cup
            has_inside = any_point_inside_cup(shifted, W, D)
            if not has_inside:
                continue
            # 4. No point on sauce cup strictly inside polygon
            no_cup_inside = no_cup_points_inside_polygon(shifted, W, D)
            if not no_cup_inside:
                continue
            # If all conditions met
            return True
    return False

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        parts = sys.stdin.readline().split()
        while len(parts) < 3:
            parts += sys.stdin.readline().split()
        N, W, D = map(int, parts)
        polygon = []
        for _ in range(N):
            x, y = map(int, sys.stdin.readline().split())
            polygon.append((x, y))
        result = can_fit(polygon, W, D)
        print(f"Case #{case}: {'Yes' if result else 'No'}")

if __name__ == "__main__":
    main()