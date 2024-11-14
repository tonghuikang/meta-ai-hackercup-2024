import sys
import threading

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)
    T_and_N = sys.stdin.read().split()
    T = int(T_and_N[0])
    N_list = list(map(int, T_and_N[1:T+1]))
    N_max = max(N_list)

    # Sieve of Eratosthenes up to N_max
    sieve = [True] * (N_max + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(N_max)) +1):
        if sieve[i]:
            sieve[i*i:N_max+1:i] = [False] * len(range(i*i, N_max+1, i))
    # Create list of primes
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    # Create sieve as integer bitmask
    A = 0
    for p in primes:
        A |= 1 << p

    # For faster access, create a list to map N to its corresponding prime set
    # But since N can be up to 10^7, we need a way to handle it
    # Instead, for each N, we can mask the sieve up to N

    # Precompute cumulative prime list
    # Not necessary, as we have the list

    # Process each test case
    for idx in range(T):
        N = N_list[idx]
        # Mask the sieve up to N
        A_N = A & ((1 << (N +1)) -1)
        count = 0
        for p in primes:
            if p > N:
                break
            # Check if there exists r <=N - p such that r is prime and p + r is prime
            # Which is equivalent to checking if (A << p) & A_N has any bit set
            shifted = A_N << p
            # Only keep bits up to N + p, but since A_N has bits up to N, shifted has bits up to 2N
            # But p <=N, so p + r <= N + p <= 2N, but we need p + r <= N, so r <=N - p
            # Thus, mask shifted with (1 << (N +1)) -1
            shifted &= (1 << (N +1)) -1
            if (shifted & A_N) !=0:
                count +=1
        print(f"Case #{idx+1}: {count}")

threading.Thread(target=main).start()