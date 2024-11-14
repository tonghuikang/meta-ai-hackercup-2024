MOD = 998244353

def solve():
    import sys
    import threading
    def main():
        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            N = int(sys.stdin.readline())
            S = []
            max_len = 0
            for _ in range(N):
                s = sys.stdin.readline().strip()
                S.append(s)
                max_len = max(max_len, len(s))
            N_patterns = N
            visited = set()
            from collections import deque
            initial_mask = 0
            for i in range(N):
                if len(S[i]) > 0:
                    initial_mask |= (1 << i)
            queue = deque()
            queue.append((0, initial_mask))
            total_nodes = 0
            while queue:
                pos, mask = queue.popleft()
                if (pos, mask) in visited:
                    continue
                visited.add((pos, mask))
                total_nodes += 1
                # For each possible character c
                for c in range(26):
                    new_mask = 0
                    for i in range(N):
                        if (mask & (1 << i)) == 0:
                            continue
                        if pos >= len(S[i]):
                            continue
                        ch = S[i][pos]
                        if ch == '?' or ch == chr(ord('A') + c):
                            new_mask |= (1 << i)
                    if new_mask != 0:
                        queue.append((pos +1, new_mask))
            total_nodes %= MOD
            print(f"Case #{test_case}: {total_nodes}")
    threading.Thread(target=main).start()