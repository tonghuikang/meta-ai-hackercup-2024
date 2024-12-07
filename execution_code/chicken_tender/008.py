import sys
import math

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, angle):
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    return [(x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta) for (x, y) in polygon]

def translate_polygon(polygon, dx, dy):
    return [(x + dx, y + dy) for (x, y) in polygon]

def point_in_polygon(x, y, polygon):
    # Ray casting algorithm for point in polygon
    n = len(polygon)
    inside = False
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i+1)%n]
        if ((yi > y) != (yj > y)):
            intersect = (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi
            if x < intersect:
                inside = not inside
    return inside

def polygon_contains_polygon(p1, p2):
    # Check if any point of p2 is inside p1
    for x, y in p2:
        if point_in_polygon(x, y, p1):
            return True
    return False

def polygon_contains_cup(polygon, W, D):
    # Check if any point inside the cup is inside the polygon
    # To simplify, check the center of the cup
    return point_in_polygon(W/2, D/2, polygon)

def cup_contains_polygon(polygon, W, D):
    # Check if any point on the sauce cup is inside the polygon
    # Check boundaries: left, bottom, right
    # We can sample points on the boundaries
    steps = 100
    # Left boundary from (0,0) to (0,D)
    for i in range(steps+1):
        y = D * i / steps
        if point_in_polygon(0, y, polygon):
            return True
    # Bottom boundary from (0,0) to (W,0)
    for i in range(steps+1):
        x = W * i / steps
        if point_in_polygon(x, 0, polygon):
            return True
    # Right boundary from (W,0) to (W,D)
    for i in range(steps+1):
        y = D * i / steps
        if point_in_polygon(W, y, polygon):
            return True
    return False

def can_fit(polygon, W, D):
    N = len(polygon)
    for i in range(N):
        # Align edge i to i+1 with x-axis
        p1 = polygon[i]
        p2 = polygon[(i+1)%N]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        angle = math.atan2(dy, dx)
        rotated = rotate_polygon(polygon, -angle)
        # After rotation, edge i to i+1 should be horizontal
        # Now, translate so that p1 is on the x-axis
        rotated_p1 = rotated[i]
        # Shift vertically so that p1.y == 0
        shifted = translate_polygon(rotated, 0, -rotated_p1[1])
        # Now, p1 is on x-axis, p2 is at some x, 0
        # We need to translate horizontally such that p1.x is between 0 and W
        edge_length = math.hypot(p2[0]-p1[0], p2[1]-p1[1])
        min_x = 0
        max_x = W
        # p1.x can be shifted to min_x to max_x
        # So shift_x ranges from min_x - shifted[i][0] to max_x - shifted[i][0]
        shift_x_min = min_x - shifted[i][0]
        shift_x_max = max_x - shifted[i][0]
        # To handle floating precision, sample some shifts
        for shift_x in [shift_x_min, shift_x_max]:
            translated = translate_polygon(shifted, shift_x, 0)
            # Check all vertices are on or above x-axis
            if any(y < -1e-6 for (x, y) in translated):
                continue
            # Check some vertex is on x-axis between 0 and W
            on_x_axis = any(abs(y) < 1e-6 and 0 -1e-6 <= x <= W +1e-6 for (x, y) in translated)
            if not on_x_axis:
                continue
            # Check some point is strictly inside the cup
            # For simplicity, check the centroid
            centroid_x = sum(x for x, y in translated) / N
            centroid_y = sum(y for x, y in translated) / N
            if not (0 < centroid_x < W and 0 < centroid_y < D):
                # Alternatively, check vertices
                inside_cup = False
                for x, y in translated:
                    if 0 < x < W and 0 < y < D:
                        inside_cup = True
                        break
                if not inside_cup:
                    continue
            # Check no point on the sauce cup is strictly inside the polygon
            if cup_contains_polygon(translated, W, D):
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