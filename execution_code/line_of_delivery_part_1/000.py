def simulate_stones(N, G, energies):
    # Create a list of tuples (energy, index) to store the original indices
    stones = [(energies[i], i + 1) for i in range(N)]  # (Energy, 1-indexed position)
    
    # Sort stones by energy descending, so we process the strongest first
    stones.sort(reverse=True, key=lambda x: x[0])

    positions = [0] * N  # Where each stone ends up
    for energy, idx in stones:
        # Start at position 0
        position = 0
        remaining_energy = energy
        
        while remaining_energy > 0:
            if position < N and positions[position] == 0:
                # No stone at this position: move forward
                positions[position] = idx
                break
            elif position < N and positions[position] != 0:
                # Collision: transfer energy
                remaining_energy -= 1  # moving to the occupied site
                position += 1
            else:
                # If we are at a point beyond existing stones, can place the stone
                positions.append(idx)  # Appends if it's out of the current dynamic range
                break

    # Find the stone closest to the goal G
    closest_stone_index = -1
    closest_distance = float('inf')

    for i in range(N):
        stone_position = positions[i]
        distance_to_goal = abs(G - stone_position)

        if distance_to_goal < closest_distance:
            closest_distance = distance_to_goal
            closest_stone_index = i + 1  # 1-based index
        elif distance_to_goal == closest_distance:
            if i + 1 < closest_stone_index:
                closest_stone_index = i + 1

    return closest_stone_index, closest_distance


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
        energies = [int(data[index + i]) for i in range(N)]
        index += N
        
        closest_stone_index, closest_distance = simulate_stones(N, G, energies)
        results.append(f"Case #{case_number}: {closest_stone_index} {closest_distance}")

    print("\n".join(results))


if __name__ == "__main__":
    main()