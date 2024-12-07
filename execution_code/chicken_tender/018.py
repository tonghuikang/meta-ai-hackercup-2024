import sys
import math

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, angle):
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    rotated = []
    for x, y in polygon:
        xr = x * cos_theta - y * sin_theta
        yr = x * sin_theta + y * cos_theta
        rotated.append((xr, yr))
    return rotated

def translate_polygon(polygon, dx, dy):
    return [(x + dx, y + dy) for x, y in polygon]

def point_in_polygon(point, polygon):
    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]
        if ((yi > y) != (yj > y)):
            intersect_x = (xj - xi) * (y - yi) / (yj - yi + 1e-20) + xi
            if x < intersect_x:
                inside = not inside
    return inside

def polygon_min_y(polygon):
    return min(y for x, y in polygon)

def get_vertices_on_x_axis(polygon, eps=1e-6):
    return [ (x, y) for x, y in polygon if abs(y) < eps ]

def get_sample_points_within(W, D):
    # Sample the center and four quadrants
    return [
        (W / 2.0, D / 2.0),
        (W * 0.25, D * 0.25),
        (W * 0.75, D * 0.25),
        (W * 0.25, D * 0.75),
        (W * 0.75, D * 0.75)
    ]

def get_boundary_points(W, D):
    # Corners and midpoints
    return [
        (0,0), (W,0), (W,D), (0,D),
        (W/2.0,0), (W/2.0,D),
        (0,D/2.0), (W,D/2.0)
    ]

def can_fit(N, W, D, polygon):
    for i in range(N):
        # Current edge is from polygon[i] to polygon[(i+1)%N]
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1)%N]
        dx = x2 - x1
        dy = y2 - y1
        angle = math.atan2(dy, dx)
        # Rotate polygon to align this edge with x-axis
        rotated = rotate_polygon(polygon, -angle)
        # After rotation, the edge from i to i+1 should be horizontal
        # Shift vertically so that the edge is on y=0
        min_y = min(y for x, y in rotated)
        rotated_shifted = translate_polygon(rotated, 0, -min_y)
        # Find vertices on x-axis
        vertices_on_x = get_vertices_on_x_axis(rotated_shifted)
        if not vertices_on_x:
            continue
        for vx, vy in vertices_on_x:
            # We need to translate so that vx is between 0 and W
            # So, dx can be from -vx to W - vx
            # To simplify, we try to place vx at 0 and at W
            # and also check if it already lies within [0, W]
            candidate_shifts = [0, W - vx]
            if 0 <= vx <= W:
                candidate_shifts.append(0)  # No shift
            for shift_x in candidate_shifts:
                translated = translate_polygon(rotated_shifted, shift_x, 0)
                # Check all y >=0
                if any(y < -1e-6 for x, y in translated):
                    continue
                # Check some vertex on x-axis between 0 and W
                vertices_on_x_new = get_vertices_on_x_axis(translated)
                if not vertices_on_x_new:
                    continue
                # Ensure at least one vertex on x-axis within [0, W]
                valid_vertex = any(0 - 1e-6 <= x <= W + 1e-6 for x, y in vertices_on_x_new)
                if not valid_vertex:
                    continue
                # Check some point inside rectangle is inside polygon
                sample_points = get_sample_points_within(W, D)
                has_inside = False
                for sp in sample_points:
                    sx, sy = sp
                    if 0 < sx < W and 0 < sy < D:
                        if point_in_polygon(sp, translated):
                            has_inside = True
                            break
                if not has_inside:
                    continue
                # Check no boundary point is inside polygon
                boundary_points = get_boundary_points(W, D)
                boundary_inside = False
                for bp in boundary_points:
                    bx, by = bp
                    # Points on the boundary should not be strictly inside
                    # Allow points on the edge to be considered not inside
                    if point_in_polygon(bp, translated):
                        # To ensure it's strictly inside, check if not on edge
                        # Since polygon is convex and no three points colinear,
                        # if point is exactly on an edge, consider it not inside
                        boundary_inside = True
                        break
                if boundary_inside:
                    continue
                # All constraints satisfied
                return True
    return False

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T + 1):
        N, W, D = readints()
        polygon = []
        for _ in range(N):
            x, y = readints()
            polygon.append( (x, y) )
        result = can_fit(N, W, D, polygon)
        print(f"Case #{tc}: {'Yes' if result else 'No'}")

if __name__ == "__main__":
    main()