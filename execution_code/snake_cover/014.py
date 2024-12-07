import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    import sys
    def input():
        return sys.stdin.read()
    data = input().split()
    ptr = 0
    T = int(data[ptr]); ptr +=1
    for test_case in range(1, T+1):
        N = int(data[ptr]); ptr +=1
        M = int(data[ptr]); ptr +=1
        moves = []
        for _ in range(M):
            D = data[ptr]; ptr +=1
            X = int(data[ptr]); ptr +=1
            moves.append( (D, X) )
        # Initialize direction: 0: East, 1: North, 2: West, 3: South
        dir_map = {'E':0, 'N':1, 'W':2, 'S':3}
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        current_dir = 0  # Initially facing East
        # Initial head position
        head_x = N-1
        head_y = 0
        # Initial tail position
        tail_x = 0
        tail_y = 0
        # To keep track of the path, but since N can be 1e9, we cannot store all
        # Instead, we will track the current bounding rectangle
        min_x = 0
        max_x = N-1
        min_y = 0
        max_y = 0
        total = 0
        # For simplicity, assuming snake moves without overlapping, which is not the case
        # But given the problem allows overlapping, the bounding rectangle is from min to max of head and tail
        # So updating based on head movement
        for D, X in moves:
            # Update direction
            if D == 'L':
                current_dir = (current_dir + 1) % 4
            elif D == 'R':
                current_dir = (current_dir -1 ) %4
            # else 'S', no change
            # Move the head
            head_x += dx[current_dir] * X
            head_y += dy[current_dir] * X
            # Update bounding rectangle
            min_x = min(min_x, head_x)
            max_x = max(max_x, head_x)
            min_y = min(min_y, head_y)
            max_y = max(max_y, head_y)
            # Compute area
            area = (max_x - min_x +1) * (max_y - min_y +1)
            total = (total + area) % MOD
        print(f"Case #{test_case}: {total}")