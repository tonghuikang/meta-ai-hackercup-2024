import sys
import threading

def main():
    import bisect
    T = int(sys.stdin.readline())
    Ns = [int(sys.stdin.readline()) for _ in range(T)]
    N_MAX = max(Ns) + 10  # Incremented to ensure we cover up to N

    # Sieve of Eratosthenes
    is_prime = [True] * (N_MAX)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(N_MAX**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N_MAX, i):
                is_prime[j] = False
    # Generate list of primes
    primes_list = [p for p in range(2, N_MAX) if is_prime[p]]

    # Precompute primes set for quick lookup
    # is_prime list is already there

    for idx, N in enumerate(Ns, 1):
        ans = 0
        small_primes = [2, 3, 5, 7]
        index_limit = bisect.bisect_right(primes_list, N - 2)
        for p in primes_list[:index_limit]:
            for p2 in small_primes:
                p1 = p + p2
                if p1 > N:
                    break
                if is_prime[p1]:
                    ans += 1
                    break  # Stop checking other small_primes for this p
        print(f"Case #{idx}: {ans}")

threading.Thread(target=main).start()