def curling_simulation(test_cases):
    results = []
    
    for case_index in range(len(test_cases)):
        N, G, energies = test_cases[case_index]
        
        # Positions of stones after all have been thrown
        positions = [0] * N
        
        for i in range(N):
            energy = energies[i]
            pos = 0
            
            while energy > 0:
                if pos + 1 < N and positions[pos + 1] > pos + 1:
                    # We have a stone at pos+1
                    positions[pos] = pos
                    energy -= (positions[pos + 1] - pos - 1)
                    pos += 1
                    continue
                elif pos < energy:
                    pos += 1
                    energy -= 1
                else:
                    break
            
            positions[i] = pos
            
            # If the stone stopped and there's energy left to transfer
            for j in range(i + 1, N):
                if positions[j - 1] + 1 == positions[j]:
                    positions[j] = positions[j - 1] + 1
                else:
                    break
        
        # Find the stone closest to the goal
        closest_stone_index = -1
        closest_distance = float('inf')
        
        for i in range(N):
            distance = abs(positions[i] - G)
            if distance < closest_distance:
                closest_distance = distance
                closest_stone_index = i
            elif distance == closest_distance:
                closest_stone_index = min(closest_stone_index, i)

        results.append(f"Case #{case_index + 1}: {closest_stone_index + 1} {closest_distance}")

    return results


def main():
    import sys
    input = sys.stdin.read
    
    # Read input
    data = input().strip().splitlines()
    T = int(data[0])
    test_cases = []
    
    index = 1
    for _ in range(T):
        N, G = map(int, data[index].split())
        index += 1
        energies = []
        
        for _ in range(N):
            energies.append(int(data[index]))
            index += 1
        
        test_cases.append((N, G, energies))
    
    # Solve the cases
    results = curling_simulation(test_cases)
    
    # Output the results
    for result in results:
        print(result)


if __name__ == "__main__":
    main()