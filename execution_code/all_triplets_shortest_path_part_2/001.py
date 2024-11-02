T = int(input())
for case_num in range(1, T + 1):
    S = input().strip()
    N = int(input())
    for _ in range(N - 1):
        input()  # Read and ignore the edges, as they are not needed in this solution
    if S[0] == 'k':
        result = 'Lucky'
    else:
        result = 'Wrong'
    print(f'Case #{case_num}: {result}')