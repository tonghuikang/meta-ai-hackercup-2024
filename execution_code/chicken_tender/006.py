import sys
import math

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    return [ (x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta) for (x,y) in polygon ]

def translate_polygon(polygon, dx, dy):
    return [ (x + dx, y + dy) for (x,y) in polygon ]

def is_all_y_non_negative(polygon, epsilon=1e-6):
    for x, y in polygon:
        if y < -epsilon:
            return False
    return True

def has_vertex_on_x_axis_in_W(polygon, W, epsilon=1e-6):
    for x, y in polygon:
        if abs(y) <= epsilon and -epsilon <= x <= W + epsilon:
            return True
    return False

def polygon_contains_some_point_in_cup(polygon, W, D, epsilon=1e-6):
    # Check if any vertex is strictly inside the cup
    for x, y in polygon:
        if epsilon < x < W - epsilon and epsilon < y < D - epsilon:
            return True
    # Additionally, check if any edge intersects the interior
    # For simplicity, check midpoints of edges
    N = len(polygon)
    for i in range(N):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1)%N]
        xm = (x1 + x2)/2
        ym = (y1 + y2)/2
        if epsilon < xm < W - epsilon and epsilon < ym < D - epsilon:
            return True
    return False

def point_on_sauce_cup(x, y, W, D, epsilon=1e-6):
    # Points on the sauce cup boundaries
    if abs(y) <= epsilon and 0 - epsilon <= x <= W + epsilon:
        return True
    if abs(x - 0) <= epsilon and 0 <= y <= D + epsilon:
        return True
    if abs(x - W) <= epsilon and 0 <= y <= D + epsilon:
        return True
    if abs(y - D) <= epsilon and 0 <= x <= W + epsilon:
        return True
    return False

def is_point_inside_polygon(x, y, polygon):
    # Ray casting algorithm for point in polygon
    n = len(polygon)
    inside = False
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i+1)%n]
        if ((yi > y) != (yj > y)):
            intersect = (xj - xi) * (y - yi) / (yj - yi + 1e-20) + xi
            if x < intersect:
                inside = not inside
    return inside

def sauce_cup_points(W, D, num_samples=10):
    # Sample points on the sauce cup boundaries
    samples = []
    # Bottom edge (0,0) to (W,0)
    for i in range(1, num_samples+1):
        x = W * i / (num_samples +1)
        samples.append( (x, 0) )
    # Right edge (W,0) to (W,D)
    for i in range(1, num_samples+1):
        y = D * i / (num_samples +1)
        samples.append( (W, y) )
    # Top edge (W,D) to (0,D)
    for i in range(1, num_samples+1):
        x = W - W * i / (num_samples +1)
        samples.append( (x, D) )
    # Left edge (0,D) to (0,0)
    for i in range(1, num_samples+1):
        y = D - D * i / (num_samples +1)
        samples.append( (0, y) )
    return samples

def no_sauce_cup_inside_polygon(polygon, W, D, epsilon=1e-6):
    samples = sauce_cup_points(W, D, num_samples=10)
    for x, y in samples:
        if is_point_inside_polygon(x, y, polygon):
            return False
    return True

def can_fit(polygon, W, D):
    N = len(polygon)
    for i in range(N):
        vx, vy = polygon[i]
        theta = math.atan2(vy, vx)
        rotated = rotate_polygon(polygon, -theta)
        # After rotation, the i-th vertex should lie on x-axis
        rotated_vx, rotated_vy = rotated[i]
        # Translate vertically to make y=0
        translated = translate_polygon(rotated, 0, -rotated_vy)
        # Now, translated[i] has y=0
        # Now, translate horizontally so that translated[i][0] is within [0, W]
        # The translated[i][0] can be placed anywhere from 0 to W
        # So, shift x by dx such that 0 <= translated[i][0] + dx <= W
        xi = translated[i][0]
        # To cover all possibilities, shift so that translated[i][0] is between 0 and W
        # This means dx in [-xi, W - xi]
        # For simplicity, place translated[i][0] at 0
        shifted = translate_polygon(translated, -xi, 0)
        # Now, translated[i][0] =0
        # Check if any part of the polygon is beyond W after shifting
        min_x = min(x for x, y in shifted)
        max_x = max(x for x, y in shifted)
        if min_x > W + 1e-6 or max_x < 0 - 1e-6:
            continue  # Doesn't overlap horizontally
        # Alternatively, try to shift such that translated[i][0] is within [0, W]
        # Find dx such that 0 <= xi + dx <= W
        # So dx >= -xi and dx <= W - xi
        # We can choose dx = min(max(-xi, 0), W)
        # For better coverage, try shifting so that translated[i][0] is exactly 0 and W
        for target_x in [0, W]:
            dx = target_x - translated[i][0]
            final_shifted = translate_polygon(translated, dx, 0)
            # Now check conditions
            if not is_all_y_non_negative(final_shifted):
                continue
            if not has_vertex_on_x_axis_in_W(final_shifted, W):
                continue
            if not polygon_contains_some_point_in_cup(final_shifted, W, D):
                continue
            if not no_sauce_cup_inside_polygon(final_shifted, W, D):
                continue
            return True
    return False

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, W, D = readints()
        polygon = []
        for _ in range(N):
            x, y = readints()
            polygon.append( (x, y) )
        result = can_fit(polygon, W, D)
        print(f"Case #{test_case}: {'Yes' if result else 'No'}")

if __name__ == "__main__":
    main()