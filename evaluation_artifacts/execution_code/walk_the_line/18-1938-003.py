def solve_bridge_crossing():
    import sys

    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        N, K = map(int, sys.stdin.readline().split())
        S = [int(sys.stdin.readline()) for _ in range(N)]
        S.sort()
        total_time = 0
        i = N
        while i > 0:
            if i == 1:
                total_time += S[0]
                i -= 1
            elif i == 2:
                total_time += S[1]
                i -= 2
            elif i == 3:
                total_time += S[0] + S[1] + S[2]
                i -= 3
            else:
                # Two strategies
                option1 = 2 * S[0] + S[i-2] + S[i-1]
                option2 = S[1] + S[0] + S[i-1] + S[1]
                total_time += min(option1, option2)
                i -= 2
        if total_time <= K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{case}: {result}")

if __name__ == "__main__":
    solve_bridge_crossing()