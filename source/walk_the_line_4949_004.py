import sys

def minimal_time(N, S):
    S.sort()
    total_time = 0
    i = N - 1
    while i >= 0:
        if i == 0:
            # Only one person left
            total_time += S[0]
            i -= 1
        elif i == 1:
            # Two people left
            total_time += S[0]
            i -= 2
        elif i == 2:
            # Three people left
            total_time += S[0] + S[1] + S[2]
            i -= 3
        else:
            # More than three people left
            # Strategy 1: S[0] carries S[i] and S[i-1], then S[0] returns
            strategy1 = S[i-1] + S[i] + S[0] + S[i-1]
            # Strategy 2: S[0] and S[1] carry S[i] and S[i-1], then S[1] returns
            strategy2 = S[1] + S[0] + S[i] + S[1]
            total_time += min(strategy1, strategy2)
            i -= 2
    return total_time

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for test_case in range(1, T + 1):
        N = int(data[idx])
        K = int(data[idx + 1])
        idx +=2
        S = []
        for _ in range(N):
            S.append(int(data[idx]))
            idx +=1
        total = minimal_time(N, S)
        if total <= K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()