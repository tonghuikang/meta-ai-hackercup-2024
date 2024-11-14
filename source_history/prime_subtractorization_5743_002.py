import sys
import numpy as np

def sieve_of_eratosthenes(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    sqrt_n = int(n**0.5) + 1
    for p in range(2, sqrt_n):
        if sieve[p]:
            sieve[p*p:n+1:p] = False
    return sieve

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    N_values = list(map(int, data[1:T+1]))
    max_N = max(N_values) if T > 0 else 0
    sieve = sieve_of_eratosthenes(max_N)
    primes = np.nonzero(sieve)[0]
    
    # Convert sieve to integer bitmask
    # Since 10^7 bits is manageable, but in Python, it's okay
    # Initialize sieve_int as integer bitmask
    sieve_int = 0
    for p in primes:
        sieve_int |= (1 << p)
    
    for idx, N in enumerate(N_values, 1):
        if N < 2:
            count = 0
        else:
            # Get primes_S which are primes <= N -2
            # Using numpy for fast filtering
            # Find the index in primes where p <= N -2
            # Since primes are sorted, we can use searchsorted
            upper_S = N -2
            if upper_S < 2:
                count = 0
            else:
                # Find the boundary index
                boundary = np.searchsorted(primes, upper_S, side='right')
                primes_S = primes[:boundary]
                # Convert primes_S to a list for faster iteration
                primes_S = primes_S.tolist()
                # Create sieve_N
                # To limit to N bits
                if N >=0:
                    sieve_N_int = sieve_int & ((1 << (N+1)) -1)
                else:
                    sieve_N_int = 0
                c = 0
                for S in primes_S:
                    # Check if there exists p <=N where p is prime and p - S is prime
                    # Which is equivalent to checking if (sieve_N >> S) & sieve_int is non-zero
                    shifted = sieve_N_int >> S
                    possible = shifted & sieve_int
                    if possible !=0:
                        c +=1
                count = c
        print(f"Case #{idx}: {count}")

if __name__ == "__main__":
    main()