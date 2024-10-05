import sys
import threading
import bisect
import random

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    from bisect import bisect_right, insort

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N_G = sys.stdin.readline()
        while N_G.strip() == '':
            N_G = sys.stdin.readline()
        N, G = map(int, N_G.strip().split())
        E = []
        count = 0
        while count < N:
            line = sys.stdin.readline()
            if line.strip() == '':
                continue
            E.append(int(line.strip()))
            count +=1
        # Initialize sorted_positions and stones mapping
        sorted_positions = []
        stones = dict()
        final_pos = [0] * (N +1)  # 1-based indexing

        for stone_num in range(1, N+1):
            E_i = E[stone_num -1]
            moving_stone = stone_num
            energy = E_i
            pos =0
            while True:
                target_pos = pos + energy
                idx = bisect_right(sorted_positions, pos)
                if idx == len(sorted_positions):
                    # No collision
                    final_pos[moving_stone] = target_pos
                    insort(sorted_positions, target_pos)
                    stones[target_pos] = moving_stone
                    break
                else:
                    P = sorted_positions[idx]
                    if P > target_pos:
                        # No collision
                        final_pos[moving_stone] = target_pos
                        insort(sorted_positions, target_pos)
                        stones[target_pos] = moving_stone
                        break
                    else:
                        # Collision at P
                        d = P - pos
                        remaining = energy - d
                        final_pos[moving_stone] = P
                        existing_stone = stones[P]
                        # Replace the stone at P with moving_stone
                        stones[P] = moving_stone
                        # Now, existing_stone needs to be moved with remaining energy
                        moving_stone = existing_stone
                        energy = remaining
                        pos = P
        # Find the stone closest to G
        min_distance = None
        min_index = None
        for i in range(1, N+1):
            distance = abs(final_pos[i] - G)
            if min_distance is None or distance < min_distance or (distance == min_distance and i < min_index):
                min_distance = distance
                min_index = i
        print(f"Case #{test_case}: {min_index} {min_distance}")

threading.Thread(target=main,).start()