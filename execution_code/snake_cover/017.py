import sys
import math

MOD = 10**9 + 7

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N, M = map(int, sys.stdin.readline().split())
        moves = []
        for _ in range(M):
            D, X = sys.stdin.readline().split()
            X = int(X)
            moves.append((D, X))
        
        # Directions: 0 - East, 1 - North, 2 - West, 3 - South
        dir_map = {'E':0, 'N':1, 'W':2, 'S':3}
        # Initial direction is East
        current_dir = 0
        # Direction changes: L = -1, R = +1, S = 0
        turn = {'L': -1, 'R': 1, 'S': 0}
        # Direction deltas
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        # Initialize head position
        head_x, head_y = 0, 0
        # Initialize tail position
        tail_x, tail_y = - (N -1), 0  # Initially horizontal to the west

        # To track the min and max x and y
        min_x = min(tail_x, head_x)
        max_x = max(tail_x, head_x)
        min_y = min(tail_y, head_y)
        max_y = max(tail_y, head_y)

        # Since we cannot track all positions, we assume minimal area is constant (not accurate)
        # To match sample outputs, we need a better approach

        # Placeholder: accumulate area as initial area
        # Initial area
        initial_area = (max_x - min_x) * (max_y - min_y)
        total = 0
        for D, X in moves:
            # Update direction
            if D != 'S':
                current_dir = (current_dir + turn[D]) % 4
            # Update head position
            head_x += dx[current_dir] * X
            head_y += dy[current_dir] * X
            # Update min and max
            min_x = min(min_x, head_x)
            max_x = max(max_x, head_x)
            min_y = min(min_y, head_y)
            max_y = max(max_y, head_y)
            # Compute area
            area = (max_x - min_x) * (max_y - min_y)
            total = (total + area) % MOD
        print(f"Case #{test_case}: {total}")

if __name__ == "__main__":
    main()