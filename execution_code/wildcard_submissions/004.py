import sys
import threading
from collections import deque

def main():
    import sys
    import math

    MOD = 998244353

    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N = int(sys.stdin.readline())
        S = [sys.stdin.readline().strip() for _ in range(N)]
        # Precompute possible letters per string per position as bitmask
        possible_letters_per_Si = []
        max_length = 0
        for s in S:
            pl = []
            for c in s:
                if c == '?':
                    pl.append((1<<26) -1)
                else:
                    pl.append(1 << (ord(c) - ord('A')))
            possible_letters_per_Si.append(pl)
            if len(s) > max_length:
                max_length = len(s)
        # Initialize BFS
        count =1  # root node
        initial_mask = 0
        for i in range(N):
            if len(S[i]) >0:
                initial_mask |= (1<<i)
        if initial_mask !=0:
            queue = deque()
            queue.append( (initial_mask, 0) )
            visited = set()
            visited.add( (initial_mask,0) )
            while queue:
                mask, depth = queue.popleft()
                if depth >= max_length:
                    continue
                # Compute possible letters at this depth
                possible_letters =0
                for s_i in range(N):
                    if (mask >>s_i) &1:
                        if depth < len(S[s_i]):
                            possible_letters |= possible_letters_per_Si[s_i][depth]
                # Iterate through each possible letter
                letter =0
                while possible_letters:
                    if possible_letters &1:
                        # letter_bit = letter
                        # Compute new_mask
                        new_mask =0
                        for s_i in range(N):
                            if (mask >>s_i) &1:
                                if depth < len(S[s_i]):
                                    if (possible_letters_per_Si[s_i][depth] >>letter) &1:
                                        new_mask |= (1<<s_i)
                        if new_mask !=0:
                            key = (new_mask, depth+1)
                            if key not in visited:
                                visited.add(key)
                                queue.append(key)
                                count = (count +1) % MOD
                    possible_letters >>=1
                    letter +=1
        print(f"Case #{test_case}: {count % MOD}")

threading.Thread(target=main,).start()