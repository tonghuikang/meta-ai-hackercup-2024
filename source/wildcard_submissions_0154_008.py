import sys
import threading

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        patterns = [sys.stdin.readline().strip() for _ in range(N)]
        trie = [[-1] * 26]
        node_count = 1
        for pattern in patterns:
            current_nodes = [0]
            for c in pattern:
                next_nodes = []
                if c != '?':
                    idx = ord(c) - ord('A')
                    for node in current_nodes:
                        if trie[node][idx] == -1:
                            trie[node][idx] = node_count
                            trie.append([-1] * 26)
                            node_count +=1
                        next_nodes.append(trie[node][idx])
                else:
                    for node in current_nodes:
                        for i in range(26):
                            if trie[node][i] == -1:
                                trie[node][i] = node_count
                                trie.append([-1] * 26)
                                node_count +=1
                            next_nodes.append(trie[node][i])
                current_nodes = next_nodes
        print(f"Case #{test_case}: {node_count % MOD}")

threading.Thread(target=main).start()