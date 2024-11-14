import sys
import threading

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)
    T_and_cases = sys.stdin.read().split()
    T = int(T_and_cases[0])
    Ns = list(map(int, T_and_cases[1:T+1]))
    max_N = max(Ns)

    # Sieve of Eratosthenes
    sieve = [True] * (max_N + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(math.isqrt(max_N)) + 1):
        if sieve[i]:
            sieve[i*i:max_N+1:i] = [False] * len(range(i*i, max_N+1, i))
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Initialize a list to mark p's
    subtractorizations = [0] * (max_N + 1)

    # Use a set for O(1) lookup
    prime_set = set(primes)

    # Iterate through all primes q
    for q in primes:
        # Iterate through primes r where r <= q - 2
        # Because p = q - r >= 2
        for r in primes:
            if r > q - 2:
                break
            p = q - r
            if p > max_N:
                continue
            if sieve[p]:
                subtractorizations[p] = 1

    # Create prefix sum
    prefix = [0] * (max_N + 1)
    count = 0
    for i in range(2, max_N + 1):
        if subtractorizations[i]:
            count += 1
        prefix[i] = count

    # Answer each test case
    for idx, N in enumerate(Ns, 1):
        print(f"Case #{idx}: {prefix[N]}")

if __name__ == "__main__":
    threading.Thread(target=main).start()