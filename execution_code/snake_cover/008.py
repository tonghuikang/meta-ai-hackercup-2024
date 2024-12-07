import sys
import math

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    from collections import deque

    T = int(sys.stdin.readline())
    MOD = 10**9 + 7
    for test_case in range(1, T + 1):
        N, M = map(int, sys.stdin.readline().split())
        moves = []
        for _ in range(M):
            D_i, X_i = sys.stdin.readline().split()
            X_i = int(X_i)
            moves.append((D_i, X_i))
        
        # Directions: 0 - East, 1 - North, 2 - West, 3 - South
        dir_map = {'E':0, 'N':1, 'W':2, 'S':3}
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        current_dir = 0  # Initially facing east
        head_x, head_y = 0, 0
        # Initialize the snake in horizontal position facing east
        # The initial positions range from (head_x - N +1, head_y) to (head_x, head_y)
        min_x = head_x - N + 1
        max_x = head_x
        min_y = head_y
        max_y = head_y
        
        t = 0
        result = 0
        for D_i, X_i in moves:
            # Update direction
            if D_i == 'L':
                current_dir = (current_dir + 1) % 4
            elif D_i == 'R':
                current_dir = (current_dir + 3) % 4
            # else 'S': no change
            
            # Movement in current_dir for X_i steps
            # After each step, update head position
            # and update min/max accordingly
            # Since N can be large, and we cannot track all positions,
            # we assume that after the first N steps, the snake fully occupies the path
            # So the bounding rectangle depends on the extremes reached during the move
            
            # Compute new head position after X_i steps
            new_head_x = head_x + dx[current_dir] * X_i
            new_head_y = head_y + dy[current_dir] * X_i
            
            # Update min and max
            min_x = min(min_x, new_head_x)
            max_x = max(max_x, new_head_x)
            min_y = min(min_y, new_head_y)
            max_y = max(max_y, new_head_y)
            
            # Compute area
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            # For f(i), since the rectangle area monotonically increases or stays the same
            # during a move, the minimal area is the area after the first step of the move
            # which would be the current area before the move
            # To simplify, we'll take the minimal area as the current area
            result = (result + area) % MOD
            
            # Update head position
            head_x, head_y = new_head_x, new_head_y
            t += X_i
        
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()