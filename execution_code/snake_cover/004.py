import sys
import sys
import math

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    MOD = 10**9 +7
    for tc in range(1, T+1):
        N = int(input[ptr])
        M = int(input[ptr+1])
        ptr +=2
        moves = []
        for _ in range(M):
            D = input[ptr]
            X = int(input[ptr+1])
            ptr +=2
            moves.append( (D,X) )
        # Initialize
        head_x =0
        head_y =0
        min_x = -(N-1)
        max_x =0
        min_y =0
        max_y =0
        direction =0 # 0:east,1:north,2:west,3:south
        dir_map = {
            0:(1,0),
            1:(0,1),
            2:(-1,0),
            3:(0,-1)
        }
        sum_f=0
        for D,X in moves:
            # Update direction
            if D == 'L':
                direction = (direction +1)%4
            elif D == 'R':
                direction = (direction -1 +4)%4
            elif D == 'S':
                pass
            else:
                pass # Invalid
            dx, dy = dir_map[direction]
            # Compute A1
            new_head_x1 = head_x + dx
            new_head_y1 = head_y + dy
            temp_min_x1 = min(min_x, new_head_x1)
            temp_max_x1 = max(max_x, new_head_x1)
            temp_min_y1 = min(min_y, new_head_y1)
            temp_max_y1 = max(max_y, new_head_y1)
            A1 = (temp_max_x1 - temp_min_x1 +1) * (temp_max_y1 - temp_min_y1 +1)
            # Compute A2
            new_head_xX = head_x + dx * X
            new_head_yX = head_y + dy * X
            if dx ==1:
                temp_max_x2 = max_x + X
                temp_min_x2 = min_x
            elif dx == -1:
                temp_min_x2 = min_x + X
                temp_max_x2 = max_x
            else:
                temp_min_x2 = min_x
                temp_max_x2 = max_x
            if dy ==1:
                temp_max_y2 = max_y + X
                temp_min_y2 = min_y
            elif dy == -1:
                temp_min_y2 = min_y + X
                temp_max_y2 = max_y
            else:
                temp_min_y2 = min_y
                temp_max_y2 = max_y
            A2 = (temp_max_x2 - temp_min_x2 +1) * (temp_max_y2 - temp_min_y2 +1)
            f_i = min(A1, A2)
            sum_f = (sum_f + f_i)%MOD
            # Update min_x, max_x, min_y, max_y
            min_x = temp_min_x1
            max_x = temp_max_x1
            min_y = temp_min_y1
            max_y = temp_max_y1
            # Update after full move
            if dx ==1:
                max_x += (X -1)*dx
            elif dx == -1:
                min_x += (X -1)*dx
            if dy ==1:
                max_y += (X -1)*dy
            elif dy == -1:
                min_y += (X -1)*dy
            # Head position
            head_x += dx * X
            head_y += dy * X
        print(f"Case #{tc}: {sum_f}")
                

if __name__ == "__main__":
    main()