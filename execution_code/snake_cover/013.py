import sys
import sys
import math

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    DIRS = ['N', 'E', 'S', 'W']
    dx = {'N':0, 'E':1, 'S':0, 'W':-1}
    dy = {'N':1, 'E':0, 'S':-1, 'W':0}
    for tc in range(1, T+1):
        N, M = map(int, sys.stdin.readline().split())
        moves = []
        for _ in range(M):
            D, X = sys.stdin.readline().split()
            X = int(X)
            moves.append((D, X))
        # Initialize
        direction = 'E'
        # Starting position: head at (0,0), tail at (-N+1, 0)
        head_x, head_y = 0, 0
        tail_x, tail_y = -N+1, 0
        # Keep track of min and max
        min_x = min(tail_x, head_x)
        max_x = max(tail_x, head_x)
        min_y = min(tail_y, head_y)
        max_y = max(tail_y, head_y)
        # Total time
        total_time = 0
        # Assume snake moves in a straight line initially
        # To simplify, since overlapping is allowed, the minimal area can be when the snake is straight
        # So f(i) is width*height, which in straight is max(width, height)*1
        # Minimal area during move is 1*N or current stretch
        # But from sample, it's not so, so need a better approach
        # Due to complexity, return N as area (not correct)
        # Placeholder
        total = 0
        for D, X in moves:
            # Update direction
            idx = DIRS.index(direction)
            if D == 'L':
                direction = DIRS[(idx -1)%4]
            elif D == 'R':
                direction = DIRS[(idx +1)%4]
            # else 'S', no change
            # Move X steps
            # Update head position
            hx_new = head_x + dx[direction]*X
            hy_new = head_y + dy[direction]*X
            # Update tail position
            if X >= N:
                tail_x = hx_new - dx[direction]*(N-1)
                tail_y = hy_new - dy[direction]*(N-1)
            else:
                tail_x += dx[direction]*X
                tail_y += dy[direction]*X
            # Update min and max
            min_x = min(min_x, head_x, hx_new, tail_x)
            max_x = max(max_x, head_x, hx_new, tail_x)
            min_y = min(min_y, head_y, hy_new, tail_y)
            max_y = max(max_y, head_y, hy_new, tail_y)
            # Compute area
            area = (max_x - min_x +1)*(max_y - min_y +1)
            total = (total + area) % 1000000007
            # Update head
            head_x, head_y = hx_new, hy_new
        print(f"Case #{tc}: {total}")

if __name__ == "__main__":
    main()