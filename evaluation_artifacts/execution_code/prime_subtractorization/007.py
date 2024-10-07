import sys
import bisect
import numpy as np

def main():
    import sys

    MAX_N =10_000_000
    SIEVE_LIMIT =2 * MAX_N +1

    # Initialize sieve
    sieve = np.ones(SIEVE_LIMIT, dtype=bool)
    sieve[:2] = False

    # Sieve of Eratosthenes
    sqrt_limit = int(SIEVE_LIMIT**0.5) +1
    for i in range(2, sqrt_limit):
        if sieve[i]:
            sieve[i*i:SIEVE_LIMIT:i] = False

    # Extract primes up to MAX_N
    primes_p = np.nonzero(sieve[:MAX_N+1])[0]
    primes_r = primes_p.copy()

    # Initialize min_N array
    min_N = np.zeros(MAX_N+1, dtype=np.int32)

    # Iterate over r in primes_r
    for r in primes_r:
        # Compute p + r
        p_plus_r = primes_p + r

        # Create mask where p + r is prime and <= MAX_N
        mask = (p_plus_r <= MAX_N) & sieve[p_plus_r]

        # Get p candidates where p + r is prime
        p_candidates = primes_p[mask]

        # Further mask to find p's where min_N[p] is not yet set
        unmarked = (min_N[p_candidates] ==0)
        p_use = p_candidates[unmarked]

        # Set min_N[p] = p + r
        min_N[p_use] = p_use + r

    # Extract min_N[p] for p in primes_p where min_N[p] >0
    valid_min_N = min_N[primes_p]
    valid_min_N = valid_min_N[valid_min_N >0]

    # Sort the valid_min_N array
    sorted_min_N = np.sort(valid_min_N)

    # Read input
    input = sys.stdin.read().split()
    T =int(input[0])
    for i in range(1,T+1):
        N = int(input[i])
        # Use binary search to find the count of min_N[p] <=N
        count = bisect.bisect_right(sorted_min_N, N)
        print(f"Case #{i}: {count}")

if __name__ == '__main__':
    main()