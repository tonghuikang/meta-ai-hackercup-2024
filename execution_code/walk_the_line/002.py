import sys

def minimal_crossing_time(sorted_s, N):
    total_time = 0
    s1 = sorted_s[0]
    s2 = sorted_s[1] if N >=2 else float('inf')
    
    while N > 3:
        # Option 1: Two fastest escort two slowest
        option1 = 2 * s2 + sorted_s[N-2] + sorted_s[N-1]
        # Option 2: Fastest escorts one slowest twice
        option2 = 2 * s1 + sorted_s[N-3] + sorted_s[N-1]
        total_time += min(option1, option2)
        N -=2
    
    if N == 3:
        total_time += s1 + sorted_s[1] + sorted_s[2]
    elif N ==2:
        total_time += sorted_s[1]
    elif N ==1:
        total_time += sorted_s[0]
    
    return total_time

def main():
    input = sys.stdin.read().split()
    idx =0
    T = int(input[idx]); idx+=1
    for test_case in range(1, T+1):
        N,K = int(input[idx]), int(input[idx+1]); idx+=2
        S = []
        for _ in range(N):
            S.append(int(input[idx]))
            idx+=1
        S.sort()
        total_time = minimal_crossing_time(S, N)
        if total_time <= K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()