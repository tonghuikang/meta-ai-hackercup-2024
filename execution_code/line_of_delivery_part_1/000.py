def curling_solver(test_cases):
    results = []
    
    for case_num, (N, G, energies) in enumerate(test_cases, start=1):
        positions = [0] * N
        
        # Create tuples of (energy, original_index) and sort them by energy
        indexed_energies = sorted((e, i) for i, e in enumerate(energies))
        
        current_position = 0
        
        for energy, original_index in indexed_energies:
            # Move the stone based on its energy
            if current_position < G:
                while energy > 0:
                    if current_position < G and (current_position == positions[current_position if current_position < N else N-1]):
                        # If there's a collision, the current stone stops and stays at the last position
                        positions[original_index] = current_position
                        break
                    else:
                        # Move the stone one unit right
                        current_position += 1
                        energy -= 1
                else:
                    # If energy runs out, place stone at the current position
                    positions[original_index] = current_position

        # Finding the closest stone to the goal G
        closest_distance = float('inf')
        closest_index = -1
        
        for i in range(N):
            distance = abs(positions[i] - G)
            if distance < closest_distance or (distance == closest_distance and i < closest_index):
                closest_distance = distance
                closest_index = i
        
        # Prepare the result for this test case
        results.append(f"Case #{case_num}: {closest_index + 1} {closest_distance}")
    
    return results

# Read inputs
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []

line_index = 1
for _ in range(T):
    N, G = map(int, data[line_index].split())
    line_index += 1
    energies = [int(data[line_index + i]) for i in range(N)]
    test_cases.append((N, G, energies))
    line_index += N

# Get results
results = curling_solver(test_cases)

# Print results
for result in results:
    print(result)