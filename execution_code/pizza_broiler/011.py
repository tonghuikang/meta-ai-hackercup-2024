import sys
import math

MOD = 10**9 + 7

def readints():
    return list(map(int, sys.stdin.readline().split()))

def count_lattice_points_in_triangle_and_circle(xa, ya, xb, yb, xc, yc, R_sq):
    # Find the bounding box of the triangle
    min_y = math.ceil(min(ya, yb, yc))
    max_y = math.floor(max(ya, yb, yc))
    count = 0

    # To handle edge cases, collect all edges
    edges = []
    points = [(xa, ya), (xb, yb), (xc, yc)]
    for i in range(3):
        p1 = points[i]
        p2 = points[(i+1)%3]
        if p1[1] == p2[1]:
            continue  # horizontal edges will be handled in fill step
        if p1[1] < p2[1]:
            edges.append(p1 + p2)
        else:
            edges.append(p2 + p1)

    # For each scanline y
    for y in range(int(math.ceil(min(ya, yb, yc))), int(math.floor(max(ya, yb, yc))) + 1):
        # Find intersections with triangle edges
        x_intersections = []
        for edge in edges:
            x1, y1, x2, y2 = edge
            if y1 <= y < y2:
                # Compute intersection x
                dy = y2 - y1
                dx = x2 - x1
                if dy == 0:
                    continue  # parallel to scanline
                t = (y - y1) / dy
                x = x1 + t * dx
                x_intersections.append(x)
        if len(x_intersections) < 2:
            continue
        x_intersections.sort()
        x_start = math.ceil(x_intersections[0])
        x_end = math.floor(x_intersections[1])
        if x_start > x_end:
            continue
        # Now, intersect with circle
        y_sq = y * y
        if y_sq > R_sq:
            continue
        dx = math.isqrt(R_sq - y_sq) if R_sq - y_sq >=0 else 0
        circle_left = -dx
        circle_right = dx
        # Compute overlap
        final_left = max(x_start, math.ceil(circle_left))
        final_right = min(x_end, math.floor(circle_right))
        if final_left > final_right:
            continue
        count += final_right - final_left + 1
    return count

def main():
    import sys
    import threading

    def run():
        T = int(sys.stdin.readline())
        for tc in range(1, T+1):
            N, R = map(int, sys.stdin.readline().split())
            R_sq = R * R
            total = 0
            for _ in range(N):
                xa, ya, xb, yb, xc, yc = map(int, sys.stdin.readline().split())
                cnt = count_lattice_points_in_triangle_and_circle(xa, ya, xb, yb, xc, yc, R_sq)
                total = (total + cnt) % MOD
            print(f"Case #{tc}: {total}")
    threading.Thread(target=run).start()