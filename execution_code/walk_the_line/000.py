def main():
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for tc in range(1, T+1):
        N, K = int(data[idx]), int(data[idx+1]); idx +=2
        S = []
        for _ in range(N):
            S.append(int(data[idx]))
            idx +=1
        S.sort()
        total_time = 0
        m = N
        while m > 2:
            # Strategy: cross two slowest, return the slower one
            total_time += S[m-2]  # Cross two slowest
            total_time += S[m-2]  # Return the slower one
            m -=1
        if m >0:
            total_time += S[0]  # Final crossing
        if total_time <= K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()