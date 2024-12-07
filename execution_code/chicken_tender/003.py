import sys
import math
from math import atan2, cos, sin, hypot
from itertools import combinations
import sys

def input():
    return sys.stdin.read()

def rotate_polygon(polygon, angle):
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return [(x * cos_a - y * sin_a, x * sin_a + y * cos_a) for x, y in polygon]

def translate_polygon(polygon, dx, dy):
    return [(x + dx, y + dy) for x, y in polygon]

def point_in_polygon(point, polygon):
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

def polygon_contains_point(polygon, point):
    return point_in_polygon(point, polygon)

def readints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N, W, D = map(int, sys.stdin.readline().split())
        polygon = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
        possible = False
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                xi, yi = polygon[i]
                xj, yj = polygon[j]
                angle = math.atan2(yj - yi, xj - xi)
                # Rotate so that edge i-j is horizontal
                rotated = rotate_polygon(polygon, -angle)
                # Now, place vertex i on the x-axis
                min_y = min(y for x, y in rotated)
                # Translate vertically so that vertex i is on x-axis
                translated = translate_polygon(rotated, 0, -rotated[i][1])
                # Check all vertices are on or above x-axis
                if any(y < -1e-6 for x, y in translated):
                    continue
                # Now, find the x-coordinate of vertex i after translation
                xi_new, yi_new = translated[i]
                # Vertex i should be on x-axis between 0 and W
                if not (0 - 1e-6 <= xi_new <= W + 1e-6):
                    continue
                # Now, check if any point of the polygon is strictly inside the sauce cup
                # We can sample the centroid
                centroid_x = sum(x for x, y in translated) / N
                centroid_y = sum(y for x, y in translated) / N
                if not (0 < centroid_x < W and 0 < centroid_y < D):
                    continue
                # Also ensure no point on the sauce cup is strictly inside the polygon
                # Check the four corners
                sauce_points = [(0,0), (W,0), (W,D), (0,D)]
                overlap = False
                for sp in sauce_points:
                    if polygon_contains_point(translated, sp):
                        overlap = True
                        break
                if overlap:
                    continue
                # If all conditions met
                possible = True
                break
            if possible:
                break
        print(f"Case #{tc}: {'Yes' if possible else 'No'}")

if __name__ == "__main__":
    main()