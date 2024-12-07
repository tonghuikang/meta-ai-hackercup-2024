import sys
import math

MOD = 10**9 + 7

def input():
    return sys.stdin.read()

def is_point_in_circle(x, y, R_sq):
    return x*x + y*y <= R_sq

def area_sign(x1, y1, x2, y2, x3, y3):
    return (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

def point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    # Barycentric Technique
    det = area_sign(x1, y1, x2, y2, x3, y3)
    a = area_sign(px, py, x2, y2, x3, y3)
    b = area_sign(x1, y1, px, py, x3, y3)
    c = area_sign(x1, y1, x2, y2, px, py)
    if det == 0:
        return False
    if det < 0:
        return a <=0 and b <=0 and c <=0
    else:
        return a >=0 and b >=0 and c >=0

def pick_theorem(x1, y1, x2, y2, x3, y3):
    # Calculate area using shoelace formula
    area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))/2
    # Calculate boundary points
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    b1 = gcd(abs(x2 - x1), abs(y2 - y1))
    b2 = gcd(abs(x3 - x2), abs(y3 - y2))
    b3 = gcd(abs(x1 - x3), abs(y1 - y3))
    B = b1 + b2 + b3
    # Pick's theorem: A = I + B/2 -1 => I = A - B/2 + 1
    I = int(area - B/2 +1)
    return I

def count_lattice_points_in_triangle(x1, y1, x2, y2, x3, y3, R_sq):
    # Bounding box of the triangle and the circle
    min_x = max(min(x1, x2, x3, -math.isqrt(R_sq)), -math.isqrt(R_sq))
    max_x = min(max(x1, x2, x3, math.isqrt(R_sq)), math.isqrt(R_sq))
    count = 0
    for x in range(min_x, max_x +1):
        # For each x, find the y range within the triangle
        # Find all edges that intersect with this x
        ys = []
        edges = [(x1, y1, x2, y2), (x2, y2, x3, y3), (x3, y3, x1, y1)]
        for ex1, ey1, ex2, ey2 in edges:
            if ex1 == ex2:
                continue
            if (x < min(ex1, ex2)) or (x > max(ex1, ex2)):
                continue
            # Compute y at this x
            t = (x - ex1) / (ex2 - ex1)
            y = ey1 + t * (ey2 - ey1)
            ys.append(y)
        if len(ys) <2:
            continue
        y_min, y_max = math.floor(min(ys)), math.ceil(max(ys))
        # Now, intersect with circle y range
        y_circle_max = math.isqrt(R_sq - x*x) if x*x <= R_sq else -1
        y_circle_min = -y_circle_max
        y_final_min = max(y_min, y_circle_min)
        y_final_max = min(y_max, y_circle_max)
        if y_final_min > y_final_max:
            continue
        count += y_final_max - y_final_min +1
    return count

def main():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); R = int(data[idx+1]); idx +=2
        R_sq = R*R
        total = 0
        for _ in range(N):
            XA = int(data[idx]); YA = int(data[idx+1])
            XB = int(data[idx+2]); YB = int(data[idx+3])
            XC = int(data[idx+4]); YC = int(data[idx+5]); idx +=6
            # Check if all vertices are inside or on the circle
            inside_A = XA*XA + YA*YA <= R_sq
            inside_B = XB*XB + YB*YB <= R_sq
            inside_C = XC*XC + YC*YC <= R_sq
            if inside_A and inside_B and inside_C:
                # Fully inside the circle
                count = pick_theorem(XA, YA, XB, YB, XC, YC)
                total = (total + count) % MOD
            else:
                # Partially inside the circle
                # For simplicity, iterate over bounding box
                # WARNING: This is not efficient for large inputs
                count = 0
                min_x = max(min(XA, XB, XC, -R), -R)
                max_x = min(max(XA, XB, XC, R), R)
                for x in range(min_x, max_x +1):
                    # For each x, find y range within the triangle
                    ys = []
                    edges = [(XA, YA, XB, YB), (XB, YB, XC, YC), (XC, YC, XA, YA)]
                    for ex1, ey1, ex2, ey2 in edges:
                        if ex1 == ex2:
                            if x == ex1:
                                ys.extend([ey1, ey2])
                            continue
                        if (x < min(ex1, ex2)) or (x > max(ex1, ex2)):
                            continue
                        t = (x - ex1) / (ex2 - ex1)
                        y = ey1 + t * (ey2 - ey1)
                        ys.append(y)
                    if len(ys) <2:
                        continue
                    y_min, y_max = math.floor(min(ys)), math.ceil(max(ys))
                    # Now, intersect with circle y range
                    if x*x > R_sq:
                        continue
                    y_circle_max = math.isqrt(R_sq - x*x)
                    y_circle_min = -y_circle_max
                    y_final_min = max(y_min, y_circle_min)
                    y_final_max = min(y_max, y_circle_max)
                    if y_final_min > y_final_max:
                        continue
                    count += y_final_max - y_final_min +1
                total = (total + count) % MOD
        print(f"Case #{test_case}: {total}")

if __name__ == "__main__":
    main()