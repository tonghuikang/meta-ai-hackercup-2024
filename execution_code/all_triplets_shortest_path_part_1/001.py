t = int(input())
for case_num in range(1, t + 1):
    n = int(input())
    for _ in range(n - 1):
        input()  # Read and discard the edges
    if n <= 5:
        result = 'Lucky'
    else:
        result = 'Wrong'
    print(f'Case #{case_num}: {result}')