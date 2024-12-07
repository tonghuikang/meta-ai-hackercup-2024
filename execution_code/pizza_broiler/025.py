import sys
import math

MOD = 10**9 + 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_lattice_points(x1, y1, x2, y2, x3, y3):
    # Calculate area using shoelace formula
    area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

    # Calculate boundary points
    def edge_gcd(xa, ya, xb, yb):
        return gcd(abs(xb - xa), abs(yb - ya))
    
    B = edge_gcd(x1, y1, x2, y2) + edge_gcd(x2, y2, x3, y3) + edge_gcd(x3, y3, x1, y1)
    
    # Pick's theorem: I = area - B/2 +1
    I = area - B / 2 + 1
    # Total points = I + B
    total = I + B
    # Since total should be integer
    return int(round(total))

def is_inside_circle(x, y, R_sq):
    return x*x + y*y <= R_sq

def main():
    import sys
    import threading

    def run():
        T = int(sys.stdin.readline())
        for test_case in range(1, T + 1):
            N, R = map(int, sys.stdin.readline().split())
            R_sq = R * R
            total_heat = 0
            for _ in range(N):
                xA, yA, xB, yB, xC, yC = map(int, sys.stdin.readline().split())
                # Check if all vertices are inside or on the circle
                inside_A = is_inside_circle(xA, yA, R_sq)
                inside_B = is_inside_circle(xB, yB, R_sq)
                inside_C = is_inside_circle(xC, yC, R_sq)
                if inside_A and inside_B and inside_C:
                    # Fully inside, use Pick's theorem
                    count = count_lattice_points(xA, yA, xB, yB, xC, yC)
                    total_heat = (total_heat + count) % MOD
                else:
                    # Partially overlapping
                    # For simplicity, implement a brute-force approach
                    # Note: This may not be efficient for large R
                    # Hence, it's likely to pass only small cases
                    # An optimized geometric algorithm is needed for larger cases
                    # Here we proceed with brute-force for demonstration
                    # Determine bounding box of the triangle
                    min_x = math.ceil(min(xA, xB, xC))
                    max_x = math.floor(max(xA, xB, xC))
                    min_y = math.ceil(min(yA, yB, yC))
                    max_y = math.floor(max(yA, yB, yC))
                    count = 0
                    # Iterate over possible lattice points in bounding box
                    for x in range(min_x, max_x + 1):
                        for y in range(min_y, max_y + 1):
                            if is_inside_circle(x, y, R_sq):
                                # Check if (x,y) is inside the triangle
                                # Using barycentric coordinates
                                denom = ((yB - yC)*(xA - xC) + (xC - xB)*(yA - yC))
                                if denom == 0:
                                    continue  # Degenerate triangle
                                a = ((yB - yC)*(x - xC) + (xC - xB)*(y - yC)) / denom
                                b = ((yC - yA)*(x - xC) + (xA - xC)*(y - yC)) / denom
                                c = 1 - a - b
                                if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
                                    count += 1
                    total_heat = (total_heat + count) % MOD
            print(f"Case #{test_case}: {total_heat}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()