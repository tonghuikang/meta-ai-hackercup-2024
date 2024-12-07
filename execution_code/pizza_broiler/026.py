import sys
import math

MOD = 10**9 + 7

def readints():
    import sys
    return list(map(int, sys.stdin.read().split()))

def point_in_circle(x, y, R):
    return x*x + y*y <= R*R

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

def point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    # Barycentric Technique
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(px, py, x2, y2, x3, y3)
    A2 = area(x1, y1, px, py, x3, y3)
    A3 = area(x1, y1, x2, y2, px, py)
    return math.isclose(A, A1 + A2 + A3) or (A1 + A2 + A3) < A + 1e-9

def main():
    data = readints()
    idx = 0
    T = data[idx]
    idx += 1
    for test_case in range(1, T+1):
        N, R = data[idx], data[idx+1]
        idx += 2
        triangles = []
        for _ in range(N):
            Xa, Ya, Xb, Yb, Xc, Yc = data[idx:idx+6]
            triangles.append((Xa, Ya, Xb, Yb, Xc, Yc))
            idx += 6
        # Precompute all lattice points within the circle
        lattice_points = []
        for x in range(-R, R+1):
            y_max = int(math.floor(math.sqrt(R*R - x*x)))
            for y in range(-y_max, y_max+1):
                lattice_points.append((x, y))
        total = 0
        for tri in triangles:
            Xa, Ya, Xb, Yb, Xc, Yc = tri
            count = 0
            for (x, y) in lattice_points:
                if point_in_triangle(x, y, Xa, Ya, Xb, Yb, Xc, Yc):
                    count += 1
            total = (total + count) % MOD
        print(f"Case #{test_case}: {total}")

if __name__ == "__main__":
    main()