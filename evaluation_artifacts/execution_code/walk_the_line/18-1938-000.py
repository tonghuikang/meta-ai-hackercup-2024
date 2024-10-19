import sys

def can_cross(N, K, S):
    S.sort()
    total_time = 0
    left = N
    i = N - 1

    while left > 0:
        if left == 1:
            total_time += S[0]
            left -= 1
        elif left == 2:
            total_time += S[0]
            left -= 2
        elif left == 3:
            total_time += S[0] + S[1] + S[2]
            left -= 3
        else:
            option1 = S[1] + S[0] + S[i] + S[1]
            option2 = S[i] + S[0] + S[i-1] + S[0]
            total_time += min(option1, option2)
            left -= 2
            i -= 2

    return total_time <= K

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    ptr = 1
    for test_case in range(1, T+1):
        N, K = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        S = []
        for _ in range(N):
            S.append(int(input[ptr]))
            ptr +=1
        result = "YES" if can_cross(N, K, S) else "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()