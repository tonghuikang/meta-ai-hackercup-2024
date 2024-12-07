import sys
import math

def readints():
    return list(map(int, sys.stdin.read().split()))

def rotate_polygon(polygon, theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    rotated = []
    for x, y in polygon:
        x_new = x * cos_theta - y * sin_theta
        y_new = x * sin_theta + y * cos_theta
        rotated.append((x_new, y_new))
    return rotated

def translate_polygon(polygon, shift_x, shift_y=0):
    translated = []
    for x, y in polygon:
        translated.append((x + shift_x, y + shift_y))
    return translated

def point_in_convex_polygon(x, y, polygon):
    n = len(polygon)
    prev = None
    for i in range(n):
        x0, y0 = polygon[i]
        x1, y1 = polygon[(i+1)%n]
        cross = (x1 - x0)*(y - y0) - (y1 - y0)*(x - x0)
        if cross == 0:
            continue
        sign = 1 if cross > 0 else -1
        if prev is None:
            prev = sign
        else:
            if sign != prev:
                return False
    return True if prev is not None else False

def polygon_has_point_inside_cup(polygon, W, D):
    for x, y in polygon:
        if 0 < x < W and 0 < y < D:
            return True
    # Additionally, check if any edge crosses the interior
    # For simplicity, not implemented
    return False

def sauce_cup_boundary_points(W, D, samples=10):
    points = []
    # Bottom edge: x from 0 to W, y=0
    for i in range(samples +1):
        x = W * i / samples
        y = 0.0
        points.append((x, y))
    # Right edge: x=W, y from 0 to D
    for i in range(1, samples +1):
        x = W
        y = D * i / samples
        points.append((x, y))
    # Top edge: x from W to 0, y=D
    for i in range(1, samples +1):
        x = W - W * i / samples
        y = D
        points.append((x, y))
    # Left edge: x=0, y from D to 0
    for i in range(1, samples):
        x = 0.0
        y = D - D * i / samples
        points.append((x, y))
    return points

def check_no_sauce_cup_points_inside(polygon, W, D):
    boundary_points = sauce_cup_boundary_points(W, D, samples=20)
    for x, y in boundary_points:
        if point_in_convex_polygon(x, y, polygon):
            return False
    return True

def solve():
    data = readints()
    idx = 0
    T = data[idx]; idx +=1
    for test in range(1, T+1):
        N, W, D = data[idx], data[idx+1], data[idx+2]; idx +=3
        polygon = []
        for _ in range(N):
            x, y = data[idx], data[idx+1]; idx +=2
            polygon.append((x, y))
        possible = False
        for i in range(N):
            x_i, y_i = polygon[i]
            # Compute rotation angle to make y_i' =0
            if x_i ==0 and y_i ==0:
                theta =0.0
            elif x_i ==0:
                theta = -math.pi /2 if y_i >0 else math.pi /2
            else:
                theta = math.atan2(-y_i, x_i)
            rotated = rotate_polygon(polygon, theta)
            x_i_rot, y_i_rot = rotated[i]
            # y_i_rot should be approximately 0
            # Now, shift_x so that x_i_rot + shift_x ∈ [0, W]
            shift_x_min = -x_i_rot
            shift_x_max = W - x_i_rot
            # Try shifting to place vertex at 0, W, and W/2
            shifts = [shift_x_min, shift_x_max, (shift_x_min + shift_x_max)/2]
            for shift_x in shifts:
                shifted = translate_polygon(rotated, shift_x, shift_y=0.0)
                # Check all y >=0
                all_y_non_negative = all(y >= -1e-8 for x,y in shifted)
                if not all_y_non_negative:
                    continue
                # Check some point of polygon inside sauce cup
                has_point_inside_cup = polygon_has_point_inside_cup(shifted, W, D)
                if not has_point_inside_cup:
                    continue
                # Check no sauce cup boundary point inside polygon
                no_cup_point_inside = check_no_sauce_cup_points_inside(shifted, W, D)
                if not no_cup_point_inside:
                    continue
                # All conditions satisfied
                possible = True
                break
            if possible:
                break
        print(f"Case #{test}: {'Yes' if possible else 'No'}")

if __name__ == "__main__":
    solve()