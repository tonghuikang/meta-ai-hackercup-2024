import sys
import string
from collections import defaultdict

def readints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        R, C = readints()
        G = []
        robots = []
        for r in range(R):
            line = sys.stdin.readline().strip()
            G.append(line)
            for c in range(C):
                if line[c].isupper():
                    robots.append((r, c))
        # Initialize tray strings for robots
        S = []
        for r, c in robots:
            S.append(G[r][c].lower())
        # Initialize active robots
        active = list(range(len(robots)))
        # Initialize robot positions
        positions = list(robots)
        # Initialize a list to store the tray strings
        trays = [ [G[r][c].lower()] for r, c in positions ]
        # Initialize grid occupancy
        grid = defaultdict(int)
        for idx, (r, c) in enumerate(positions):
            grid[(r, c)] = idx + 1  # mark occupied
        # Simulate moves
        while active:
            # Propose moves
            proposals = {}
            for idx in active:
                r, c = positions[idx]
                moves = []
                if r + 1 < R:
                    moves.append((r+1, c))
                if c + 1 < C:
                    moves.append((r, c+1))
                # Choose the move that gives the lex largest next character
                best_move = None
                best_char = ''
                for nr, nc in moves:
                    char = G[nr][nc].lower()
                    if char > best_char:
                        best_char = char
                        best_move = (nr, nc)
                if best_move:
                    proposals[idx] = (best_move, best_char)
                else:
                    proposals[idx] = None  # No move, will deactivate
            # Check for conflicts
            target_cells = defaultdict(list)
            for idx, prop in proposals.items():
                if prop:
                    target_cells[prop[0]].append(idx)
            # Resolve conflicts
            to_deactivate = set()
            for cell, idxs in target_cells.items():
                if len(idxs) > 1:
                    # Conflict, deactivate all these robots
                    to_deactivate.update(idxs)
            # Apply moves
            new_positions = {}
            for idx, prop in proposals.items():
                if prop:
                    if idx in to_deactivate:
                        continue
                    nr, nc = prop[0]
                    trays[idx].append(prop[1])
                    new_positions[idx] = (nr, nc)
            # Update positions and grid
            grid = defaultdict(int)
            new_active = []
            for idx in active:
                if idx in to_deactivate:
                    continue
                if idx in new_positions:
                    positions[idx] = new_positions[idx]
                    grid[positions[idx]] = idx + 1
                    new_active.append(idx)
                else:
                    # Deactivate
                    pass
            active = new_active
        # Find the minimal tray string
        min_S = min([''.join(tray) for tray in trays])
        print(f"Case #{tc}: {min_S}")

if __name__ == "__main__":
    main()