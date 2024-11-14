import sys
import numpy as np
import math

def sieve_of_eratosthenes(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    sqrt_n = int(math.isqrt(n)) +1
    for p in range(2, sqrt_n):
        if sieve[p]:
            sieve[p*p:n+1:p] = False
    return sieve

def main():
    import sys
    import threading

    def run():
        import sys

        T_and_cases = sys.stdin.read().split()
        T = int(T_and_cases[0])
        Ns = list(map(int, T_and_cases[1:T+1]))
        max_N = max(Ns)

        # Step 1: Sieve up to max_N
        sieve = sieve_of_eratosthenes(max_N)

        # Step 2: Create S array for FFT
        S = sieve.astype(float)

        # Step 3: Determine the next power of two for padding
        fft_size = 1 << (max_N*2-1).bit_length()
        fft_size = 1
        while fft_size < 2 * max_N:
            fft_size <<=1

        # Step 4: Pad S to fft_size
        S_padded = np.zeros(fft_size, dtype=float)
        S_padded[:max_N +1] = S

        # Step 5: Perform FFT
        FFT_S = np.fft.fft(S_padded)

        # Step 6: Compute cross-correlation via inverse FFT of FFT_S * conj(FFT_S)
        C_FFT = FFT_S * np.conj(FFT_S)
        C = np.fft.ifft(C_FFT).real.round()

        # Step 7: Extract relevant part of C
        C = C[:max_N +1].astype(int)

        # Step 8: Determine P's that are prime and have at least one representation
        mask_P = sieve[:max_N +1] & (C[:max_N +1] >=1)

        # Step 9: Create cumulative counts
        list_P = np.nonzero(mask_P)[0]
        counts = np.zeros(max_N +1, dtype=int)
        counts[list_P] =1
        counts = np.cumsum(counts)

        # Step 10: Answer each test case
        for idx, N in enumerate(Ns, 1):
            if N >=0:
                cnt = counts[N]
            else:
                cnt =0
            print(f"Case #{idx}: {cnt}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()