import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1000000)
    MOD = 998244353

    T = int(sys.stdin.readline())

    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]

        # Define the trie node
        class TrieNode:
            __slots__ = ['children']
            def __init__(self):
                self.children = {}

        root = TrieNode()
        total_nodes = 1  # Start with root

        for s in strings:
            def insert(pos, node):
                nonlocal total_nodes
                if pos == len(s):
                    return
                c = s[pos]
                if c != '?':
                    if c not in node.children:
                        node.children[c] = TrieNode()
                        total_nodes = (total_nodes + 1) % MOD
                    insert(pos + 1, node.children[c])
                else:
                    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if char not in node.children:
                            node.children[char] = TrieNode()
                            total_nodes = (total_nodes + 1) % MOD
                        insert(pos + 1, node.children[char])

            insert(0, root)

        print(f"Case #{test_case}: {total_nodes}")

if __name__ == "__main__":
    threading.Thread(target=main).start()