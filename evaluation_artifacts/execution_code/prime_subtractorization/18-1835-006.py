import sys
import threading

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    Ns = [int(sys.stdin.readline()) for _ in range(T)]
    N_max = max(Ns)

    # Sieve of Eratosthenes
    sieve_size = N_max + 1
    sieve = bytearray([1]) * sieve_size
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(math.isqrt(N_max)) + 1):
        if sieve[i]:
            sieve[i*i:N_max+1:i] = b'\x00' * len(sieve[i*i:N_max+1:i])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Initialize an array to mark if a prime can be expressed as a difference
    subtractorizations = bytearray(sieve_size)

    # Iterate over primes and mark possible p = q - r
    for r in primes:
        # q = p + r <= N_max => p <= N_max - r
        for q in primes:
            if q < r:
                continue
            p = q - r
            if p > 0 and sieve[p]:
                subtractorizations[p] = 1
            if q > N_max - r:
                break

    # Create prefix sums
    prefix_counts = [0] * (N_max + 1)
    count = 0
    for i in range(2, N_max + 1):
        if sieve[i] and subtractorizations[i]:
            count += 1
        prefix_counts[i] = count

    # Answer each test case
    for idx, N in enumerate(Ns, 1):
        result = prefix_counts[N]
        print(f"Case #{idx}: {result}")

if __name__ == "__main__":
    threading.Thread(target=main).start()