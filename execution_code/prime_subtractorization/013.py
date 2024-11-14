import sys
import threading
import bisect

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    max_N = max(Ns) if Ns else 0

    # Sieve of Eratosthenes up to max_N + max_N to cover p + b up to 2*max_N
    sieve_size = max_N + 1
    sieve = [True] * (sieve_size)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(max_N)) + 1):
        if sieve[i]:
            sieve[i*i:max_N+1:i] = [False] * len(range(i*i, max_N+1, i))
    # List of primes up to max_N
    primes = [i for i, is_p in enumerate(sieve) if is_p]

    # Create a set for O(1) lookups
    sieve_set = set(primes)

    # Precompute prefix sums or other structures if needed

    for idx, N in enumerate(Ns, 1):
        count = 0
        # Iterate through primes up to N
        for p in primes:
            if p > N:
                break
            # b must be <= N - p
            # Find the index in primes where prime > N - p
            # All primes up to N - p are candidates for b
            # We can iterate through primes up to N - p and check if p + b is prime
            # To optimize, iterate through primes and break early
            # Since p + b must be prime and p + b <=N
            # We can iterate through b's primes <= N - p
            # and check if p + b is in sieve
            # To speed up, iterate through b primes and check p + b
            # But in the worst case, this is still O(M^2)
            # So, instead, iterate through b's primes up to N - p and check
            # if p + b is prime
            # To further optimize, iterate through b's starting from smallest prime
            # and break as soon as p + b > N
            # But this doesn't help much
            # Alternative Idea:
            # Iterate through a = p + b <= N, where b is prime and a is prime
            # So we can iterate through a's and see if a - p is prime and <= N
            # However, the initial approach remains feasible in Python with constraints
            # To speed up, use a generator expression with any()
            # Find if any b is prime and p + b is prime
            # Limit b to <= N - p
            # We can use bisect to find the upper limit index
            upper = N - p
            # Find the index where prime > upper
            # bisect_right returns the insertion point, so primes[:bisect_right(...)]

            # binary search to find rightmost b <= upper
            right = bisect.bisect_right(primes, upper)
            # Iterate through primes[:right] and check if p + b is prime
            # Use any to short-circuit as soon as a valid b is found
            # which makes p a subtractorization
            # To speed up, iterate over primes[:right] and check
            # if p + b is in sieve_set
            # Since sieve_set is a set, lookup is O(1)
            has_subtractorization = False
            for b in primes[:right]:
                a = p + b
                if a > N:
                    break
                if a in sieve_set:
                    has_subtractorization = True
                    break
            if has_subtractorization:
                count +=1
        print(f"Case #{idx}: {count}")

threading.Thread(target=main,).start()