# Read input from standard input and write output to standard output

T = int(input())
M = 998244353

for case_num in range(1, T + 1):
    W_str, G_str, L_str = input().split()
    W = int(W_str)
    G = int(G_str)
    L = int(L_str)

    D = W - G
    N = 2 * L + 1

    D_mod = D % M
    N_mod = N % M

    ExpectedTimeMod = (D_mod * N_mod) % M

    print(f'Case #{case_num}: {ExpectedTimeMod}')