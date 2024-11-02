for (int i = 1; i <= N; i++)
  for (int k = 1; k <= N; k++)
    for (int j = 1; j <= N; j++)
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

for k from 1 to N:
  for i from 1 to N:
    for j from 1 to N:
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    for _ in range(N - 1):
        input()
    result = 'Lucky' if N <= 5 else 'Wrong'
    print(f"Case #{case_num}: {result}")