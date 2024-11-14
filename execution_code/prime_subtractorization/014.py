import sys
import numpy as np

def main():
    import sys
    import threading

    def solve():
        import sys

        T = int(sys.stdin.readline())
        N_list = [int(sys.stdin.readline()) for _ in range(T)]
        N_max = max(N_list)

        sieve_size = N_max + 2  # To handle P + R up to N_max
        sieve = np.ones(sieve_size, dtype=bool)
        sieve[:2] = False
        sqrt_n = int(np.sqrt(N_max)) +1
        for i in range(2, sqrt_n):
            if sieve[i]:
                sieve[i*i:N_max+1:i] = False
        primes = np.nonzero(sieve)[0]
        P = primes

        N_P = np.zeros(N_max +1, dtype=np.int32)

        # Iterate through R in primes
        for R in primes:
            Q = P + R
            mask = (Q <= N_max)
            Q = Q[mask]
            P_subset = P[mask]
            Q_prime = sieve[Q]
            P_valid = P_subset[Q_prime]
            mask_unset = (N_P[P_valid] ==0)
            P_final = P_valid[mask_unset]
            Q_final = Q[Q_prime][mask_unset]
            N_P[P_final] = Q_final
            # Early termination if all P have been set
            if np.all(N_P[P] !=0):
                break

        # Now, gather all Q's where N_P[P] =Q
        Q_list = N_P[P]
        Q_list = Q_list[Q_list >0]
        # Count the number of Q's <=N for each N
        counts_inc = np.bincount(Q_list, minlength=N_max +1)
        counts_prefix = np.cumsum(counts_inc)
        # For each test case, print the result
        for idx, N in enumerate(N_list,1):
            if N >=0:
                count = counts_prefix[N]
            else:
                count =0
            print(f"Case #{idx}: {count}")

    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()