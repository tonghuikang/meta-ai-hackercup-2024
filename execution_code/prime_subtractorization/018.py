import sys
import sys
import sys
import sys

def sieve_of_eratosthenes(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i : limit+1 : i] = b'\x00' * len(sieve[i*i : limit+1 : i])
    return sieve

def main():
    import sys
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    max_N = max(Ns)
    sieve = sieve_of_eratosthenes(max_N)
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    primes_set = set(primes)
    for idx, N in enumerate(Ns, 1):
        count = 0
        for P in primes:
            if P > N:
                break
            # R needs to be prime and Q = P + R <=N
            # So R <= N - P
            # Iterate through primes <= N - P
            # Find the upper bound for R
            # Using binary search
            left = 0
            right = len(primes)
            target = N - P
            # Binary search to find the index where primes[index] > target
            l = 0
            r = len(primes)
            while l < r:
                m = (l + r) // 2
                if primes[m] > target:
                    r = m
                else:
                    l = m + 1
            # Now primes[0:l] are <= target
            for R in primes[:l]:
                Q = P + R
                if Q > N:
                    break
                if sieve[Q]:
                    count +=1
                    break
        print(f"Case #{idx}: {count}")

if __name__ == "__main__":
    main()