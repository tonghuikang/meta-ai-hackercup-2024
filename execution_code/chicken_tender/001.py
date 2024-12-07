import sys
import math

def isclose(a, b, eps=1e-9):
    return abs(a - b) < eps

def read_input():
    import sys
    import threading
    def main():
        import math
        import sys
        import shapely.geometry
        from shapely.geometry import Polygon, Point
        import shapely.affinity
        T = int(sys.stdin.readline())
        for case_num in range(1, T+1):
            N, W, D = map(int, sys.stdin.readline().split())
            points = []
            for _ in range(N):
                x_i, y_i = map(float, sys.stdin.readline().split())
                points.append((x_i, y_i))
            result = solve_case(N, W, D, points)
            print(f"Case #{case_num}: {result}")
    threading.Thread(target=main).start()

def solve_case(N, W, D, points):
    import math
    import shapely.geometry
    from shapely.geometry import Polygon, Point
    import shapely.affinity
    eps = 1e-8
    cup_polygon = Polygon([(0,0), (W,0), (W,D), (0,D)])

    # Collect all possible angles
    angles = set()
    for i in range(N):
        xi, yi = points[i]
        for j in range(i+1, N):
            xj, yj = points[j]
            delta_x = xj - xi
            delta_y = yj - yi
            angle = math.atan2(delta_y, delta_x)
            angles.add(angle)
            angles.add(angle + math.pi)
    angles = list(angles)
    for angle in angles:
        # Rotate polygon
        rotated_points = [rotate_point(p, angle) for p in points]
        # Translate polygon vertically so that all y >= 0
        y_coords = [p[1] for p in rotated_points]
        ymin = min(y_coords)
        rotated_translated_points = [(x, y - ymin) for x, y in rotated_points]
        # Check if any vertex is at y=0
        vertices_at_y0 = [p for p in rotated_translated_points if isclose(p[1], 0)]
        if not vertices_at_y0:
            continue
        # For each vertex at y=0, try to align it to x in [0, W]
        x_values = [p[0] for p in vertices_at_y0]
        for x_i in x_values:
            # Since we can shift along x, we can choose any shift to place x_i at x0 in [0,W]
            x_shifts = [ - x_i + x0 for x0 in [0, W] ]
            x_shifts += [ - x_i + x0 for x0 in [max(0, x_i), min(W, x_i)] ]
            # We can also consider any x0 in [0,W], but since we can shift arbitrarily, let's pick x0 = min(max(0,x_i), W)
            # Let's pick x_offset such that x_i + x_offset in [0,W]
            if x_i < 0:
                x_offset = - x_i
            elif x_i > W:
                x_offset = W - x_i
            else:
                x_offset = 0  # x_i is already in [0,W]
            x_offset_variations = [x_offset]
            for x_offset in x_offset_variations:
                # Shift polygon
                shifted_points = [(x + x_offset, y) for x, y in rotated_translated_points]
                polygon = Polygon(shifted_points)
                # Check intersection with cup
                intersection = polygon.intersection(cup_polygon)
                if intersection.is_empty:
                    continue
                if intersection.area == 0:
                    continue
                # Check if any cup corner is inside the polygon
                cup_corners = [Point(0,0), Point(0,D), Point(W,0), Point(W,D)]
                cup_corner_inside = False
                for corner in cup_corners:
                    if polygon.contains(corner):
                        cup_corner_inside = True
                        break
                if cup_corner_inside:
                    continue
                # All conditions met
                return 'Yes'
    return 'No'

def rotate_point(p, angle):
    x, y = p
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    new_x = x * cos_theta - y * sin_theta
    new_y = x * sin_theta + y * cos_theta
    return (new_x, new_y)

if __name__ == '__main__':
    import sys

    try:
        import shapely
    except ImportError:
        print("This solution requires the 'shapely' library.")
        sys.exit(1)
    read_input()