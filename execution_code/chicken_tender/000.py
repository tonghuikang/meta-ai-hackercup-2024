import sys
import math
from shapely.geometry import Polygon, LineString, Point
from shapely.affinity import rotate, translate

def readints():
    return list(map(int, sys.stdin.readline().split()))

def can_fit(N, W, D, vertices):
    # Create shapely polygon
    poly = Polygon(vertices)
    if not poly.is_valid or not poly.is_convex:
        return False
    # Define sauce cup boundary
    cup_boundary = LineString([(0,0), (W,0), (W,D), (0,D), (0,0)])
    cup_interior = Polygon([(0,0), (W,0), (W,D), (0,D)])
    
    for i in range(N):
        xi, yi = vertices[i]
        if xi == 0 and yi ==0:
            angle = 0.0
        else:
            angle = math.atan2(-yi, xi) * 180 / math.pi
        rotated = rotate(poly, angle, origin=(0,0), use_radians=False)
        # After rotation, vertex i should be on x-axis
        rotated_vertices = list(rotated.exterior.coords)[:-1]
        xi_rot, yi_rot = rotated_vertices[i]
        if abs(yi_rot) > 1e-6:
            continue
        # Now, translate in x to place xi_rot between 0 and W
        min_shift = -xi_rot
        max_shift = W - xi_rot
        # Sample shifts from min_shift to max_shift
        # To handle precision, sample shifts at intervals
        samples = 100
        for s in range(samples +1):
            shift = min_shift + (max_shift - min_shift) * s / samples
            translated = translate(rotated, xoff=shift, yoff=0)
            translated_vertices = list(translated.exterior.coords)[:-1]
            # Check all y >=0
            if any(y < -1e-6 for (_, y) in translated_vertices):
                continue
            # Check vertex i is on x-axis within [0, W]
            xi_final, yi_final = translated_vertices[i]
            if not (abs(yi_final) <=1e-6 and 0 -1e-6 <= xi_final <= W +1e-6):
                continue
            # Check some interior point is within (0,W)x(0,D)
            intersection = translated.intersection(cup_interior)
            if intersection.is_empty:
                continue
            # Check that no point on cup boundary is strictly inside the polygon
            # Except possibly the vertex on bottom
            # To simplify, check intersection between polygon interior and cup boundary
            # Allow touching but not intersecting
            cup_boundary_points = [
                # Sample points on boundaries
                LineString([(0,0), (0,D)]),
                LineString([(0,D), (W,D)]),
                LineString([(W,D), (W,0)]),
                LineString([(W,0), (0,0)])
            ]
            violating = False
            for boundary in cup_boundary_points:
                inter = translated.intersection(boundary)
                if inter.is_empty:
                    continue
                if isinstance(inter, Point):
                    # Allow the vertex on bottom
                    if not (inter.x == xi_final and abs(inter.y) <=1e-6):
                        violating = True
                        break
                else:
                    # Line or multiple points
                    for geom in inter:
                        if isinstance(geom, Point):
                            if not (geom.x == xi_final and abs(geom.y) <=1e-6):
                                violating = True
                                break
                        else:
                            violating = True
                            break
                if violating:
                    break
            if violating:
                continue
            # Passed all checks
            return True
    return False

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N, W, D = readints()
        vertices = [tuple(readints()) for _ in range(N)]
        # Check if convex
        # Shapely does not have is_convex, so we check convex hull
        poly = Polygon(vertices)
        if not poly.is_valid:
            convex = False
        else:
            convex = poly.equals(poly.convex_hull)
        if not convex:
            result = False
        else:
            result = can_fit(N, W, D, vertices)
        print(f"Case #{tc}: {'Yes' if result else 'No'}")

if __name__ == "__main__":
    main()