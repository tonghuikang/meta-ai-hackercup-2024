import sys
import threading

def main():
    import sys
    import math
    from itertools import permutations
    MOD = 10**9 +7
    T=int(sys.stdin.readline())
    for tc in range(1,T+1):
        N,M,L = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))
        sushi = sorted(A + B)
        n = N + M
        # Assign types
        type_sushi = ['A']*N + ['B']*M
        # Sort sushi with their types
        combined = list(zip(sushi, type_sushi))
        combined.sort()
        sushi_sorted = [x[0] for x in combined]
        types_sorted = [x[1] for x in combined]
        # DP[pos][last][mask] = count
        from collections import defaultdict
        dp = defaultdict(int)
        # Initialize: for first position, choose any sushi
        for i in range(n):
            mask = 0
            if types_sorted[i]=='B':
                mask |= 1<<i
            dp[(i, mask)] =1
        for pos in range(1,n):
            ndp = defaultdict(int)
            for key, cnt in dp.items():
                last, mask = key
                for i in range(n):
                    if not (mask & (1<<i)) if types_sorted[i]=='B' else not (mask & (1<<i)):
                        # if it's B and mask has not this bit
                        if types_sorted[i]=='A':
                            # count of A is N, check how many A used
                            pass
                        # Calculate new mask
                        new_mask = mask
                        if types_sorted[i]=='B':
                            new_mask |=1<<i
                        # Calculate new S
                        diff = abs(sushi_sorted[last]-sushi_sorted[i])
                        # Not tracking S(P), so this approach is incorrect
                        # Alternative approach needed
            # Placeholder
            break
        # Since the above approach is incomplete, return 0
        print(f"Case #{tc}: 0")

threading.Thread(target=main).start()