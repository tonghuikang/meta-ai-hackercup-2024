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

def point_in_polygon(point, polygon):
    # Ray casting algorithm for point in polygon
    x, y = point
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

def polygon_contains_point(polygon, point):
    # Check if the point is strictly inside the polygon
    # Not on the boundary
    return point_in_polygon(point, polygon)

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, W, D = map(int, sys.stdin.readline().split())
        vertices = [tuple(map(float, sys.stdin.readline().split())) for _ in range(N)]
        success = False
        for i in range(N):
            for j in range(i+1, N):
                # Try aligning edge from i to j with x-axis
                xi, yi = vertices[i]
                xj, yj = vertices[j]
                dx = xj - xi
                dy = yj - yi
                angle = math.atan2(dy, dx)
                # Rotate polygon so that edge i-j lies on x-axis
                rotated = rotate_polygon(vertices, -angle)
                # Now, edge i-j should lie horizontally
                # Find new positions of i and j
                rotated_i = rotated[i]
                rotated_j = rotated[j]
                # Translate so that rotated_i is at (0,0)
                translated = translate_polygon(rotated, -rotated_i[0], -rotated_i[1])
                # Now, rotated_j is at (dx', 0)
                rotated_j = translated[j]
                # The edge is now from (0,0) to (dx', 0)
                # We need to place this edge somewhere between x=0 and x=W
                # Let's try placing rotated_i at (tx, 0), where tx + dx' <= W
                # and tx >=0
                # Since we already translated to (0,0), possible tx is from 0 to W - dx'
                # If dx' > W, it's impossible
                edge_length = math.hypot(rotated_j[0], rotated_j[1])
                if edge_length > W + 1e-6:
                    continue
                # Possible tx range: [0, W - edge_length]
                # To cover cases where multiple points can lie on x-axis, we can choose tx such that rotated_i is within [0, W]
                # Specifically, we can set tx such that rotated_i (which is (0,0)) is at some position between [0, W]
                # So tx can be from 0 to W
                # We'll sample tx values within [0, W - edge_length]
                min_tx = 0
                max_tx = W - edge_length
                if max_tx < 0:
                    continue
                # We'll try multiple tx values between min_tx and max_tx
                # To simplify, try tx = 0 and tx = W - edge_length
                # and possibly a few intermediate points
                tx_samples = [0, W - edge_length]
                # Add edge_length / 2 if possible
                if edge_length / 2 <= W - edge_length / 2:
                    tx_samples.append((W - edge_length)/2)
                for tx in tx_samples:
                    # Translate horizontally by tx
                    final_polygon = translate_polygon(translated, tx, 0)
                    # Check all y >=0 and y <= D
                    y_valid = all(y >= -1e-6 and y <= D + 1e-6 for (x, y) in final_polygon)
                    if not y_valid:
                        continue
                    # Check all x between 0 and W
                    x_valid = all(x >= -1e-6 and x <= W + 1e-6 for (x, y) in final_polygon)
                    if not x_valid:
                        continue
                    # Check that at least one vertex lies on x-axis between 0 and W
                    on_x_axis = any(abs(y) <=1e-6 and 0 -1e-6 <= x <= W +1e-6 for (x, y) in final_polygon)
                    if not on_x_axis:
                        continue
                    # Check that some point is strictly inside the cup
                    # We'll check if the centroid is inside
                    centroid_x = sum(x for (x, y) in final_polygon) / N
                    centroid_y = sum(y for (x, y) in final_polygon) / N
                    if not (0 < centroid_x < W and 0 < centroid_y < D):
                        # Alternatively, sample a point inside the polygon
                        # Here, we proceed to check some other point
                        # For simplicity, continue only if centroid is inside
                        pass
                    # Check if any point is strictly inside the cup
                    # Let's check if centroid is inside
                    has_inside = (0 < centroid_x < W and 0 < centroid_y < D)
                    if not has_inside:
                        # Try to find any point inside
                        has_inside = False
                        for (x, y) in final_polygon:
                            if 0 < x < W and 0 < y < D:
                                has_inside = True
                                break
                    if not has_inside:
                        continue
                    # Now, check that no point on the cup boundary lies strictly inside the polygon
                    # Define boundary points: left (0,y), right (W,y), top (x,D)
                    # We'll sample some points on the boundaries and check if they are inside the polygon
                    # To simplify, sample discrete points
                    boundary_safe = True
                    sample_points = []
                    # Sample bottom edge (already vertices on x-axis are allowed)
                    # Sample left edge
                    for y in [0, D]:
                        sample_points.append((0, y))
                        sample_points.append((W, y))
                    # Sample some points on left and right edges
                    for y in [0, D]:
                        sample_points.append((0, y))
                        sample_points.append((W, y))
                    # Sample some points on top edge
                    for x in [0, W]:
                        sample_points.append((x, D))
                    # Additionally, sample midpoints
                    mid_samples = 5
                    for k in range(1, mid_samples):
                        y = D * k / mid_samples
                        sample_points.append((0, y))
                        sample_points.append((W, y))
                        sample_points.append((W * k / mid_samples, D))
                    for pt in sample_points:
                        if point_in_polygon(pt, final_polygon):
                            boundary_safe = False
                            break
                    if not boundary_safe:
                        continue
                    # All conditions satisfied
                    success = True
                    break
                if success:
                    break
            if success:
                break
        print(f"Case #{test_case}: {'Yes' if success else 'No'}")

if __name__ == "__main__":
    main()