import sys
import threading

MOD = 998244353

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]

        trie = {}
        node_count = 1  # root node

        for s in strings:
            nodes = [(trie, 0)]
            while nodes:
                current_node, index = nodes.pop()
                if index == len(s):
                    continue
                char = s[index]
                if char == '?':
                    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if c not in current_node:
                            current_node[c] = {}
                            node_count = (node_count + 1) % MOD
                        nodes.append((current_node[c], index + 1))
                else:
                    if char not in current_node:
                        current_node[char] = {}
                        node_count = (node_count + 1) % MOD
                    nodes.append((current_node[char], index + 1))

        print(f"Case #{test_case}: {node_count}")

threading.Thread(target=main).start()