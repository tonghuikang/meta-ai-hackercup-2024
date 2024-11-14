import sys
import threading

def main():
    import sys
    import math

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

    primes = [i for i, is_p in enumerate(sieve) if is_p]

    # Initialize subtractorization markers
    is_subtractorization = [False] * (max_N +1)

    # Iterate through primes and mark P = p2 - p1
    # To avoid duplicates, we'll iterate p2 and p1 < p2
    for p2 in primes:
        for p1 in primes:
            if p1 >= p2:
                break
            P = p2 - p1
            if P > max_N:
                break
            if sieve[P]:
                is_subtractorization[P] = True

    # Create cumulative counts
    cum_count = [0] * (max_N +1)
    count = 0
    for i in range(2, max_N +1):
        if is_subtractorization[i]:
            count +=1
        cum_count[i] = count

    # Output results
    for idx, N in enumerate(Ns, 1):
        print(f"Case #{idx}: {cum_count[N]}")

# To handle large input sizes, use threading
threading.Thread(target=main).start()