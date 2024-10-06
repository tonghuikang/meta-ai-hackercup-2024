import sys
import threading

def main():
    import bisect
    import math
    import sys

    sys.setrecursionlimit(1 << 25)
    NMAX = 10000000

    is_prime = [True] * (NMAX + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(NMAX ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, NMAX+1, i):
                is_prime[j] = False

    primes_list = [i for i, val in enumerate(is_prime) if val]
    primes_set = set(primes_list)

    counts = [0] * (NMAX + 1)

    for P in primes_list:
        found = False
        idx = bisect.bisect_left(primes_list, P)
        for p1 in primes_list[idx:]:
            p2 = p1 - P
            if p2 < 2:
                break
            if p2 in primes_set:
                counts[P] = 1
                found = True
                break
        # If P is very small, p1 - P may still be out of primes range, so let's check the minimum p1
        if not found:
            for p1 in primes_list:
                if p1 < P:
                    continue
                p2 = p1 - P
                if p2 < 2:
                    break
                if p2 in primes_set:
                    counts[P] = 1
                    break

    # Compute cumulative counts
    counts_cum = [0] * (NMAX + 1)
    total = 0
    for i in range(1, NMAX + 1):
        total += counts[i]
        counts_cum[i] = total

    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N_line = ''
        while N_line.strip() == '':
            N_line = sys.stdin.readline()
        N = int(N_line)
        if N > NMAX:
            N = NMAX
        print(f"Case #{case_num}: {counts_cum[N]}")

threading.Thread(target=main).start()