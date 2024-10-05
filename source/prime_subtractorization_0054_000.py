import sys
import threading

def main():
    import sys
    import math
    import bisect

    T_and_cases = sys.stdin.read().split()
    T = int(T_and_cases[0])
    cases = list(map(int, T_and_cases[1:T+1]))
    max_N = max(cases) if T >0 else 0

    # Sieve of Eratosthenes up to max_N
    sieve_size = max_N + 1
    sieve = bytearray([True]) * sieve_size
    sieve[0:2] = b'\x00\x00'  # 0 and 1 are not prime
    for i in range(2, int(math.isqrt(max_N)) +1):
        if sieve[i]:
            sieve[i*i:max_N+1:i] = b'\x00' * len(sieve[i*i:max_N+1:i])
    primes = [i for i, is_p in enumerate(sieve) if is_p]

    # Precompute prefix sums for faster queries
    # Not necessary here, as we need to check for each p individually

    for idx, N in enumerate(cases, 1):
        count =0
        # Find the index of the first prime >N
        # Using bisect_right
        upper = bisect.bisect_right(primes, N)
        # Iterate through primes up to N
        for i in range(0, upper):
            p = primes[i]
            # b needs to be <=N -p
            b_max = N - p
            if b_max <2:
                continue
            # Find the index of the first prime >b_max
            b_upper = bisect.bisect_right(primes, b_max)
            # Iterate through primes up to b_max
            for j in range(0, b_upper):
                b = primes[j]
                a = p + b
                if a >N:
                    break
                if sieve[a]:
                    count +=1
                    break
        print(f"Case #{idx}: {count}")

threading.Thread(target=main,).start()