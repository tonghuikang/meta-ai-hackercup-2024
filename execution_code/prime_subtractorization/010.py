import sys
import threading

def main():
    import sys
    import math

    T_and_N = sys.stdin.read().split()
    T = int(T_and_N[0])
    Ns = list(map(int, T_and_N[1:T+1]))
    max_N = max(Ns) if Ns else 0

    # Sieve of Eratosthenes up to max_N
    sieve = [False, False] + [True] * (max_N -1)
    for p in range(2, int(math.isqrt(max_N)) +1):
        if sieve[p]:
            for multiple in range(p*p, max_N+1, p):
                sieve[multiple] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    prime_set = set(primes)

    # Precompute prefix sums for faster queries if necessary
    # But here, process each test case individually

    for idx, N in enumerate(Ns, 1):
        count = 0
        # Iterate through primes <= N
        for s in primes:
            if s > N:
                break
            # Need to find at least one q such that s + q is prime and <=N
            # Since s and q are primes <=N, p = s + q <= N
            # So q <= N - s
            # Iterate through primes <= N - s
            # To optimize, iterate through primes <= N - s
            # and check if p = s + q is prime
            # Since primes are sorted, we can stop early
            for q in primes:
                if q > N - s:
                    break
                if sieve[s + q]:
                    count +=1
                    break
        print(f"Case #{idx}: {count}")

if __name__ == "__main__":
    threading.Thread(target=main).start()