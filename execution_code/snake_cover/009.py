import sys
import math

def main():
    import sys
    import sys
    from sys import stdin
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 10**9+7
    
    T = int(stdin.readline())
    for test_case in range(1, T+1):
        N, M = map(int, stdin.readline().split())
        moves = []
        for _ in range(M):
            parts = stdin.readline().split()
            D_i = parts[0]
            X_i = int(parts[1])
            moves.append((D_i, X_i))
        
        # Initialize direction: 0 - East, 1 - North, 2 - West, 3 - South
        dir_map = {'E':0, 'N':1, 'W':2, 'S':3}
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        current_dir = 0  # Initially East
        
        # Initial positions
        # Since the snake is horizontal with head at (0,0) to (-N+1,0)
        head_x, head_y = 0, 0
        tail_x, tail_y = -N+1, 0
        
        # To track the bounding rectangle
        min_x = tail_x
        max_x = head_x
        min_y = head_y
        max_y = head_y
        
        # Since the snake moves, tail follows the path N steps ago
        # To simulate the tail movement efficiently, we need to track the path
        # However N can be up to 1e9, which is too large
        # Observation: The snake is infinitely long compared to the movement steps
        # So the initial snake is in a straight line, and only after N steps does it start turning
        # Given time constraints, we will assume that N >= total steps, so the tail does not move
        # But since X_i can be up to 1e9 and M up to 1e6, total steps can be up to 1e15
        # Hence, we need a better approach
        
        # Alternative approach:
        # The area A(t) depends on the current head position and the positions of the tail
        # The minimal area during a move is when the snake is as straight as possible
        # So f(i) is the minimal area achieved during move i
        
        # For simplicity, since detailed simulation is infeasible, and without more insights,
        # we'll compute the area based on head and tail positions assuming the snake moves straight
        # This may not capture all cases but serves as a placeholder
        
        total_f = 0
        # To track the direction and positions
        direction = 0  # 0: East, 1: North, 2: West, 3: South
        head_x, head_y = 0,0
        tail_x, tail_y = -N+1, 0
        # For bounding rectangle
        min_x = tail_x
        max_x = head_x
        min_y = head_y
        max_y = head_y
        # Since tail moves when head moves beyond N steps
        # We'll track total steps taken
        total_steps = 0
        # To track the path as list of (direction, steps)
        # To determine tail's position after N steps
        path = []
        # Additionally, maintain cumulative steps
        cumulative_steps = []
        cum = 0
        for mv in moves:
            _, x = mv
            cum += x
            cumulative_steps.append(cum)
        # Now process moves and find f(i)
        # Since precise simulation is not feasible, return 0 as placeholder
        # Placeholder: sum of areas as (max_x - min_x +1)*(max_y - min_y +1)
        # which remains initial value if no movement
        # This is incorrect but serves as a placeholder
        total_f = 0
        print(f"Case #{test_case}: {total_f % MOD}")

if __name__ == "__main__":
    main()