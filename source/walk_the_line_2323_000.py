# Python code to solve the bridge crossing problem

def solve_bridge_crossing():
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
        S.sort()
        total_time =0
        i = N-1
        while i >=0:
            if i ==0:
                # Only one person left
                total_time += S[0]
                i -=1
            elif i ==1:
                # Two people left
                total_time += S[0]
                i -=2
            elif i ==2:
                # Three people left
                total_time += S[0] + S[1] + S[2]
                i -=3
            else:
                # More than three people left
                option1 = 2 * S[0] + S[i-1] + S[i]
                option2 = 2 * S[1] + S[0] + S[i]
                total_time += min(option1, option2)
                i -=2
        if total_time <=K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{test_case}: {result}")

# Run the function
if __name__ == "__main__":
    solve_bridge_crossing()