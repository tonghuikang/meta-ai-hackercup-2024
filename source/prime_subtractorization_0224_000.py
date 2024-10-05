import sys
import numpy as np
import bisect

def main():
    import sys
    import numpy as np
    import bisect

    # Read all input first
    input = sys.stdin.read().split()

    T = int(input[0])
    test_cases = list(map(int, input[1:T+1]))
    if not test_cases:
        test_cases = []
    
    # Find the maximum N to define sieve size
    Nmax = max(test_cases) if test_cases else 0

    if Nmax < 5:
        sieve_size = 5  # Minimal size to cover up to N=5
    else:
        sieve_size = Nmax + 3  # To cover p + 2 up to Nmax +2

    # Initialize sieve: True means prime
    sieve = np.ones(sieve_size, dtype=bool)
    sieve[:2] = False  # 0 and 1 are not primes

    # Sieve of Eratosthenes using NumPy for efficiency
    for p in range(2, int(np.sqrt(Nmax)) + 1):
        if sieve[p]:
            sieve[p*p:Nmax+3:p] = False

    # Identify twin primes: p and p+2 are both primes
    # We start from p=3 to p=Nmax-2
    # twin_primes contains the p's such that (p, p+2) are both primes
    if Nmax >= 3:
        twin_primes_np = np.where(sieve[3:Nmax +1] & sieve[5:Nmax +3])[0]
        twin_primes = twin_primes_np.tolist()
    else:
        twin_primes = []

    # Process each test case
    for idx, N in enumerate(test_cases, 1):
        if N <5:
            count = 0
        else:
            count = 1  # Include p=2
            upper_p = N -2
            # Count the number of twin primes p <= upper_p
            twin_count = bisect.bisect_right(twin_primes, upper_p)
            count += twin_count
        print(f"Case #{idx}: {count}")

if __name__ == '__main__':
    main()