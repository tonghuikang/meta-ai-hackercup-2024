import sys
import threading

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)

    T = int(sys.stdin.readline())
    Ns = [int(sys.stdin.readline()) for _ in range(T)]
    maxN = max(Ns)

    # Sieve of Eratosthenes
    sieve_size = maxN + 1
    sieve = bytearray([1]) * sieve_size
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(math.isqrt(maxN)) + 1):
        if sieve[i]:
            sieve[i*i:maxN+1:i] = b'\x00' * len(sieve[i*i:maxN+1:i])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Create a set for faster lookup
    sieve_set = sieve

    # Precompute cumulative counts for all N up to maxN
    # Initialize count_subtract = [0]*(maxN +1)
    # But memory would be too high, so process each test case separately

    for idx, N in enumerate(Ns, 1):
        count = 0
        # Iterate through primes <=N
        for p in primes:
            if p > N:
                break
            # We need to find if there exists a prime q <=N -p such that p + q is prime
            # Iterate through q's primes <=N -p
            # To optimize, iterate q from smallest to largest
            # Stop once q > N -p
            # If any p + q is prime, count p and break
            # To speed up, iterate through primes up to N -p
            # Find the index of the largest q <=N -p
            # Using binary search
            left = 0
            right = len(primes) -1
            target = N - p
            q_limit = target
            # Binary search to find the upper bound for q
            q_idx = -1
            l = 0
            r = len(primes) -1
            while l <= r:
                m = (l + r) //2
                if primes[m] <= q_limit:
                    q_idx = m
                    l = m +1
                else:
                    r = m -1
            if q_idx == -1:
                continue
            found = False
            for q in primes[:q_idx +1]:
                p_plus_q = p + q
                if p_plus_q > N:
                    break
                if sieve_set[p_plus_q]:
                    count +=1
                    found = True
                    break
            # If not found, do not count
        print(f"Case #{idx}: {count}")

threading.Thread(target=main).start()