def bridge_crossing():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for tc in range(1, T+1):
        N = int(data[idx]); K = int(data[idx+1]); idx +=2
        S = []
        for _ in range(N):
            S.append(int(data[idx]))
            idx +=1
        S.sort()
        total_time =0
        n = N
        while n >0:
            if n ==1:
                total_time += S[0]
                n -=1
            elif n ==2:
                total_time += S[0]
                n -=2
            elif n ==3:
                # Minimal strategy: 3 * S1
                total_time += 3 * S[0]
                n -=3
            else:
                option1 = S[0] + 2 * S[1] + S[n-1]
                option2 = 2 * S[0] + S[n-2] + S[n-1]
                total_time += min(option1, option2)
                n -=2
        if total_time <= K:
            print(f"Case #{tc}: YES")
        else:
            print(f"Case #{tc}: NO")

if __name__ == "__main__":
    bridge_crossing()