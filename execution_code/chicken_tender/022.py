import math
import sys

def rotate_polygon(polygon, theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    return [ (x * cos_theta - y * sin_theta,
              x * sin_theta + y * cos_theta) for (x, y) in polygon ]

def translate_polygon(polygon, dx, dy):
    return [ (x + dx, y + dy) for (x, y) in polygon ]

def point_in_polygon(x, y, polygon):
    inside = False
    n = len(polygon)
    for i in range(n):
        j = (i +1) %n
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        if ((yi > y) != (yj > y)):
            if yj - yi == 0:
                continue
            intersect_x = (xj - xi) * (y - yi) / (yj - yi) + xi
            if x < intersect_x:
                inside = not inside
    return inside

def generate_boundary_samples(W, D, num_samples=10):
    sampled_points = []
    for i in range(num_samples +1):
        t = i / num_samples
        # Bottom edge (0,0) to (W,0)
        sampled_points.append( (t * W, 0.0) )
        # Top edge (0,D) to (W,D)
        sampled_points.append( (t * W, D) )
        # Left edge (0,0) to (0,D)
        sampled_points.append( (0.0, t * D) )
        # Right edge (W,0) to (W,D)
        sampled_points.append( (W, t * D) )
    return sampled_points

def readints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        N, W, D = map(int, line.strip().split())
        polygon = []
        for _ in range(N):
            xi, yi = map(int, sys.stdin.readline().split())
            polygon.append( (xi, yi) )
        possible = False
        for i in range(N):
            xi, yi = polygon[i]
            if xi ==0 and yi ==0:
                theta =0.0
            else:
                theta = math.atan2(-yi, xi)
            rotated = rotate_polygon(polygon, theta)
            x_rot = rotated[i][0]
            y_rot = rotated[i][1]
            # Now y_rot should be approximately 0
            # Try placing the vertex at x=0
            shift_x0 = 0.0 - x_rot
            translated0 = translate_polygon(rotated, shift_x0, 0.0)
            # Check condition a
            all_y_non_negative = all( y >= -1e-8 for (x, y) in translated0 )
            if not all_y_non_negative:
                pass
            else:
                # Check condition b: vertex i is at x=0
                xi_new, yi_new = translated0[i]
                if 0 <= xi_new +1e-8 <= W:
                    # Check condition c: some point inside cup is inside polygon
                    center_x = W /2.0
                    center_y = D /2.0
                    inside_c = point_in_polygon(center_x, center_y, translated0)
                    if not inside_c:
                        pass
                    else:
                        # Check condition d: no boundary points inside polygon
                        boundary_samples = generate_boundary_samples(W, D, num_samples=10)
                        boundary_inside = False
                        for (bx, by) in boundary_samples:
                            if point_in_polygon(bx, by, translated0):
                                boundary_inside = True
                                break
                        if not boundary_inside:
                            possible = True
                            break
            if possible:
                break
            # Try placing the vertex at x=W
            shift_xW = W - x_rot
            translatedW = translate_polygon(rotated, shift_xW, 0.0)
            # Check condition a
            all_y_non_negative = all( y >= -1e-8 for (x, y) in translatedW )
            if not all_y_non_negative:
                pass
            else:
                # Check condition b: vertex i is at x=W
                xi_new, yi_new = translatedW[i]
                if 0 <= xi_new +1e-8 <= W:
                    # Check condition c: some point inside cup is inside polygon
                    center_x = W /2.0
                    center_y = D /2.0
                    inside_c = point_in_polygon(center_x, center_y, translatedW)
                    if not inside_c:
                        pass
                    else:
                        # Check condition d: no boundary points inside polygon
                        boundary_samples = generate_boundary_samples(W, D, num_samples=10)
                        boundary_inside = False
                        for (bx, by) in boundary_samples:
                            if point_in_polygon(bx, by, translatedW):
                                boundary_inside = True
                                break
                        if not boundary_inside:
                            possible = True
                            break
            if possible:
                break
        if possible:
            print(f"Case #{test_case}: Yes")
            continue
        # Additionally, try translating the vertex to other positions within [0, W]
        # To cover more possible placements, sample shift_x
        for i in range(N):
            xi, yi = polygon[i]
            theta = math.atan2(-yi, xi)
            rotated = rotate_polygon(polygon, theta)
            x_rot = rotated[i][0]
            y_rot = rotated[i][1]
            if y_rot < -1e-6:
                continue
            # Now, shift_x such that the vertex is placed somewhere in [0, W]
            # Sample shift_x in [ -x_rot, W - x_rot ] with some step
            shift_x_min = 0.0 - x_rot
            shift_x_max = W - x_rot
            steps = 20
            for s in range(steps +1):
                t = s / steps
                shift_x = shift_x_min + t * (shift_x_max - shift_x_min)
                translated = translate_polygon(rotated, shift_x, 0.0)
                # Check condition a
                all_y_non_negative = all( y >= -1e-8 for (x, y) in translated )
                if not all_y_non_negative:
                    continue
                # Check condition b: vertex i is at x_shifted
                xi_new, yi_new = translated[i]
                if not ( -1e-8 <= xi_new <= W +1e-8 ):
                    continue
                # Check condition c: some point inside cup is inside polygon
                center_x = W /2.0
                center_y = D /2.0
                inside_c = point_in_polygon(center_x, center_y, translated)
                if not inside_c:
                    continue
                # Check condition d: no boundary points inside polygon
                boundary_samples = generate_boundary_samples(W, D, num_samples=10)
                boundary_inside = False
                for (bx, by) in boundary_samples:
                    if point_in_polygon(bx, by, translated):
                        boundary_inside = True
                        break
                if not boundary_inside:
                    possible = True
                    break
            if possible:
                break
        if possible:
            print(f"Case #{test_case}: Yes")
        else:
            print(f"Case #{test_case}: No")

if __name__ == "__main__":
    main()