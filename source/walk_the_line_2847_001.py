import sys

def can_cross(N, K, S):
    S.sort()
    total = 0
    left = N
    p = N -1
    while left >0:
        if left ==1:
            total += S[0]
            left -=1
        elif left ==2:
            # Fastest carries the second person
            total += S[0]
            left -=2
        elif left ==3:
            # Fastest carries the third, returns, fast carries second
            total += S[0] + S[1] + S[2]
            left -=3
        else:
            option1 = 2 * S[0] + S[p] + S[p-1]
            option2 = 2 * S[1] + S[0] + S[p]
            total += min(option1, option2)
            left -=2
            p -=2
    return total <= K

def main():
    input = sys.stdin.read().split()
    idx =0
    T = int(input[idx]); idx +=1
    for tc in range(1, T+1):
        N = int(input[idx]); K = int(input[idx+1]); idx +=2
        S = []
        for _ in range(N):
            S.append(int(input[idx]))
            idx +=1
        result = "YES" if can_cross(N, K, S) else "NO"
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()