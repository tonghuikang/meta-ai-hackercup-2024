import sys
import sys
import sys

def main():
    import sys
    import sys
    import sys

    import sys
    def input():
        return sys.stdin.read()

    data = sys.stdin.read().split()
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    max_N = max(Ns) if Ns else 0

    sieve = [True] * (max_N + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(max_N**0.5) +1):
        if sieve[p]:
            for multiple in range(p*p, max_N +1, p):
                sieve[multiple] = False

    # Build twin prime prefix count
    twin_count_prefix = [0]*(max_N +1)
    count =0
    for i in range(2, max_N +1):
        twin_count_prefix[i] = twin_count_prefix[i-1]
        if i >=3 and sieve[i] and sieve[i -2]:
            twin_count_prefix[i] +=1

    # Precompute if p=2 is included
    # p=2 is included if N >=5 and sieve[5] is True
    # But sieve[5] is already checked in twin_count_prefix
    # So simply p=2 is included if N >=5
    for idx, N in enumerate(Ns,1):
        total = twin_count_prefix[N]
        if N >=5:
            total +=1
        print(f"Case #{idx}: {total}")

if __name__ == "__main__":
    main()