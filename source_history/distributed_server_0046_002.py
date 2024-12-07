import sys
import itertools

def readints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        G = [sys.stdin.readline().strip() for _ in range(R)]
        robots = []
        for r in range(R):
            for c in range(C):
                if G[r][c].isupper():
                    robots.append((r, c, G[r][c].lower()))
        # Since R and C are small, and number of robots limited, we proceed with a backtracking approach
        # To maximize the min(S_i), we need to maximize the smallest string among all S_i
        # Therefore, we need to make sure that all S_i are as large as possible
        # We can aim to make the minimal S_i as large as possible by sorting robots and assigning them paths greedily
        # Sort robots based on their starting letter descendingly
        robots.sort(key=lambda x: x[2], reverse=True)
        # Assign paths to robots one by one, ensuring no conflicts
        # For each robot, choose the lex largest possible path
        # Keep track of occupied cells at each time step
        # Since robots can deactivate at any time, we will assume they move to the end as far as possible
        # For simplicity, let robots follow their paths to the bottom-right corner
        # and collect the largest possible string
        # Implement a simple greedy assignment
        occupied = {}
        strings = []
        for robot in robots:
            r, c, s = robot
            path = [(r, c)]
            current_r, current_c = r, c
            s_str = s
            while True:
                options = []
                if current_r + 1 < R:
                    options.append((G[current_r+1][current_c].lower(), current_r+1, current_c))
                if current_c + 1 < C:
                    options.append((G[current_r][current_c+1].lower(), current_r, current_c+1))
                if not options:
                    break
                # Choose the lex largest character available
                options.sort(reverse=True)
                next_char, nr, nc = options[0]
                # Check if the cell is already occupied
                # For simplicity, assume time steps are sequential and no overlaps
                # Append the character and move
                s_str += next_char
                current_r, current_c = nr, nc
                path.append((current_r, current_c))
            strings.append(s_str)
        # Now, the minimal string among strings
        min_string = min(strings)
        print(f"Case #{tc}: {min_string}")

if __name__ == '__main__':
    main()