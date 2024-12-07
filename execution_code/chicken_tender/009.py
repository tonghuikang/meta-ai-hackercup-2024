import math
import sys
from shapely.geometry import Polygon, Point, LineString
from shapely import affinity

def can_fit(N, W, D, vertices):
    # Define the sauce cup polygon
    sauce_cup = Polygon([(0,0), (W,0), (W,D), (0,D)])
    sauce_cup_interior = sauce_cup.intersection(sauce_cup.buffer(-1e-9))
    
    for i in range(N):
        x_i, y_i = vertices[i]
        if x_i == 0 and y_i == 0:
            theta = 0.0
        else:
            theta = math.atan2(-y_i, x_i)
        # Rotate all vertices
        rotated = []
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        for x, y in vertices:
            x_rot = x * cos_theta - y * sin_theta
            y_rot = x * sin_theta + y * cos_theta
            rotated.append( (x_rot, y_rot) )
        # Find minimum y to determine vertical translation
        min_y = min(y for _, y in rotated)
        t_y = max(-min_y, 0)
        # Apply vertical translation
        translated = [ (x, y + t_y) for x, y in rotated ]
        # The selected vertex is now at y=0 + t_y >=0
        x_selected = translated[i][0]
        # The selected vertex must lie within [0, W]
        # So translate horizontally by t_x such that x_selected + t_x ∈ [0, W]
        t_x_min = -x_selected
        t_x_max = W - x_selected
        # To cover possible positions, we consider placing the vertex at 0 and at W
        # and also check if placing it anywhere in between can satisfy the conditions
        possible_t_x = [0, W - x_selected]
        # Additionally, consider placing it on other vertices to maximize chances
        for t_x in possible_t_x:
            # Apply horizontal translation
            final_translated = [ (x + t_x, y) for x, y in translated ]
            # Check if the selected vertex is within [0, W]
            x_final = final_translated[i][0]
            if x_final < -1e-6 or x_final > W + 1e-6:
                continue
            # Create shapely polygon
            polygon = Polygon(final_translated)
            if not polygon.is_valid:
                continue
            # Check all vertices are on or above x-axis
            if any(y < -1e-6 for x, y in final_translated):
                continue
            # Check some point lies strictly within the sauce cup
            if not polygon.intersects(sauce_cup_interior):
                continue
            # Check no point on the sauce cup boundary lies strictly inside the polygon
            sauce_cup_boundary = sauce_cup.boundary
            intersection = polygon.intersection(sauce_cup_boundary)
            # If intersection contains any interior points, then some boundary point lies inside
            if intersection and not intersection.is_empty:
                # We need to check if any point on the boundary is inside the polygon interior
                # which in shapely can be checked using 'within'
                # However, shapely's intersection includes boundaries, so we need to ensure
                # that no boundary point is within the polygon's interior
                # One way is to check if the interior of intersection is non-empty
                if intersection.area > 1e-9:
                    continue
            # All conditions satisfied
            return True
    return False

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        parts = sys.stdin.readline().strip().split()
        while len(parts) < 3:
            parts += sys.stdin.readline().strip().split()
        N, W, D = map(int, parts)
        vertices = []
        read = 0
        while read < N:
            parts = sys.stdin.readline().strip().split()
            while len(parts) < 2:
                parts += sys.stdin.readline().strip().split()
            x, y = map(int, parts[:2])
            vertices.append( (x, y) )
            read +=1
        if can_fit(N, W, D, vertices):
            print(f"Case #{case}: Yes")
        else:
            print(f"Case #{case}: No")

if __name__ == "__main__":
    main()