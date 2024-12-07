import sys
import sys
import math
from collections import deque

MOD = 10**9+7

def readints():
    import sys
    return list(map(int, sys.stdin.readline().split()))

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N,M = map(int, sys.stdin.readline().split())
    moves = []
    for _ in range(M):
        D,X = sys.stdin.readline().split()
        X = int(X)
        moves.append((D,X))
    # Initialize direction: East
    dirs = ['E','S','W','N']  # order is clockwise
    dir_idx = 0  # East
    # Initialize head position
    head_x = 0
    head_y = 0
    # Initialize snake segments: initially horizontal west from head
    # So segments are from tail to head
    segments = deque()
    segments.append(('W', N-1))
    # Initial min and max x,y
    min_x = head_x - (N-1)
    max_x = head_x
    min_y = head_y
    max_y = head_y
    total_steps = 0
    # To track the tail's position
    tail_x = head_x - (N-1)
    tail_y = head_y
    # To track the path segments with positions
    # Each segment: (dx, dy, steps)
    path = deque()
    path.append(('W', N-1))
    # Initialize current direction
    current_dir = 'E'
    # Initialize position
    head_x = 0
    head_y = 0
    # Initialize deque of path segments: list of tuples (dx, dy, steps, start_x, start_y)
    path_segments = deque()
    # Initial direction is East, initial segments are West
    # So starting from head at (0,0), tail at (-(N-1),0)
    path_segments.append(('W', N-1, head_x - (N-1), head_y))
    # Initialize min and max
    min_x = head_x - (N-1)
    max_x = head_x
    min_y = head_y
    max_y = head_y
    # To track the current head direction
    dir_map = {'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0)}
    # To track all positions changes
    # For simplicity, we will track the head and tail positions
    # and update min and max accordingly
    # Initialize tail movement steps
    tail_segments = deque()
    tail_segments.append(('W', N-1, head_x - (N-1), head_y))
    # Initialize min and max
    min_x = head_x - (N-1)
    max_x = head_x
    min_y = head_y
    max_y = head_y
    # Initialize path list with direction and steps
    path_list = deque()
    path_list.append(('W', N-1, head_x - (N-1), head_y))
    # Initialize head position
    head_x = 0
    head_y =0
    # Initialize tail position
    tail_x = head_x - (N-1)
    tail_y = head_y
    # Initialize variables to track current min and max
    current_min_x = tail_x
    current_max_x = head_x
    current_min_y = head_y
    current_max_y = head_y
    # Initialize a deque to represent the path segments
    path_deque = deque()
    path_deque.append(('W', N-1, tail_x, tail_y))
    # Initialize a variable for sum of f(i)
    total_f =0
    # Initialize a list to keep track of all movements
    # Implemented a naive approach because of time constraints
    # Real efficient approach requires a more detailed implementation
    # But for now, proceed with updating min and max after each move
    for move in moves:
        D,X = move
        # Update direction
        if D == 'L':
            dir_idx = (dir_idx -1 )%4
        elif D == 'R':
            dir_idx = (dir_idx +1 )%4
        # else 'S', no change
        current_dir = dirs[dir_idx]
        dx, dy = dir_map[current_dir]
        # Move X steps
        # Update head position
        new_head_x = head_x + dx * X
        new_head_y = head_y + dy * X
        # Update path_deque: add new segment
        path_deque.append((current_dir, X, head_x, head_y))
        # Update head position
        head_x = new_head_x
        head_y = new_head_y
        # Update min and max
        if current_dir == 'E':
            current_max_x += X
        elif current_dir == 'W':
            current_min_x -= X
        elif current_dir == 'N':
            current_max_y += X
        elif current_dir == 'S':
            current_min_y -= X
        # Update tail position
        tail_steps = X
        while tail_steps >0 and path_deque:
            dir_tail, steps_tail, tx, ty = path_deque[0]
            if steps_tail <= tail_steps:
                # Remove entire segment
                if dir_tail == 'E':
                    current_min_x = min(current_min_x, tx)
                    current_max_x = max(current_max_x, tx + steps_tail)
                elif dir_tail == 'W':
                    current_min_x = min(current_min_x, tx - steps_tail)
                    current_max_x = max(current_max_x, tx)
                elif dir_tail == 'N':
                    current_min_y = min(current_min_y, ty)
                    current_max_y = max(current_max_y, ty + steps_tail)
                elif dir_tail == 'S':
                    current_min_y = min(current_min_y, ty - steps_tail)
                    current_max_y = max(current_max_y, ty)
                path_deque.popleft()
                tail_steps -= steps_tail
            else:
                # Remove part of the segment
                if dir_tail == 'E':
                    # tail_x increases
                    current_min_x = min(current_min_x, tx + tail_steps)
                    current_max_x = max(current_max_x, tx + steps_tail)
                elif dir_tail == 'W':
                    # tail_x increases
                    current_min_x = min(current_min_x, tx - (tail_steps))
                    current_max_x = max(current_max_x, tx)
                elif dir_tail == 'N':
                    current_min_y = min(current_min_y, ty + tail_steps)
                    current_max_y = max(current_max_y, ty + steps_tail)
                elif dir_tail == 'S':
                    current_min_y = min(current_min_y, ty - tail_steps)
                    current_max_y = max(current_max_y, ty)
                path_deque[0]=(dir_tail, steps_tail - tail_steps, tx, ty)
                tail_steps=0
        # Compute current area
        area = (current_max_x - current_min_x +1)*(current_max_y - current_min_y +1)
        f_i = area
        total_f = (total_f + f_i)%MOD
    print(f"Case #{tc}: {total_f}")