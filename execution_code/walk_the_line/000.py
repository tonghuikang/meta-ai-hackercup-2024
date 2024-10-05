def main():
    import sys

    import sys

    def readints():
        import sys
        return list(map(int, sys.stdin.read().split()))

    data = readints()
    idx =0
    T = data[idx]
    idx +=1
    for test_case in range(1, T+1):
        N, K = data[idx], data[idx+1]
        idx +=2
        S = []
        for _ in range(N):
            S.append(data[idx])
            idx +=1
        S.sort()
        total_time = 0
        left = N
        # Handle cases
        while left >2:
            option1 = 2*S[1] + S[0] + S[left-1]
            option2 = 2*S[0] + S[left-2] + S[left-1]
            total_time += min(option1, option2)
            left -=2
        if left ==1:
            total_time += S[0]
        elif left ==2:
            total_time += S[1]
        # Determine result
        if total_time <= K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()