import sys
import math
import sys
import sys
from collections import deque

MOD = 10**9 + 7

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for tc in range(1, T + 1):
        N,M = map(int, sys.stdin.readline().split())
        moves = []
        for _ in range(M):
            D,X = sys.stdin.readline().split()
            X = int(X)
            moves.append( (D, X) )
        # Initialize direction: 0-east, 1-south,2-west,3-north
        dir = 0
        # Direction vectors
        dirs = [ (1,0), (0,-1), (-1,0), (0,1) ]
        # Head position
        hx, hy = 0,0
        # Tail movement queue: store (direction, length)
        tail_queue = deque()
        tail_x, tail_y = 0,0
        tail_remaining = N
        # Current min and max
        min_x = max_x = hx
        min_y = max_y = hy
        sum_f = 0
        for D,X in moves:
            # Update direction
            if D == 'L':
                dir = (dir + 3) % 4
            elif D == 'R':
                dir = (dir + 1) % 4
            # else 'S', no change
            # Move head
            dx, dy = dirs[dir]
            hx_new = hx + dx * X
            hy_new = hy + dy * X
            # Add to tail queue
            tail_queue.append( (dir, X) )
            # Update head position
            hx, hy = hx_new, hy_new
            # Update min and max
            min_x = min(min_x, hx)
            max_x = max(max_x, hx)
            min_y = min(min_y, hy)
            max_y = max(max_y, hy)
            # Update tail
            tail_steps = X
            while tail_steps > 0 and tail_remaining > 0:
                td, tx = tail_queue.popleft()
                if tx > tail_steps:
                    tail_queue.appendleft( (td, tx - tail_steps) )
                    tail_steps = 0
                    tail_remaining -= tail_steps
                else:
                    tail_steps -= tx
                    tail_remaining -= tx
            # Compute area
            area = (max_x - min_x +1) * (max_y - min_y +1)
            sum_f = (sum_f + area) % MOD
        print(f"Case #{tc}: {sum_f}")

if __name__ == "__main__":
    main()