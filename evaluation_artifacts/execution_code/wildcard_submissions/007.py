import sys
import sys
import sys
from collections import defaultdict

import sys
def main():
    import sys
    import sys
    sys.setrecursionlimit(1000000)
    MOD = 998244353

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]
        
        # Define the trie as a list of dicts
        # Each node is a dict mapping characters to child node indices
        trie = [{}]
        node_count = 1  # root node
        
        for s in strings:
            # Start from root
            nodes = [0]
            for c in s:
                next_nodes = []
                if c == '?':
                    possible_chars = [chr(ord('A') + i) for i in range(26)]
                else:
                    possible_chars = [c]
                for node in nodes:
                    for ch in possible_chars:
                        if ch not in trie[node]:
                            trie[node][ch] = node_count
                            trie.append({})
                            node_count += 1
                        next_nodes.append(trie[node][ch])
                nodes = list(set(next_nodes))
            # No need to mark end of string
        print(f"Case #{test_case}: {node_count % MOD}")

if __name__ == "__main__":
    main()