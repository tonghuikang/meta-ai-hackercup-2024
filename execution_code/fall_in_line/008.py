import sys
import random
import math
from collections import defaultdict

def readints():
    return list(map(int, sys.stdin.readline().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    A = y2 - y1
    B = x1 - x2
    C = A * x1 + B * y1
    # Normalize
    g = gcd(abs(A), abs(B))
    g = gcd(g, abs(C)) if C != 0 else g
    A //= g
    B //= g
    C //= g
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return (A, B, C)

def main():
    import sys
    import time
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N = int(sys.stdin.readline())
        points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
        if N <= 2:
            print(f"Case #{test_case}: 0")
            continue
        max_on_line = 0
        # Number of random samples
        samples = 30
        for _ in range(samples):
            p1, p2 = random.sample(points, 2)
            A = p2[1] - p1[1]
            B = p1[0] - p2[0]
            C = A * p1[0] + B * p1[1]
            # Normalize
            g = gcd(abs(A), abs(B))
            g = gcd(g, abs(C)) if C != 0 else g
            A //= g
            B //= g
            C //= g
            if A < 0 or (A == 0 and B < 0):
                A, B, C = -A, -B, -C
            count = 0
            for x, y in points:
                if A * x + B * y == C:
                    count +=1
            if count > max_on_line:
                max_on_line = count
                if max_on_line > N - max_on_line:
                    break
        M = N - max_on_line
        print(f"Case #{test_case}: {M}")

if __name__ == "__main__":
    main()