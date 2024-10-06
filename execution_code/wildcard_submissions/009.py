import sys
import threading

MOD = 998244353

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        patterns = [sys.stdin.readline().strip() for _ in range(N)]
        
        # Initialize the trie
        trie = {}
        node_count = 1  # Start with root
        nodes = [trie]
        
        for pattern in patterns:
            # Function to insert the pattern into the trie, counting new nodes
            def insert(node, pos):
                nonlocal node_count
                if pos == len(pattern):
                    return
                c = pattern[pos]
                if c == '?':
                    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if ch not in node:
                            node[ch] = {}
                            node_count = (node_count + 1) % MOD
                        insert(node[ch], pos + 1)
                else:
                    if c not in node:
                        node[c] = {}
                        node_count = (node_count + 1) % MOD
                    insert(node[c], pos + 1)
            
            insert(trie, 0)
        
        print(f"Case #{test_case}: {node_count}")
                

threading.Thread(target=main).start()