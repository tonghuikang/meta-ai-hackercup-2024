import sys
import threading

def main():
    import sys
    import math
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353
    for case in range(1, T + 1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]
        trie = [{}]
        node_count = 1
        for s in strings:
            current_nodes = [0]
            for c in s:
                next_nodes = []
                if c == '?':
                    letters = list(range(26))
                else:
                    letters = [ord(c) - 65]
                for node in current_nodes:
                    for l in letters:
                        if l not in trie[node]:
                            trie.append({})
                            trie[node][l] = node_count
                            node_count += 1
                        next_nodes.append(trie[node][l])
                current_nodes = next_nodes
            # No need to mark end of string
        print(f"Case #{case}: {node_count % MOD}")

threading.Thread(target=main).start()