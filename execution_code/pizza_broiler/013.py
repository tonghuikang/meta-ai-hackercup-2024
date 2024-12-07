import sys
import math
import threading

MOD = 10**9 + 7

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N, R = map(int, sys.stdin.readline().split())
        R_sq = R * R
        total = 0
        for _ in range(N):
            Xa, Ya, Xb, Yb, Xc, Yc = map(int, sys.stdin.readline().split())
            # Compute bounding box of the triangle and the circle
            min_x = max(min(Xa, Xb, Xc, -R), -R)
            max_x = min(max(Xa, Xb, Xc, R), R)
            min_y = max(min(Ya, Yb, Yc, -R), -R)
            max_y = min(max(Ya, Yb, Yc, R), R)
            count = 0
            # Iterate over all lattice points in the bounding box
            for y in range(min_y, max_y + 1):
                # For a given y, find the intersection with circle
                dy_sq = y * y
                if dy_sq > R_sq:
                    continue
                dx_limit = int(math.sqrt(R_sq - dy_sq))
                x_min_circle = -dx_limit
                x_max_circle = dx_limit
                # Clip the x range to the bounding box
                x_start = max(min_x, x_min_circle)
                x_end = min(max_x, x_max_circle)
                for x in range(x_start, x_end + 1):
                    # Check if (x, y) is inside the triangle
                    # Using barycentric coordinates
                    denom = (Yb - Yc)*(Xa - Xc) + (Xc - Xb)*(Ya - Yc)
                    if denom == 0:
                        continue
                    a = ((Yb - Yc)*(x - Xc) + (Xc - Xb)*(y - Yc)) / denom
                    b = ((Yc - Ya)*(x - Xc) + (Xa - Xc)*(y - Yc)) / denom
                    c = 1 - a - b
                    if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
                        count += 1
            total = (total + count) % MOD
        print(f"Case #{test_case}: {total}")

threading.Thread(target=main).start()