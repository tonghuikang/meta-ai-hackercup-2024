import sys
import math
import threading

def main():
    T = int(sys.stdin.readline())
    MOD = 10**9+7

    for case_num in range(1, T+1):
        N, M, L = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))
        N_fact = math.factorial(N)
        M_fact = math.factorial(M)

        A_sorted = sorted(A)
        B_sorted = sorted(B)

        # Calculate minimal unevenness for nigiri and sashimi when sorted
        S_nigiri = sum(abs(A_sorted[i+1] - A_sorted[i]) for i in range(N-1))
        S_sashimi = sum(abs(B_sorted[i+1] - B_sorted[i]) for i in range(M-1))

        # Option 1: Nigiri first, then sashimi
        if N > 0 and M > 0:
            diff_ns = abs(A_sorted[-1] - B_sorted[0])
        elif N > 0:
            diff_ns = 0
        elif M > 0:
            diff_ns = 0
        else:
            diff_ns = 0
        S_total_ns = S_nigiri + diff_ns + S_sashimi

        # Option 2: Sashimi first, then nigiri
        if N > 0 and M > 0:
            diff_sn = abs(B_sorted[-1] - A_sorted[0])
        elif N > 0:
            diff_sn = 0
        elif M > 0:
            diff_sn = 0
        else:
            diff_sn = 0
        S_total_sn = S_sashimi + diff_sn + S_nigiri

        count = 0
        if S_total_ns <= L:
            count = (N_fact * M_fact) % MOD
        if S_total_sn <= L:
            count = (count + (N_fact * M_fact)) % MOD
        # If both sequences are acceptable, we have counted twice
        if S_total_ns <= L and S_total_sn <= L:
            # Both arrangements are acceptable
            count = (N_fact * M_fact * 2) % MOD

        print(f'Case #{case_num}: {count % MOD}')

threading.Thread(target=main).start()