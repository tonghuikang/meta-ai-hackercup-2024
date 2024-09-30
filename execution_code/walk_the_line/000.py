def can_cross_bridge(travelers, K):
    N = len(travelers)
    if N == 0:
        return True
    
    travelers.sort()
    
    total_time = 0
    while N > 3:
        # Two strategies to consider:
        
        # Strategy 1: Two slowest cross, one returns, then the two fastest cross, the fastest returns
        time1 = travelers[N-1] + travelers[N-2] + 2 * travelers[0]
        
        # Strategy 2: Two fastest cross, one returns, then the two slowest cross, one fastest returns
        time2 = travelers[1] + travelers[0] + travelers[N-1] + travelers[N-2]
        
        # Choose the minimum of the two strategies
        total_time += min(time1, time2)
        N -= 2  # 2 travelers crossed

    # Handle the last 2 or 3 travelers
    if N == 3:
        total_time += travelers[2] + travelers[1] + travelers[0]  # Group of 3
    elif N == 2:
        total_time += travelers[1]  # Group of 2
    elif N == 1:
        total_time += travelers[0]  # Single traveler
    
    return total_time <= K

def bridge_problem(test_cases):
    results = []
    for case_number in range(1, len(test_cases) + 1):
        N, K, travelers = test_cases[case_number - 1]
        if can_cross_bridge(travelers, K):
            results.append(f"Case #{case_number}: YES")
        else:
            results.append(f"Case #{case_number}: NO")
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []
index = 1

for _ in range(T):
    N, K = map(int, data[index].split())
    travelers = [int(data[i]) for i in range(index + 1, index + 1 + N)]
    test_cases.append((N, K, travelers))
    index += N + 1

# Solve the bridge problem
results = bridge_problem(test_cases)

# Output results
for result in results:
    print(result)