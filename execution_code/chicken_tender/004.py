import math
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, angle):
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    return [(x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta) for x, y in polygon]

def translate_polygon(polygon, dx, dy):
    return [(x + dx, y + dy) for x, y in polygon]

def point_inside_polygon(x, y, polygon):
    # Ray casting algorithm for point inside polygon
    n = len(polygon)
    inside = False
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]
        if ((yi > y) != (yj > y)):
            intersect = (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi
            if x < intersect:
                inside = not inside
    return inside

def any_point_inside_cup(polygon, W, D):
    # Check if any point inside the cup
    # Sample points inside the cup
    # To optimize, we can check the intersection between polygon and the interior of the cup
    # Alternatively, check if any vertex is inside the cup (excluding edges)
    for x, y in polygon:
        if 0 < x < W and 0 < y < D:
            return True
    # Additionally, edges of the polygon might pass through the interior
    # For simplicity, we stick with vertex check
    return False

def any_cup_point_inside_polygon(polygon, W, D):
    # Check if any point on the boundary of the cup is inside the polygon
    # Check corners and potentially sampled points on edges
    points = [(0,0), (W,0), (W,D), (0,D)]
    # Sample additional points on edges
    steps = 10
    for i in range(steps +1):
        points.append((W * i / steps, 0))
        points.append((W, D * i / steps))
        points.append((W * (steps - i) / steps, D))
        points.append((0, D * (steps - i) / steps))
    for x, y in points:
        if point_inside_polygon(x, y, polygon):
            # If the point is on the boundary, it's not strictly inside
            # So we need to ensure it's strictly inside
            min_dist = min([math.hypot(x - vx, y - vy) for vx, vy in polygon])
            if min_dist > 1e-6:
                return True
    return False

def can_fit(polygon, W, D):
    N = len(polygon)
    for i in range(N):
        # Current vertex to align to x-axis
        vx, vy = polygon[i]
        angle = -math.atan2(vy, vx - vx) if vx != vx else 0
        # Calculate the angle to rotate so that this vertex lies on the x-axis
        angle = -math.atan2(vy, vx - vx)
        # Compute the required rotation angle
        if vy == 0:
            theta = 0
        else:
            theta = -math.atan2(vy, 1)
        # Alternatively, compute the angle to make this vertex horizontal
            theta = -math.atan2(vy, 1)
        # Let's compute the angle needed to make y=0
        theta = -math.atan2(vy, 1e-6)  # To avoid division by zero
        rotated = rotate_polygon(polygon, theta)
        # After rotation, the i-th vertex should be on the x-axis
        # Translate so that the i-th vertex is on x-axis and between 0 and W
        rx, ry = rotated[i]
        dx_options = [ -rx, W - rx]
        dy = -ry
        for dx in dx_options:
            translated = translate_polygon(rotated, dx, dy)
            # Check if the i-th vertex is on x-axis between 0 and W
            xi, yi = translated[i]
            if not (0 <= xi <= W and abs(yi) < 1e-6):
                continue
            # Check all vertices are on or above x-axis
            if any(y < -1e-6 for x, y in translated):
                continue
            # Check some point is strictly inside the cup
            if not any_point_inside_cup(translated, W, D):
                continue
            # Check no point on the cup lies strictly inside the polygon
            if any_cup_point_inside_polygon(translated, W, D):
                continue
            # All conditions met
            return True
    return False

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N, W, D = readints()
        polygon = [tuple(map(float, sys.stdin.readline().split())) for _ in range(N)]
        if can_fit(polygon, W, D):
            print(f"Case #{tc}: Yes")
        else:
            print(f"Case #{tc}: No")

if __name__ == "__main__":
    main()