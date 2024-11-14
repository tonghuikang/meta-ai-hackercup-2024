import sys
import threading

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353
    for tc in range(1, T+1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]
        trie = [{}]
        node_count = 1
        for s in strings:
            current_nodes = [0]
            for c in s:
                next_nodes = []
                if c == '?':
                    letters = [chr(ord('A') + i) for i in range(26)]
                else:
                    letters = [c]
                for node in current_nodes:
                    for letter in letters:
                        if letter not in trie[node]:
                            trie.append({})
                            trie[node][letter] = node_count
                            node_count +=1
                        next_nodes.append(trie[node][letter])
                current_nodes = next_nodes
            # To prevent the list from growing too large unnecessarily, optionally clear next_nodes
        print(f"Case #{tc}: {node_count % MOD}")

threading.Thread(target=main).start()