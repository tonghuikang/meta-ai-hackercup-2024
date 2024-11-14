import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]
        # Initialize trie
        trie = [{}]
        count = 1  # root
        for s in strings:
            # Use a stack for iterative DFS
            stack = [(0, 0)]
            while stack:
                node, pos = stack.pop()
                if pos == len(s):
                    continue
                c = s[pos]
                if c == '?':
                    chars = [chr(ord('A') + i) for i in range(26)]
                else:
                    chars = [c]
                for ch in chars:
                    if ch not in trie[node]:
                        trie.append({})
                        trie[node][ch] = len(trie) - 1
                        count = (count + 1) % MOD
                    child = trie[node][ch]
                    stack.append((child, pos + 1))
        print(f"Case #{test_case}: {count}")

threading.Thread(target=main,).start()