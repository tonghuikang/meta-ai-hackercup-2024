def solve_bridge_crossing():
    import sys
    import math

    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N,K = map(int, sys.stdin.readline().split())
        S = []
        for _ in range(N):
            S.append(int(sys.stdin.readline()))
        S.sort()
        total_time =0
        p = N-1
        while p >=3:
            # Option1: S1 and S2 cross, S1 returns, SN-1 and SN cross, S2 returns
            option1 = 2*S[1] + S[0] + S[p]
            # Option2: S1 and SN cross, S1 returns, S1 and SN-1 cross, S1 returns
            option2 = 2*S[0] + S[p-1] + S[p]
            total_time += min(option1, option2)
            p -=2
        if p ==2:
            total_time += S[0] + S[1] + S[2]
        elif p ==1:
            total_time += S[1]
        elif p ==0:
            total_time += S[0]
        if total_time <= K:
            print(f"Case #{tc}: YES")
        else:
            print(f"Case #{tc}: NO")