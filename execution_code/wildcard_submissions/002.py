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
        trie = {}
        node_count = 1  # start with root
        for s in strings:
            stack = [(trie, 0)]
            while stack:
                current_node, pos = stack.pop()
                if pos == len(s):
                    continue
                c = s[pos]
                if c == '?':
                    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if ch not in current_node:
                            current_node[ch] = {}
                            node_count = (node_count + 1) % MOD
                        stack.append((current_node[ch], pos+1))
                else:
                    ch = c
                    if ch not in current_node:
                        current_node[ch] = {}
                        node_count = (node_count + 1) % MOD
                    stack.append((current_node[ch], pos+1))
        print(f"Case #{test_case}: {node_count % MOD}")

threading.Thread(target=main).start()