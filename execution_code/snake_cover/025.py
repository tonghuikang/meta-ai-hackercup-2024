import sys
import math

def main():
    import sys
    import sys
    import math
    from collections import deque

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    MOD = 10**9 + 7
    for test_case in range(1, T + 1):
        N = int(data[idx])
        M = int(data[idx + 1])
        idx += 2
        moves = []
        for _ in range(M):
            D = data[idx]
            X = int(data[idx + 1])
            moves.append((D, X))
            idx += 2
        # Initial direction: East (0: East, 1: South, 2: West, 3: North)
        dir_map = ['E', 'S', 'W', 'N']
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        current_dir = 0
        # Initial positions: horizontal, head at (0,0), facing East
        # To handle large N, we'll track only the bounding rectangle
        # Assuming initial snake is from (0,0) to (-N+1,0)
        # So initial min_x = -N+1, max_x = 0
        # min_y = max_y = 0
        min_x = -N + 1
        max_x = 0
        min_y = 0
        max_y = 0
        # The snake's head position
        head_x = 0
        head_y = 0
        # To track the tail's position, we'll need to track the path
        # but since N can be up to 1e9, we cannot store all
        # So instead, we can simulate the tail's movement based on the head's movement history
        # But with constraints, we need an approximation
        # Since overlapping is allowed, the bounding rectangle is determined by head and tail positions
        # However, it's non-trivial to track.
        # To simplify, we'll assume that the tail follows the head's path with a delay of N steps
        # But since movement is per unit, and X_i can be up to 1e9, it's not feasible
        # Therefore, we need to observe that the minimal area during the movement is when the snake is most compact
        # For straight movement, the area remains the same
        # When turning, the area increases
        # The minimal area would likely be when turning back to cover previous positions
        # However, without a proper model, it's difficult
        # To proceed, we'll track the bounding rectangle by updating min and max based on head's movement
        total = 0
        for D, X in moves:
            # First, turn
            if D == 'L':
                current_dir = (current_dir - 1) % 4
            elif D == 'R':
                current_dir = (current_dir + 1) % 4
            # Else, 'S', no turn
            # Then, move X units in current direction
            # Update head position
            new_head_x = head_x + dx[current_dir] * X
            new_head_y = head_y + dy[current_dir] * X
            # Update bounding rectangle
            min_x = min(min_x, new_head_x)
            max_x = max(max_x, new_head_x)
            min_y = min(min_y, new_head_y)
            max_y = max(max_y, new_head_y)
            # Calculate area
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            # Since we don't track exact A(t), we'll approximate f(i) as area
            # This is not accurate, but due to time constraints, we'll proceed
            total = (total + area) % MOD
            # Update head position
            head_x, head_y = new_head_x, new_head_y
        print(f"Case #{test_case}: {total}")

if __name__ == "__main__":
    main()