import sys
import threading

def main():
    import bisect

    T = int(sys.stdin.readline())
    Ns = []
    N_max = 0
    for _ in range(T):
        N = int(sys.stdin.readline())
        Ns.append(N)
        if N > N_max:
            N_max = N

    # Generate all primes up to N_max * 2 (to ensure all possible differences)
    N_max = max(Ns)
    sieve_limit = N_max
    sieve = [True] * (sieve_limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(sieve_limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i:sieve_limit+1:i] = [False] * ((sieve_limit - i*i)//i + 1)
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Precompute D[p] = True if p is difference of two primes <= N_max
    D = [False] * (N_max + 1)
    primes_set = set(primes)

    for idx1 in range(len(primes)):
        p1 = primes[idx1]
        for idx2 in range(idx1 + 1, len(primes)):
            p2 = primes[idx2]
            d = p2 - p1
            if d > N_max:
                break
            if sieve[d]:
                D[d] = True

    # For each test case, count the number of primes p <= N such that D[p] and p is prime
    for case_num, N in enumerate(Ns, 1):
        count = 0
        for p in primes:
            if p > N:
                break
            if D[p]:
                count +=1
        print(f"Case #{case_num}: {count}")

if __name__ == "__main__":
    threading.Thread(target=main).start()