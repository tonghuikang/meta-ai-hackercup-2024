import sys
import math
from itertools import combinations

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, angle):
    """Rotate polygon by angle radians."""
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return [(x * cos_a - y * sin_a, x * sin_a + y * cos_a) for (x, y) in polygon]

def translate_polygon(polygon, tx, ty):
    """Translate polygon by tx and ty."""
    return [(x + tx, y + ty) for (x, y) in polygon]

def point_inside_rect(x, y, W, D):
    """Check if point is strictly inside the sauce cup."""
    return 0 < x < W and 0 < y < D

def polygon_contains_point(polygon, point):
    """Check if polygon contains the point using ray casting."""
    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i+1)%n]
        if ((yi > y) != (yj > y)):
            x_intersect = (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi
            if x < x_intersect:
                inside = not inside
    return inside

def segments_intersect(p1, p2, q1, q2):
    """Check if segments p1p2 and q1q2 intersect."""
    def ccw(a, b, c):
        return (c[1]-a[1])*(b[0]-a[0]) > (b[1]-a[1])*(c[0]-a[0])
    return (ccw(p1, q1, q2) != ccw(p2, q1, q2)) and (ccw(p1, p2, q1) != ccw(p1, p2, q2))

def sauce_cup_points(W, D, step=1):
    """Generate points on the boundary of the sauce cup."""
    points = []
    # Bottom edge
    for x in range(0, W+1, step):
        points.append((x, 0))
    # Right edge
    for y in range(0, D+1, step):
        points.append((W, y))
    # Top edge
    for x in range(W, -1, -step):
        points.append((x, D))
    # Left edge
    for y in range(D, -1, -step):
        points.append((0, y))
    return points

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, W, D = readints()
        polygon = [tuple(map(float, sys.stdin.readline().split())) for _ in range(N)]
        found = False
        for i in range(N):
            # Consider vertex i to be on x-axis
            for j in range(i+1, N):
                # Consider edge from i to j to determine rotation
                dx = polygon[j][0] - polygon[i][0]
                dy = polygon[j][1] - polygon[i][1]
                if dy == 0:
                    angle = 0
                else:
                    angle = -math.atan2(dy, dx)
                rotated = rotate_polygon(polygon, angle)
                min_y = min(y for (x, y) in rotated)
                # Translate vertically so that min_y == 0
                translated = translate_polygon(rotated, 0, -min_y)
                # Now, vertex i is at some (x, 0)
                xi, yi = translated[i]
                # We need to place xi between 0 and W
                tx_min = -xi
                tx_max = W - xi
                # Check feasible translation
                if tx_min > tx_max:
                    continue
                # Try translating to tx_min and tx_max
                for tx in [tx_min, tx_max]:
                    final = translate_polygon(translated, tx, 0)
                    # Check all vertices are on or above x-axis
                    if any(y < -1e-6 for (x, y) in final):
                        continue
                    # Check some vertex is on x-axis between 0 and W
                    on_x_axis = any(0-1e-6 <= y <= 1e-6 and 0 -1e-6 <= x <= W +1e-6 for (x, y) in final)
                    if not on_x_axis:
                        continue
                    # Check some point is strictly inside sauce cup
                    # We can check the centroid
                    centroid_x = sum(x for (x, y) in final) / N
                    centroid_y = sum(y for (x, y) in final) / N
                    if not point_inside_rect(centroid_x, centroid_y, W, D):
                        # Try checking more points
                        # Alternatively, check if any vertex is strictly inside
                        inside = any(point_inside_rect(x, y, W, D) for (x, y) in final)
                        if not inside:
                            continue
                    # Check no point on sauce cup is strictly inside the polygon
                    # Sample points on sauce cup
                    satisfies = True
                    # To speed up, sample with step size
                    cup_boundary = sauce_cup_points(W, D, step=1)
                    for (x, y) in cup_boundary:
                        if polygon_contains_point(final, (x, y)):
                            satisfies = False
                            break
                    if satisfies:
                        found = True
                        break
                if found:
                    break
            if found:
                break
        result = "Yes" if found else "No"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()