import sys
import threading
import math

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 1_000_000_007
    for case_num in range(1, T + 1):
        N, R = map(int, sys.stdin.readline().split())
        R_squared = R * R
        triangles = []
        for _ in range(N):
            xA, yA, xB, yB, xC, yC = map(int, sys.stdin.readline().split())
            triangles.append(((xA, yA), (xB, yB), (xC, yC)))

        total_count = 0

        for triangle in triangles:
            (x0, y0), (x1, y1), (x2, y2) = triangle

            xs = [x0, x1, x2]
            ys = [y0, y1, y2]
            min_x = min(xs)
            max_x = max(xs)

            min_x_int = int(math.floor(min(xs)))
            max_x_int = int(math.ceil(max(xs)))

            edges = []
            points = [(x0, y0), (x1, y1), (x2, y2)]
            for i in range(3):
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % 3]
                if x1 == x2:
                    x_min = x1
                    x_max = x1
                else:
                    x_min = min(x1, x2)
                    x_max = max(x1, x2)
                edges.append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2,
                              'x_min': x_min, 'x_max': x_max})

            for x in range(min_x_int, max_x_int + 1):
                y_list = []
                for edge in edges:
                    x1 = edge['x1']
                    x2 = edge['x2']
                    y1 = edge['y1']
                    y2 = edge['y2']
                    x_min = edge['x_min']
                    x_max = edge['x_max']
                    if x1 == x2:
                        if x == x1:
                            y_list.append(y1)
                            y_list.append(y2)
                    else:
                        if x_min <= x <= x_max:
                            t = (x - x1) / (x2 - x1)
                            y = y1 + t * (y2 - y1)
                            y_list.append(y)
                if len(y_list) < 2:
                    continue  # No intersection at this x
                y_list = list(set(y_list))  # Remove duplicates
                y_list.sort()
                # Since it's a triangle, y_list should have pairs
                for i in range(0, len(y_list) - 1, 2):
                    y_lower = y_list[i]
                    y_upper = y_list[i + 1]
                    y_start = int(math.ceil(min(y_lower, y_upper)))
                    y_end = int(math.floor(max(y_lower, y_upper)))
                    for y in range(y_start, y_end + 1):
                        if x * x + y * y <= R_squared:
                            total_count += 1
                            if total_count >= MOD:
                                total_count -= MOD
        print(f"Case #{case_num}: {total_count % MOD}")

threading.Thread(target=main).start()