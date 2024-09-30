# Python code to solve the bridge crossing problem

def bridge_crossing(T, test_cases):
    results = []
    for case_num in range(1, T + 1):
        N, K, S = test_cases[case_num - 1]
        S.sort()
        if N <= 2:
            total_time = S[0]
        else:
            sum_S = sum(S[1:N-1]) if N > 2 else 0
            total_time = S[0] + 2 * sum_S
        result = "YES" if total_time <= K else "NO"
        results.append(f"Case #{case_num}: {result}")
    return results

# Read input from standard input
import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    test_cases = []
    for _ in range(T):
        N = int(input[idx])
        K = int(input[idx +1])
        idx +=2
        S = []
        for _ in range(N):
            S.append(int(input[idx]))
            idx +=1
        test_cases.append((N, K, S))
    results = bridge_crossing(T, test_cases)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()