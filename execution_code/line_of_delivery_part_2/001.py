import sys
import threading

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N_str, G_str = sys.stdin.readline().split()
        N = int(N_str)
        G = int(G_str)
        E = [int(sys.stdin.readline()) for _ in range(N)]
        positions = [0] * N
        stack = []
        for i in range(N - 1, -1, -1):
            E_i = E[i]
            while stack and E_i >= stack[-1] - 1:
                stack.pop()
            if not stack:
                pos = E_i
            else:
                pos = min(E_i, stack[-1] - 1)
            positions[i] = pos
            stack.append(pos)
        min_distance = float('inf')
        min_index = -1
        for i in range(N):
            distance = abs(G - positions[i])
            if distance < min_distance or (distance == min_distance and i + 1 < min_index):
                min_distance = distance
                min_index = i + 1  # Convert to 1-based index
        print(f"Case #{test_case}: {min_index} {min_distance}")

if __name__ == "__main__":
    threading.Thread(target=main).start()