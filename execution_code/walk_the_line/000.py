def can_cross_in_time(travelers, K):
    N = len(travelers)
    travelers.sort()

    total_time = 0
    while N > 3:
        # Option 1 - send the two fastest and bring one back (i.e., send 0 and 1, bring back 0)
        time1 = 2 * travelers[1] + travelers[0] + travelers[N - 1]
        # Option 2 - send the two slowest and bring the fastest back (i.e., send N-2 and N-1, bring back 1)
        time2 = 2 * travelers[0] + travelers[N - 2] + travelers[N - 1]

        # Choose the minimum time option
        total_time += min(time1, time2)
        N -= 2

    if N == 3:
        total_time += travelers[2] + travelers[1] + travelers[0]
    elif N == 2:
        total_time += travelers[1]
    elif N == 1:
        total_time += travelers[0]

    return total_time <= K

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    index = 1
    results = []
    for t in range(1, T + 1):
        N, K = map(int, data[index].split())
        index += 1
        travelers = []
        for i in range(N):
            travelers.append(int(data[index]))
            index += 1

        if can_cross_in_time(travelers, K):
            results.append(f"Case #{t}: YES")
        else:
            results.append(f"Case #{t}: NO")
    
    # Print all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()