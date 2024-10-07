import sys
import threading
import bisect

def main():
    import sys

    import math

    sys.setrecursionlimit(1 << 25)

    T_and_rest = sys.stdin.read().split()
    T = int(T_and_rest[0])
    Ns = list(map(int, T_and_rest[1:T+1]))
    max_N = max(Ns)

    # Sieve of Eratosthenes
    sieve_size = max_N + 1
    sieve = [True] * sieve_size
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(max_N)) +1):
        if sieve[i]:
            for j in range(i*i, sieve_size, i):
                sieve[j] = False

    # List of primes
    primes = [i for i, is_p in enumerate(sieve) if is_p]

    # Precompute prefix sums for primes for faster access
    # Not necessary here, as we need to iterate through primes

    for test_case, N in enumerate(Ns, 1):
        count = 0
        # Iterate through primes <=N
        for P in primes:
            if P > N:
                break
            # We need to find at least one R such that R is prime and P + R is prime and P + R <=N
            # Since R >=2, P +2 <=N
            if P + 2 > N:
                continue
            if sieve[P + 2]:
                count +=1
                continue
            # Else, check other R's
            # Iterate through primes R >=3 and <=N -P
            # Using binary search to find the starting index
            # Since primes are sorted
            # Find the first R >=3
            # R's are in primes list
            # Find the index of R >=3
            left = bisect.bisect_left(primes,3)
            # Find the primes R <= N - P
            right = bisect.bisect_right(primes, N - P)
            # Iterate from left to right
            found = False
            for R in primes[left:right]:
                if sieve[P + R]:
                    count +=1
                    found = True
                    break
            if not found:
                continue
        print(f"Case #{test_case}: {count}")

threading.Thread(target=main).start()