import sys

def can_cross_all(S, N, K):
    S.sort()
    total_time = 0
    left = N
    while left > 0:
        if left == 1:
            total_time += S[0]
            left -=1
        elif left ==2:
            total_time += S[0]
            left -=2
        elif left ==3:
            total_time += S[0] + S[1] + S[2]
            left -=3
        else:
            option1 = 2*S[1] + S[0] + S[left-1]
            option2 = S[left-1] + S[0] + S[left-2] + S[0]
            total_time += min(option1, option2)
            left -=2
    return total_time <= K

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for case in range(1, T+1):
        N = int(input[idx])
        K = int(input[idx+1])
        idx +=2
        S = []
        for _ in range(N):
            S.append(int(input[idx]))
            idx +=1
        if can_cross_all(S, N, K):
            print(f"Case #{case}: YES")
        else:
            print(f"Case #{case}: NO")

if __name__ == "__main__":
    main()