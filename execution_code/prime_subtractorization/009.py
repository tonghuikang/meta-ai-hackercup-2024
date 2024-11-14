import sys
import threading

def main():
    import sys

    import sys

    T_and_tests = sys.stdin.read().split()
    T = int(T_and_tests[0])
    Ns = list(map(int, T_and_tests[1:T+1]))

    max_N = max(Ns)

    # Sieve of Eratosthenes
    sieve_size = max_N + 1
    sieve = bytearray([1]) * sieve_size
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(max_N**0.5) + 1):
        if sieve[i]:
            sieve[i*i:max_N+1:i] = b'\x00' * len(sieve[i*i:max_N+1:i])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Create a set for faster lookup
    prime_set = set(primes)

    # Precompute subtractorizations
    # For each prime q, iterate through primes r <= q, p = q - r
    # If p is prime and p <= max_N, mark p
    # To optimize, iterate through primes and for each q, iterate through r until r > q
    # But even better, for each q, iterate through r until q - r >= 2
    subtractorizations = [0] * (max_N +1)
    for q in primes:
        for r in primes:
            if r > q:
                break
            p = q - r
            if p < 2:
                continue
            if sieve[p]:
                subtractorizations[p] = 1
    # Now, create a prefix sum array
    prefix_sum = [0] * (max_N +1)
    count = 0
    for i in range(2, max_N +1):
        if subtractorizations[i]:
            count +=1
        prefix_sum[i] = count

    for idx, N in enumerate(Ns,1):
        print(f"Case #{idx}: {prefix_sum[N]}")

if __name__ == "__main__":
    threading.Thread(target=main).start()