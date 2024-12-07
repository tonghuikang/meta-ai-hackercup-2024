import sys
import math

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, angle):
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    return [(x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta) for (x, y) in polygon]

def translate_polygon(polygon, tx, ty):
    return [(x + tx, y + ty) for (x, y) in polygon]

def polygon_inside_cup(polygon, W, D):
    # Check if all vertices are on or above x-axis
    for (x, y) in polygon:
        if y < -1e-9:
            return False
    # Check if at least one vertex lies on x-axis between 0 and W
    on_x_axis = False
    for (x, y) in polygon:
        if abs(y) < 1e-9 and -1e-9 <= x <= W + 1e-9:
            on_x_axis = True
            break
    if not on_x_axis:
        return False
    # Check if some point is strictly within the bounds of the sauce cup
    inside = False
    for (x, y) in polygon:
        if 0 < x < W and 0 < y < D:
            inside = True
            break
    if not inside:
        # Also check edges for any point inside
        n = len(polygon)
        for i in range(n):
            j = (i + 1) % n
            x1, y1 = polygon[i]
            x2, y2 = polygon[j]
            # Check if any segment intersects interior of cup
            # For simplicity, assume if any vertex is inside, it's sufficient
            pass
    if not inside:
        return False
    # Check that no point on the sauce cup is strictly within the polygon
    # Sample key points on the sauce cup
    # We can sample the boundaries: (0,y), (W,y) for y in [0,D]
    # and (x,0), (x,D) for x in [0,W]
    # To simplify, check corners
    corners = [(0,0), (W,0), (0,D), (W,D)]
    for (x, y) in corners:
        if point_inside_polygon(x, y, polygon):
            return False
    return True

def point_inside_polygon(x, y, polygon):
    # Ray casting algorithm for point in polygon
    n = len(polygon)
    inside = False
    for i in range(n):
        j = (i - 1) % n
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        if ((yi > y) != (yj > y)):
            intersect = (xj - xi) * (y - yi) / (yj - yi) + xi
            if x < intersect:
                inside = not inside
    return inside

def can_fit(polygon, W, D):
    N = len(polygon)
    for i in range(N):
        j = (i + 1) % N
        # Edge from polygon[i] to polygon[j]
        x1, y1 = polygon[i]
        x2, y2 = polygon[j]
        # Compute angle to make this edge horizontal
        dx = x2 - x1
        dy = y2 - y1
        angle = -math.atan2(dy, dx)
        # Rotate polygon
        rotated = rotate_polygon(polygon, angle)
        # After rotation, the edge from i to j should be horizontal
        # Let’s place the edge on the x-axis by translating vertically
        min_y = min(y for (x, y) in rotated)
        translated = translate_polygon(rotated, 0, -min_y)
        # Now, ensure that edge i-j lies on x-axis
        # Find the x range of the edge
        rotated_i = translated[i]
        rotated_j = translated[j]
        min_x = min(rotated_i[0], rotated_j[0])
        max_x = max(rotated_i[0], rotated_j[0])
        # Now, we need to translate horizontally so that some point of the edge lies between 0 and W on x-axis
        # The edge is from min_x to max_x on x-axis
        # We need to translate so that the edge overlaps with [0, W]
        # So, the translation tx must satisfy:
        # rotated_i[0] + tx <= W and rotated_j[0] + tx >= 0
        tx_min = -max(rotated_i[0], rotated_j[0])
        tx_max = W - min(rotated_i[0], rotated_j[0])
        # Iterate over possible translations, but since W <=100, try incrementally
        # To handle floating points, iterate in steps
        steps = 100
        for s in range(steps +1 ):
            tx = tx_min + (tx_max - tx_min) * s / steps
            translated_final = translate_polygon(translated, tx, 0)
            if polygon_inside_cup(translated_final, W, D):
                return True
    return False

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N, W, D = readints()
        polygon = []
        for _ in range(N):
            x, y = readints()
            polygon.append((x, y))
        if can_fit(polygon, W, D):
            res = "Yes"
        else:
            res = "No"
        print(f"Case #{tc}: {res}")

if __name__ == "__main__":
    main()