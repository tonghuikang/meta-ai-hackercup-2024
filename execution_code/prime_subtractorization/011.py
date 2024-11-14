import sys
import threading
import bisect

def main():
    import sys

    import math

    sys.setrecursionlimit(1 << 25)
    from sys import stdin
    input = sys.stdin.read

    data = input().split()
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    N_max = max(Ns)

    # Sieve of Eratosthenes
    sieve_size = N_max + 1
    sieve = bytearray([True]) * sieve_size
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(N_max)) + 1):
        if sieve[i]:
            sieve[i*i:N_max+1:i] = b'\x00' * len(sieve[i*i:N_max+1:i])

    # Generate list of primes
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    # For faster access, convert sieve to a list
    sieve_list = sieve

    # Precompute prefix counts
    # Initialize an array to store the count up to each N
    # To save memory, we can compute counts on the fly for each N
    # However, precomputing would be faster for multiple test cases
    # So we precompute a list where count_list[i] is the count up to N=i
    # Initialize count_list with zeros
    count_list = [0] * (N_max + 1)
    # Initialize a set for quick lookup of primes
    # primes_set = set(primes)  # Not needed as we have sieve_list
    # Iterate through primes and mark valid subtractorizations
    # To optimize, iterate through primes in order and use two pointers
    # We will iterate through primes and for each prime P, check if any prime P2 exists such that P + P2 is prime
    # To do this efficiently, iterate for each P and try to find a P2

    # Initialize a list to mark P as valid subtractorizations
    valid_P = bytearray(N_max +1)

    for P in primes:
        # P needs to be <= N
        # We need to find at least one P2 such that P + P2 is prime and P2 is prime and P + P2 <= N_max
        # We iterate through primes P2 <= N_max - P
        # To optimize, iterate through primes up to N_max - P
        # Since primes are sorted, find the index where prime > N_max - P
        # Then iterate through primes[:idx]
        if P > N_max:
            continue
        # Find the upper bound for P2
        # Use bisect to find the index
        idx = bisect.bisect_right(primes, N_max - P)
        for P2 in primes[:idx]:
            Q = P + P2
            if Q > N_max:
                break
            if sieve_list[Q]:
                valid_P[P] = 1
                break  # Only need at least one P2

    # Now, compute the prefix sum of valid_P
    count = 0
    for i in range(2, N_max +1):
        if valid_P[i]:
            count +=1
        count_list[i] = count

    # Now, answer each test case
    for idx, N in enumerate(Ns, 1):
        res = count_list[N]
        print(f"Case #{idx}: {res}")

threading.Thread(target=main).start()