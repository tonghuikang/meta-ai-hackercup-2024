import sys
import sys
import sys
import sys
import sys
import sys
import sys
import sys
import sys

import sys
import sys
import sys

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N, G = int(data[idx]), int(data[idx+1]); idx +=2
        E = []
        for _ in range(N):
            E.append(int(data[idx]))
            idx +=1
        parent = {}
        def find(p):
            if p not in parent:
                return p
            if parent[p] != p:
                parent[p] = find(parent[p])
            return parent[p]
        final_pos = []
        for stone_idx in range(N):
            desired_p = E[stone_idx]
            p = find(desired_p)
            final_pos.append(p)
            parent[p] = p +1
        # Now find the stone closest to G
        min_dist = None
        min_stone = None
        for stone_idx in range(N):
            dist = abs(final_pos[stone_idx] - G)
            if (min_dist is None) or (dist < min_dist) or (dist == min_dist and stone_idx+1 < min_stone):
                min_dist = dist
                min_stone = stone_idx +1
        print(f"Case #{test_case}: {min_stone} {min_dist}")

if __name__ == "__main__":
    main()