import sys
import math
import threading
from math import gcd, sqrt, floor, ceil

MOD = 10**9 + 7

def main():
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx += 1
    for test_case in range(1, T+1):
        N, R = int(data[idx]), int(data[idx+1]); idx +=2
        triangles = []
        for _ in range(N):
            Xa, Ya, Xb, Yb, Xc, Yc = map(int, data[idx:idx+6]); idx +=6
            triangles.append(((Xa, Ya), (Xb, Yb), (Xc, Yc)))
        total = 0
        R_sq = R * R
        for triangle in triangles:
            A, B, C = triangle
            # Check if all vertices are inside or on the circle
            in_A = A[0]**2 + A[1]**2 <= R_sq
            in_B = B[0]**2 + B[1]**2 <= R_sq
            in_C = C[0]**2 + C[1]**2 <= R_sq
            if in_A and in_B and in_C:
                # Use Pick's Theorem
                # Compute area
                area2 = abs( (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0]) )
                A_pick = area2 / 2
                # Compute boundary points
                def edge_boundary(p1, p2):
                    dx = abs(p2[0] - p1[0])
                    dy = abs(p2[1] - p1[1])
                    return gcd(dx, dy)
                B_count = edge_boundary(A, B) + edge_boundary(B, C) + edge_boundary(C, A)
                # Number of interior points
                I = A_pick - B_count / 2 + 1
                # Total points
                total_points = int(I + B_count)
                total = (total + total_points) % MOD
            else:
                # Partial intersection: Enumerate points within triangle and circle
                # Find bounding box of triangle and circle
                min_x = max(ceil(min(A[0], B[0], C[0], -R)), -R)
                max_x = min(floor(max(A[0], B[0], C[0], R)), R)
                # Similarly for y
                min_y = max(ceil(min(A[1], B[1], C[1], -R)), -R)
                max_y = min(floor(max(A[1], B[1], C[1], R)), R)
                # Function to check if point is inside triangle using barycentric coordinates
                def point_in_triangle(px, py, A, B, C):
                    # Compute vectors
                    v0x = C[0] - A[0]
                    v0y = C[1] - A[1]
                    v1x = B[0] - A[0]
                    v1y = B[1] - A[1]
                    v2x = px - A[0]
                    v2y = py - A[1]
                    # Compute dot products
                    dot00 = v0x * v0x + v0y * v0y
                    dot01 = v0x * v1x + v0y * v1y
                    dot02 = v0x * v2x + v0y * v2y
                    dot11 = v1x * v1x + v1y * v1y
                    dot12 = v1x * v2x + v1y * v2y
                    # Compute barycentric coordinates
                    denom = dot00 * dot11 - dot01 * dot01
                    if denom == 0:
                        return False
                    inv_denom = 1 / denom
                    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
                    v = (dot00 * dot12 - dot01 * dot02) * inv_denom
                    return (u >= 0) and (v >= 0) and (u + v <= 1)
                count = 0
                for x in range(min_x, max_x +1):
                    x_sq = x * x
                    y_limit_sq = R_sq - x_sq
                    if y_limit_sq < 0:
                        continue
                    y_limit = floor(sqrt(y_limit_sq))
                    y_min = max(min_y, -y_limit)
                    y_max = min(max_y, y_limit)
                    for y in range(y_min, y_max +1):
                        if point_in_triangle(x, y, A, B, C):
                            count +=1
                total = (total + count) % MOD
        print(f"Case #{test_case}: {total}")

threading.Thread(target=main).start()