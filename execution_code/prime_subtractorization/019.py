import sys
import threading

def main():
    import sys
    import math
    from bisect import bisect_right

    T = int(sys.stdin.readline())
    Ns = [int(sys.stdin.readline()) for _ in range(T)]
    max_N = max(Ns)

    # Sieve of Eratosthenes
    sieve = [True] * (max_N + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(max_N)) + 1):
        if sieve[i]:
            for j in range(i*i, max_N +1, i):
                sieve[j] = False

    # List of primes
    primes = [i for i, is_p in enumerate(sieve) if is_p]

    # Precompute prefix sums if needed
    # Not needed here

    # For faster access, convert list to set
    # Not necessary since sieve allows O(1) lookups

    # Process each test case
    for idx, N in enumerate(Ns, 1):
        count = 0
        # Iterate through primes <=N
        for p in primes:
            if p > N:
                break
            # Find if there exists r <=N -p such that r is prime and p + r is prime
            # Iterate through primes <= N -p
            # Since primes are sorted, find the upper bound for r
            # Using bisect_right to find the index where r > N -p
            max_r = N - p
            if max_r < 2:
                continue
            # Find the index up to which r <= max_r
            # r_list = primes up to max_r
            # Binary search
            r_idx = bisect_right(primes, max_r)
            # Iterate through r in primes[:r_idx]
            # Check if p + r is prime
            # Since p + r <= N, and sieve is up to N
            for r in primes[:r_idx]:
                q = p + r
                if q > N:
                    break
                if sieve[q]:
                    count +=1
                    break  # Only need at least one r for each p
        print(f"Case #{idx}: {count}")

# For faster input reading and to avoid recursion limits
threading.Thread(target=main).start()