import sys
import threading

def main():
    import sys

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N, K = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(N):
            grid.append(sys.stdin.readline().strip())
        
        # Find existing '1's
        ones = []
        ques = []
        for r in range(N):
            for c in range(N):
                if grid[r][c] == '1':
                    ones.append((r, c))
                elif grid[r][c] == '?':
                    ques.append((r, c))
        
        if not ones:
            # No existing '1's, set K '1's anywhere
            # To maximize area, set '1's at corners
            # The maximal rectangle would be between the minimal and maximal selected '1's
            # Since K >=1, select K corners as far apart as possible
            # The maximal area is (max_r - min_r +1) * (max_c - min_c +1)
            if K ==0:
                area =0
            else:
                selected = sorted(ques, key=lambda x: (x[0], x[1]))
                # To maximize spread, select corners
                top = min(ques, key=lambda x: x[0])[0]
                bottom = max(ques, key=lambda x: x[0])[0]
                left = min(ques, key=lambda x: x[1])[1]
                right = max(ques, key=lambda x: x[1])[1]
                # If K >=4, we can set all four corners
                # Else, set as much spread as possible
                # For simplicity, set min and max rows and columns
                possible_rows = sorted(set([x[0] for x in ques]))
                possible_cols = sorted(set([x[1] for x in ques]))
                # Depending on K, choose rows and columns to extend
                # Here, we can set up to min(K, len(possible_rows)*len(possible_cols))
                # For simplicity, set min and max rows and cols
                min_r = possible_rows[0]
                max_r = possible_rows[-1]
                min_c = possible_cols[0]
                max_c = possible_cols[-1]
                area = (max_r - min_r +1) * (max_c - min_c +1)
        else:
            # Existing '1's
            min_r = min(r for r, c in ones)
            max_r = max(r for r, c in ones)
            min_c = min(c for r, c in ones)
            max_c = max(c for r, c in ones)
            # To maximize area, try to expand the rectangle by setting '1's
            # outside the current boundaries
            # Gather potential expansion positions
            top_candidates = sorted([r for r, c in ques if r < min_r])
            bottom_candidates = sorted([r for r, c in ques if r > max_r], reverse=True)
            left_candidates = sorted([c for r, c in ques if c < min_c])
            right_candidates = sorted([c for r, c in ques if c > max_c], reverse=True)
            
            # To maximize area, we need to maximize (new_max_r - new_min_r +1) * (new_max_c - new_min_c +1)
            # Each expansion in rows or columns costs some K
            # Try all possible expansions in rows and columns within K
            # Since N <= 2500 and K <= number of '?', it's not feasible to try all
            
            # Instead, we can precompute how much we can expand in each direction with given K
            # For simplicity, let's try expanding each direction independently
            # and choose the best combination
            
            # Precompute expansion options
            # For each possible number of expansions in top, bottom, left, right,
            # up to K, compute the possible new boundaries and area
            # To reduce complexity, limit to up to K expansions in each direction
            
            # Prepare lists
            top_positions = sorted(set(r for r, c in ques if r < min_r))
            bottom_positions = sorted(set(r for r, c in ques if r > max_r), reverse=True)
            left_positions = sorted(set(c for r, c in ques if c < min_c))
            right_positions = sorted(set(c for r, c in ques if c > max_c), reverse=True)
            
            # Calculate prefix counts
            top_prefix = []
            for idx in range(len(top_candidates)+1):
                top_prefix.append(idx)
            bottom_prefix = []
            for idx in range(len(bottom_candidates)+1):
                bottom_prefix.append(idx)
            left_prefix = []
            for idx in range(len(left_candidates)+1):
                left_prefix.append(idx)
            right_prefix = []
            for idx in range(len(right_candidates)+1):
                right_prefix.append(idx)
            
            # Since K is up to number of '?', and N up to 2500, iterate over possible expansions
            # Limit the number of expansions in each direction by K
            max_expansions = min(K, max(len(top_candidates), len(bottom_candidates), len(left_candidates), len(right_candidates)))
            # To reduce complexity, limit the number of expansions in each direction up to some small number
            # e.g., 100, since K can be large, but many expansions would give diminishing returns
            limit = min(K, 1000)
            # Initialize max area
            area = (max_r - min_r +1) * (max_c - min_c +1)
            for t in range(0, min(K+1, len(top_candidates)+1)):
                for b in range(0, min(K - t +1, len(bottom_candidates)+1)):
                    for l in range(0, min(K - t - b +1, len(left_candidates)+1)):
                        r = K - t - b - l
                        if r > len(right_candidates):
                            continue
                        new_min_r = min_r
                        new_max_r = max_r
                        new_min_c = min_c
                        new_max_c = max_c
                        if t >0:
                            new_min_r = min(new_min_r, top_candidates[t-1])
                        if b >0:
                            new_max_r = max(new_max_r, bottom_candidates[b-1])
                        if l >0:
                            new_min_c = min(new_min_c, left_candidates[l-1])
                        if r >0:
                            new_max_c = max(new_max_c, right_candidates[r-1])
                        current_area = (new_max_r - new_min_r +1) * (new_max_c - new_min_c +1)
                        if current_area > area:
                            area = current_area
            # Note: The above triple loop can be too slow when K is large.
            # To optimize, we can instead prioritize expansions in each direction separately and combine.
            # Here's an optimized approach:
            # Calculate the best expansion in each direction up to K
            top_expansions = [min_r]
            for i in range(min(K, len(top_candidates))):
                top_expansions.append(min(top_expansions[-1], top_candidates[i]))
            bottom_expansions = [max_r]
            for i in range(min(K, len(bottom_candidates))):
                bottom_expansions.append(max(bottom_expansions[-1], bottom_candidates[i]))
            left_expansions = [min_c]
            for i in range(min(K, len(left_candidates))):
                left_expansions.append(min(left_expansions[-1], left_candidates[i]))
            right_expansions = [max_c]
            for i in range(min(K, len(right_candidates))):
                right_expansions.append(max(right_expansions[-1], right_candidates[i]))
            # Now, try all possible distributions of K among the four directions
            # To keep it efficient, iterate over possible number of expansions in each direction
            # such that total expansions <= K
            # This is a 4-dimensional loop, which is too slow
            # Instead, iterate over possible expansions in one direction and calculate the best for others
            # Here's a 2-direction approach:
            # Split K into two parts: rows and columns
            # Rows: number of expansions in top and bottom
            # Columns: number of expansions in left and right
            # Precompute for rows and columns
            row_best = [min(m, K) for m in range(K+1)]
            col_best = [min(m, K) for m in range(K+1)]
            # However, to maximize, we need to try all possible splits
            # To keep it simple, iterate over possible top and bottom expansions
            # and assign remaining K to left and right
            for t in range(0, min(K, len(top_candidates)) +1):
                for b in range(0, min(K - t, len(bottom_candidates)) +1):
                    remaining = K - t - b
                    if remaining <0:
                        continue
                    # Assign remaining to left and right
                    # Maximize the spread
                    # Assign as much as possible to left and right
                    l = min(remaining, len(left_candidates))
                    r = min(remaining - l, len(right_candidates))
                    new_min_r = top_expansions[t] if t >0 else min_r
                    new_max_r = bottom_expansions[b] if b >0 else max_r
                    new_min_c = left_expansions[l] if l >0 else min_c
                    new_max_c = right_expansions[r] if r >0 else max_c
                    current_area = (new_max_r - new_min_r +1) * (new_max_c - new_min_c +1)
                    if current_area > area:
                        area = current_area
            # Alternatively, use the earlier area calculated
        print(f"Case #{test_case}: {area}")

# Run the main function in a new thread.
# This is to increase the recursion limit and stack size in some environments.
threading.Thread(target=main,).start()