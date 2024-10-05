import sys
import threading

def main():
    import bisect
    import math
    T = int(sys.stdin.readline())
    Ns = []
    N_max = 0
    for _ in range(T):
        N = int(sys.stdin.readline())
        Ns.append(N)
        if N > N_max:
            N_max = N
    N_max += 1  # Ensure inclusive

    # Sieve of Eratosthenes to generate all primes up to N_max
    is_prime = [True] * N_max
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N_max ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N_max, i):
                is_prime[j] = False

    primes = [i for i, val in enumerate(is_prime) if val]
    primes_set = set(primes)

    # Precompute min_P_for_D for each prime D
    min_P_for_D = {}
    for D in primes:
        min_P = None
        for P in primes:
            if P <= D:
                continue
            if (P - D) in primes_set:
                min_P = P
                break
        if min_P:
            min_P_for_D[D] = min_P
        else:
            min_P_for_D[D] = None

    # Process each test case
    for idx, N in enumerate(Ns, 1):
        count = 0
        for D in primes:
            if D > N:
                break
            if min_P_for_D[D] is not None and min_P_for_D[D] <= N:
                count += 1
        print(f'Case #{idx}: {count}')

if __name__ == "__main__":
    threading.Thread(target=main,).start()