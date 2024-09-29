def simulate_curling(N, G, energies):
    # To store the final positions of the stones
    positions = [0] * N

    for i in range(N):
        energy = energies[i]
        pos = max(0, min(G + 1000000, energy))
        
        while pos > 0 and positions[pos - 1] != 0:
            remaining_energy = energy - (pos - (positions[pos - 1] + 1))
            if remaining_energy < 0:
                break
            energy = remaining_energy
            pos -= 1
            
        positions[pos] = energy
    
    # Final positions after handling collisions
    final_positions = []
    for i in range(N):
        if positions[i] > 0:
            final_positions.append((i + 1, i))  # Store stone index (1-based) and its position

    # Extract positions
    final_positions = sorted(final_positions, key=lambda x: (abs(G - x[1]), x[0]))
    
    # Find the closest stone
    closest_stone_index = final_positions[0][0]
    distance_to_G = abs(G - final_positions[0][1])
    
    return closest_stone_index, distance_to_G


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    index = 1
    results = []
    
    for t in range(1, T + 1):
        N, G = map(int, data[index].split())
        index += 1
        
        energies = []
        for _ in range(N):
            energy = int(data[index])
            energies.append(energy)
            index += 1
        
        closest_stone_index, distance_to_G = simulate_curling(N, G, energies)
        results.append(f"Case #{t}: {closest_stone_index} {distance_to_G}")
    
    # Print all results
    print("\n".join(results))


if __name__ == "__main__":
    main()