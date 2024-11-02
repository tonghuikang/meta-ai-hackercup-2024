from sys import stdin
import threading

def main():
    import sys
    import math
    import threading
    sys.setrecursionlimit(1 << 25)
    T = int(stdin.readline())
    for test_case in range(1, T + 1):
        N, K = map(int, stdin.readline().split())
        grid = []
        for _ in range(N):
            grid.append(stdin.readline().strip())
        N_cols = len(grid[0])

        h = [0] * N_cols
        q = [0] * N_cols
        max_area = 0

        for i in range(N):
            stack = []
            for j in range(N_cols):
                if grid[i][j] == '0':
                    h[j] = 0
                    q[j] = 0
                else:
                    h[j] += 1
                    if grid[i][j] == '?':
                        q[j] += 1
                    else:
                        q[j] += 0  # '1'

            cumulative_q = 0
            j = 0
            stack = []
            while j < N_cols:
                if not stack or h[j] >= stack[-1][1]:
                    # Push current bar onto stack
                    cumulative_q = q[j]
                    pos = j
                    stack.append([pos, h[j], cumulative_q])
                    j += 1
                else:
                    # Pop the stack
                    last = stack.pop()
                    pos = last[0]
                    height = last[1]
                    cum_q = last[2]
                    # Determine width
                    width = j - pos
                    # Compute cumulative '?' count
                    # cum_q already includes cumulative '?'s in the rectangle
                    if cum_q <= K:
                        area = height * width
                        max_area = max(max_area, area)
                    # Update cumulative_q for next rectangle
                    if stack:
                        stack[-1][2] += cum_q
            while stack:
                last = stack.pop()
                pos = last[0]
                height = last[1]
                cum_q = last[2]
                width = N_cols - pos
                if cum_q <= K:
                    area = height * width
                    max_area = max(max_area, area)
                if stack:
                    stack[-1][2] += cum_q
        print(f'Case #{test_case}: {max_area}')

threading.Thread(target=main).start()