import sys
import sys
import sys
from collections import deque

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    from sys import stdin
    import sys
    def input():
        return sys.stdin.read()

    data = input().split()
    idx = 0
    T = int(data[idx]); idx += 1
    MOD = 10**9 + 7
    for test_case in range(1, T + 1):
        N = int(data[idx]); M = int(data[idx+1]); idx += 2
        moves = []
        for _ in range(M):
            D = data[idx]; X = int(data[idx+1]); idx += 2
            moves.append((D, X))
        # Initialize direction: 0=E,1=S,2=W,3=N
        dir_map = {'E':0, 'S':1, 'W':2, 'N':3}
        # Initial direction is east
        current_dir = 0
        # Direction vectors: E, S, W, N
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        # Current head position
        head_x, head_y = 0, 0
        # We'll keep track of the path as direction and steps
        path = deque()
        path.append((current_dir, N))
        # Current min and max
        min_x = head_x
        max_x = head_x
        min_y = head_y
        max_y = head_y
        # Total time
        total_time = 0
        result = 0
        # To track the tail position, we need to know when the head has moved N steps
        # We'll keep track of segments with remaining steps
        tail_segments = deque()
        tail_x, tail_y = head_x, head_y
        for move_dir, move_steps in moves:
            # Update direction
            if move_dir == 'L':
                current_dir = (current_dir + 3) % 4
            elif move_dir == 'R':
                current_dir = (current_dir + 1) % 4
            elif move_dir == 'S':
                pass
            else:
                pass
            # Add the new movement to the path
            path.append((current_dir, move_steps))
            # Now, update the min and max based on the movement
            # Since the snake moves in straight lines, we can calculate the new head position
            head_x_new = head_x + dx[current_dir] * move_steps
            head_y_new = head_y + dy[current_dir] * move_steps
            # Update min and max
            min_x = min(min_x, head_x_new)
            max_x = max(max_x, head_x_new)
            min_y = min(min_y, head_y_new)
            max_y = max(max_y, head_y_new)
            # Update head position
            head_x, head_y = head_x_new, head_y_new
            # Update total time
            total_time += move_steps
            # For simplicity, assume f(i) is the area after the move
            area = (max_x - min_x) * (max_y - min_y)
            result = (result + area) % MOD
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()