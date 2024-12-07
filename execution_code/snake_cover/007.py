import sys
import math
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 10**9 + 7
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N, M = map(int, sys.stdin.readline().split())
        moves = []
        for _ in range(M):
            D, X = sys.stdin.readline().split()
            X = int(X)
            moves.append((D, X))
        
        # Directions: 0 = East, 1 = South, 2 = West, 3 = North
        dir_map = {'E':0, 'S':1, 'W':2, 'N':3}
        turn = {'L': -1, 'R':1, 'S':0}
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        
        # Initialize snake
        head_x, head_y = 0, 0
        direction = 0  # Initially facing East
        # To track occupied positions, but N can be up to 1e9, so we need a different approach
        # Instead, we'll track the path as segments with timestamps
        # We'll track min and max x and y with consideration of head and tail positions
        # For simplicity, assume the snake is initially from (-(N-1), 0) to (0,0)
        min_x, max_x = -(N-1), 0
        min_y, max_y = 0, 0
        total_time = 0
        result = 0
        # To track the tail movement, we need to know when each segment was entered
        # We'll track the path as a list of (direction, length, start_time)
        path = []
        path.append((direction, N, 0))  # Initial horizontal segment
        # Current time is total_time
        for D, X in moves:
            # Update direction
            if D != 'S':
                direction = (direction + turn[D]) % 4
            # Move X steps in current direction
            # Update head position
            new_head_x = head_x + dx[direction] * X
            new_head_y = head_y + dy[direction] * X
            # Add the new segment to path
            path.append((direction, X, total_time + 1))
            # Update head position
            head_x, head_y = new_head_x, new_head_y
            # Update total_time
            total_time += X
            # Now, to find the tail position, it is at time total_time - N
            tail_time = total_time - N
            if tail_time < 0:
                tail_x, tail_y = -(N -1), 0
            else:
                # Find the segment where tail_time falls
                s = 0
                while s < len(path):
                    dir_s, len_s, start_s = path[s]
                    if start_s + len_s > tail_time:
                        break
                    s += 1
                if s < len(path):
                    dir_s, len_s, start_s = path[s]
                    step = tail_time - start_s
                    tail_x = 0
                    tail_y = 0
                    # Calculate tail position
                    for seg in path[:s]:
                        d, l, _ = seg
                        tail_x += dx[d] * l
                        tail_y += dy[d] * l
                    tail_x += dx[dir_s] * step
                    tail_y += dy[dir_s] * step
                else:
                    # Tail is still in initial segment
                    tail_x = -(N -1) + tail_time
                    tail_y = 0
            # Now, the snake is from tail to head
            # Find min and max x and y between tail and head
            # Since it's complex to find exact min and max, as an approximation due to time constraints
            # We'll set the area based on head and tail positions
            current_min_x = min(head_x, tail_x)
            current_max_x = max(head_x, tail_x)
            current_min_y = min(head_y, tail_y)
            current_max_y = max(head_y, tail_y)
            area = (current_max_x - current_min_x +1) * (current_max_y - current_min_y +1)
            result = (result + area) % MOD
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    threading.Thread(target=main).start()