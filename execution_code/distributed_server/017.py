import sys
import sys
import sys
from collections import deque
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        G = [sys.stdin.readline().strip() for _ in range(R)]
        
        # Find initial robots
        robots = []
        for r in range(R):
            for c in range(C):
                if 'A' <= G[r][c] <= 'Z':
                    robots.append( (r, c, G[r][c].lower()) )
        
        # Since R and C are small, we can represent paths with positions
        # To maximize min(S_i), we need to maximize the lex min of S_i
        # We can try to find the minimum string that is as large as possible
        # Essentially, we want the min(S_i) to be as large as possible lex
        
        # To do this, we can perform a BFS-like search, keeping track of the current prefix
        # and trying to append the largest possible next character that can be achieved by all robots
        
        # Initialize the current prefix
        prefix = ""
        
        while True:
            # For each robot, find the possible next characters
            next_chars = []
            for r, c, s in robots:
                chars = []
                # Option to deactivate, keep current s
                chars.append(None)  # Indicates deactivation
                # Move right
                if c + 1 < C:
                    chars.append(G[r][c+1].lower())
                # Move down
                if r + 1 < R:
                    chars.append(G[r+1][c].lower())
                # Get possible next character, or keep s if deactivate
                possible = [ch for ch in chars if ch is not None]
                if possible:
                    next_chars.append( max(possible) )
                else:
                    # Must deactivate
                    next_chars.append(None)
            # Determine the minimum among next_chars, ignoring None
            # We need the min(S_i) to be as large as possible
            # So we need to maximize the min among all possible next characters
            # The candidate is the smallest next_chars
            candidate = min([ch for ch in next_chars if ch is not None], default=None)
            if candidate is None:
                break
            # Now, check if all robots can have next character >= candidate
            feasible = True
            for ch in next_chars:
                if ch is not None and ch < candidate:
                    feasible = False
                    break
            if not feasible:
                break
            # Append candidate to prefix
            prefix += candidate
            # Move robots that can move with character >= candidate
            new_robots = []
            occupied = set()
            for i, (r, c, s) in enumerate(robots):
                ch = next_chars[i]
                if ch is None:
                    # Deactivate
                    continue
                if ch == candidate:
                    # Choose to move this way
                    # Prefer right over down, or vice versa
                    # For simplicity, choose right first
                    moved = False
                    if c +1 < C and G[r][c+1].lower() == ch:
                        if (r, c+1) not in occupied:
                            new_robots.append( (r, c+1, s + ch) )
                            occupied.add( (r, c+1) )
                            moved = True
                    if not moved and r +1 < R and G[r+1][c].lower() == ch:
                        if (r+1, c) not in occupied:
                            new_robots.append( (r+1, c, s + ch) )
                            occupied.add( (r+1, c) )
                else:
                    # Cannot use this path
                    # Should have already ensured all ch >= candidate
                    pass
            robots = new_robots
        print(f"Case #{test_case}: {prefix}")

if __name__ == '__main__':
    main()