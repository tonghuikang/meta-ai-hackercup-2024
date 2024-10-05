import sys
import sys
import sys
def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    from collections import defaultdict

    T = int(sys.stdin.readline())
    for test_case in range(1, T +1):
        N, G = map(int, sys.stdin.readline().split())
        E = []
        for _ in range(N):
            E.append(int(sys.stdin.readline()))
        
        parent = {}

        stones = {}
        
        def find(p):
            # Iterative find with path compression
            stack = []
            while p in parent:
                stack.append(p)
                p = parent[p]
            for pos in stack:
                parent[pos] = p
            return p
        
        for idx, e in enumerate(E, 1):
            p = e
            p_final = find(p)
            stones[p_final] = idx
            parent[p_final] = p_final +1
        
        # Now, find the stone closest to G
        # Iterate through all stones and find the minimal |p - G|
        min_dist = float('inf')
        min_stone = N+1
        for p, stone in stones.items():
            dist = abs(G - p)
            if dist < min_dist or (dist == min_dist and stone < min_stone):
                min_dist = dist
                min_stone = stone
        print(f"Case #{test_case}: {min_stone} {min_dist}")

import sys
import sys
import sys
def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    from collections import defaultdict

    T = int(sys.stdin.readline())
    for test_case in range(1, T +1):
        N, G = map(int, sys.stdin.readline().split())
        E = []
        for _ in range(N):
            E.append(int(sys.stdin.readline()))
        
        parent = {}

        stones = {}
        
        def find(p):
            # Iterative find with path compression
            stack = []
            while p in parent:
                stack.append(p)
                p = parent[p]
            for pos in stack:
                parent[pos] = p
            return p
        
        for idx, e in enumerate(E, 1):
            p = e
            p_final = find(p)
            stones[p_final] = idx
            parent[p_final] = p_final +1
        
        # Now, find the stone closest to G
        # Iterate through all stones and find the minimal |p - G|
        min_dist = float('inf')
        min_stone = N+1
        for p, stone in stones.items():
            dist = abs(G - p)
            if dist < min_dist or (dist == min_dist and stone < min_stone):
                min_dist = dist
                min_stone = stone
        print(f"Case #{test_case}: {min_stone} {min_dist}")