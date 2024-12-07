import sys
import math
from math import atan2, cos, sin, sqrt
from itertools import combinations

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, angle):
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return [(x * cos_a - y * sin_a, x * sin_a + y * cos_a) for (x, y) in polygon]

def translate_polygon(polygon, dx, dy):
    return [(x + dx, y + dy) for (x, y) in polygon]

def point_inside_polygon(x, y, polygon):
    # Ray casting algorithm for point inside polygon
    inside = False
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]
        if ((yi > y) != (yj > y)):
            intersect = (xj - xi) * (y - yi) / (yj - yi) + xi
            if x < intersect:
                inside = not inside
    return inside

def polygon_inside_cup(polygon, W, D):
    # Check if any point is strictly inside the cup
    for (x, y) in polygon:
        if 0 < x < W and 0 < y < D:
            return True
    return False

def cup_points_inside_polygon(polygon, W, D):
    # Check edges of the cup to see if any point is strictly inside the polygon
    # Since polygon is convex, it's sufficient to check a few points on each edge
    steps = 10
    for i in range(steps + 1):
        x = i * W / steps
        y = 0
        if point_inside_polygon(x, y, polygon):
            return True
        y = D
        if point_inside_polygon(x, y, polygon):
            return True
    for i in range(steps + 1):
        y = i * D / steps
        x = 0
        if point_inside_polygon(x, y, polygon):
            return True
        x = W
        if point_inside_polygon(x, y, polygon):
            return True
    return False

def all_vertices_above_x(polygon):
    for (x, y) in polygon:
        if y < -1e-6:
            return False
    return True

def can_fit(polygon, W, D):
    N = len(polygon)
    for i in range(N):
        # Rotate so that polygon[i] is on the x-axis
        xi, yi = polygon[i]
        angle = -math.atan2(yi, 1e-6 if xi == 0 and yi ==0 else xi)
        # To place on x-axis, calculate angle to make this point horizontal
        # Better: Calculate angle to make the edge from polygon[i] to polygon[i+1] horizontal
        # Or to make the point polygon[i] lie on x-axis by rotating by its own angle
        # More precise approach:
        angle = -math.atan2(yi, xi) if not (xi == 0 and yi ==0) else 0
        rotated = rotate_polygon(polygon, angle)
        # Now polygon[i] is on x-axis; get its new position
        rx, ry = rotated[i]
        # Translate so that rx is in [0, W]
        # We need to place rx somewhere in [0, W]
        # Let us set rx to any position between 0 and W by translating by tx
        # To cover all possibilities, we can set tx such that rx + tx is in [0, W]
        # So tx in [-rx, W - rx]
        # Let's choose tx such that rx + tx = 0, tx = -rx
        # and also rx + tx = W, tx = W - rx
        # To cover, we can test multiple tx in this range
        # To simplify, let's set tx so that rx + tx = midpoint between 0 and W
        # Or iterate over possible tx placements
        # Since W <=100 and precision allows, sample tx values
        # But to make it efficient, just try placing at 0 and at W
        possible_txs = [ -rx, W - rx ]
        for tx in possible_txs:
            translated = translate_polygon(rotated, tx, -rotated[i][1])  # y of i to 0
            if not all_vertices_above_x(translated):
                continue
            # Check some vertex is on x-axis between 0 and W
            on_x_axis = False
            for (x, y) in translated:
                if abs(y) < 1e-6 and 0 -1e-6 <= x <= W +1e-6:
                    on_x_axis = True
                    break
            if not on_x_axis:
                continue
            # Check some point strictly inside the cup
            if not polygon_inside_cup(translated, W, D):
                continue
            # Check no point on the cup is strictly inside the polygon
            if cup_points_inside_polygon(translated, W, D):
                continue
            # All conditions met
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
        result = "Yes" if can_fit(polygon, W, D) else "No"
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()