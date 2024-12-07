import sys
import math
import sys
from collections import deque

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 10**9 + 7
    T = int(sys.stdin.readline())
    for test_case in range(1, T +1):
        N, M = map(int, sys.stdin.readline().split())
        moves = []
        for _ in range(M):
            D, X = sys.stdin.readline().split()
            X = int(X)
            moves.append((D, X))
        # Initialize direction: 0=East, 1=North, 2=West, 3=South
        dir_map = {'E':0, 'N':1, 'W':2, 'S':3}
        # Initial direction is East
        current_dir = 0
        # Directions: East=(1,0), North=(0,1), West=(-1,0), South=(0,-1)
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        # Initialize head position
        head_x, head_y = 0,0
        # Initialize snake positions: since N can be up to 1e9, we cannot store them
        # Instead, track the path as a deque
        # But even deque is too large, so track segments
        # We need to track when tail moves in which direction
        # So we use a deque of (direction, steps)
        path = deque()
        path.append((current_dir, N))
        tail_x, tail_y = head_x, head_y
        # Initialize bounding box
        min_x = head_x
        max_x = head_x
        min_y = head_y
        max_y = head_y
        # Initialize total time
        total_time = 0
        # Initialize answer
        answer = 0
        for D, X in moves:
            # Update direction
            if D == 'L':
                current_dir = (current_dir +1 ) %4
            elif D == 'R':
                current_dir = (current_dir +3 ) %4
            # else 'S', no change
            # Now, move head by X units in current_dir
            dx, dy = dirs[current_dir]
            # Update head position
            new_head_x = head_x + dx * X
            new_head_y = head_y + dy * X
            # Update path
            path.append((current_dir, X))
            # Update tail
            steps_to_move = X
            while steps_to_move >0:
                dir_tail, steps_tail = path[0]
                if steps_tail > steps_to_move:
                    path[0] = (dir_tail, steps_tail - steps_to_move)
                    tail_x += dirs[dir_tail][0] * steps_to_move
                    tail_y += dirs[dir_tail][1] * steps_to_move
                    steps_to_move =0
                else:
                    path.popleft()
                    tail_x += dirs[dir_tail][0] * steps_tail
                    tail_y += dirs[dir_tail][1] * steps_tail
                    steps_to_move -= steps_tail
            head_x, head_y = new_head_x, new_head_y
            # Update bounding box
            min_x = min(min_x, head_x, tail_x)
            max_x = max(max_x, head_x, tail_x)
            min_y = min(min_y, head_y, tail_y)
            max_y = max(max_y, head_y, tail_y)
            # Compute area
            area = (max_x - min_x +1 ) * (max_y - min_y +1 )
            # Update answer
            answer = (answer + area) % MOD
            total_time += X
        print(f"Case #{test_case}: {answer}")

if __name__ == "__main__":
    main()