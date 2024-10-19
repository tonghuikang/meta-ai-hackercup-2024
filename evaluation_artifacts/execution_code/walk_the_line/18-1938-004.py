import sys

def can_cross_within_k(N, K, S):
    S.sort()
    total_time = 0
    left = N
    # If only one or two people
    if N == 1:
        total_time = S[0]
    elif N == 2:
        total_time = S[1]
    else:
        while left > 3:
            option1 = S[1] + S[0] + S[left-1] + S[1]
            option2 = S[left-1] + S[0] + S[left-2] + S[0]
            total_time += min(option1, option2)
            left -= 2
        if left == 3:
            total_time += S[0] + S[1] + S[2]
        elif left == 2:
            total_time += S[1]
        else: # left ==1
            total_time += S[0]
    return total_time <= K

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx +=1
    for test_case in range(1, T+1):
        N, K = int(input[idx]), int(input[idx+1]); idx +=2
        S = []
        for _ in range(N):
            S.append(int(input[idx]))
            idx +=1
        result = "YES" if can_cross_within_k(N, K, S) else "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()