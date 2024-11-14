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
        strings = [sys.stdin.readline().strip() for _ in range(N)]
        # Implement the trie
        # Use list of lists for children, use 0 as root
        nodes = [{}]
        count = 1
        for s in strings:
            stack = [(0, 0)]  # (current node, position in string)
            while stack:
                node, pos = stack.pop()
                if pos == len(s):
                    continue
                c = s[pos]
                if c != '?':
                    if c not in nodes[node]:
                        nodes.append({})
                        nodes[node][c] = count
                        count += 1
                    stack.append((nodes[node][c], pos + 1))
                else:
                    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if ch not in nodes[node]:
                            nodes.append({})
                            nodes[node][ch] = count
                            count += 1
                        stack.append((nodes[node][ch], pos + 1))
        print(f"Case #{test_case}: {count % MOD}")

threading.Thread(target=main).start()