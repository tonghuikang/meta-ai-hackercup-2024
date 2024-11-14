import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353
    T = int(sys.stdin.readline())
    for tc in range(1, T + 1):
        N = int(sys.stdin.readline())
        patterns = [sys.stdin.readline().strip() for _ in range(N)]
        
        # Initialize trie
        # Each node has 26 possible children (A-Z). Initialize with root node.
        trie = [[]]
        # Using list of lists. Each inner list has 26 elements, initialized to -1
        trie = [[-1] * 26]
        node_count = 1  # Start with root node
        
        for pattern in patterns:
            # We will use a queue for BFS insertion to handle wildcards
            # Each element in the queue is a tuple (current_node, position in pattern)
            queue = [(0, 0)]
            while queue:
                current_node, pos = queue.pop()
                if pos == len(pattern):
                    continue
                c = pattern[pos]
                if c == '?':
                    possible_chars = range(26)
                else:
                    possible_chars = [ord(c) - ord('A')]
                for ch in possible_chars:
                    if trie[current_node][ch] == -1:
                        trie.append([-1] * 26)
                        trie[current_node][ch] = node_count
                        node_count += 1
                    next_node = trie[current_node][ch]
                    queue.append((next_node, pos + 1))
        print(f"Case #{tc}: {node_count % MOD}")

threading.Thread(target=main,).start()