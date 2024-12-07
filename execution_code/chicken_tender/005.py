import sys
import math

sys.setrecursionlimit(1000000)

def readints():
    return map(int, sys.stdin.readline().split())

def rotate_polygon(polygon, angle):
    # Rotate the polygon by angle degrees
    theta = math.radians(angle)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    rotated = []
    for (x, y) in polygon:
        x_new = x * cos_theta - y * sin_theta
        y_new = x * sin_theta + y * cos_theta
        rotated.append((x_new, y_new))
    return rotated

def point_in_convex_polygon(point, polygon):
    # Check if point is inside convex polygon
    x, y = point
    n = len(polygon)
    prev_side = None
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1)%n]
        dx = x2 - x1
        dy = y2 - y1
        dxp = x - x1
        dyp = y - y1
        cross = dx * dyp - dy * dxp
        side = 0
        if cross > 1e-8:
            side = 1
        elif cross < -1e-8:
            side = -1
        if side != 0:
            if prev_side is None:
                prev_side = side
            elif prev_side != side:
                return False
    return True

def check_intersection(polygon, seg):
    # Check if segment seg intersects with polygon (excluding touching at endpoints)
    x1, y1 = seg[0]
    x2, y2 = seg[1]
    for i in range(len(polygon)):
        x3, y3 = polygon[i]
        x4, y4 = polygon[(i+1)%len(polygon)]
        denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
        if abs(denom) < 1e-8:
            continue
        t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) / denom
        u = ((x1 - x3)*(y1 - y2) - (y1 - y3)*(x1 - x2)) / denom
        if 1e-8 < t < 1 - 1e-8 and 1e-8 < u < 1 - 1e-8:
            return True
    return False

def solve_case(case_num, N, W, D, polygon):
    possible = False
    for angle in range(0, 360, 3):
        rotated = rotate_polygon(polygon, angle)
        y_low = min(y for (x, y) in rotated)
        x_low_points = [(x, y) for (x, y) in rotated if abs(y - y_low) < 1e-8]
        y_high = max(y for (x, y) in rotated)
        for x_low, y_low in x_low_points:
            x_shifts = []
            x_min = 0 - x_low
            x_max = W - x_low
            if x_min > x_max:
                continue
            # Sample shifts across the possible range
            num_samples = 10
            for k in range(num_samples + 1):
                x_shift = x_min + k * (x_max - x_min) / num_samples
                shifted = [ (x + x_shift, y - y_low) for (x, y) in rotated ]
                x_btm = x_low + x_shift
                if x_btm < -1e-8 or x_btm > W + 1e-8:
                    continue
                # Check all vertices are above y=0
                if any(y < -1e-8 for (x, y) in shifted):
                    continue
                # Check some point of polygon is within cup
                point_inside_cup = False
                for (x, y) in shifted:
                    if 0 + 1e-8 < x < W - 1e-8 and 0 + 1e-8 < y < D - 1e-8:
                        point_inside_cup = True
                        break
                if not point_inside_cup:
                    continue
                # Check the cup sides are not inside the polygon
                cup_sides = [ ((0, 0), (0, D)), ((0, 0), (W, 0)), ((W, 0), (W, D)) ]
                cup_points = [ (0, D/2), (W, D/2), (W/2, 0) ]
                contains_cup_side = False
                for seg in cup_sides:
                    if check_intersection(shifted, seg):
                        contains_cup_side = True
                        break
                    # Check midpoint of side
                    mx = (seg[0][0] + seg[1][0]) / 2
                    my = (seg[0][1] + seg[1][1]) / 2
                    if point_in_convex_polygon( (mx, my), shifted ):
                        contains_cup_side = True
                        break
                if contains_cup_side:
                    continue
                possible = True
                break
            if possible:
                break
        if possible:
            break
    result = 'Yes' if possible else 'No'
    print(f'Case #{case_num}: {result}')

def main():
    T = int(sys.stdin.readline())
    for case_num in range(1, T+1):
        N, W, D = map(int, sys.stdin.readline().split())
        polygon = []
        for _ in range(N):
            x_i, y_i = map(float, sys.stdin.readline().split())
            polygon.append( (x_i, y_i) )
        solve_case(case_num, N, W, D, polygon)

if __name__ == '__main__':
    main()