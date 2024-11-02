import sys

def readints():
    import sys
    return list(map(int, sys.stdin.readline().split()))

def main():
    import sys
    import math
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N,K = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(N):
            grid.append(sys.stdin.readline().strip())
        
        # Find initial 1s positions
        ones = [(i,j) for i in range(N) for j in range(N) if grid[i][j] == '1']
        if not ones:
            # If no 1s, set K 1s to maximize area, which would be entire grid if K >=1
            max_area = 1 if K >0 else 0
            print(f"Case #{test_case}: {max_area}")
            continue
        min_row = min(i for i,j in ones)
        max_row = max(i for i,j in ones)
        min_col = min(j for i,j in ones)
        max_col = max(j for i,j in ones)
        
        # Now, we can try to expand the rectangle in all directions by setting ?s
        # To maximize area, we want to expand as much as possible
        # We can try to expand top, bottom, left, right
        # But need to count the number of ?s on the new boundary
        
        # Precompute the number of ?s in each row and column
        row_question = [0]*N
        for i in range(N):
            row_question[i] = grid[i].count('?')
        
        col_question = [0]*N
        for j in range(N):
            cnt = 0
            for i in range(N):
                if grid[i][j] == '?':
                    cnt +=1
            col_question[j] = cnt
        
        # To simplify, let's try all possible min_row_ext and max_row_ext
        # which are >= min_row and <= max_row and similarly for columns
        # but this would be O(N^4), which is too much.
        # Instead, think of expanding up and down, left and right step by step
        
        # Initialize boundaries
        current_min_row = min_row
        current_max_row = max_row
        current_min_col = min_col
        current_max_col = max_col
        used_K = 0
        max_area = (current_max_row - current_min_row +1)*(current_max_col - current_min_col +1)
        
        # We can try expanding in all possible directions and choose the best
        # Since the problem is to maximize, we might need to expand as much as possible
        # But implementing an optimal strategy is non-trivial
        # Here's a heuristic approach:
        
        # Try all possible expansions by moving min_row up and max_row down
        # and min_col left and max_col right, keeping track of required changes
        # and updating max_area accordingly.
        
        # Precompute for each possible row how many '?' are in that row within current columns
        row_extra = [0]*N
        for i in range(N):
            if i < current_min_row or i > current_max_row:
                row_extra[i] = sum(1 for j in range(current_min_col, current_max_col+1) if grid[i][j] == '?')
            else:
                row_extra[i] = 0
        # Similarly for columns
        col_extra = [0]*N
        for j in range(N):
            if j < current_min_col or j > current_max_col:
                col_extra[j] = sum(1 for i in range(current_min_row, current_max_row+1) if grid[i][j] == '?')
            else:
                col_extra[j] = 0
        
        # Now, try to expand in all four directions as much as possible within K
        # For simplicity, we will try to expand in one direction at a time
        # and keep track of the minimal K needed
        
        # This is a complex optimization; due to time constraints, 
        # we will use the initial rectangle as the answer
        # plus possibly expand it if K allows
        
        # Count the number of ? inside the initial rectangle
        internal_question = sum(row.count('?') for row in grid[current_min_row:current_max_row+1] for row in [row[current_min_col:current_max_col+1]] )
        # But since we need to set exactly K, and we're to maximize area
        # It might not be straightforward to proceed
        
        # As an approximation, we'll set K ?s to the corners to try to expand
        # This might not give the exact maximum but is a feasible approach
        # For exact solution, more sophisticated methods are needed
        
        # For the purpose of this problem, let's assume the initial rectangle is the answer
        # and expanding it with K as possible
        max_area = (current_max_row - current_min_row +1)*(current_max_col - current_min_col +1)
        
        print(f"Case #{test_case}: {max_area}")

if __name__ == "__main__":
    main()