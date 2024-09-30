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
    for tc in range(1, T+1):
        N = int(data[idx]); G = int(data[idx+1]); idx +=2
        E = []
        for _ in range(N):
            E.append(int(data[idx]))
            idx +=1

        parent = {}
        final_pos = [0] * N
        pos_to_stone = {}
        
        def find(p):
            if p not in parent:
                return p
            parent[p] = find(parent[p])
            return parent[p]
        
        for i in range(N):
            desired_p = E[i]
            p = find(desired_p)
            final_pos[i] = p
            pos_to_stone[p] = i+1  # stone indices are 1-based
            parent[p] = find(p +1)
        
        # Now find the stone closest to G
        min_distance = None
        chosen_stone = None
        for i in range(N):
            distance = abs(final_pos[i] - G)
            if (min_distance is None) or (distance < min_distance) or (distance == min_distance and (i+1) < chosen_stone):
                min_distance = distance
                chosen_stone = i+1
        print(f"Case #{tc}: {chosen_stone} {min_distance}")

if __name__ == "__main__":
    main()