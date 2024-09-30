def can_cross(N, K, S):
    # Special case: If there's only one traveler
    if N == 1:
        return S[0] <= K

    # Sort the times to make strategy easier
    S.sort()
    
    total_time = 0
    left = N  # Number of travelers still to cross

    # If the number of travelers is more than 2, we need to use a strategy
    while left > 3:
        # Time to cross for the two slowest and return for the fastest
        option1 = S[1] + S[0] + S[left - 1] + S[1]  # 2 slowest cross + fastest returns
        option2 = S[left - 1] + S[left - 2] + 2 * S[0]  # Slowest cross + 2 fastes return
        total_time += min(option1, option2)
        
        # After two go, reduce the number of travelers left by 2
        left -= 2

    # Handle the last three or fewer cases directly
    if left == 3:
        total_time += S[2] + S[1] + S[0]  # All three cross, the fastest will return
    elif left == 2:
        total_time += S[1]  # Just the second fastest crosses
    elif left == 1:
        total_time += S[0]  # The only traveler crosses

    return total_time <= K


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    index = 1
    results = []
    
    for i in range(1, T + 1):
        N, K = map(int, data[index].split())
        index += 1
        
        S = []
        for j in range(N):
            S.append(int(data[index]))
            index += 1
        
        # Check if they can cross within K seconds
        if can_cross(N, K, S):
            results.append(f"Case #{i}: YES")
        else:
            results.append(f"Case #{i}: NO")

    print("\n".join(results))


if __name__ == "__main__":
    main()