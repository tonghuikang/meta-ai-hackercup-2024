import sys
import numpy as np

def sieve_eratosthenes(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    sqrt_n = int(n**0.5) + 1
    for p in range(2, sqrt_n):
        if sieve[p]:
            sieve[p*p:n+1:p] = False
    return sieve

def main():
    import sys
    import numpy as np

    input = sys.stdin.read().split()
    T = int(input[0])
    Ns = list(map(int, input[1:T+1]))
    N_max = max(Ns)
    
    sieve = sieve_eratosthenes(N_max)
    primes = np.nonzero(sieve)[0]
    
    subtractor = np.zeros(N_max + 1, dtype=bool)
    
    for r in primes:
        if r > N_max:
            break
        p_upper = N_max + 1 - r
        if p_upper <= 0:
            continue
        # Logical AND between p and p + r
        subtractor[:p_upper] |= (sieve[:p_upper] & sieve[r:p_upper + r])
    
    counts = np.cumsum(subtractor).astype(int)
    
    for idx, N in enumerate(Ns, 1):
        print(f"Case #{idx}: {counts[N]}")

if __name__ == "__main__":
    main()