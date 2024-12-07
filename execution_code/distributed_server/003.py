import sys
import string
from collections import deque

def readints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        R, C = readints()
        G = []
        robots = []
        for r in range(R):
            row = sys.stdin.readline().strip()
            G.append(row)
            for c in range(C):
                if row[c].isupper():
                    robots.append( (r, c, row[c]) )
        # Function to get possible tray strings for a robot
        def get_max_tray(r0, c0, first_char):
            # We want the lex max tray, so always choose the max possible path
            tray = first_char
            r, c = r0, c0
            while True:
                moves = []
                if r +1 < R:
                    moves.append( (G[r+1][c].lower(), r+1, c) )
                if c +1 < C:
                    moves.append( (G[r][c+1].lower(), r, c+1) )
                if not moves:
                    break
                # Choose the move with the maximum character
                moves.sort(reverse=True)
                next_char, nr, nc = moves[0]
                tray += next_char
                r, c = nr, nc
            return tray
        # For each robot, compute its max tray
        tray_max = []
        for robot in robots:
            r, c, ch = robot
            tray_max.append( get_max_tray(r, c, ch) )
        # The min tray_max is the answer
        answer = min(tray_max)
        print(f"Case #{test_case}: {answer.lower()}")

if __name__ == "__main__":
    main()