import sys
import sys
def main():
    import sys

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        R, C = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(R):
            grid.append(sys.stdin.readline().strip())

        robots = []
        for r in range(R):
            for c in range(C):
                if grid[r][c].isupper():
                    robots.append( (r, c) )

        # Initialize S as the minimal starting letter
        starting_letters = [ grid[r][c].lower() for r, c in robots ]
        min_start = min(starting_letters)
        S = min_start

        # Initialize active robots: those with starting letter == min_start
        active = []
        for idx, (r, c) in enumerate(robots):
            if grid[r][c].lower() == min_start:
                active.append( (r, c) )

        # Continue building S
        while True:
            # For each active robot, find possible next characters
            min_c_per_robot = []
            possible_next = []
            for r, c in active:
                next_chars = []
                if c + 1 < C:
                    next_chars.append( grid[r][c + 1].lower() )
                if r + 1 < R:
                    next_chars.append( grid[r + 1][c].lower() )
                if next_chars:
                    min_c = min(next_chars)
                    min_c_per_robot.append(min_c)
                    possible_next.append( set(next_chars) )
                else:
                    # If a robot cannot move further, it cannot contribute to extending S
                    # But since S is already a prefix of its S_i, it's fine
                    min_c_per_robot.append(None)
                    possible_next.append( set() )

            # Collect min_c's that are not None
            current_min_cs = [ c for c in min_c_per_robot if c is not None ]
            if not current_min_cs:
                break  # No active robots can extend S
            # Find c_k as the maximum of the min c's
            c_k = max(current_min_cs)

            # Verify that all robots can have min_c_i <= c_k
            feasible = True
            for i, c in enumerate(min_c_per_robot):
                if c is not None and c > c_k:
                    feasible = False
                    break
            if not feasible:
                break

            # Append c_k to S
            S += c_k

            # Update active robots: those that can append c_k
            new_active = []
            for i, (r, c) in enumerate(active):
                possible = []
                if c + 1 < C and grid[r][c + 1].lower() == c_k:
                    possible.append( (r, c + 1) )
                if r + 1 < R and grid[r + 1][c].lower() == c_k:
                    possible.append( (r + 1, c) )
                if possible:
                    new_active.extend(possible)
            if not new_active:
                break
            active = new_active

        print(f"Case #{test_case}: {S}")

if __name__ == "__main__":
    main()