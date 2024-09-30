def bridge_crossing():
    import sys

    import sys

    def input():
        return sys.stdin.read()

    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N, K = int(data[idx]), int(data[idx+1]); idx +=2
        S = []
        for _ in range(N):
            S.append(int(data[idx]))
            idx +=1
        S.sort()
        total =0
        i =N
        while i >0:
            if i ==1:
                total += S[0]
                i -=1
            elif i ==2:
                total += S[0]
                i -=2
            elif i ==3:
                # Two crossings: S[1] + S[1] + S[0]
                total += S[1] + S[1] + S[0]
                i -=2
            else:
                option1 = 2 * S[1] + S[i-2] + S[i-1]
                option2 = 2 * S[i-2] + S[1] + S[i-1]
                total += min(option1, option2)
                i -=2
        if total <= K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    bridge_crossing()