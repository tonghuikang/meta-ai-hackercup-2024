def can_cross(N, K, S):
    S.sort()
    
    # If only one traveler, just check their individual time
    if N == 1:
        return S[0] <= K
    
    total_time = 0

    # A function to compute the time for the two slowest individuals using the wheelbarrow method
    def two_pair_cross_time(s1, s2):
        return max(s1, s2) + min(s1, s2)  # Total time for the round trip (one carrying the other)

    # While more than 3 travelers remain on the starting side
    while N > 3:
        option1 = 2 * S[1] + S[0] + S[N - 1]  # 2nd fastest returns
        option2 = 2 * S[0] + S[N - 2] + S[N - 1]  # Fastest returns
        total_time += min(option1, option2)
        N -= 2  # Two travelers successfully crossed

    # Handle the last 3 or fewer travelers
    if N == 3:
        total_time += S[2] + S[1] + S[0]  # All three cross together with round trip
    elif N == 2:
        total_time += S[1]  # Just two cross
    elif N == 1:
        total_time += S[0]  # Just one crosses

    return total_time <= K

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    results = []

    index = 1
    for t in range(1, T + 1):
        N, K = map(int, data[index].split())
        S = [int(data[index + i + 1]) for i in range(N)]
        index += N + 1
        
        if can_cross(N, K, S):
            results.append(f"Case #{t}: YES")
        else:
            results.append(f"Case #{t}: NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()