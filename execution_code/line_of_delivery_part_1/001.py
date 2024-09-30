def process_case(N, G, energies):
    stones = [(energies[i], i) for i in range(N)]  # (energy, index)
    stones.sort()  # Sort stones by their energy, processing from the lowest energy to highest
    positions = [0] * N  # To keep track of final positions of stones
    for energy, index in stones:
        position = positions[index]
        current_energy = energy
        # Move the stone until it hits another stationary stone or runs out of energy
        while current_energy > 0:
            # If there is no stone at the next position, the stone moves there
            if position + 1 >= len(positions) or positions[position + 1] == 0:
                position += 1
                current_energy -= 1
            else:
                # It collides with a stone at position + 1
                # Transfer the remaining energy to that stone
                collided_index = positions[position + 1]
                current_energy = (positions[collided_index] + current_energy) - (position + 1)
                break
            
        positions[index] = position  # Final position for the stone
    
    # Now we need to determine the closest stone to the goal G
    closest_index = -1
    closest_distance = float('inf')
    
    for i in range(N):
        distance = abs(positions[i] - G)
        if (distance < closest_distance) or (distance == closest_distance and i < closest_index):
            closest_distance = distance
            closest_index = i

    return closest_index + 1, closest_distance  # 1-based index

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    index = 1
    results = []

    for case_number in range(1, T + 1):
        N, G = map(int, data[index].split())
        index += 1
        energies = []
        for _ in range(N):
            energies.append(int(data[index]))
            index += 1
        
        closest_stone_index, distance = process_case(N, G, energies)
        results.append(f"Case #{case_number}: {closest_stone_index} {distance}")

    print("\n".join(results))

if __name__ == "__main__":
    main()