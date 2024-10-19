T = int(input())
for test_case in range(1, T+1):
    import sys
    input_data = []
    while len(input_data) < 2:
        input_data += sys.stdin.readline().split()
    N, K = map(int, input_data[:2])
    input_data = input_data[2:]
    S = []
    while len(S) < N:
        if len(input_data) == 0:
            input_data += sys.stdin.readline().split()
        S.append(int(input_data.pop(0)))
    S.sort()
    total_time = 0
    n = N
    while n > 3:
        Option1_time = S[0] + 2*S[1] + S[n-1]
        Option2_time = 2*S[0] + S[n-2] + S[n-1]
        total_time += min(Option1_time, Option2_time)
        n -= 2  # Two travelers have crossed to the other side
    if n == 1:
        total_time += S[0]
    elif n == 2:
        total_time += S[1]
    elif n == 3:
        total_time += min(
            S[0] + S[1] + S[2],
            2*S[1] + S[0],
            2*S[0] + S[1]
        )
    if total_time <= K:
        print(f"Case #{test_case}: YES")
    else:
        print(f"Case #{test_case}: NO")