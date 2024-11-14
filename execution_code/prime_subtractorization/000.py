import sys
import threading
import sys
import math
import sys

def main():
    import sys
    import math

    import sys

    sys.setrecursionlimit(1 << 25)
    from sys import stdin
    from math import isqrt

    T_and_Ns = sys.stdin.read().split()
    T = int(T_and_Ns[0])
    Ns = list(map(int, T_and_Ns[1:T+1]))
    N_max = max(Ns)

    sieve_size = N_max + 1
    sieve = bytearray([1]) * sieve_size
    sieve[0:2] = b'\0\0'

    for i in range(2, isqrt(N_max) +1):
        if sieve[i]:
            sieve[i*i:N_max+1:i] = b'\0' * len(sieve[i*i:N_max+1:i])

    list_primes = [p for p, is_p in enumerate(sieve) if is_p]

    # Initialize min_N as N_max +1
    min_N = [N_max +1] * (N_max +1)

    # Create a list of primes up to N_max
    for p in list_primes:
        # Find the smallest b such that b is prime and p + b is prime
        # Since list_primes is sorted, iterate through b from smallest to largest
        # Stop when b > N_max -p
        # Use binary search to find the starting index for b >=2
        # but since list_primes starts from 2, just iterate through the list until b > N_max -p
        for b in list_primes:
            if b > N_max - p:
                break
            if sieve[p + b]:
                min_N[p] = p + b
                break

    # Now, precompute counts
    counts = [0] * (N_max +1)
    count =0
    for N in range(1, N_max +1):
        if sieve[N] and min_N[N] <=N:
            count +=1
        counts[N] = count

    # Now, answer the test cases
    for idx, N in enumerate(Ns, 1):
        if N <2:
            result =0
        else:
            result = counts[N]
        print(f"Case #{idx}: {result}")



threading.Thread(target=main,).start()