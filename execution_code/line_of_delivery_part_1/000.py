def curling_game(T, test_cases):
    results = []
    
    for case_index in range(T):
        N, G = test_cases[case_index][0]
        energies = test_cases[case_index][1]
        
        # List that will hold the final positions of the stones
        positions = [0] * N
        
        # List to track the stones in terms of (energy, index)
        # Sort by energy, as no two energies are the same
        stone_energy_index = sorted(((energies[i], i) for i in range(N)), reverse=True)
        
        pos = 0  # This represents the absolute position of the stone being moved
        for energy, index in stone_energy_index:
            # Assign the new position either to the next free spot
            # or to the position where it's being blocked by a previous stone
            if pos < energy:
                positions[index] = energy
                pos = energy
            else:
                # If the position is occupied, move forward one unit at a time until we can place the stone
                positions[index] = pos + 1
                pos += 1
                
        # Determine the closest stone to the goal
        closest_index = -1
        closest_distance = float('inf')
        
        for i in range(N):
            distance_to_goal = abs(positions[i] - G)
            if (distance_to_goal < closest_distance) or (
                distance_to_goal == closest_distance and (closest_index == -1 or i < closest_index)):
                closest_distance = distance_to_goal
                closest_index = i
        
        # Store the result for this test case in 1-indexed format
        results.append(f"Case #{case_index + 1}: {closest_index + 1} {closest_distance}")
    
    return results

# Reading input
import sys

input_data = sys.stdin.read().strip().splitlines()
T = int(input_data[0])
test_cases = []

index = 1
for _ in range(T):
    N, G = map(int, input_data[index].split())
    energies = [int(input_data[index + i + 1]) for i in range(N)]
    test_cases.append(((N, G), energies))
    index += N + 1

# Running the game logic
results = curling_game(T, test_cases)

# Outputting the results
for result in results:
    print(result)