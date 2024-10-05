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
        
        trie = {}
        node_count = 1  # Starting with the root node

        for s in strings:
            # Each path can branch due to wildcards
            # We'll use a list of current nodes to process
            current_nodes = [trie]
            for c in s:
                next_nodes = []
                if c == '?':
                    for node in current_nodes:
                        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                            if letter not in node:
                                node[letter] = {}
                                node_count += 1
                            next_nodes.append(node[letter])
                else:
                    for node in current_nodes:
                        if c not in node:
                            node[c] = {}
                            node_count += 1
                        next_nodes.append(node[c])
                current_nodes = next_nodes
            # No need to mark end of string
        print(f"Case #{test_case}: {node_count % MOD}")

if __name__ == "__main__":
    threading.Thread(target=main).start()