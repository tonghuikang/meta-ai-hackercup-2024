import sys
import threading
import bisect

def main():
    import sys
    import bisect
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N, G = map(int, sys.stdin.readline().split())
        E_list = []
        for _ in range(N):
            E = int(sys.stdin.readline())
            E_list.append(E)
        stationary_positions = []
        position_to_stone_index = dict()
        final_position = dict()

        for stone_index, energy in enumerate(E_list, start=1):
            moving_stone_index = stone_index
            moving_energy = energy
            moving_position = 0
            while moving_energy > 0:
                # Find the next collision position
                idx = bisect.bisect_right(stationary_positions, moving_position)
                if idx == len(stationary_positions):
                    # No stationary stones ahead
                    moving_position += moving_energy
                    moving_energy = 0
                    # Record final position
                    final_position[moving_stone_index] = moving_position
                    # Add to stationary stones
                    bisect.insort(stationary_positions, moving_position)
                    position_to_stone_index[moving_position] = moving_stone_index
                    break
                else:
                    next_stationary_pos = stationary_positions[idx]
                    distance_to_next_stationary = next_stationary_pos - moving_position - 1
                    if moving_energy <= distance_to_next_stationary:
                        moving_position += moving_energy
                        moving_energy = 0
                        # Record final position
                        final_position[moving_stone_index] = moving_position
                        # Add to stationary stones
                        bisect.insort(stationary_positions, moving_position)
                        position_to_stone_index[moving_position] = moving_stone_index
                        break
                    else:
                        # Move to just before the collision
                        moving_position += distance_to_next_stationary + 1
                        moving_energy -= distance_to_next_stationary + 1
                        # Collision happens at moving_position
                        # Record final position of moving stone
                        final_position[moving_stone_index] = moving_position
                        # Add moving stone to stationary stones
                        bisect.insort(stationary_positions, moving_position)
                        position_to_stone_index[moving_position] = moving_stone_index
                        # The stationary stone becomes moving
                        stationary_stone_index = position_to_stone_index.pop(moving_position)
                        # Remove from stationary positions
                        stationary_positions.pop(idx)  # Remove the stationary stone
                        # Set the new moving stone index
                        moving_stone_index = stationary_stone_index
                        # moving_position remains the same
                        # Continue the loop with updated moving_stone_index and moving_energy
                        continue
        # After processing all stones, compute distances to G
        min_distance = None
        min_stone_index = None
        for stone_index in range(1, N +1):
            position = final_position[stone_index]
            distance = abs(position - G)
            if min_distance is None or distance < min_distance or \
                (distance == min_distance and stone_index < min_stone_index):
                min_distance = distance
                min_stone_index = stone_index
        print(f"Case #{case_num}: {min_stone_index} {min_distance}")
        
threading.Thread(target=main).start()