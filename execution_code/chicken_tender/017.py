import sys
import math
from itertools import combinations

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, angle):
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return [(x * cos_a - y * sin_a, x * sin_a + y * cos_a) for (x, y) in polygon]

def translate_polygon(polygon, dx, dy):
    return [(x + dx, y + dy) for (x, y) in polygon]

def is_point_inside_rect(x, y, W, D):
    return 0 < x < W and 0 < y < D

def no_point_in_polygon(polygon, W, D):
    # Check corners of sauce cup
    corners = [(0,0), (W,0), (W,D), (0,D)]
    for cx, cy in corners:
        if point_in_polygon(cx, cy, polygon):
            return False
    return True

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

def has_point_inside(polygon, W, D):
    # Check if any point inside the sauce cup is inside the polygon
    # Using sampling
    step = 0.5
    x = step
    while x < W:
        y = step
        while y < D:
            if point_in_polygon(x, y, polygon):
                return True
            y += step
        x += step
    return False

def can_fit(N, W, D, polygon):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            # Calculate angle to place edge i-j on x-axis
            x1, y1 = polygon[i]
            x2, y2 = polygon[j]
            angle = math.atan2(y2 - y1, x2 - x1)
            rotated = rotate_polygon(polygon, -angle)
            # After rotation, y1 should be 0
            rotated = translate_polygon(rotated, -rotated[i][0], -rotated[i][1])
            # Now, check if rotated[j] lies on x-axis between 0 and W
            xj = rotated[j][0]
            if not (0 <= xj <= W):
                continue
            # Check all y >=0
            if min(y for x, y in rotated) < -1e-6:
                continue
            # Check some point inside the sauce cup
            if not has_point_inside(rotated, W, D):
                continue
            # Check no point of the sauce cup is inside the polygon
            if not no_point_in_polygon(rotated, W, D):
                continue
            return True
    return False

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N, W, D = readints()
        polygon = [tuple(readints()) for _ in range(N)]
        if can_fit(N, W, D, polygon):
            result = "Yes"
        else:
            result = "No"
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()