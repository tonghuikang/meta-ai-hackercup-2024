import sys
import sys
import sys

import sys
def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    from sys import stdin
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx +=1
    for tc in range(1, T+1):
        N, G = int(input[idx]), int(input[idx+1]); idx +=2
        E = []
        for _ in range(N):
            E.append(int(input[idx]))
            idx +=1
        pos = [0]*(N+1)
        stack = []
        for i in range(1, N+1):
            E_i = E[i-1]
            while stack and E_i > pos[stack[-1]]:
                j = stack.pop()
                remaining_E = E_i - pos[j]
                pos[j] += remaining_E
                E_i = pos[j]
            pos[i] = E_i
            stack.append(i)
        # Now, find the closest stone to G
        min_dist = float('inf')
        min_idx = -1
        for i in range(1, N+1):
            dist = abs(pos[i] - G)
            if dist < min_dist or (dist == min_dist and i < min_idx):
                min_dist = dist
                min_idx = i
        print(f"Case #{tc}: {min_idx} {min_dist}")

if __name__ == "__main__":
    main()