import math
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    rotated = []
    for (x, y) in polygon:
        xr = x * cos_theta - y * sin_theta
        yr = x * sin_theta + y * cos_theta
        rotated.append((xr, yr))
    return rotated

def translate_polygon(polygon, tx, ty):
    return [(x + tx, y + ty) for (x, y) in polygon]

def point_inside_rect(x, y, W, D, eps=1e-9):
    return eps < x < W - eps and eps < y < D - eps

def sauce_cup_edges(W, D):
    # Returns list of points on the edges of the sauce cup
    # Bottom: (0,0) to (W,0)
    # Right: (W,0) to (W,D)
    # Top: (W,D) to (0,D)
    # Left: (0,D) to (0,0)
    # We'll sample points on these edges
    # For simplicity, only consider the edges as infinite lines for containment tests
    # But since we need to ensure no point on the sauce cup is inside the polygon,
    # we can check vertices and maybe some sampled points
    return [
        # Bottom edge
        lambda t: (t, 0) for t in [0, W],
        # Right edge
        lambda t: (W, t) for t in [0, D],
        # Top edge
        lambda t: (t, D) for t in [W, 0],
        # Left edge
        lambda t: (0, t) for t in [D, 0],
    ]

def polygon_contains_point(polygon, point):
    # Ray casting algorithm for point in polygon
    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]
        if ((yi > y) != (yj > y)):
            x_intersect = (xj - xi) * (y - yi) / (yj - yi + 1e-20) + xi
            if x < x_intersect:
                inside = not inside
    return inside

def has_intersection_polygon_rect(polygon, W, D):
    # Check if any point of the polygon is strictly inside the sauce cup
    for (x, y) in polygon:
        if 0 < x < W and 0 < y < D:
            return True
    return False

def no_sauce_cup_point_inside_polygon(polygon, W, D):
    # Check that no point on the sauce cup boundary is strictly inside the polygon
    # We'll sample points on the boundaries
    # To keep it simple, sample integer points along the boundaries
    for t in range(0, W+1):
        if polygon_contains_point(polygon, (t, 0)):
            return False
        if polygon_contains_point(polygon, (t, D)):
            return False
    for t in range(0, D+1):
        if polygon_contains_point(polygon, (0, t)):
            return False
        if polygon_contains_point(polygon, (W, t)):
            return False
    return True

def can_fit(polygon, W, D):
    N = len(polygon)
    eps = 1e-6
    for j in range(N):
        vx, vy = polygon[j]
        alpha = math.atan2(vy, vx)
        theta = -alpha
        rotated = rotate_polygon(polygon, theta)
        # After rotation, the j-th vertex should be on x-axis
        # Check y >= 0
        min_y = min(y for (x, y) in rotated)
        if min_y < -eps:
            continue
        # Now, the j-th vertex has y=0 (within epsilon)
        rotated_j_x, rotated_j_y = rotated[j]
        # Now, translate so that rotated_j_x is between 0 and W
        # The translation on x is tx = desired_x - rotated_j_x
        # desired_x can be from 0 to W
        # So tx can be from -rotated_j_x to W - rotated_j_x
        # We need to find tx such that after translation:
        # All x in [0, W] and all y in [0, D]
        # And some point is strictly inside the sauce cup
        # And no point on the sauce cup is strictly inside the polygon
        # Since tx is continuous, check if there exists tx where:
        # min_x + tx >=0 and max_x + tx <= W
        # And min_y >=0 and max_y <= D
        rotated_x = [x for (x, y) in rotated]
        rotated_y = [y for (x, y) in rotated]
        min_x = min(rotated_x)
        max_x = max(rotated_x)
        min_y = min(rotated_y)
        max_y = max(rotated_y)
        # Possible tx range
        tx_min = -rotated_j_x
        tx_max = W - rotated_j_x
        # Also, ensure that after translation, min_x + tx >=0 and max_x + tx <=W
        tx_min = max(tx_min, -min(rotated_x))
        tx_max = min(tx_max, W - max(rotated_x))
        if tx_min > tx_max:
            continue
        # We can choose tx such that the vertex j is placed at tx_position in [0, W]
        # For simplicity, choose tx such that vertex j is placed at 0, W/2, W
        # and check if any of these positions work
        test_tx = [0, W/2, W]
        # Also include tx_min and tx_max
        test_tx.extend([tx_min, tx_max])
        # Remove duplicates
        test_tx = list(set(test_tx))
        for tx in test_tx:
            # Check tx within [tx_min, tx_max]
            if tx < tx_min - eps or tx > tx_max + eps:
                continue
            translated = translate_polygon(rotated, tx, 0)
            # Check all x in [0, W] and y in [0, D]
            if any(x < -eps or x > W + eps for (x, y) in translated):
                continue
            if any(y < -eps or y > D + eps for (x, y) in translated):
                continue
            # Check some point is strictly inside the sauce cup
            if not has_intersection_polygon_rect(translated, W, D):
                continue
            # Check no point on the sauce cup is strictly inside the polygon
            if not no_sauce_cup_point_inside_polygon(translated, W, D):
                continue
            # If all conditions met
            return True
    return False

T = int(sys.stdin.readline())
for test_case in range(1, T+1):
    N, W, D = map(int, sys.stdin.readline().split())
    polygon = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        polygon.append((x, y))
    result = "Yes" if can_fit(polygon, W, D) else "No"
    print(f"Case #{test_case}: {result}")