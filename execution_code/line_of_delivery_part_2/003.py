def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    
    from sys import stdin
    import sys

    def find_next_free(p, parent):
        while p != parent[p]:
            parent[p] = parent[parent[p]]  # Path compression
            p = parent[p]
        return p

    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        G = int(data[idx]); idx +=1
        E = []
        for _ in range(N):
            E_i = int(data[idx]); idx +=1
            E.append(E_i)
        
        # Initialize parent and position to stone mapping
        parent = list(range(G + 2))  # parent[p] = p initially
        pos_to_stone = [-1] * (G + 2)  # -1 indicates free
        final_pos = [0] * (N + 1)  # final_pos[stone] = position

        for i in range(1, N+1):
            stone_idx = i
            energy = E[i-1]
            p = 0
            while True:
                desired_p = p + energy
                if desired_p > G:
                    desired_p = G
                free_p = find_next_free(desired_p, parent)

                if free_p <= G and pos_to_stone[free_p] != -1:
                    # Position is occupied, need to transfer energy
                    existing_stone = pos_to_stone[free_p]
                    rem_energy = energy - (free_p - p)

                    # Assign current stone to free_p -1
                    new_p = free_p -1
                    pos_to_stone[new_p] = stone_idx
                    final_pos[stone_idx] = new_p

                    # Update parent for the new position
                    parent[new_p] = find_next_free(new_p +1, parent)

                    # Now, the existing stone needs to be moved with remaining energy
                    stone_idx = existing_stone
                    energy = rem_energy
                else:
                    # Assign stone to free_p
                    pos_to_stone[free_p] = stone_idx
                    final_pos[stone_idx] = free_p

                    # Update parent for the assigned position
                    parent[free_p] = find_next_free(free_p +1, parent)
                    break
        
        # Determine the stone closest to G
        min_distance = G +1
        min_stone = N +1
        for i in range(1, N+1):
            distance = abs(final_pos[i] - G)
            if distance < min_distance or (distance == min_distance and i < min_stone):
                min_distance = distance
                min_stone = i

        print(f"Case #{test_case}: {min_stone} {min_distance}")

if __name__ == "__main__":
    main()