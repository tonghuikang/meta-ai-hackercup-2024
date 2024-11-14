import sys
import numpy as np

def sieve_eratosthenes(max_n):
    sieve = np.ones(max_n + 1, dtype=bool)
    sieve[:2] = False
    sieve[4::2] = False  # Eliminate even numbers >2
    for p in range(3, int(max_n**0.5) + 1, 2):
        if sieve[p]:
            sieve[p*p::2*p] = False
    return sieve

def main():
    import sys
    import threading

    def run():
        T_and_cases = sys.stdin.read().split()
        T = int(T_and_cases[0])
        cases = list(map(int, T_and_cases[1:T+1]))
        max_N = max(cases)
        sieve = sieve_eratosthenes(max_N)
        primes = np.nonzero(sieve)[0]
        # Create a list of primes for faster iteration
        prime_list = primes.tolist()
        sieve_set = set(prime_list)  # Optional: for faster lookup, but might be slower in Python

        for idx, N in enumerate(cases, 1):
            count = 0
            # Find primes <= N-2 using binary search
            # Using numpy's searchsorted for efficiency
            upper = np.searchsorted(primes, N-1, side='right')
            for P in primes[:upper]:
                # We need R <= N - P
                max_R = N - P
                if max_R < 2:
                    continue
                # Find the index of the last prime <= max_R
                R_upper = np.searchsorted(primes, max_R, side='right')
                if R_upper == 0:
                    continue
                # Slice the primes array for R
                possible_R = primes[:R_upper]
                # Check if P + R is prime
                # Since P and R are primes, P + R might be even, but need to check
                # To speed up, vectorize the check
                Q = P + possible_R
                if Q[-1] > max_N:
                    # Limit Q to max_N
                    Q = Q[Q <= N]
                if np.any(sieve[Q]):
                    count +=1
            print(f"Case #{idx}: {count}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()