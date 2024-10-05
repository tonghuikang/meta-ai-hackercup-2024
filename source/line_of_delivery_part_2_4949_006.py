import sys
import sys
import sys
import sys
import sys
def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    from sys import stdin
    input = stdin.read().split()
    idx = 0
    T = int(input[idx]); idx +=1
    for ttt in range(1, T+1):
        N, G = int(input[idx]), int(input[idx+1]); idx +=2
        E = []
        for _ in range(N):
            E.append(int(input[idx]))
            idx +=1
        # Initialize DSU
        parent = {}
        pos = {}
        stone_at = {}
        def find(p):
            if p not in parent:
                return p
            parent[p] = find(parent[p])
            return parent[p]
        # Process stones in order
        for i in range(N):
            stone = i+1
            energy = E[i]
            # Start from position 0
            current_pos = 0
            remaining_energy = energy
            while remaining_energy >0:
                next_pos = current_pos + remaining_energy
                # Find the first occupied position >= current_pos +1
                # We need to find the furthest position we can reach
                # Using DSU to find the next available position
                target = find(current_pos +1)
                if target > next_pos:
                    # Can move to next_pos without collision
                    current_pos = next_pos
                    remaining_energy =0
                else:
                    # Collision at target
                    # Move to target -1
                    if target -1 >= current_pos:
                        move = target -1 - current_pos
                        current_pos += move
                        remaining_energy -= move
                    else:
                        # Can't move forward
                        pass
                    # Now at current_pos, collision at target
                    remaining_energy -=1
                    # Transfer remaining_energy to stone at target
                    if target in stone_at:
                        collided_stone = stone_at[target]
                        # Now, the collided stone needs to move with remaining_energy
                        # Recursively process the collided stone
                        # To prevent deep recursion, use iteration
                        stack = [(collided_stone, remaining_energy)]
                        remaining_energy =0
                        while stack:
                            s, e_remain = stack.pop()
                            # Find current position of stone s
                            s_pos = pos[s]
                            # Stone s is at s_pos, needs to move with energy e_remain
                            new_energy = e_remain
                            current_s_pos = s_pos
                            current_e = new_energy
                            while current_e >0:
                                target_s = find(current_s_pos +1)
                                next_target = current_s_pos + current_e
                                if target_s > next_target:
                                    # Can move to next_target
                                    pos[s] = next_target
                                    # Update DSU
                                    parent[next_target] = next_target +1
                                    # Remove stone from old position
                                    del stone_at[current_s_pos]
                                    # Place stone at new position
                                    stone_at[next_target] = s
                                    current_e =0
                                else:
                                    # Collision at target_s
                                    move_s = target_s -1 - current_s_pos
                                    if move_s >=0:
                                        current_s_pos += move_s
                                        current_e -= move_s
                                    # Now, at current_s_pos, collision at target_s
                                    current_e -=1
                                    # Transfer remaining energy to stone at target_s
                                    if target_s in stone_at:
                                        s_collide = stone_at[target_s]
                                        stack.append((s_collide, current_e))
                                    # Stone s stops at current_s_pos
                                    pos[s] = current_s_pos
                                    stone_at[current_s_pos] = s
                                    # Update DSU
                                    parent[current_s_pos] = current_s_pos +1
                                    current_e =0
                    # Stone stops at current_pos
                    pos[stone] = current_pos
                    stone_at[current_pos] = stone
                    # Update DSU
                    parent[current_pos] = current_pos +1
                    remaining_energy =0
        # After all stones, find the stone closest to G
        min_distance = float('inf')
        min_stone = N+1
        for s in range(1, N+1):
            distance = abs(G - pos[s])
            if distance < min_distance or (distance == min_distance and s < min_stone):
                min_distance = distance
                min_stone = s
        print(f"Case #{ttt}: {min_stone} {min_distance}")

if __name__ == "__main__":
    main()