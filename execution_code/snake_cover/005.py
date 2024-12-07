import sys

sys.setrecursionlimit(1 << 25)

def main():
    MOD = 10**9 + 7
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N_str, M_str = sys.stdin.readline().split()
        N = int(N_str)
        M = int(M_str)
        min_x = 0
        max_x = N - 1  # Initially, snake occupies x = 0 to N-1
        min_y = 0
        max_y = 0      # y coordinate is 0 initially
        head_x = N -1  # Head is at x = N-1
        head_y = 0
        area = (max_x - min_x + 1) * (max_y - min_y + 1)
        total_sum = 0
        for _ in range(M):
            D_X = sys.stdin.readline().strip().split()
            if len(D_X) !=2:
                D_str = D_X[0]
                X_i = int(sys.stdin.readline().strip())
            else:
                D_str, X_i_str = D_X
                X_i = int(X_i_str)
            D_i = D_str
            if D_i == 'L':
                # Turn left: Update direction
                # From current facing direction, left turn
                if head_x != N -1 or head_y != 0:
                    if dir == 'N':
                        dir = 'W'
                    elif dir == 'E':
                        dir = 'N'
                    elif dir == 'S':
                        dir = 'E'
                    elif dir == 'W':
                        dir = 'S'
                else:
                    dir = 'N'  # Initially facing East, left turn to North
            elif D_i == 'R':
                # Turn right
                if head_x != N -1 or head_y != 0:
                    if dir == 'N':
                        dir = 'E'
                    elif dir == 'E':
                        dir = 'S'
                    elif dir == 'S':
                        dir = 'W'
                    elif dir == 'W':
                        dir = 'N'
                else:
                    dir = 'S'  # Initially facing East, right turn to South
            elif D_i == 'S':
                # Keep going straight
                if head_x != N -1 or head_y != 0:
                    pass
                else:
                    dir = 'E'  # Initially facing East
            else:
                # Invalid direction
                continue
            # Move the snake
            X_i = int(X_i)
            delta_x = 0
            delta_y = 0
            if dir == 'N':
                delta_y = X_i
            elif dir == 'S':
                delta_y = -X_i
            elif dir == 'E':
                delta_x = X_i
            elif dir == 'W':
                delta_x = -X_i
            else:
                # Invalid direction
                continue
            new_head_x = head_x + delta_x
            new_head_y = head_y + delta_y
            # Update boundaries
            old_area = area
            new_min_x = min(min_x, new_head_x)
            new_max_x = max(max_x, new_head_x)
            new_min_y = min(min_y, new_head_y)
            new_max_y = max(max_y, new_head_y)
            new_area = (new_max_x - new_min_x + 1) * (new_max_y - new_min_y +1)
            # The minimal area during the move is the minimum of old_area and new_area
            f_i = min(old_area, new_area)
            total_sum = (total_sum + f_i) % MOD
            # Update head position and boundaries
            head_x = new_head_x
            head_y = new_head_y
            min_x = new_min_x
            max_x = new_max_x
            min_y = new_min_y
            max_y = new_max_y
            area = new_area
        print(f"Case #{case_num}: {total_sum}")

if __name__ == "__main__":
    main()