import sys

def readints():
    import sys
    return list(map(int, sys.stdin.readline().split()))

def solve():
    import sys
    import math
    from collections import defaultdict
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N,K = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(N):
            grid.append(sys.stdin.readline().strip())
        # Find initial 1s
        rows_with_1 = set()
        cols_with_1 = set()
        question_marks = []
        for r in range(N):
            for c in range(N):
                if grid[r][c] == '1':
                    rows_with_1.add(r)
                    cols_with_1.add(c)
                elif grid[r][c] == '?':
                    question_marks.append( (r,c) )
        if not rows_with_1:
            # No initial 1s, need to set K ones to maximize the area
            if K ==0:
                max_area = 0
            else:
                # Choose two distinct rows and two distinct columns if possible
                if K ==1:
                    max_area =1
                else:
                    # To maximize area, set 1s on corners
                    # The maximum area is (min(K, N)) * (min(K, N))
                    max_area = min(K, N) * min(K, N)
        else:
            min_r = min(rows_with_1)
            max_r = max(rows_with_1)
            min_c = min(cols_with_1)
            max_c = max(cols_with_1)
            current_area = (max_r - min_r +1) * (max_c - min_c +1)
            # Potential to expand top, bottom, left, right
            # Collect possible expansions
            expand_up = set()
            expand_down = set()
            expand_left = set()
            expand_right = set()
            for r,c in question_marks:
                if r < min_r:
                    expand_up.add( (r,c) )
                if r > max_r:
                    expand_down.add( (r,c) )
                if c < min_c:
                    expand_left.add( (r,c) )
                if c > max_c:
                    expand_right.add( (r,c) )
            # The maximum possible expansion in each direction
            possible_up = min_r
            possible_down = N-1 - max_r
            possible_left = min_c
            possible_right = N-1 - max_c
            # Count available '?' in each direction
            cnt_up = len(expand_up)
            cnt_down = len(expand_down)
            cnt_left = len(expand_left)
            cnt_right = len(expand_right)
            # To maximize area, try to maximize height and width
            # The increase is height and width
            # We need to decide how many to assign to each direction
            # It can be complex, so we'll try all possible allocations within K
            max_area = current_area
            # To limit the iterations, since N<=2500, and K<=UM, which is up to N^2
            # But to be efficient, we can iterate over possible expansions
            # Iterate over possible number of expansions upwards
            for up in range(0, min(cnt_up, K)+1):
                remaining1 = K - up
                for down in range(0, min(cnt_down, remaining1)+1):
                    remaining2 = remaining1 - down
                    for left in range(0, min(cnt_left, remaining2)+1):
                        right = min(cnt_right, remaining2 - left)
                        # Now, calculate new boundaries
                        new_min_r = min_r
                        new_max_r = max_r
                        new_min_c = min_c
                        new_max_c = max_c
                        if up >0:
                            new_min_r = min_r - up
                        if down >0:
                            new_max_r = max_r + down
                        if left >0:
                            new_min_c = min_c - left
                        if right >0:
                            new_max_c = max_c + right
                        # Clamp to grid
                        new_min_r = max(0, new_min_r)
                        new_max_r = min(N-1, new_max_r)
                        new_min_c = max(0, new_min_c)
                        new_max_c = min(N-1, new_max_c)
                        area = (new_max_r - new_min_r +1) * (new_max_c - new_min_c +1)
                        if area > max_area:
                            max_area = area
            # Additional possibility: If K not used up, assign remaining to expand further
            # But for simplicity, we can keep the above approach
        print(f"Case #{test_case}: {max_area}")