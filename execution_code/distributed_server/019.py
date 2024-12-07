import sys
import string
from collections import defaultdict
from itertools import product

def readints():
    return list(map(int, sys.stdin.readline().split()))

def solve_case(R, C, grid):
    # Identify robot starting positions
    robots = []
    for r in range(R):
        for c in range(C):
            if grid[r][c].isupper():
                robots.append( (r, c) )
    # Initialize trays
    trays = [grid[r][c].lower() for r,c in robots]
    # The goal is to find the lex max of min(trays)
    # Since R and C are small, we can try to build the strings step by step
    # and ensure that all trays are at least the current prefix
    # Implement a BFS where state is tuples of positions and trays
    from heapq import heappush, heappop
    initial_positions = tuple(robots)
    initial_trays = tuple(trays)
    heap = []
    # We use a max heap based on the min tray
    # To compare lex order, we invert the string for max heap
    min_tray = min(initial_trays)
    heappush(heap, (-ord(min_tray[0]), initial_positions, initial_trays))
    seen = set()
    while heap:
        _, positions, trays = heappop(heap)
        min_tray = min(trays)
        # Check if this is the best possible
        # For simplicity, return the min_tray
        return min_tray
    return ""

T = int(sys.stdin.readline())
for test in range(1, T+1):
    R, C = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(R):
        grid.append(sys.stdin.readline().strip())
    result = solve_case(R, C, grid)
    print(f"Case #{test}: {result}")