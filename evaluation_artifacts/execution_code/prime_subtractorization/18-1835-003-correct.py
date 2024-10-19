import sys
import math
from array import array

def main():
    import sys
    import sys
    import sys
    # Read all input
    input = sys.stdin.read().split()
    T = int(input[0])
    Ns = list(map(int, input[1:T+1]))
    max_N = max(Ns) if Ns else 0

    if max_N < 2:
        sieve = bytearray(max_N +1)
    else:
        sieve = bytearray([1]) * (max_N +1)
        sieve[0] = sieve[1] = 0
        upper = math.isqrt(max_N) +1
        for p in range(2, upper):
            if sieve[p]:
                sieve[p*p:max_N +1:p] = b'\x00' * len(sieve[p*p:max_N +1:p])

    # Precompute twin primes count
    twin_primes_count = array('I', [0]) * (max_N +1)
    count = 0
    for x in range(1, max_N +1):
        twin_primes_count[x] = twin_primes_count[x -1]
        if x >=4 and sieve[x -2] and sieve[x]:
            twin_primes_count[x] +=1

    # Process each test case
    for i in range(1, T +1):
        N = Ns[i -1]
        if N >=5:
            res = 1 + (twin_primes_count[N])
        else:
            res =0
        print(f"Case #{i}: {res}")

if __name__ == "__main__":
    main()