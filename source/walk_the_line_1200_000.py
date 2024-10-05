def solve_bridge_crossing():
    import sys
    import math
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, K = map(int, sys.stdin.readline().split())
        S = []
        for _ in range(N):
            S.append(int(sys.stdin.readline()))
        S.sort()
        total_time = 0
        left = N
        i = N - 1
        while left > 0:
            if left ==1:
                total_time += S[0]
                left -=1
            elif left ==2:
                total_time += S[1]
                left -=2
            elif left ==3:
                total_time += S[0] + S[1] + S[2]
                left -=3
            else:
                option1 = 2 * S[1] + S[0] + S[i]
                option2 = 2 * S[0] + S[i-1] + S[i]
                if option1 < option2:
                    total_time += option1
                else:
                    total_time += option2
                left -=2
                i -=2
        if total_time <= K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{test_case}: {result}")

# The function can be called to execute the solution
if __name__ == "__main__":
    solve_bridge_crossing()