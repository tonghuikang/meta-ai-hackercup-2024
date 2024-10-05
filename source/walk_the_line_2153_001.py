import sys

def compute_min_time(S, N):
    S.sort()
    total = 0
    while N > 0:
        if N == 1:
            total += S[0]
            break
        elif N == 2:
            total += S[0]
            break
        elif N == 3:
            total += S[0] + S[0] + S[2]
            break
        else:
            # Option1: Two fastest go with carrier S[0]
            option1 = 2 * S[0] + S[N-2] + S[N-1]
            # Option2: Fastest and second fastest go first
            option2 = 2 * S[0] + S[1] + S[N-1]
            total += min(option1, option2)
            N -= 2
    return total

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for test_case in range(1, T+1):
        N, K = int(input[idx]), int(input[idx+1])
        idx +=2
        S = []
        for _ in range(N):
            S.append(int(input[idx]))
            idx +=1
        min_time = compute_min_time(S, N)
        result = "YES" if min_time <= K else "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()