import math
import sys
import sys
from typing import List, Tuple

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon: List[Tuple[float, float]], angle: float) -> List[Tuple[float, float]]:
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return [(x * cos_a - y * sin_a, x * sin_a + y * cos_a) for (x, y) in polygon]

def translate_polygon(polygon: List[Tuple[float, float]], tx: float, ty: float) -> List[Tuple[float, float]]:
    return [(x + tx, y + ty) for (x, y) in polygon]

def point_inside_rect(x, y, W, D):
    return 0 < x < W and 0 < y < D

def polygon_contains_point(polygon: List[Tuple[float, float]], point: Tuple[float, float]) -> bool:
    x, y = point
    n = len(polygon)
    inside = False
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]
        if ((yi > y) != (yj > y)):
            intersect = (xj - xi) * (y - yi) / (yj - yi) + xi
            if x < intersect:
                inside = not inside
    return inside

def any_point_inside(polygon: List[Tuple[float, float]], W: float, D: float) -> bool:
    # Check if any vertex is strictly inside
    for x, y in polygon:
        if 0 < x < W and 0 < y < D:
            return True
    # Otherwise, sample some points or use polygon intersection
    # For simplicity, check centroid
    cx = sum(x for x, y in polygon) / len(polygon)
    cy = sum(y for x, y in polygon) / len(polygon)
    return point_inside_rect(cx, cy, W, D) and polygon_contains_point(polygon, (cx, cy))

def cup_boundary_points(W, D):
    # Returns a list of points along the boundary of the cup
    # For simplicity, sample some points
    points = []
    # Bottom edge
    for x in range(0, W+1):
        points.append((x, 0))
    # Left edge
    for y in range(0, D+1):
        points.append((0, y))
    # Right edge
    for y in range(0, D+1):
        points.append((W, y))
    # Top edge is open
    return points

def no_cup_boundary_inside(polygon: List[Tuple[float, float]], W, D):
    # Check that no boundary point of the cup is strictly inside the polygon
    boundary_points = []
    # Sample boundary points with sufficient granularity
    steps = max(W, D) * 4  # finer steps
    for i in range(steps +1):
        t = i / steps
        # Bottom edge
        x = t * W
        y = 0
        boundary_points.append((x, y))
        # Left edge
        x = 0
        y = t * D
        boundary_points.append((x, y))
        # Right edge
        x = W
        y = t * D
        boundary_points.append((x, y))
    # Top edge is open, so not included
    for point in boundary_points:
        if polygon_contains_point(polygon, point):
            return False
    return True

def solve():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, W, D = readints()
        polygon = []
        for _ in range(N):
            x, y = readints()
            polygon.append( (x, y) )
        success = False
        for i in range(N):
            vx, vy = polygon[i]
            angle = math.atan2(vy, vx) - 0  # We need to rotate so that vy' =0
            # The angle to rotate so that this vertex is on x-axis
            # Desired: rotated vy =0
            # Current: vy
            # Rotate by -theta where theta = atan2(vy, vx)
            theta = math.atan2(vy, vx)
            rotation_angle = -theta
            rotated = rotate_polygon(polygon, rotation_angle)
            # Now, rotated vertex i should be on x-axis (y=0)
            # Due to floating point, set ty = -rotated[i][1]
            ty = -rotated[i][1]
            translated = translate_polygon(rotated, 0, ty)
            # Now, rotated[i] is at y=0
            # Find rotated[i][0] + tx is within [0, W]
            rx, ry = translated[i]
            # ry should be 0
            # tx needs to satisfy 0 <= rx + tx <= W
            tx_min = -rx
            tx_max = W - rx
            # To avoid floating precision issues, add a small epsilon
            epsilon = 1e-9
            tx_possible_min = tx_min
            tx_possible_max = tx_max
            # Try tx such that translated[i][0] + tx in [0, W]
            # To simplify, can set translated[i][0] + tx to 0 and W, and see if any feasible tx in between
            # We'll sample tx in tx_min to tx_max
            samples = 10
            for s in range(samples+1):
                tx = tx_min + (tx_max - tx_min) * s / samples
                final = translate_polygon(translated, tx, 0)
                # Check all vertices have y >=0
                all_y_non_negative = all(y >= -1e-9 for x, y in final)
                if not all_y_non_negative:
                    continue
                # Check some point is strictly inside sauce cup
                has_inside = any_point_inside(final, W, D)
                if not has_inside:
                    continue
                # Check no cup boundary point is inside polygon
                no_boundary_inside = no_cup_boundary_inside(final, W, D)
                if not no_boundary_inside:
                    continue
                # Also, check that at least one vertex is on x-axis within [0, W]
                # Which is true by construction
                # All conditions satisfied
                success = True
                break
            if success:
                break
        result = "Yes" if success else "No"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    solve()