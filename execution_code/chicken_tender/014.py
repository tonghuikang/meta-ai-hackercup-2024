import sys
import math
from shapely.geometry import Polygon, LineString, Point
from shapely.affinity import rotate, translate

def can_fit(N, W, D, vertices):
    original_polygon = Polygon(vertices)
    if not original_polygon.is_valid or not original_polygon.is_convex:
        original_polygon = original_polygon.convex_hull
    # Sauce cup boundary as LineStrings
    sauce_boundary = LineString([(0, D), (0, 0), (W, 0), (W, D)])
    for i in range(N):
        xi, yi = vertices[i]
        if xi == 0 and yi == 0:
            theta = 0
        else:
            theta = math.degrees(math.atan2(-yi, xi))
        rotated = rotate(original_polygon, theta, origin=(0,0), use_radians=False)
        # After rotation, the i-th vertex should be on x-axis
        # Find the i-th vertex's new position
        vx, vy = rotated.exterior.coords[i]
        # Translate vertically so that vy = 0
        translated = translate(rotated, yoff=-vy)
        # Now, translate horizontally so that vx is between 0 and W
        min_tx = -vx
        max_tx = W - vx
        # Since it must lie within [0, W], we need to translate tx in [min_tx, max_tx]
        # To cover all possibilities, we can choose tx such that vx + tx = 0 to W
        # But to simplify, choose tx such that vx + tx = 0 and W
        for tx in [0 - vx, W - vx]:
            final_polygon = translate(translated, xoff=tx)
            # Check all vertices are on or above x-axis
            if any(pt[1] < -1e-8 for pt in final_polygon.exterior.coords):
                continue
            # Check some point of the polygon is strictly within the sauce cup
            # We'll check the centroid
            centroid = final_polygon.centroid
            if not (0 < centroid.x < W and 0 < centroid.y < D):
                # Alternatively, check if intersection between polygon and interior of cup is non-empty
                cup_interior = Polygon([(0,0), (W,0), (W,D), (0,D)])
                if not final_polygon.intersection(cup_interior).is_empty:
                    pass
                else:
                    continue
            # Check no point on the sauce cup lies strictly within the polygon
            # Check boundary lines of sauce cup
            intersects = False
            for line in [(0, D, 0, 0), (0,0, W,0), (W,0, W,D)]:
                ls = LineString([(line[0], line[1]), (line[2], line[3])])
                if final_polygon.contains(ls):
                    intersects = True
                    break
            if intersects:
                continue
            # Additionally, ensure that sauce cup boundary does not lie inside the polygon
            # which can be checked by intersection of interiors
            # Define sauce cup as closed boundaries
            sauce_edges = [
                LineString([(0, D), (0, 0)]),
                LineString([(0, 0), (W, 0)]),
                LineString([(W, 0), (W, D)])
            ]
            boundary_inside = False
            for edge in sauce_edges:
                if final_polygon.contains(edge):
                    boundary_inside = True
                    break
            if boundary_inside:
                continue
            # All conditions satisfied
            return True
    return False

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N,W,D = map(int, sys.stdin.readline().split())
        vertices = []
        for _ in range(N):
            x,y = map(int, sys.stdin.readline().split())
            vertices.append((x,y))
        if can_fit(N, W, D, vertices):
            print(f"Case #{tc}: Yes")
        else:
            print(f"Case #{tc}: No")

# Adding an extension to check convexity using shapely
def extend_shapely():
    from shapely.geometry import Polygon

    def is_convex(self):
        if not self.is_valid or self.is_empty:
            return False
        coords = list(self.exterior.coords)
        if len(coords) < 4:
            return True
        sign = 0
        n = len(coords) -1
        for i in range(n):
            dx1 = coords[(i+1) % n][0] - coords[i][0]
            dy1 = coords[(i+1) % n][1] - coords[i][1]
            dx2 = coords[(i+2) % n][0] - coords[(i+1) % n][0]
            dy2 = coords[(i+2) % n][1] - coords[(i+1) % n][1]
            z = dx1 * dy2 - dy1 * dx2
            if z != 0:
                if sign == 0:
                    sign = 1 if z > 0 else -1
                elif (z > 0 and sign == -1) or (z < 0 and sign ==1):
                    return False
        return True

    Polygon.is_convex = is_convex

extend_shapely()

if __name__ == "__main__":
    main()