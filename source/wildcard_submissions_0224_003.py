import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]
        # Initialize trie as list of lists, each with 26 elements initialized to -1
        # Use a list to store children, each child is an integer index
        trie = [[-1]*26]
        node_count = 1
        for s in strings:
            # We will use a list to keep track of current nodes
            current_nodes = [0]
            for c in s:
                next_nodes = []
                if c != '?':
                    idx = ord(c) - ord('A')
                    for node in current_nodes:
                        if trie[node][idx] == -1:
                            trie.append([-1]*26)
                            trie[node][idx] = node_count
                            node_count += 1
                        next_nodes.append(trie[node][idx])
                else:
                    for node in current_nodes:
                        for idx in range(26):
                            if trie[node][idx] == -1:
                                trie.append([-1]*26)
                                trie[node][idx] = node_count
                                node_count += 1
                            next_nodes.append(trie[node][idx])
                current_nodes = next_nodes
            # No need to mark end of string
        print(f"Case #{test_case}: {node_count % MOD}")

threading.Thread(target=main,).start()