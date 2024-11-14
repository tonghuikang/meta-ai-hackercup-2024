import sys
import threading

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        S = [sys.stdin.readline().strip() for _ in range(N)]
        trie = [{}]
        node_count = 1
        for s in S:
            stack = [(0, 0)]  # (current_node, position in string)
            while stack:
                current_node, pos = stack.pop()
                if pos == len(s):
                    continue
                char = s[pos]
                if char == '?':
                    possibilities = [chr(ord('A') + i) for i in range(26)]
                else:
                    possibilities = [char]
                for c in possibilities:
                    if c not in trie[current_node]:
                        trie.append({})
                        trie[current_node][c] = node_count
                        node_count += 1
                    child_node = trie[current_node][c]
                    stack.append((child_node, pos + 1))
        print(f"Case #{test_case}: {node_count % MOD}")

threading.Thread(target=main,).start()