import sys
import bisect
from collections import deque

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx +=1
    for test_case in range(1, T+1):
        N, G = int(data[idx]), int(data[idx+1])
        idx +=2
        E = []
        for _ in range(N):
            E.append(int(data[idx]))
            idx +=1
        # Initialize
        occupied = []
        pos_to_index = {}
        for stone in range(1, N+1):
            queue = deque()
            queue.append( (stone, 0, E[stone-1]) )
            while queue:
                i, p, E_i = queue.popleft()
                p_max = p + E_i
                # Find first occupied position >= p+1
                ind = bisect.bisect_left(occupied, p +1)
                if ind < len(occupied) and occupied[ind] <= p_max:
                    p_occ = occupied[ind]
                    p_final = p_occ -1
                    E_rem = E_i - (p_final - p)
                    # Place current stone at p_final
                    if p_final not in pos_to_index:
                        bisect.insort(occupied, p_final)
                        pos_to_index[p_final] = i
                    else:
                        # Already occupied, but according to problem, E_i >=N so no overlap here
                        pass
                    # Remove p_occ from occupied and pos_to_index
                    occupied.pop(ind)
                    j = pos_to_index.pop(p_occ)
                    # Transfer E_rem to stone j at position p_occ
                    queue.append( (j, p_occ, E_rem) )
                else:
                    p_final = p_max
                    if p_final not in pos_to_index:
                        bisect.insort(occupied, p_final)
                        pos_to_index[p_final] = i
                    # Else, already occupied, do nothing as E_i >= N ensures no pile-up near 0
        # Now, collect stone positions
        stone_positions = [0]*(N+1)  # 1-based
        for p, i in pos_to_index.items():
            stone_positions[i] = p
        # Find the stone closest to G
        min_dist = None
        min_index = None
        for i in range(1, N+1):
            p_i = stone_positions[i]
            dist = abs(p_i - G)
            if min_dist is None or dist < min_dist or (dist == min_dist and i < min_index):
                min_dist = dist
                min_index = i
        print(f"Case #{test_case}: {min_index} {min_dist}")

if __name__ == "__main__":
    main()