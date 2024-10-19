import sys
import sys
import math

def sieve(max_n):
    sieve = bytearray([True]) * (max_n + 1)
    sieve[0:2] = b'\x00\x00'
    for num in range(2, int(math.isqrt(max_n)) + 1):
        if sieve[num]:
            sieve[num*num:max_n+1:num] = b'\x00' * len(sieve[num*num:max_n+1:num])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return sieve, primes

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    max_N = max(Ns)
    sieve_arr, primes = sieve(max_N)
    prime_set = set(primes)
    for idx, N in enumerate(Ns, 1):
        count = 0
        # Iterate through primes P up to N
        for P in primes:
            if P > N:
                break
            # Find if there exists a prime B <= N - P such that P + B is prime
            # Iterate through primes B <= N - P
            # To optimize, iterate B starting from smallest
            # and break once a valid B is found
            # Since P and B are primes, and P + B should be prime
            upper_B = N - P
            if upper_B < 2:
                continue
            # Binary search to find the index up to which B can be
            # Since primes are sorted, we can use bisect
            left = 0
            right = len(primes)
            while left < right:
                mid = (left + right) // 2
                if primes[mid] > upper_B:
                    right = mid
                else:
                    left = mid + 1
            # Iterate through primes up to left
            found = False
            for B in primes[:left]:
                A = P + B
                if A > N:
                    break
                if sieve_arr[A]:
                    count +=1
                    found = True
                    break
            if not found:
                continue
        print(f"Case #{idx}: {count}")

if __name__ == "__main__":
    main()