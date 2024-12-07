import sys
import math
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, angle_rad):
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)
    rotated = []
    for x, y in polygon:
        xr = x * cos_theta - y * sin_theta
        yr = x * sin_theta + y * cos_theta
        rotated.append( (xr, yr) )
    return rotated

def translate_polygon(polygon, tx, ty):
    return [ (x + tx, y + ty) for x, y in polygon ]

def min_max_x(polygon):
    xs = [x for x, y in polygon]
    return min(xs), max(xs)

def min_max_y(polygon):
    ys = [y for x, y in polygon]
    return min(ys), max(ys)

def point_inside_polygon(point, polygon):
    # Ray Casting algorithm for point in polygon
    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i+1)%n]
        if ((yi > y) != (yj > y)):
            intersect_x = (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi
            if x < intersect_x:
                inside = not inside
    return inside

def any_point_inside(polygon, W, D):
    # Check if any vertex is strictly inside the sauce cup
    for x, y in polygon:
        if 0 < x < W and 0 < y < D:
            return True
    return False

def sauce_cup_points(W, D):
    # Sample points on the sauce cup edges
    samples = []
    steps = 10  # Number of samples per edge
    for i in range(1, steps):
        # Bottom edge (0,0) to (W,0) - but y=0 is boundary
        # Top edge (0,D) to (W,D)
        samples.append( (W * i / steps, D) )
        # Left edge (0,0) to (0,D)
        samples.append( (0, D * i / steps) )
        # Right edge (W,0) to (W,D)
        samples.append( (W, D * i / steps) )
    return samples

def sauce_cup_boundary_points(W, D):
    # Get exact boundary points excluding corners
    points = []
    for i in range(1, 100):
        t = i / 100
        if t < 1:
            points.append( (t * W, 0) )      # Bottom edge
            points.append( (t * W, D) )      # Top edge
            points.append( (0, t * D) )      # Left edge
            points.append( (W, t * D) )      # Right edge
    return points

def float_equal(a, b, eps=1e-6):
    return abs(a - b) < eps

def can_fit(polygon, W, D):
    N = len(polygon)
    epsilon = 1e-8
    for i in range(N):
        xi, yi = polygon[i]
        if yi == 0:
            angle = 0.0
        else:
            angle = math.atan2(yi, xi)  # Angle to rotate to set vertex on x-axis
            angle = -math.atan2(yi, xi)
        rotated = rotate_polygon(polygon, angle)
        # After rotation, the ith vertex should be on x-axis
        rx, ry = rotated[i]
        # Due to rotation, ry should be 0
        if not float_equal(ry, 0.0):
            continue
        # Now, translate the polygon so that this vertex lies between 0 and W on x-axis
        # Its current x is rx, need to translate so that rx + tx is between 0 and W
        # So tx can be from -rx to W - rx
        tx_min = -rx
        tx_max = W - rx
        # To ensure the polygon is above the x-axis after rotation, check min y
        min_y = min(y for x, y in rotated)
        if min_y < -epsilon:
            continue
        # Now, sample translation positions where the vertex is on [0, W]
        # To handle floating points, sample multiple positions between tx_min and tx_max
        # For precision, we can set tx such that the vertex is exactly at 0 and W
        tx_candidates = [0 - rx, W - rx]
        # Additionally, consider all vertices x positions to lie in [0, W]
        # But for simplicity, test at tx_min and tx_max
        for tx in tx_candidates:
            translated = translate_polygon(rotated, tx, 0)
            # Check all vertices are on or above x-axis
            if any(y < -epsilon for x, y in translated):
                continue
            # Check that at least one vertex is on x-axis between 0 and W
            on_x_axis = [x for x, y in translated if float_equal(y, 0.0) and 0 - epsilon <= x <= W + epsilon]
            if not on_x_axis:
                continue
            # Check some point of the polygon is strictly within the sauce cup
            has_inside = any_point_inside(translated, W, D)
            if not has_inside:
                continue
            # Check no point on the sauce cup is strictly within the polygon
            # We'll sample multiple points on the cup boundary
            # and ensure none are inside the polygon
            boundary_points = sauce_cup_boundary_points(W, D)
            violates = False
            for bx, by in boundary_points:
                if point_inside_polygon( (bx, by), translated ):
                    violates = True
                    break
            if violates:
                continue
            # All conditions satisfied
            return True
    return False

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N, W, D = readints()
        polygon = []
        for _ in range(N):
            x, y = readints()
            polygon.append( (x, y) )
        if can_fit(polygon, W, D):
            print(f"Case #{tc}: Yes")
        else:
            print(f"Case #{tc}: No")

if __name__ == "__main__":
    main()