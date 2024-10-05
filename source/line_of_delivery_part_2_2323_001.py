import sys
import threading

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
        
        pos = dict()  # position -> stone index
        # To keep track of each stone's final position
        stone_pos = [0]*(N+1)  # stone_pos[stone_index] = position

        for stone_idx in range(1, N +1):
            E_i = E[stone_idx -1]
            p_max = E_i
            # Assign the stone to p_max, handling collisions
            stack = [(p_max, E_i, stone_idx)]
            while stack:
                p, E_current, s = stack.pop()
                if p not in pos:
                    pos[p] = s
                    stone_pos[s] = p
                else:
                    existing_s = pos[p]
                    pos[p] = s
                    stone_pos[s] = p
                    # Calculate remaining energy after reaching p
                    # Since all stones start from 0, steps taken to reach p is p
                    E_new = E_current - p
                    if E_new >0:
                        p_new = p + E_new
                        stack.append((p_new, E_new, existing_s))
                    else:
                        # If no remaining energy, existing stone cannot move
                        # It becomes stationary at p
                        stone_pos[existing_s] = p
        # After all assignments, find the stone closest to G
        min_distance = float('inf')
        chosen_stone = -1
        for stone_idx in range(1, N +1):
            distance = abs(stone_pos[stone_idx] - G)
            if distance < min_distance or (distance == min_distance and stone_idx < chosen_stone):
                min_distance = distance
                chosen_stone = stone_idx
        print(f"Case #{test_case}: {chosen_stone} {min_distance}")

threading.Thread(target=main).start()