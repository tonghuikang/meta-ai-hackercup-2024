import sys
import bisect

def solve():
    import sys, bisect
    from sys import stdin
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx +=1
    for tc in range(1, T+1):
        N, G = int(data[idx]), int(data[idx+1])
        idx +=2
        E = [0]*(N+1)
        for i in range(1, N+1):
            E[i] = int(data[idx])
            idx +=1
        sorted_p = []
        pos_to_stone_id = {}
        stone_final_pos = [0]*(N+1)
        for stone_id in range(1, N+1):
            stack = [ (stone_id, 0, E[stone_id]) ]
            while stack:
                current_id, pos, energy = stack.pop()
                if energy <=0:
                    continue
                target_pos = pos + energy
                # Find first p > pos
                # bisect_right returns the insertion point which is after pos
                idx_p = bisect.bisect_right(sorted_p, pos)
                if idx_p < len(sorted_p) and sorted_p[idx_p] <= target_pos:
                    p_found = sorted_p[idx_p]
                    stone_final_pos[current_id] = p_found
                    old_id = pos_to_stone_id[p_found]
                    pos_to_stone_id[p_found] = current_id
                    remaining_energy = energy - (p_found - pos)
                    stack.append( (old_id, p_found, remaining_energy) )
                else:
                    # No collision
                    stone_final_pos[current_id] = target_pos
                    bisect.insort(sorted_p, target_pos)
                    pos_to_stone_id[target_pos] = current_id
        # Now find the stone closest to G
        min_dist = None
        min_id = None
        for stone_id in range(1, N+1):
            pos = stone_final_pos[stone_id]
            dist = abs(pos - G)
            if (min_dist is None) or (dist < min_dist) or (dist == min_dist and stone_id < min_id):
                min_dist = dist
                min_id = stone_id
        print(f"Case #{tc}: {min_id} {min_dist}")

# To execute the solve function, uncomment the following line:
# solve()