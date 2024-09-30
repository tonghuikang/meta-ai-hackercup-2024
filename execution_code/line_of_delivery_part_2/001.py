def curling_game(test_cases):
    results = []
    
    for case_number, (N, G, energies) in enumerate(test_cases):
        positions = [0] * N  # to track final positions
        
        for i in range(N):
            energy = energies[i]
            pos = 0
            
            while energy > 0 and pos < N:
                if pos < N - 1 and positions[pos + 1] == 0:  # There is space to collide
                    pos += 1  # Move to the next position
                    energy -= 1
                elif pos < N - 1 and positions[pos + 1] > 0:  # There is a stone at the next position
                    transfer_energy = min(energy, N - positions[pos])  # Energy can be transferred
                    energy -= transfer_energy
                    positions[pos + 1] += transfer_energy
                    if energy > 0:  # If energy is left, the stone stops here
                        break
                else:
                    break  # No movement can be made anymore
            
            positions[pos] += 1  # Place the stone here
        
        # Calculating the closest stone to G and its distance
        closest_index = -1
        closest_distance = float('inf')

        for idx in range(N):
            if positions[idx] > 0:  # If there's a stone here
                distance_to_goal = abs(G - idx)
                if distance_to_goal < closest_distance:
                    closest_distance = distance_to_goal
                    closest_index = idx
                elif distance_to_goal == closest_distance:
                    if idx < closest_index:  # In case of tie by index
                        closest_index = idx
        
        results.append(f"Case #{case_number + 1}: {closest_index + 1} {closest_distance}")
    
    return results


# Input reading
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    T = int(data[0])
    idx = 1
    test_cases = []
    
    for _ in range(T):
        N, G = map(int, data[idx].split())
        idx += 1
        energies = []
        for __ in range(N):
            energies.append(int(data[idx]))
            idx += 1
        test_cases.append((N, G, energies))
    
    results = curling_game(test_cases)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()