import sys
import threading
import math
import bisect

def main():
    import sys
    import sys
    import math
    from bisect import bisect_right

    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    Ns = []
    max_N = 0
    for _ in range(T):
        N = int(sys.stdin.readline())
        Ns.append(N)
        if N > max_N:
            max_N = N

    # Sieve of Eratosthenes up to max_N
    sieve_size = max_N + 1
    sieve = bytearray([1]) * sieve_size
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(math.isqrt(max_N)) +1):
        if sieve[i]:
            sieve[i*i : sieve_size : i] = b'\x00' * len(sieve[i*i : sieve_size : i])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Precompute cumulative subtractorizations
    # Initialize a list to hold counts up to max_N
    count_subtractor = [0] * (max_N +1)
    # Initialize a boolean array to mark m's
    marked = bytearray(max_N +1)
    for p in primes:
        if p < 2:
            continue
        # Iterate through q in primes up to p -2
        # Since primes are sorted, find the index where q > p -2
        # Use bisect to find upper bound
        # q must be <= p -2
        upper_q = p -2
        if upper_q < 2:
            continue
        idx = bisect.bisect_right(primes, upper_q)
        for q in primes[:idx]:
            m = p - q
            if m >=2 and sieve[m]:
                marked[m] = 1
    # Now, compute the cumulative counts
    count = 0
    for m in range(2, max_N +1):
        if marked[m]:
            count +=1
        count_subtractor[m] = count

    # Now, answer each test case
    for idx, N in enumerate(Ns,1):
        print(f"Case #{idx}: {count_subtractor[N]}")

threading.Thread(target=main).start()