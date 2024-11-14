import sys
import threading

def main():
    T = int(sys.stdin.readline())
    N_list = [int(sys.stdin.readline()) for _ in range(T)]
    N_max = max(N_list)
    is_prime = [True] * (N_max + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N_max ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N_max + 1, i):
                is_prime[j] = False
    primes = [i for i, val in enumerate(is_prime) if val]
    counts = [0] * (N_max + 1)
    for N in range(2, N_max + 1):
        counts[N] = counts[N - 1]  # Start with the previous count
        for p in primes:
            if p > N // 2:
                break
            if is_prime[N - p]:
                counts[N] += 1
    for idx, N in enumerate(N_list, 1):
        result = counts[N]
        print(f"Case #{idx}: {result}")

threading.Thread(target=main).start()