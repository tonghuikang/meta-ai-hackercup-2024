import sys
import sys
from collections import deque
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def to_lower(c):
    return c.lower()

def solve_case(R, C, grid):
    robots = []
    for r in range(R):
        for c in range(C):
            if grid[r][c].isupper():
                robots.append((r, c))
    # Precompute for each robot all possible paths and their S_i
    # But this is too expensive
    
    # Instead, we try to build the min S_i step by step
    # Initialize the current strings for robots
    initial_strings = [to_lower(grid[r][c]) for r,c in robots]
    # To maximize min(S_i), we need to maximize the minimal string
    # Let's perform a binary search-like approach on the possible strings
    # But instead, implement a greedy approach to build the string character by character
    prefix = ""
    positions = [robots[i] for i in range(len(robots))]
    active = [True] * len(robots)
    # To manage robot paths, keep track of their current positions
    current_positions = list(positions)
    # To manage the cells occupied at each step
    while True:
        # For the next character, try from 'z' to 'a'
        found = False
        for c in reversed('abcdefghijklmnopqrstuvwxyz'):
            # Check if for all robots, they can append c
            # We need to assign moves to robots such that:
            # - Each active robot can either deactivate or move to a cell with letter >= c
            # - No two robots move to the same cell
            # This is complex, so simplifying:
            # Require that for each robot, either it can deactivate, or it can move to a cell with letter >= c
            # Additionally, assignments to cells must be unique
            # To maximize min(S_i), we need all robots to have S_i >= prefix + c
            # So for each robot, it must either already have S_i >= prefix + c, or can extend to do so
            # Given the complexity, implement a simplified approach:
            # Try to move all robots right or down if the next cell's letter >= c
            move_possible = True
            proposed_moves = {}
            for i, (r, c_pos) in enumerate(current_positions):
                if not active[i]:
                    continue
                # Look for possible moves
                candidates = []
                if r + 1 < R:
                    candidates.append((r+1, c_pos))
                if c_pos + 1 < C:
                    candidates.append((r, c_pos+1))
                # Find the maximum letter among possible moves
                max_char = None
                best_moves = []
                for nr, nc in candidates:
                    char = to_lower(grid[nr][nc])
                    if char >= c:
                        if max_char is None or char > max_char:
                            max_char = char
                            best_moves = [(nr, nc)]
                        elif char == max_char:
                            best_moves.append((nr, nc))
                if max_char is None:
                    # Cannot move to a cell with letter >= c, must deactivate
                    # But to have S_i >= prefix + c, it must not deactivate, which fails
                    move_possible = False
                    break
                else:
                    proposed_moves[i] = best_moves
            if move_possible:
                # Now, assign moves ensuring no two robots go to the same cell
                # This is equivalent to finding a matching where each robot selects one of its possible cells without conflict
                # Implement backtracking matching
                assignments = {}
                used = set()
                def backtrack(robot_idx):
                    if robot_idx == len(robots):
                        return True
                    if not active[robot_idx]:
                        return backtrack(robot_idx + 1)
                    if robot_idx not in proposed_moves:
                        return False
                    for move in proposed_moves[robot_idx]:
                        if move not in used:
                            assignments[robot_idx] = move
                            used.add(move)
                            if backtrack(robot_idx + 1):
                                return True
                            used.remove(move)
                    return False
                if backtrack(0):
                    # Assign the moves
                    prefix += c
                    for i in range(len(robots)):
                        if not active[i]:
                            continue
                        if i in assignments:
                            move = assignments[i]
                            current_positions[i] = move
                            # Append the character
                            # initial_strings[i] += to_lower(grid[move[0]][move[1]])
                        else:
                            # Should not happen
                            active[i] = False
                    found = True
                    break
        if not found:
            break
    return prefix

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(R):
            row = sys.stdin.readline().strip()
            grid.append(row)
        result = solve_case(R, C, grid)
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()