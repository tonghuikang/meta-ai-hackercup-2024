import sys
import threading

MOD = 998244353

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]
        
        trie = {}
        node_count = 1  # Start with root node
        
        for s in strings:
            stack = [(trie, 0)]
            # Use a list of tuples: (current_node, position in string)
            # Since we have wildcards, we need to keep track of multiple paths
            # We'll use BFS to avoid stack overflow
            queue = [(trie, 0)]
            while queue:
                current_node, pos = queue.pop()
                if pos == len(s):
                    continue
                char = s[pos]
                if char == '?':
                    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if c not in current_node:
                            current_node[c] = {}
                            node_count = (node_count + 1) % MOD
                        queue.append((current_node[c], pos + 1))
                else:
                    c = char
                    if c not in current_node:
                        current_node[c] = {}
                        node_count = (node_count + 1) % MOD
                    queue.append((current_node[c], pos + 1))
        print(f"Case #{case}: {node_count % MOD}")

threading.Thread(target=main).start()