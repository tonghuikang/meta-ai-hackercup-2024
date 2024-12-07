import sys
import threading
from collections import defaultdict
import math

MOD = 10**9 + 7

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, M, L = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))
        
        # Combine all elements with their types
        elements = []
        for a in A:
            elements.append(('A', a))
        for b in B:
            elements.append(('B', b))
        
        # Assign unique indices
        indices = list(range(N+M))
        
        # Precompute differences
        diffs = [[0]*(N+M) for _ in range(N+M)]
        for i in range(N+M):
            for j in range(N+M):
                diffs[i][j] = abs(elements[i][1] - elements[j][1])
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dp(mask, last, s):
            if s > L:
                return 0
            if mask == (1<<(N+M)) -1:
                return 1
            total = 0
            for next in range(N+M):
                if not (mask & (1<<next)):
                    if last == -1:
                        new_sum = s
                    else:
                        new_sum = s + diffs[last][next]
                    if new_sum > L:
                        continue
                    total += dp(mask | (1<<next), next, new_sum)
                    if total >= MOD:
                        total -= MOD
            return total % MOD
        
        result = dp(0, -1, 0)
        print(f"Case #{test_case}: {result}")

threading.Thread(target=main,).start()