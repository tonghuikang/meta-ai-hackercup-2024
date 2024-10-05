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

        # Define the trie as nested dictionaries
        trie = {}
        count = 1  # Start with root node

        for s in strings:
            def insert(node, pos):
                nonlocal count
                if pos == len(s):
                    return
                c = s[pos]
                if c == '?':
                    keys = [chr(ord('A') + i) for i in range(26)]
                else:
                    keys = [c]
                for ch in keys:
                    if ch not in node:
                        node[ch] = {}
                        count = (count + 1) % MOD
                    insert(node[ch], pos + 1)

            insert(trie, 0)

        print(f"Case #{test_case}: {count % MOD}")

threading.Thread(target=main,).start()