# Python code to solve the bridge crossing problem

def compute_min_time(S, N):
    S.sort()
    total = 0
    i = N - 1
    while i >= 3:
        # Option 1: Fastest and second fastest escort the two slowest
        option1 = 2 * S[1] + S[0] + S[i]
        # Option 2: Fastest escorts the slowest, then escorts the second slowest
        option2 = 2 * S[0] + S[i - 1] + S[i]
        total += min(option1, option2)
        i -= 2
    if i == 2:
        total += S[0] + S[1] + S[2]
    elif i == 1:
        total += S[1]
    elif i == 0:
        total += S[0]
    return total

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx +=1
    for test_case in range(1, T+1):
        N, K = map(int, data[idx:idx+2])
        idx +=2
        S = []
        for _ in range(N):
            S.append(int(data[idx]))
            idx +=1
        total_time = compute_min_time(S, N)
        result = "YES" if total_time <= K else "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()