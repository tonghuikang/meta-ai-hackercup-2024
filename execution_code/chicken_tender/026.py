import math
import sys
import sys
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def rotate_polygon(polygon, theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    rotated = []
    for x, y in polygon:
        xr = x * cos_theta - y * sin_theta
        yr = x * sin_theta + y * cos_theta
        rotated.append((xr, yr))
    return rotated

def translate_polygon(polygon, tx, ty):
    return [(x + tx, y + ty) for x, y in polygon]

def is_all_y_non_negative(polygon):
    for x, y in polygon:
        if y < -1e-9:
            return False
    return True

def point_in_convex_polygon(point, polygon):
    # Using winding number for convex polygons
    x, y = point
    n = len(polygon)
    prev = polygon[-1]
    for curr in polygon:
        cross = (curr[0] - prev[0])*(y - prev[1]) - (curr[1] - prev[1])*(x - prev[0])
        if cross < -1e-9:
            return False
        prev = curr
    return True

def polygon_intersects_rectangle(polygon, W, D):
    # Check if any point inside rectangle is inside polygon
    # Check center
    if point_in_convex_polygon((W/2, D/2), polygon):
        return True
    # Check edges
    # Sample some points
    samples = 10
    for i in range(1, samples):
        x = W * i / samples
        y = D * i / samples
        if point_in_convex_polygon((x, y), polygon):
            return True
    return False

def has_point_inside_cup(polygon, W, D):
    # Check if there exists a point (x, y) with 0 <x < W and 0 <y < D inside the polygon
    # Simplest: check the center
    return point_in_convex_polygon((W/2, D/2), polygon)

def check_no_sauce_inside(polygon, W, D):
    # Check that no point on the sides is inside the polygon
    # Check left side x=0, y from 0 to D
    samples = 50
    for i in range(0, samples+1):
        y = D * i / samples
        if point_in_convex_polygon((0, y), polygon):
            return False
    # Check right side x=W, y from 0 to D
    for i in range(0, samples+1):
        y = D * i / samples
        if point_in_convex_polygon((W, y), polygon):
            return False
    # Check bottom side y=0, x from 0 to W
    for i in range(0, samples+1):
        x = W * i / samples
        if point_in_convex_polygon((x, 0), polygon):
            # Allow if it's the vertex on the bottom
            # But since we have a vertex on x-axis, it's okay
            # So, ensure it's a boundary point
            # Here, we assume polygon vertices on x-axis are allowed
            # So, check if (x,0) is exactly one of the vertices
            if not any(abs(px - x) < 1e-6 and abs(py - 0) < 1e-6 for px, py in polygon):
                return False
    return True

def any_intersection(polygon, W, D):
    # Check if polygon has any point strictly inside the sauce cup
    # We already have has_point_inside_cup
    return has_point_inside_cup(polygon, W, D)

def solve_case(N, W, D, vertices):
    for i in range(N):
        vx, vy = vertices[i]
        if vy == 0:
            theta = 0.0
        else:
            theta = -math.atan2(vy, 1e-9 if vx ==0 else vx)
            # To rotate the vertex to y=0
            theta = math.atan2(vy, vx)  # angle to x-axis
            theta = -theta
        rotated = rotate_polygon(vertices, theta)
        # Find the rotated vertex
        rvx, rvy = rotated[i]
        # Since we've rotated to make rvy = 0 (approx)
        # Now, place it between x=0 and x=W
        # We can try placing it at x=0 and x=W
        for tx in [ -rvx, W - rvx ]:
            translated = translate_polygon(rotated, tx, 0)
            # Check all y >=0
            if not is_all_y_non_negative(translated):
                continue
            # Check some point inside the cup is inside polygon
            if not any_intersection(translated, W, D):
                continue
            # Check no point on sauce cup is inside polygon
            if not check_no_sauce_inside(translated, W, D):
                continue
            # Additionally, ensure at least one vertex is on x-axis between 0 and W
            # Which is already satisfied by placing vertex at x=0 or x=W
            return True
    return False

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N, W, D = readints()
        vertices = []
        for _ in range(N):
            x, y = readints()
            vertices.append((x, y))
        can_fit = solve_case(N, W, D, vertices)
        print(f"Case #{tc}: {'Yes' if can_fit else 'No'}")

if __name__ == "__main__":
    main()