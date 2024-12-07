import sys
import math
import threading

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)
    MOD = 10**9 + 7

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N, R = map(int, sys.stdin.readline().split())
        triangles = []
        for _ in range(N):
            coords = list(map(int, sys.stdin.readline().split()))
            triangles.append(coords)
        
        # Precompute circle x limits for each y
        y_min_circle = -R
        y_max_circle = R
        circle_x_limits = {}
        for y in range(-R, R + 1):
            temp = R*R - y*y
            if temp < 0:
                continue
            x_max = int(math.isqrt(temp))
            circle_x_limits[y] = (-x_max, x_max)
        
        total_heat = 0
        for tri in triangles:
            x1, y1, x2, y2, x3, y3 = tri
            # Find y range of the triangle
            min_y = min(y1, y2, y3)
            max_y = max(y1, y2, y3)
            # Clamp to circle's y range
            min_y_clamped = max(min_y, -R)
            max_y_clamped = min(max_y, R)
            # If no overlap, skip
            if min_y_clamped > max_y_clamped:
                continue
            # Prepare edges
            edges = [
                (x1, y1, x2, y2),
                (x2, y2, x3, y3),
                (x3, y3, x1, y1)
            ]
            # For each y in clamped range
            for y in range(min_y_clamped, max_y_clamped + 1):
                if y not in circle_x_limits:
                    continue
                intersections = []
                for edge in edges:
                    x_a, y_a, x_b, y_b = edge
                    # Check if the edge crosses the horizontal line at y
                    if y_a == y_b:
                        # Horizontal edge, skip to avoid double counting
                        continue
                    if y < min(y_a, y_b) or y > max(y_a, y_b):
                        continue
                    # Compute intersection x
                    # Avoid division by zero
                    dx = x_b - x_a
                    dy = y_b - y_a
                    if dy == 0:
                        continue
                    x = x_a + (dx * (y - y_a)) / dy
                    intersections.append(x)
                if len(intersections) < 2:
                    continue
                x_left = min(intersections)
                x_right = max(intersections)
                # Get circle x limits for this y
                cx_min, cx_max = circle_x_limits[y]
                # Overlap x range
                overlap_min = max(x_left, cx_min)
                overlap_max = min(x_right, cx_max)
                # Ceil and floor to get integer x's
                ceil_min = math.ceil(overlap_min)
                floor_max = math.floor(overlap_max)
                if ceil_min > floor_max:
                    continue
                count = floor_max - ceil_min + 1
                total_heat = (total_heat + count) % MOD
        print(f"Case #{test_case}: {total_heat}")

threading.Thread(target=main,).start()