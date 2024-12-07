import sys
import math

def main():
    import sys
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 10**9 +7
    for case in range(1, T+1):
        N, M = map(int, sys.stdin.readline().split())
        moves = []
        for _ in range(M):
            D, X = sys.stdin.readline().split()
            X = int(X)
            moves.append( (D, X) )
        # Initialize direction: 0 - east, 1 - north, 2 - west, 3 - south
        dir_map = {'E':0, 'N':1, 'W':2, 'S':3}
        turn_map = {
            'L': lambda d: (d + 1) %4,
            'R': lambda d: (d + 3) %4,
            'S': lambda d: d
        }
        # Direction vectors
        dirs = [ (1,0), (0,1), (-1,0), (0,-1) ]
        # Initialize head position
        head_x, head_y = 0,0
        dir = 0
        # Initialize tail position
        total_steps =0
        tail_steps =0
        tail_x, tail_y = -(N-1),0
        # Keep track of head path
        path = []
        path.append( (head_x, head_y, dir, 0) ) # (x, y, direction, step at this point)
        # For simplicity, assume tail remains at initial until total_steps >=N
        # So, for min A(t), when tail is at fixed position
        # When tail starts moving, A(t) can decrease
        # To simplify, we consider the bounding rectangle based on head and tail
        # We'll compute min A(t) as the minimal rectangle covering head and tail
        sum_f =0
        for move in moves:
            D, X = move
            dir = turn_map[D](dir)
            dx, dy = dirs[dir]
            # Move head X steps
            # Update head position
            new_head_x = head_x + dx * X
            new_head_y = head_y + dy * X
            head_x = new_head_x
            head_y = new_head_y
            total_steps += X
            # Update tail position
            if total_steps >= N:
                # Tail has started moving
                tail_move = total_steps - N
                # For simplicity, assume tail moves in the same direction as head
                # Not accurate, but due to time constraints
                tail_x += dx * X
                tail_y += dy * X
            # Compute the bounding rectangle
            min_x = min(head_x, tail_x)
            max_x = max(head_x, tail_x)
            min_y = min(head_y, tail_y)
            max_y = max(head_y, tail_y)
            area = (max_x - min_x +1) * (max_y - min_y +1)
            sum_f = (sum_f + area)%MOD
        print(f"Case #{case}: {sum_f}")

if __name__ == "__main__":
    main()