import sys
import sys
import sys

def main():
    import sys
    import sys
    from sys import stdin
    import sys

    import sys

    def input():
        return sys.stdin.read()

    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    max_N = max(N_list) if T >0 else 0
    sieve_size = max_N +1

    # Initialize sieve
    sieve = [True] * sieve_size
    sieve[0]=False
    sieve[1]=False

    import math
    sqrt_max = int(math.isqrt(max_N)) +1
    for p in range(2, sqrt_max):
        if sieve[p]:
            for multiple in range(p*p, sieve_size, p):
                sieve[multiple]=False

    # Compute twin prime counts
    twin_counts = [0]*(sieve_size)
    twin_count =0
    for i in range(3, sieve_size):
        if sieve[i] and sieve[i-2]:
            twin_count +=1
        twin_counts[i] = twin_count

    # For i <3, twin_counts is 0
    for i in range(0,3):
        twin_counts[i]=0

    # Process each test case
    for idx in range(T):
        N = N_list[idx]
        if N <2:
            count =0
        else:
            if N >=3:
                twin_count_N = twin_counts[N]
            else:
                twin_count_N =0
            if twin_count_N >=1:
                count = twin_count_N +1
            else:
                count =0
        print(f"Case #{idx+1}: {count}")

if __name__ == "__main__":
    main()