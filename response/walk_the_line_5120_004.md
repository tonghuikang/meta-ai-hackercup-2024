### Key Findings

- **Sorting**: Start by sorting the crossing times in ascending order.
- **Standard Strategy**: Utilize a standard bridge-crossing strategy where you either:
  - Send the two fastest to shuttle the slower travelers.
  - Or send the fastest to assist the two slowest travelers directly.
- **Total Time Calculation**: At each step, choose the option that minimizes the total crossing time and accumulate the total time.
- **Decision**: After calculating the total crossing time using the strategy, compare it with the given time limit \( K \). If the total time is within \( K \), output "YES"; otherwise, "NO".
- **Efficiency**: The approach is efficient with a time complexity of \( O(N \log N) \) per test case due to the initial sorting.

```python
def solve_bridge_crossing():
    import sys
    import sys
    from sys import stdin
    input = sys.stdin.read
    data = input().split()
    idx =0
    T = int(data[idx])
    idx +=1
    for test_case in range(1, T+1):
        N,K = map(int, data[idx:idx+2])
        idx +=2
        S = []
        for _ in range(N):
            S.append(int(data[idx]))
            idx +=1
        S.sort()
        total =0
        left =0
        right = N-1
        while right >=0:
            if right ==0:
                total += S[0]
                right -=1
            elif right ==1:
                total += S[1]
                right -=2
            elif right ==2:
                total += S[0] + S[1] + S[2]
                right -=3
            else:
                option1 = 2 * S[1] + S[0] + S[right]
                option2 = 2 * S[0] + S[right-1] + S[right]
                total += min(option1, option2)
                right -=2
        if total <=K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{test_case}: {result}")
```

```python
def solve_bridge_crossing():
    import sys
    import sys
    from sys import stdin
    input = sys.stdin.read
    data = input().split()
    idx =0
    T = int(data[idx])
    idx +=1
    for test_case in range(1, T+1):
        N,K = map(int, data[idx:idx+2])
        idx +=2
        S = []
        for _ in range(N):
            S.append(int(data[idx]))
            idx +=1
        S.sort()
        total =0
        left =0
        right = N-1
        while right >=0:
            if right ==0:
                total += S[0]
                right -=1
            elif right ==1:
                total += S[1]
                right -=2
            elif right ==2:
                total += S[0] + S[1] + S[2]
                right -=3
            else:
                option1 = 2 * S[1] + S[0] + S[right]
                option2 = 2 * S[0] + S[right-1] + S[right]
                total += min(option1, option2)
                right -=2
        if total <=K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{test_case}: {result}")
```