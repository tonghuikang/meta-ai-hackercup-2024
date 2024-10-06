import sys
import math

def sieve_eratosthenes(n):
    sieve = bytearray([True]) * (n + 1)
    sieve[0:2] = b'\x00\x00'  # 0 and 1 are not primes
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(2, sqrt_n):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])
    return sieve

def main():
    import sys

    input = sys.stdin.read().split()
    T = int(input[0])
    N_list = list(map(int, input[1:T+1]))
    max_N = max(N_list)

    sieve = sieve_eratosthenes(max_N)
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    primes_set = set(primes)

    case_number = 1
    for N in N_list:
        # Get primes up to N
        # Since primes are sorted, we can find the index where prime > N
        # and slice the primes list accordingly
        # Using binary search for efficiency
        left, right = 0, len(primes)
        while left < right:
            mid = (left + right) // 2
            if primes[mid] > N:
                right = mid
            else:
                left = mid + 1
        primes_up_to_N = primes[:left]
        primes_up_to_N_set = set(primes_up_to_N)

        count = 0
        for d in primes_up_to_N:
            if d > N:
                break
            # To find if there exists p'' such that p'' + d is prime and <=N
            # Iterate through primes_up_to_N and check if p'' + d is prime
            # Since primes_up_to_N is sorted, we can stop when p'' > N - d
            # Implemented with early termination
            found = False
            for p_double_prime in primes_up_to_N:
                if p_double_prime > N - d:
                    break
                p_prime = p_double_prime + d
                if sieve[p_prime]:
                    count +=1
                    found = True
                    break
            if not found:
                continue
        print(f"Case #{case_number}: {count}")
        case_number +=1

if __name__ == "__main__":
    main()