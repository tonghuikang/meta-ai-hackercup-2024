import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353

    T = int(sys.stdin.readline())
    
    for test_case in range(1, T+1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]
        
        # Initialize trie
        trie = {}
        node_count = 1  # root
        
        for s in strings:
            # Each element in the queue is (current node, position in string)
            queue = [(trie, 0)]
            while queue:
                current_node, pos = queue.pop()
                if pos == len(s):
                    continue
                c = s[pos]
                if c == '?':
                    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if ch not in current_node:
                            current_node[ch] = {}
                            node_count = (node_count + 1) % MOD
                        queue.append((current_node[ch], pos + 1))
                else:
                    if c not in current_node:
                        current_node[c] = {}
                        node_count = (node_count + 1) % MOD
                    queue.append((current_node[c], pos + 1))
        
        print(f"Case #{test_case}: {node_count}")

threading.Thread(target=main,).start()